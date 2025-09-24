#Pipeline


#conflito de de dados

    #Basciamente quando uma instrução precisa de algo que ainda não foi processado.
    #Para melhorar isso criamos "pontes" como atalho para adiantar certas informações

    #Em casos que não é possível fazer isso, cria-se uma bolha, que é um comando vazio que aguarda

    #Se o pipeline enche, não há como saber qual a proximo instrução, então faz sentido criar uma bolha para esperar a proxima




#Tem também como colocar um "Chute" que vai tentar chutar se um desvio vai ser realizao ao não e continuar lendo a partir dela, se tiver errado é jogado no lixo.
    #Explo BEQ normalmente fica em um FOR, e é raro de acontecer a condição para sair. Por isso normalmente considera que ele toma o desvio.

    #As vezes é travado no hardware
    #Tem como definir isso por OPCode
    #Tem hardware com buffer na predição que guarda 1 ou dois bits
        #Nesse caso ele erra no inicio pensando que era para não dar brench, a partir dai ele sempre tenta dar brench até dar erro novamente, ou seja, acerta sempre (N-2)/N
        #Tem versões que guardam historico em 1 ou dois bits (esse que foi dito)
        #se for com 2 bits vocẽ pode programar para que precise dois erros seguidos para ele trocar o que você está predizendo, já que eu vou conseguir ter 4 estados

    #Por ultimo também tem como duplicar o hardware, para um sempre fazer o branch e o outro não, após a decisão ele escolhe o hardware correto.
        #Isso não resolve sempre também, pois pode haver um branch logo depois de outro


    #Existe também outras opções de otimização, que basicamente muda a ordem de execução para acelerar, as vezes o compilador faz isso, mas é possível fazer direto em tempo de execução
        #Tipo fazer lw 0 lw 2 sw 2 sw 0, que poderia ser lw 0 lw 2 sw 0 lw 2 que seria muito melhorar


    #Como é no MIPS
        #não tem estágio ligado
        #Intrução de tamanho unico, ou seja, só lê a instrução em uma memória
        