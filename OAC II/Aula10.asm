#Especificações do EP



#Certos requisitos, fazer tudo no logisim
    #Parte 1 31/out e parte 2 2/dez
    #Divido em duas partes, uma em ordem e uma fora de ordem
    #Entrega é um .circ

    #-COlocar pipeline e fazer essas implementações


#EP Em grupo de 4 pessoas



#Tecnologia de memória
    #Invés de usar o flipflop existem outras tecnologias
    #Flash, Static RAM, Dynamic RAM etc...
        #Nos registradores e memorias cache a SRAM é bem comum
        #Funcionam de maneiras diferentes

#Maneiras de criar um banc de registradores
    #Mutiplexadores para selecionar e comandos, bem simples. Observável no slide


#Caracteristicas
    #Capacidade
    #Latência
    #Largura de Banda



#Principios
    #Localidade Espcial, é provavel que coisas pertos sejam chamadas sem sequencia
    #Localidade Temportal, algo que acabou de ser chamado pode ser chamado novamente

#Transferencia em blocos é mais eficiente para descer a hierarquai de memorias


#Tipos de cachce
    #Muito semelhante à o já visto
    #Associativo ou mapeamento direto.
        #Mapeamento direto e mais simples mas pode dar mais colisão
        #Associativo precisa precisa fazer a confereência com todas as linhas para saber se já tem algo lá, mais complexo

#Tem o diagrama do circuito de cada um, separando Tag, tudo mais


#Além disso tem as politicas de substiuição dentro dos conjuntos.
    #Sera o LRU, FIFO e NMRU (Que é o fodase, coloca em qualquer um)

#Quando ocorre uma escrita?
    #Peço o endereço do mesmo jeito:

    #Se dá hit, eu posso escolher usar modelo Write Through, que escreve sempre na cache e na memoria principal, ou o Write Back, que só escreve na memoria quando o bloco vai ser removido da cache

    #Se dar miss, pode escolher copiar o bloco da memoria e escrever nele na cache ou ir escrever direto na memoria'


#calculo do tempo média é o Tempo do Acerto + Probabilidade de Error * Tempo se Ocorrer Error
    #Para diminuir cada um tem os "upgrades" de hardware especificos
