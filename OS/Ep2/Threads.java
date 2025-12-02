import java.util.List;
import java.util.Random;
import java.util.concurrent.locks.ReentrantReadWriteLock;

public class Threads {

    private static final ReentrantReadWriteLock lock = new ReentrantReadWriteLock(); //esse cara faz todo serviço de quando bloquear quem.
    private static final Random random = new Random();




    public static class Leitor extends Thread {
        private final List<String> palavras;

        public Leitor(List<String> palavras) {
            this.palavras = palavras;
        }




        @Override
        public void run() {
            lock.readLock().lock(); // vários leitores podem entrar aqui juntos
            try {
                for (int i = 0; i < 100; i++) {
                    int pos = random.nextInt(palavras.size());
                    String palavra = palavras.get(pos);
                    // apenas lê, não altera
                }
                Thread.sleep(1);
            } catch (InterruptedException e) {
                e.printStackTrace();
            } finally {
                lock.readLock().unlock();
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
            lock.writeLock().lock(); // apenas um escritor por vez
            try {
                for (int i = 0; i < 100; i++) {
                    int pos = random.nextInt(palavras.size());
                    palavras.set(pos, "MODIFICADO");
                }
                Thread.sleep(1);
            } catch (InterruptedException e) {
                e.printStackTrace();
            } finally {
                lock.writeLock().unlock();
            }
        }
    }
}
