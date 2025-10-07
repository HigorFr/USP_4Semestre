#Outras aulas são online, professor faltou


#Solução Leitores Escritores
    #Leitor trava base só para escritores
    #Variaveis de controle da quantidade de leitores e variáveis para controlar base dos escritores


    #Problema é que se tiver muitos leitores, escritores podem ficar esperando muito tempo
    #Solução: dar prioridade para escritores
        #Isso depende do domínio, pagina web por exemplo vale a pena




#SOlução Barbeiros dorminhocos
    #Barbeiro dorme se não tiver clientes
    #Se chegar cliente, acorda barbeiro
    #Se chegar cliente e barbeiro estiver cortando cabelo, cliente espera
    #Se chegar cliente e barbeiro estiver dormindo, acorda barbeiro
    #Se barbeiro terminar de cortar cabelo e não tiver cliente, ele dorme
    #Se barbeiro terminar de cortar cabelo e tiver cliente, ele chama o cliente

    #Problema: se chegar muitos clientes, barbeiro pode ficar sem tempo para dormir
    #Solução: limitar quantidade de clientes na fila (cadeiras)



#Gerenciamento de Memória
    #Vazar memória é quando o programa aloca memória e não libera, perde o ponteiro
    #Swapping: mover processos da memória principal para a memória secundária (disco) e vice-versa
    #Multiprogramação: ter vários processos na memória ao mesmo tempo, para aproveitar mais dela
        #Se roda 80% em entrad e saída, tem 20% de processamento, em tese você precisaria de 5 processos para ter 100% de CPU
            #Mas essa sincronia não acontece, é algo estatistico
            #Então vira um problema estatistico, p^n = probabilidade de todos os processos estarem em espera
            #O uso da CPU é 1 - p^n, a probabilidade dela estar fazendo algo
            #Por isso a memoria não é proporcional à velocidade, pois é algo quase logaritimico. Quanto menos entrda e saída, menor a efetividade da quantidade de memória.
        

#Como programa vira memória?
    #Abstação é quando O SO dá um endereço virtual para o programa, que é mapeado para um endereço físico, o hardware depois faz uma soma de base + offset
    #Sem abstração é só o offset (Endereçamento direto), o programa tem que saber onde está na memória, ele poderia inclusive invdair blocos de outros, até do proprio do SO
        #Seria impossível fazer multiprogramação sem abstração
    

#BOMBA DE FORK TOMA:

#:(){ :|:& };:


