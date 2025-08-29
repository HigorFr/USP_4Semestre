#Escolonamento de Processos I


#Relembrando
    #Contexto é tudo que está sobre o processo. Então é só copiar e jogar ele e ficará restaurado
    #Botar para rodar o nucleo do SO é muito custosa, trocar de um processamento para o outro (Ou seja, tocar totalmente o contexto)
    #Quando rola interrupções, o dispatcher que salva o bloco atual e manda para o Escalonador
    #Escolonador escolhe quem o proximo que roda, e manda o dispatcher pegar ele (Ou seja, pegar o contexto dele)
    #isso tudo é no mundo das ideias, na prática existem alguns atalhos
        #Na pratica o Dispatcher olha o tipo de interrupção e chama uma rotina que salva só o que será necessario de acordo com o que a função muda


#O dispatcher quando vai restaurar o contexto ele restaura tudo, deixando o Program Counter por último pois ele é um programa rodando no CPU. (Ou seja, ele termina o trabalho dele de substituir partes do contexto, e depois de substituir o program counter ele sai)

#Quando é rotina, ainda dá pra economizar pois o procesos é o mesmo, você só muda o que precisa
    #O problema é quando você troca pelo escalondar, que troca tudo mesmo.

#O SO também se responsabiliza por jogar lixo na CPU quando não é para ela fazer nada (STALL)
    #Isso porque a pipeline não pode ficar vazia, ou ele vai pegar algo do PC e vai começar a processar ele como uma instrução
    #Atualmente é quase impossível ficar vazio, o CPU tem muita rodando. o INIT do Unix também serve para cumprir esse propósito de ter algo rodando além de serivr de pai de todos os processos


#Terá algoritmos para fazer esses escalonamentos.

#Não preemptivo é aqueles que não sai do processador NUNCA, quase não existe processo assim em um computador normal, não há escolha
#Preemptivo é aqueles que há uma escolha se pode ser interrompido ou não

#Categorias
    #Batch
        #Lento, bloco de usuário sem usuário
        #Pouca troca de contexto
        #Pode ser Preemptivo ou não, mas como função é pra ser interativo

    #Interativo
        #Oriundo do usuário diretamente da entrada e saída, prioridade alta
        #Interação constante
        #Espera e executa comando
        #Preemptivo (Evita que um processo se apossa da CPU)
            #Isso é premissa básica, pois o usuário não pode sentir que o PC está travando, ele a todo momento rpecisa de feedback


    #Real-Time
        #Mais rapidaemnte, tempo crucial, feito para sistema crítico
        #Preemptivo
        



#Batch envia pacotes de comandos
    #Isso é útil para minimizar a fila de prontos, e para ter eficiecia, 100% de aproveitamento da CPU
    #Importamente pra prova: Tempo médio de retorno, tempo de chamar o programa até o retorno dele
    #Entrar na fila de pronto até terminar
    #É na visão do usuário, é uma média. O objetivo no final é diminuir isso.



Sistemas Interativo
    #Tempo de respsota é a prioridade, deixar o usuário alegre
    #Ele tem o poder, então é satisfazer as expectativas do usuário.
    #"Ninguem morre" se parar, mas é bom que sempre esteja rodando
    #Usa muita bufferização com base na expectativa do usuario (TIpo vídeo, é melhor travar no inicio que diminuir a qualidade conforme o tempo)
        #Isso porque é uma expectativa física (Uma vez que começa é continuo, o carro, prepar comida etc.. etc...)


#algoritmos Batch
    #FIFO
    #Shortest job First
    #




#FIFO
    #Você enfileira e roda os processos naqueal roda, ele é não premptivo, não substitui nunca exceto por interrupção/trap
    #Ordem de chegada
    #Normalmente é uma fila para cada dispotivo (mas pode ser só uma, o que seria bem ineficiente)
    #Gráfico
    #Tempo médio é literalmente a média de tempo entre vários processos

    #Fácil de programar
    #Pode criar gargalo dependendo da distribuição dos processos, pois a fila é a mesma (TIpo um carro atrás de um caminhão)

#Shortest job First
    #Também é não premptivo
    #(Job é serviço, veio dos OS antigos)
    #Utiliza uma estimativa de quanto tempo um processo irá demorar a rodar
    #Ordena pela menor tempo, então 7,6,5,4,3 vira 3,4,5,6,7 obrigatoriamente
    #Diminui turnarround médio, em um exemplo com 4 processo, a média seria (4a+3b+2c+d) /4. Logo é lógico que A seja o menor e D fique o maior
    #Pode ter desvantagem, o processo que demora muito vai ficar com "Starvation" ou seja, ele nunca vai ser processado se ficar chegando muito processo curto.
    #Para o turnarround ser de fato mínimo é necessário que todos estejam "Pronto" silmuntaneamente, em fluxo é quase impossível acontecer. Isso se deve pois não é premptivo e ele não vai trocar se aparecer um mais rápido se um mais lento já foi jogado para rodar.
    #Para melhorar isso, vire e tem que botar um lento para rodar um pouqinho

#Shortest Remaining Time Next
    #Preemptivo
    #Você ordena incialmente pelo tamanho, e conforme vai chegando novos você compara quanto tempo falta para terminar com o que está processando, se for, você troca  (porque esse pode trocar pois e premptivo)
    #Nesse caso o que precisa de mais tempo vai ser mais prejudicado ainda que no anterior

    #Na pratica é muito dificil ser imune à starvation. O mais comum é de tempos em tempos os maioroes rodarem, ou eles nunca rodam.




            