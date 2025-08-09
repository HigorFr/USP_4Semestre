#Aula 2

    #Correção do Problema
        #Tipos de circuito

        #Combinacional
            #Efeito se propaga e a saída já é afetada
            #"Passado" não é levado em conta

        #Sequencial
            #Alteraçãoes em Ciclos
            #Registrador é onde acaba o circuito combinacional
            #Precisa do clock para gravar (Para o valor "Passar por ele)

        #Edge
            #Mecanismo para pulsar um sinal sincronizado com o clock apenas uma vez
            #Bem simples, ele só salva se o botão foi apertado e vai jogar no proximo clock, depois resetar em seguida
        

        #Conforme ele vai avançando, ele vai adionando módulos no sistema, no geral bem simples
            #Primeiro vai somando manualmente, depois vai em só uma soma com o que já existe
            #Depois adiciona um mutiplexador para definir entradas
            #AInda, ele compacta o circuito, compressa ele em uma interface para realizar somas gerais

        #Precisa ficar ciclando as máquinas (Cada uma tem uma interface), e ai ele vai resolvendo através de um contador (Que literalmente só soma um por clock)
            #isso vai para um mutiplexador e para um demutiplexador (Ele seleciona saídas, diferente do mult, que seleciona entradas)
            #Depois ela retorna para a maquina original, só tendo passado pelo mesmo somador

        #Instruções
            #Formatos
            #Tipo de memorias
            #Palavras
            #Slide            

        #unidade de controle
            #Recebe instrução e coloca para todos lugares que precisa