#Ultima aula foi algoritimos de Batch (Lote)
    #Hoje veremos alguns algoritimos de sistemas interativos (Os para escolaonamento)
    #Próximo aula Thread e tempo Real


#É bom saber esses nomes pois fica fácil identificar o algorotimo
#Todos aqui são premptivos, ou seja, usuário é o que importa

#Round-Robins (Alternancia Circular)
    #Mesma ideia da fila do batch, forma-se uma ordem e elas vão sendo executadas usando uma fatia de tempo. (Quantum)
    #Ele roda, deu o tempo? Fim da fila. Precisou de I/O, vai pro bloqueado e depois para o fim da fila.
    #Se acabar antes, obiviamente você coloca outro no lugar
    
    #Quando o processo termina antes, nem sempre o Hardware permite você dar um quantum picotado para outro processo. É necessário que o SO atrase o clock para ficar no tempo certo.
        #Isso quando o clock é programável, se não for, o processo vai só rodar o restante do que ficou pronto (Isso porquê nesse caso o clock é elétrico)

    #É relativamente fácil implementar e é "justo", mas o tempo de ficar trocando (Guardar contexto e carregar contexto) é alto.
        #Fora isso, também tem aquela coisa que processos baseados em I/O vai sempre pro final e acabam processando pouco.

    #Overhead ->   (Troca de Contexto)/(???? não anotei)

    #Quantum razoável 20-50ms


#Escalonamento por Prioridades
    #Isso é uma evolução do RR, você leva em conta Prioridades
    #A prioridade é um atributo estático do processo (No linux da pra usar "Nice" para colocar)
    #(No linux, quanto menor o "Niceness",isto é, quanto mais chato você é, menos processo você deixa passar na sua frente)
        #Se for zero, é prioridade máximo, ninguém passa.
    
    #Nessa concepção pura, que ele segue a risca o valor da prioridade é meio ruim, pois processos grandes rodarão até um I/O ou terminar, (Logo os com pouca prirodade quase nunca rodam)

    #É feito com que cada vez que ele roda você tira um ponto de prioridade para resolver esse problema, muito parecido com que o linux faz
        #Então é como se eles tivessem créditos para gastar.
        #Se dois tiverem os mesmos "creditos", você pode escolher quem já estava rodando para evitar troca. 
        #Tamém usa isso para formar uma fila para cada prioridade (Classe), para economizar processamento.

    #Também da para por um quantum máximo, para evitar só um rodar.


    #Normalmente tem classes para definir a prioridades Real time -> System -> Interativo -> Batch

    #O windows tem 6 e o linux tem 2 classes. Normalmente usa-se uma organização de prioridade dentro da classe de prioridade.


#Mútiplas Filas (IBM 7094)
    #Variação da classe de priroridade, feito para coisa com pouca memória.
    #Invés de rodar todo processo, roda um quantum determinado pelo "Credito" de prioridade que o processo tem.
    #Então todos rodam 1 vez na fila 1 e caem para fila 2, onde rodam 2 e caem para fila 3 onde rodam 4 e assim por diante. (mutiplicando por 2)
        #Isso é útil para fazer os processos rápidos primeiro, eles são excluidos de cara e os maiores vão caindo.
    #Tem um numero de camadas delimitado, e a ultima camada é um round-robins com os maiores.
    #Isso é muito útil para evitar troca de memória e HD, por isso usado em coisas com pouca memória.


#Shortest Processes Next
    #Dificilmente implemntado, mais uma ideia.
    #Você estima um tempo com base nas vezes que rodou antes um certo processo. E escolhe sempre o menor processo.
    #Vai tirando uma média de A tempos anteriores para definir.

#Escalonamento Garantido
    #Escolhe sempre o processo que rodou por menos tempo, usando um registro toda vez que ele roda.
    #Ou seja, garante ao processo uma fatia do CPU para todo processo, mas exige estrutras a parte da CPU para registrar esse tempo.
    


#Escalonamento pro loteria
    #Garante que todos terão sua vez de rodar usando sorteio
    #Usa uma lista de sorteados e outra de não sorteados. Quando a lista de sorteados fica cheia, reseta.
    #Isso também permite manipular a chance de cada processo rodar (Meio que uma prioridade)

#Lembre-se que SO é um sistema de gerenciamento, o conceito pode ser até extrapolado para coisas não relacionados à computador. Por isso esses coinceitos são aplicáveis até em oturos lugares específicos. O comptuador é feito para fazer de tudo um pouco, não sengo específico em nada.

#Escalonamento por fração justa (Fari Share)
    #Invés de ser uma divisão por processo, se faz uma divisão por usuário (Aquele que iniciou o processo)
    #A divisão é feita com base no máximo do sistema
    #Então se garante uma mesma fatia para os usuários, se um tiver 9 processos e outro 1, ele revesa esses 9 processo com 1.
    #Dentro dessa divisão tem um round-robin para escolher
    #Exemplo no slide

    