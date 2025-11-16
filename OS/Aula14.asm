#Era para ver coisa online --------------------




#Independente da meneria que você implemtne a paginação o problema básico é que você precisa ficar trocando a memória.
#Algortimos definem isso, a maneira com a qual você vai trocar a página.


#Algortimo ótimo é o melhor possível, prevendo o futuro, absolutamente nenhum algorítimo na realidade vai passar desse. Usado somente como benchmark


#NRU - Não usado recentemente.
    #Registra bits forencendo se a página foi modificada ou referenciada no ultimo ciclo
    #Se ele foi referenciada, é provavel que ela seja referencaida novamente (Se você remover você vai precisar dela de novo)
    #Se ela foi modificada você precisa escrever no disco que demora.

    #No geral são classificado em classes, 00, 01, 10, 11, na ordem de melhor combinação para pior (Sendo o primeiro bit de referencaido e segundo de modificado)


#====Troca slide====


#Troca de página e implemntação da paginação

#FIFO - Primeiro qeu entra primeiro que sai.
#Você ordena as páginas pelo tempo que ela chegou e debrruba aquela que for mais antiga.
#Coloca a mais nova no fila

#Segunda chance -Versão do FIFO
#Adiciona um Bit R, que salva a referenciação. Se o bit for 1, mesmo se ela for a mais velha ela não será excluída e volta para o inicio da fila, até achar uma com o bit R em 0.
#Quando ela volta, o bit R também é setado em 0.

#Tem ainda uma outra versão do segunda chance, que faz uma lista ligada ciclica.
    #Funciona da mesma maneira, mas você economiza processamento pois não precisa trocar posições de nós.

#LRU - Muito caro, uma lista com todas as paginas e um contador de uso, removendo as mais antigas.
    #Isso não pode ser feito pelo SO pois seria muito custoso

    #Solução em Hardware
        #Invés de uso, utiliza instrução, que é mais precisamos
        #O proprio hardware conta e armazena na tabela de página.
        #Quando dá page fault, você olha a que tem menos usos para derrubar
        #É independente do tempo
        #É uma matriz de bit, que vai ligando os bits conformes não são usado. (Coluna é a pagina, linha é o tempo sem usar)
            #Se for acessada, ele simplesmente zera.
            #Gambiarra que dá certo

        #Problema: Se trocar a RAM você teria que trocar a MMU também, já que o tamanho seria novo.

    #Software
        #Foi o jeito, hardware não dava
        #A cada tick de clock você conta, não tem a precisão da instrução
        #Problema, elá não reseta contagem, então ele pode dar uma prioridade à paginas muito antigas que foram usadas muito.
            #Resolução disso foi por um "envelhecimento", que coloca o bit r de referenciamento como mais significativo na contagem.
            #Vira basicamente um NFU



#Working Set
    #Você carrega de ante-mão quais páginas um processo vai usar através de um cálculo
        #Na realidade esse calculo não existe.
    #Quando ele é reescalonado, você usa esse mesmo set salvo em uma memória.
    #O Working-Set na definição seria todas essás páginas usadas.

    #Problema: Salvar essas referencias.
        #Resolução, invés de ser preciso você chuta através de um tempo 


    #mais no slide

    #Adiciona um bit M

    #Você se precisar remover, vai procurar de preferencia um R 0 fora do range do working set, se for do working set você poupa ela.
    #Caso todas forem 1, nesse caso utilize o bit M de moficiado para exlcuir uma que não foi




#WS clock
    #Fica girando no working set, no pior caso todas estarão no working set.
    #Mais no slide



