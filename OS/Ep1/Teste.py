import pandas as pd

# Constantes e variáveis globais
MAXBUFFER = 20
MSS = 5
RTT = 40
TIMEOUT1 = 10
TIMEOUT2 = 50

# Listas para armazenar os dados de cada pacote
pacotes_A_para_B = []
pacotes_B_para_A = []

class Host:
    def __init__(self, name):
        self.name = name
        self.nxt_seq = 1
        self.snd_base = 1
        self.nxt_data = 1
        self.snd_wnd = MAXBUFFER
        self.rcv_wnd = MAXBUFFER
        self.nxt_read = 1
        self.last_ack = 1
        self.new_ack = False
        self.temp2_running = False
        self.temp2_timer = 0
        self.data_buffer_out = bytearray()
        self.data_buffer_in = bytearray()

    def send_data(self, data):
        self.data_buffer_out.extend(data)
        self.nxt_data += len(data)

    def read_data(self, length):
        if len(self.data_buffer_in) >= length:
            data = self.data_buffer_in[:length]
            del self.data_buffer_in[:length]
            self.nxt_read += length
            self.rcv_wnd = MAXBUFFER - (self.last_ack - self.nxt_read)
            return data
        return None

    def rec_seg(self, seq, ack, win, length, data, current_time):
        
        # Aumenta a janela de envio
        if ack > self.snd_base:
            self.snd_base = ack
            if self.snd_base < self.nxt_seq:
                self.temp2_timer = current_time
            else:
                self.temp2_running = False
        self.snd_wnd = win
        
        # Aloca dados no buffer de entrada
        if length > 0:
            self.new_ack = True
        if self.last_ack == seq:
            self.data_buffer_in.extend(data)
            self.last_ack = seq + length
        
        # Recalcula a janela de recebimento
        self.rcv_wnd = MAXBUFFER - (self.last_ack - self.nxt_read)

    def timeout2(self, current_time):
        length = min(MSS, self.snd_wnd, self.nxt_data - self.snd_base)
        if length > 0:
            data = self.data_buffer_out[self.snd_base-1 : self.snd_base -1 + length]
            return (self.snd_base, self.last_ack, self.rcv_wnd, length, data)
        return None

    def timeout1(self, current_time):
        
        # Envia dados
        if self.nxt_data > self.nxt_seq and self.snd_wnd > (self.nxt_seq - self.snd_base):
            length = min(MSS, self.snd_wnd - (self.nxt_seq - self.snd_base), self.nxt_data - self.nxt_seq)
            if length > 0:
                data = self.data_buffer_out[self.nxt_seq - 1 : self.nxt_seq - 1 + length]
                self.nxt_seq += length
                if not self.temp2_running:
                    self.temp2_running = True
                    self.temp2_timer = current_time
                return (self.nxt_seq - length, self.last_ack, self.rcv_wnd, length, data)
        
        # Envia ACK
        elif self.new_ack:
            self.new_ack = False
            return (self.nxt_seq, self.last_ack, self.rcv_wnd, 0, b'')
        return None

# Instancia os hospedeiros
host_a = Host("A")
host_b = Host("B")

# Dados para enviar
data_to_send = b'x' * 30

# Fila de eventos
event_queue = []

# Adiciona o primeiro evento
event_queue.append((0, "send_data", data_to_send))

# Simulação
tempo = -10
while event_queue or host_a.nxt_read < 31 or host_b.nxt_read < 31:
    tempo += 10
    
    # Executa eventos da fila
    i = 0
    while i < len(event_queue):
        e_time, e_type, e_data = event_queue[i]
        
        if e_time == tempo:
            if e_type == "send_data":
                host_a.send_data(e_data)
                
            elif e_type == "rec_seg_a":
                seq, ack, win, length, data = e_data
                host_a.rec_seg(seq, ack, win, length, data, tempo)
                
            elif e_type == "rec_seg_b":
                seq, ack, win, length, data = e_data
                host_b.rec_seg(seq, ack, win, length, data, tempo)
                
            del event_queue[i]
        else:
            i += 1
            
    # Hospedeiro B lê dados (evento ReadData)
    if tempo > 0 and tempo % 10 == 0:
        host_b.read_data(3)

    # Hospedeiro A e B rodam TimeOut1
    pacote_a_b = host_a.timeout1(tempo)
    pacote_b_a = host_b.timeout1(tempo)

    if pacote_a_b:
        pacotes_A_para_B.append([tempo, pacote_a_b[0], pacote_a_b[1], pacote_a_b[2], pacote_a_b[3]])
        event_queue.append((tempo + 20, "rec_seg_b", pacote_a_b))
    
    if pacote_b_a:
        pacotes_B_para_A.append([tempo, pacote_b_a[0], pacote_b_a[1], pacote_b_a[2], pacote_b_a[3]])
        event_queue.append((tempo + 20, "rec_seg_a", pacote_b_a))
    
    # Hospedeiro A roda TimeOut2
    if host_a.temp2_running and (tempo - host_a.temp2_timer) >= TIMEOUT2:
        pacote_retransmissao = host_a.timeout2(tempo)
        if pacote_retransmissao:
            pacotes_A_para_B.append([tempo, pacote_retransmissao[0], pacote_retransmissao[1], pacote_retransmissao[2], pacote_retransmissao[3]])
            event_queue.append((tempo + 20, "rec_seg_b", pacote_retransmissao))

# Apresenta os resultados
df_a_b = pd.DataFrame(pacotes_A_para_B, columns=['Tempo (ms)', 'Seq', 'ACK', 'Window', 'Len'])
print("--- Pacotes de A para B ---")
print(df_a_b.to_string(index=False))

print("\n")

df_b_a = pd.DataFrame(pacotes_B_para_A, columns=['Tempo (ms)', 'Seq', 'ACK', 'Window', 'Len'])
print("--- Pacotes de B para A ---")
print(df_b_a.to_string(index=False))