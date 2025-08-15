#Aula 4

#Não são programas extamente que rodam. São processos
#Dá para rodar mais de um programa em um mesmo processo.
    #Ele é todo contexto do programa. Ou seja, ele é versátil para ser guaraddo e colocado como se nada tivesse ocorrido
    

#Programa x Processo
    #Programa é basciaemnte o código, o seu .py, o processo é a instância de cada um dele (Isso é óbivo, pois eu posso abrir vários google chrome, ou vários .py por exemplo)
    #Processo é bem distinto entre sí, com as informações proprias dentro do registrador
    #Dificilmente o usuario vai fazer diretamente um processo


#Procesos pode ser de segundo plano (Deamons)
#Esses processos são criados para não ter interação entre usuário
#Um programa sempre terá virtualmente uma mémoria "virutal" infinita para usar (64Bits)
    #SO vai gerencair isso para que a memoria que você de fato tem não seja ultrapassada
    #Esse espaço de memoria (Espaço de endereçamento)
        #1 - Stack
        #2 - Vazio para expandir (Seja dado para cima, ou stack para baixo)
        #3 - Dados (Para serem usados)
        #4 - Texto (O código)

#Curiosidade, váriaveis globais são jogadas no segmentendo de data pré difiniamente

#Pilha de execução
    #Já visto em assembly
    #Guarda tudo na stack conforme chamadas de "funções"


#Contexto do processo
    #Várias cosias (Metadadados)
    #Quota, prioridade, Dono, nome do processo
    #Basicamente faz um jump para o processo

#Criar processo
    #Praticamente todo programa é um inciaidor de processo
    #No unix o processo de criação de processo duplica um já existente (Fork)
        #Por um instante dois procesoss iguais existe, uma linha depois ele mata o pai para que ele vire um processo novo, limpo. É separado por um return que indentifica (0, você é filho, -1 deu erro no fork ou um numero que é o endereço do filho, indicando que você é o pai)
        #Isso permite o filho rodar um pouco enquanto ele ta sendo resetado, compartilhando de todos descritores e rodando simultaneamente, não precsiso fazer uma estrutura inteira para os processos conversarem.
        #Diagrama nos slides msotrando melhor


#Hierarquia de Processo
    #Linux -> Pai conhece o pai, e o filho não sabe quem o Pai
        #isso quando fica escalonado forma uma árvore (um Clan )
    #Todo processo vem de um processo pai chamado init que é formado quando o sistema é ligado
    #Quando um processo da problema, os filhos dele são assumidos pelo avô


#Fianlziação de processo
    #Quando dá erro, tipo divisão por zero
    #Ou por termino involuntario, causado por outro processo, tipo um Kill no UNIX ou um processo matando o filho


#Estado de processo
    #Executando - No processador
    #???
    #Pronto - Não ta rodando, mas poderia estar
    #Zumbi no linux - Uma coisa que não deveria estar rodando mas está consumindo memória (Quando filho perde ligação com pai) 



#Todo processo termina e fica marcado para ser apagado, e noramlmente o pai quando chama o WAIT() o SO elimina.
    #Ou seja, por algum tempinho a task fica zumbi. Contudo as vezes o pai pode perder o endereço do filho e o zumbi ficará lá
    #É raro acontecer. 


#Gerenciamento feito por tabela
    #BCP guarda conteúdo do espaço de endereços do processo, assim todo processo tem  seu espaço de endereços e o próprio BCP (Inclusive BCP guarada os registadores para fazer ele rodar)
        #BCP No final é uma estrutura de dados, guarda vários dados, estados,registradores, CPU, quando foi executado, tipo metadados do processo
    #Tabelinha com vários endereços de BCPs, isso facilita acessar, as vezes ela já tem certo metadadaos para economizar acesso à memória
    #Isso será parte do EP (Um arranjo de ponteiro para um BCP)
    
#Filas
    #Também tem filas de processos, normalmente separadas naquelas bloqueadas e as prontas, isso facilita gerenciamento pelo CPU para deixar tudo mais rápido.
    #Isso é um dado redudnante do BCP, mas aqui ele está estruturado só pra ir pegando e rodando

#*Normalmente filho sempre nasce pronto



#Transições
    #Rodando -> Bloqueado (Ta esperando entrada e saída)
    #Rodando -> Pronto (Acabou tempo de rodar, depois ele volta)
    #Bloqueado -> Pronto (Chegou informação de Entrada e saída)
    #Pronto -> Rodando (Escolhido para rodar essa vez)

    #Dependendo da política do SO dá para ir de bloqueado direto pra rodando, mas isso não seria meio que "Justo" que é uma das premissas de qualquer SO, pois daria uma prioridade sem sentido.

    #Impossível ir de pronto para bloqeuado, não tem como saber se ele precisa de entrada e saída antes de passar pelo processador


#Escalonador
    #Faz a troca de processos e define quem é o proximo pra rodar
    #Inverte prioridade (As vezes o com mais prioridade tem que sair do lugar para o com menos entrar devido uma dependência)
    #Nivel baixo do SO, junto com dispatcher (O Escalonador recebe dele).
    #Depende de políticas e algoritimos para funcionar









