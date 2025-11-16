
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;


public class Main {
    public static void main(String[] args){
           
        
        int qtd_leitores = 50; //Quantidade de escritores vai ser 100 - isso.


        int soma = 0;
        int soma_sem = 0;
        
        for(int i = 0; i<50; i++){

            List<String> palavras = new ArrayList<>();

            try {
                // Lê todas as linhas do arquivo em uma lista de strings
                palavras = Files.readAllLines(Paths.get("bd.txt"));
            }
            
            catch (IOException e) {
                System.out.println("Erro ao ler: " + e.getMessage());
            }

            //Threads
            List<Thread> threads = new ArrayList<>();
            List<Thread> threads_sem = new ArrayList<>();


            //Aqui as que utilizam do sistema
            //Leitores
            for (int j = 0; j < qtd_leitores; j++) {
                Thread t = new Threads.Leitor(palavras);
                threads.add(t);
            }
                    

            //Escritores
            for (int k = qtd_leitores; k < 100; k++) {
                Thread t = new Threads.Escritor(palavras);
                threads.add(t);
            }


            //Aqui as que não utilizam
            //Leitores
            for (int j = 0; j < qtd_leitores; j++) {
                Thread t = new Threads_Locked.Leitor(palavras);
                threads_sem.add(t);
            }
                    

            //Escritores
            for (int k = qtd_leitores; k < 100; k++) {
                Thread t = new Threads_Locked.Escritor(palavras);
                threads_sem.add(t);
            }


            //Embaralha ambas
            Collections.shuffle(threads);
            Collections.shuffle(threads_sem);





            //Inicia contagem usando sistema
            long inicio = System.currentTimeMillis();

            for (Thread t : threads) t.start();

            for (Thread t : threads) { //só pra obrigar a main esperar todo mundo
                try {
                    t.join();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }

            
            long fim = System.currentTimeMillis();
            long tempoExecucao = fim - inicio;


            soma += tempoExecucao;




            //Inicia contagem sem usar o sistema
            inicio = System.currentTimeMillis();

            for (Thread t : threads_sem) t.start();

            for (Thread t : threads_sem) { //só pra obrigar a main esperar todo mundo
                try {
                    t.join();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }

            
            fim = System.currentTimeMillis();
            tempoExecucao = fim - inicio;


            soma_sem += tempoExecucao;
        }
        

        double tempo_med = soma/50.0;
        double tempo_med_sem = soma_sem/50.0;

        System.out.println(String.format("Execução com uso de leitores/escrita feita com tempo médio de: %.2f ms",tempo_med));
        System.out.println(String.format("Execução sem uso de leitores/escrita feita com tempo médio de: %.2f ms",tempo_med_sem));


    }
}
