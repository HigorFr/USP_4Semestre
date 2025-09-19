#Threads são usados para processos independentes, que não conflitam com a execução de outro.
    #Isso permite uma entrada e saída não travar todo o programa, já que a thread que não executou poderia ser escalondada.


#No modelo de núcleo, toda thread criada é criada dentro do SOckets
    #Isso independente do hardware, ele que gerencia, e pode inclusive fazer um "Pseudo-paralelismo" caso o processador não comprote Threads
    #O ruim é que criar e destruir threads é uma chamada ao SO, e isso cria muitas TRAPs que intorrompem o fluxo de processo pela troca de contexo
    #O bom é que isso permite reciclar thread
    #Todos os os sitemas operacioanis normalmente usam isso.
    #Ela que permite de fato o paralelismo

#Reciclar thread é basicamente marcar como "Morto" para ser reutilziado se preciso.
    #Isso é bem comum na computaçaõ como visto anteriormente.
    
#Threads Hibridas
    #Não anotei


    #Lembrnado que a thread de usuario é muito útil ainda mesmo sem paraleleismo, principalemnte quando você quer ordem ou não pdoe deixar o SO escolher por você.


#Tem uma comparação de modelos muito útil no slide


#Comunicação entreprocessos
    #Basciamente o ato de passar informação de um processos para o outro
    #Tem varias maneiras, como exemplo passar um arquivo
    #Tem que controlar a memoria, e a ordem de execução.


#Condição de corrida
    #Quando duas threads precisam de um mesmo recurso simultaneamente e isso pode dar uma "dissincronia"
        #Para debugar isso é um inferno também.
    #Spooler ??? não anotei
    
    #Exclusão mútua é uma solução para esse problema.
        #Regiões criticas é uma parte do seu código que permite acesso à memŕoia compartilhada por threads diferentes. Nessa regiões que ocorrem condições de corrida.
        #Temos que fazer uma então essa "Exlcusão" que é basciaemnte impedir uma thread de acessar auqela memória enquanto outra está acessadno.
            #Não precisa nesecessariamente ir para fila de bloqueado, mas precisa arranchar um jeito dele simpeslemnte não rodar.
    
    #Tem regras esepecificar para programação concorrente
        #Ninguem entra ao mesmo tempo em região critica
        #Não se pode fazer supor coisa do hardware
        #?? não anotei
        #Não pode deixar um processo rodando para sempre por conta de outra


    
#Soluções:
    #Espera Ocupada (Busy Waiting)
        #Essas soluções são bem ineficiente, você fica a todo momento fazendo uma checagem de variável  até que mude alguma variável
        
        #Primeiro méotodo é desabilitar interrupção enquanto thread estiverm em região critica. Isso obviamente dá problema, pois a thread pode simplesmente não ligar interrupções por N motivos e o processo basicamente SEQUESTRA a merda da sua CPU
        
        #Segundo é Lock variables, que consiste em travar o recurso utilizando uma variável (uma mensagem) que a outra thread vai conferir toda hora. O problma é que ainda existe o azar de em um mesmo instante a trava foi desativada e dois entraram ao mesmo tempo.
            #Tem como fazer uma "Alternancia" para impedir isso, então um roda enquanto está diferente de 0 e deixa como 1 e outro roda enquanto está diferente de 1 e deixa como 0, mas isso ainda não é eficiente pois uma thread vai ficar esperando a outra
        
        #Solução de Peterson, cria-se um arranjo com todos as threads que querem acessar o recurso compartilhado, cada thread só registra em uma posição especifica usando o ID da thread. TOdo mundo que chega entre sempre no modo espera, e um while roda que só sai quando ninguém antes dele estiver esperando.
            #independente de onde ele seja interrompido ele continua rodando
            #Mas ele vai ficando cada vez mais complicado conforme adiciona thread, com 3 é mais difícil, com 4 é mais, etc...

    #E então para simplificar esses problemas, o proprio hardware foi alterado, as soluções com ele serão nas proximas aulas