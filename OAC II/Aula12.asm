#Ultima aula foi correção da prova só, não vim



#Agora P2 começa ==========================


#Relembrando
#Monociclo, instrução executada em uma ida só com clock do tamanho da maior instrução. Todas custam o clock
#Multiciclo, instrução executada em varias etapas, clock do tamanho da maior etapas. Cada instrução o clock * etapas usadas
#Pipeline, instrução executadas em varias etapas diferentes paralelas, clock do tamanho da maior etapa. Cada instrução vai ser realizada quando o pipline estiver cheio em um clock
#Memoria cache -> Já visto. 


#Até então considerava-se que uma instrução R passava pela memoria sem utiliza-la, só para sincronizar o pipeline.

#Cache pode demorar dois ciclos (e para todo mundo)


#Superpiline é quebrar um estágio em mais estágios ainda, para poder colocar mais instruções em paralelo
    #Tem umm limite para o quanto você pode dividir. Não será trabalhado.

#Superescalar é literalmente colocar dois pipelines para rodar simultaneamente, ou seja, aumentou recurso.
    #Isso basciamente pode mutiplicar as intruções executadas (isso até um certo limite também)




#Superescalar
    #Complexidade será W² porque todos os registradores compartilhados deverão ser observados
    #ISso irá adicionar mutios tipos de conflitos novos
    #O nome do pipiline que implementamos antes era o "Piepline Rígido", esse que iremos trabalho é dinâmico, e permite mais coisas
        #Ver slide
    #Como exemplo, haverá um buffer, tanto para instruções decoficiadas, tanto para insturções prontas para fazer writeback


#Conflitos
    #Dependencia de desvio 
    #Conflito de recurso
    #dependencia de dados verdadeiras (read after write)
    #Antidependencia (write after read)
        #Esse conflito tem a ver com o nome das variáveis, ele é facilmente resolvível, pois basta trocar um registrador que seria sobrescrito em outro.
        #Ou seja, eu renomeio o nome dos registradores em tempo de execução


#Tipos de fluxos...

#Exercicio
A-
$r1 L1 L2 dado
$r3 L3 não pode rodar antes de L2
$r4 L4 não pode rodar antes do L3
$r6 L6 não pode rodar antes de L5






