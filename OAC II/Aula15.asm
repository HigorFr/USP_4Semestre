#No EP parte 2 Não é necessário fazer aplicado, é só o projeto.
#Apresentar o artigo ainda é necessário.



#Processadores Multicores.

#Pipeline reaproveita as etapas
#Superescalar aproveita para adiantar.
#Multicore é ter mais de um processador.




#Isso exigirá paralelismo em nível de dados e de threads.

#Um processador pode ser consdierado um thread (caso ele não suporte), mas na definição threads ocorrem dentro do processo.


#Abordagem Intercalada
    #Mais granular (fino)
    #Cada ciclo você troca a thread
    #Precisa de mais hardware

#Abordagem Em bloco
    #Executa até que tem uma evento de entrada/saída, cache miss etc..
    #Dá para executar no mesmo hardware.

#Principal parte é guardar o contexto e os registradores da thread.


#======

#Simultaneous Multithread
#EM cada siclo você pode carregar instrução de qualquer thread.
#Dessa forma, sempre vai ter alguma coisinha para rodar em um lugar vazio, nunca então terá operação ociosa.

Multiprocessing (Mutiplos processadores)
#Literalmente 4 CPUs



#Cache no multicore.
    #Terá um nivel 2 para todas as CPUs, mas cada uma terá uma pequena cache L1, de instrução e de dados.
    #Existirá um problema para sincronizar isso tudo também. Se algo for alterado em um L1, tem que ser alterado em todos.



#Graças a essas modificações que ocorreu um aumento exponeical no processamento 
    #Velocidade co clock faz tempo que não muda.
    #Tamanho também já não tem como reduzir.


#O programa tem que ser multithread para fazer sentido o uso de várias CPUs. 
    #Na pratica, como tem muita coisa rodando pelo SO, só isso garante que todas CPUs serão usadas já que tem varias threads (Mesmo de processos diferentes).


 #Utilizar 8 Processadores não necessariamente é 8x mais rápido.
    #as vezes é em média 4.7 vezes mais rápido


#Existem varias organizações possíveis, L2 cache pode estar fora, Pode ou não ter cache 3 etc...
#Politicas de cache também são as mesmas para repasse entre a caches, write back ou write thorugh


#Protocolo Mesi
    #Tabela que guarda informações para realizar a sincronia entre caches.
    #Especificado no slide, cada bit tem seu objetivo dependendo do modo.


#Esses mapas mudam através de uma máquina de estados.


#