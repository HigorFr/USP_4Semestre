import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;

public class Threads_Locked {

    private static final Object lock = new Object();
    private static final Random random = new Random();

    public static void main(String[] args) throws IOException {
        // Lê arquivo e carrega palavras
        List<String> palavras = Files.readAllLines(Paths.get("palavras.txt"));

        // Cria lista de threads (50 leitores e 50 escritores, por exemplo)
        List<Thread> threads = new ArrayList<>();

        for (int i = 0; i < 50; i++) {
            threads.add(new Leitor(palavras));
            threads.add(new Escritor(palavras));
        }

        long inicio = System.currentTimeMillis();

        // Inicia todas as threads
        for (Thread t : threads) {
            t.start();
        }

        // Espera todas terminarem
        for (Thread t : threads) {
            try {
                t.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        long fim = System.currentTimeMillis();
        System.out.println("Tempo total: " + (fim - inicio) + " ms");
    }




    public static class Leitor extends Thread {
        private final List<String> palavras;

        public Leitor(List<String> palavras) {
            this.palavras = palavras;
        }

        @Override
        public void run() {
            
            synchronized (lock) {
                for (int i = 0; i < 100; i++) {
                    int pos = random.nextInt(palavras.size());
                    String palavra = palavras.get(pos);
                    // Apenas leitura, mas não faz nada de fato
                }
            

                try {
                    Thread.sleep(1);
                } 
                
                catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }
    }





    public static class Escritor extends Thread {
        private final List<String> palavras;

        public Escritor(List<String> palavras) {
            this.palavras = palavras;
        }

        @Override
        public void run() {
            synchronized (lock) {
                for (int i = 0; i < 100; i++) {
                    int pos = random.nextInt(palavras.size());
                    palavras.set(pos, "MODIFICADO");
                }
                

                try {
                    Thread.sleep(1);
                }
                
                catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
