#Processo em tempo real, eles não são longos.
#Programas nesse sistemas normalmente são picotados em vários pacotes pequenos
#lembrando que tem prazo para se tratar cada processo


#Eventos periodicos 
#Eventos aperiodicos
    #Autoexplicativo

#Não há resolução clara para solucionar esses problemas de ordem

#Escalonar processos periodicos
    #Para conferir se eles são periodicos existe uma formula, que para cada i processo a soma de (Computação usada/ Periodo entre reinicio) tem que ser menor que 1 (Considerando 1 processador)


#Esses processos como são escalonáveis, a decisão de prioridade de onde ele chega pode ser definida antes, diferente dos dinamicos (Aperiodicos)



#Primeiro algoritimo RAte monotonic Scheduling
    #Todo processo termina dentro do Periodo
    #O com maior priodade é sempre aquele com a maior frequencia (Ou menor período, mesma coisa)
    #Sempre executa o com maior Prioridade
    #Os processos não escalonáveis ficam pra roda por ultimo "roda ser der tempo"
    #Define de antemão as prioridaes basciamente, depois isso só mantém


#ALgoritimos não periodicos não podem ser usadaos para periodicos, o inverso até que pode

#Eralist Deadline first
    #Para periodicos
    #O prazo mais curto primeiro, (O que vai acabar antes)
    #OU seja, ele olha quando vai "vencer" e sempre escolhe o que vence primeiro
    #Mesmo se não for periodico o processo sempre vem com as informações de tempod e de duração e "vencimento", então mesmo assim da pra usar




#Era isso de algorimo, nova matéria Threads






#================Threads=====================

#Processo nasce para fazer o agrupamento de recurso

#Até agora é imaginado 
#Thread é algo no campo das ideias, não existe fisicamente, todo processo tem uma thread (Que é a linha de execuação)
#É para organizar diferentes linhas de execução em um mesmo "código" de maneira que torna tudo "paralela"
    #É como sub-tarefas de um memsmo "processo maior", 
    #Cada threads só agrupam um conjunto de instruções e registradores, mas o espaço de memória do processo é compartilhado

#Exemplo, processar texto é uma thread, você pode escrever e já ir aparecendo
#"Mestre" e "Escravo", uma thread principal recebe e vai mandando para alguma thread escrava fazer enquanto o codigo principal não para. (muito usado em requisição de pagina web por exemplo)

#Threads em um CPU atualemnte podem escalonar por thread, e não por processo. Uma CPU de N threads podem ter infinitas threads "virtuais" (que só existam no software) e ele vai escolanonando dentro das N que ele faz simultâneas

#Threads são mais rápidas de criar e destruir, diferente de um processo que precisa limpar todo um contexto.

#Contudo as threads possuem acesso a toda memória do processo, e isso dá problema de segurança. Um navegador mal construido por exemplo, que usa guais como threads, pode acabar deixando uma aba visível à todas as outras já que é o mesmo processo.

#Manipuação de Threads
    #Criar e Matar
    #Join, Cria uma dependencia de espera de quem está chamando com o objeto, então se main chamar ThreadLegal.join() a main só continua depois de ThreadLegal terminar
    
#Podem existir organizações no espaço do usuário ou no espaço do kernel

#No espaço de usuário cada processo gerencia as threads que ele cria, então é a main meio que é uma thread que gerencia suas filhas. Como um trecho do seu programa para rodar.
    #Normalmente a Main sempre tem uma biblioteca interna para fazer gerenciamento
    #Isso não pode ser interrompido, o processo inteiro tem que ser parado se acontecer algo.
    #O SO nem sabe as threads que estão rodando, ele só continua escaloandno os processos (As mains), e elas continuam em sí escalonando as threads.
    #Outro problema nesse tipo de organização é que se alguma thread fazer O/S, todo processo para. ( O que meio que arruina com todo propósito da thread)
    #Esse é o modelo que não é usado atualmente por motivo óbivos    










    












