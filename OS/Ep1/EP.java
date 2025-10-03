import java.io.*;
import java.util.*;

public class EP {

    private static final String COM = "COM";
    private static final String ES = "E/S";
    private static final String SAIDA = "SAIDA";
    
    // BCP - Bloco de Controle de Processo
    static class BCP {

        String nome;
        int pc; // Program Counter
        String estado; // "PRONTO", "EXECUTANDO", "BLOQUEADO", "TERMINADO"
        Map<String, Integer> variaveis;
        
        public BCP(String nome) {
            this.nome = nome;
            this.pc = 0;
            this.estado = "PRONTO";
            this.variaveis = new HashMap<>();
        }
        
        public void setEstado(String estado) {
            this.estado = estado;
        }
        
        public String getEstado() {
            return estado;
        }
    }
    


    static class Processo {
        BCP bcp; // Bloco de Controle de Processo explícito
        List<String> instrucoes;
        
        public Processo(String nome) {
            this.bcp = new BCP(nome);
            this.instrucoes = new ArrayList<>();
        }
        

        public void adicionarInstrucao(String instrucao) {
            instrucoes.add(instrucao);
        }
        


        public boolean terminou() {
            return bcp.pc >= instrucoes.size() || 
                   (bcp.pc < instrucoes.size() && instrucoes.get(bcp.pc).equals(SAIDA));
        }
        


        public String proximaInstrucao() {
            if (bcp.pc < instrucoes.size()) {
                return instrucoes.get(bcp.pc);
            }
            return null;
        }
        


        public void executarInstrucao() {
            if (bcp.pc < instrucoes.size()) {
                String instrucao = instrucoes.get(bcp.pc);
                
                if (instrucao.startsWith("X=") || instrucao.startsWith("Y=")) {
                    // Atribuição de variável
                    String[] partes = instrucao.split("=");
                    String var = partes[0];
                    int valor = Integer.parseInt(partes[1]);
                    bcp.variaveis.put(var, valor);
                }
                
                bcp.pc++;
            }
        }
    }
    
    













    static class Escalonador {
        private Queue<Processo> filaExecucao;
        private Queue<Processo> filaES;
        private int quantum;
        private int tempo;
        
        public Escalonador(int quantum) {
            this.quantum = quantum;
            this.filaExecucao = new LinkedList<>();
            this.filaES = new LinkedList<>();
            this.tempo = 0;
        }
        
        public void adicionarProcesso(Processo processo) {
            filaExecucao.offer(processo);
        }
        




        
        public void executar() {
            System.out.println("*********** SIMULADOR INICIADO ***********");
            
            while (!filaExecucao.isEmpty() || !filaES.isEmpty()) {
                tempo++;
                System.out.println("\n--- TEMPO " + tempo + " ---");
                
                // Processar fila de E/S (volta para fila de execução)
                processarFilaES();
                
                // Executar processo da fila principal
                if (!filaExecucao.isEmpty()) {
                    Processo atual = filaExecucao.poll();
                    executarProcesso(atual);
                }
                
                imprimirEstado();
            }
            
            System.out.println("\n*********** SIMULADOR FINALIZADO ***********");
        }
        




        private void executarProcesso(Processo processo) {
            System.out.println("Executando: " + processo.bcp.nome);
            processo.bcp.setEstado("EXECUTANDO");
            
            int ciclosExecutados = 0;
            
            while (ciclosExecutados < quantum && !processo.terminou()) {
                String instrucao = processo.proximaInstrucao();
                
                if (instrucao == null || instrucao.equals(SAIDA)) {
                    break;
                }
                
                if (instrucao.equals(ES)) {
                    System.out.println("  " + processo.bcp.nome + " realizou E/S");
                    processo.executarInstrucao();
                    processo.bcp.setEstado("BLOQUEADO");
                    filaES.offer(processo); // Vai para fila de E/S
                    return;
                }
                
            
                processo.executarInstrucao();
                ciclosExecutados++;
                
                if (instrucao.equals(COM)) {
                    System.out.println("  " + processo.bcp.nome + " executou COM");
                } else if (instrucao.startsWith("X=") || instrucao.startsWith("Y=")) {
                    System.out.println("  " + processo.bcp.nome + " executou " + instrucao);
                }
            }
            
            
            if (!processo.terminou()) {
                System.out.println("  " + processo.bcp.nome + " voltou para fila (quantum esgotado)");
                processo.bcp.setEstado("PRONTO");
                filaExecucao.offer(processo);
            } else {
                System.out.println("  " + processo.bcp.nome + " TERMINOU");
                processo.bcp.setEstado("TERMINADO");
            }
        }
        
        private void processarFilaES() {
            if (!filaES.isEmpty()) {
                
                Processo processo = filaES.poll();
                System.out.println(processo.bcp.nome + " voltou da E/S para fila de execução");
                processo.bcp.setEstado("PRONTO");
                filaExecucao.offer(processo);
            }
        }
        
        private void imprimirEstado() {
            System.out.print("Fila de execução: ");
            for (Processo p : filaExecucao) {
                System.out.print(p.bcp.nome + " ");
            }
            System.out.println();
            
            System.out.print("Fila de E/S: ");
            for (Processo p : filaES) {
                System.out.print(p.bcp.nome + " ");
            }
            System.out.println();
        }
    }
    

    private static int carregarQuantum(String nomeArquivo) {
        try (BufferedReader br = new BufferedReader(new FileReader(nomeArquivo))) {
            String linha = br.readLine();
            return Integer.parseInt(linha.trim());
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
    

    private static Processo carregarProcesso(String nomeArquivo) {
        try (BufferedReader br = new BufferedReader(new FileReader(nomeArquivo))) {
            String nomeProcesso = br.readLine().trim();
            Processo processo = new Processo(nomeProcesso);
            
            String linha;
            while ((linha = br.readLine()) != null) {
                linha = linha.trim();
                if (!linha.isEmpty()) {
                    processo.adicionarInstrucao(linha);
                }
            }
            
            return processo;
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
    



    public static void main(String[] args) {
 
        int quantum = carregarQuantum("programas/quantum.txt");
        
        //System.out.println("Quantum carregado: " + quantum);
        
 
        Escalonador escalonador = new Escalonador(quantum);
        
 
        for (int i = 1; i <= 10; i++) {
            String nomeArquivo = String.format("programas/%02d.txt", i);
            Processo processo = carregarProcesso(nomeArquivo);
            escalonador.adicionarProcesso(processo);
            System.out.println("Processo carregado: " + processo.bcp.nome);
        }
        
 
        escalonador.executar();
    }
}