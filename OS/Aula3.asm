#Chamadas ao sistema

#Entradas e saídas são privilegiadas, precisam estar no modo Kernel, o OS faz essa barreira
#Chamada ao sistema é a interface para o modo Kernel no geral, no fim quem realiza tudo é obivamente o hardware
#Escrever na tela, acessar HD, memória etc... mas cada OS pode ter a propria



#Instruções TRAP (exceção ou interrupção de software)
    #Feitas no hardware
    #Elas que vão virar o syscall
    #Aplicação -> Chamada so sistema -> Nucleo -> Hardware

    #Quando o trap é feito, o processador vai entrar em modo kernel, no geral ela vai pegar o conetúdo de todos registradores e guardar, para então ir em uma linha da memória e jogar o nuclero do SO para rodar

    #Ela então faz um Jump para uma tabela de instruções, (é tipo uma tabela com linhas da memoria e o que ela faz dependendo da instrução)

    #Quando termina o SO volta o registradores de volta para o modo kernel, como se nada tivesse acontecido fisicamente quando o SO foi chamado

    #Isso varia conforme a arquitetura
    #Atualmente a rotina de tratamento (Serviço, Aquela que depende do JUMP) que faz o salvamento dos registradores, pois isso economiza tempo de acesso à memoria. 

    #Normalmente os registradores ficam guardados na memória


#exemplo de instrução
    #Read() -> Slide tem mais informações
    #Ela na pratica é sempre a ordem de tratamento



#Dispatch 
    #Primeiro chamado pelo TRAP no programa, ele é travado na memória e o HARDWARE sabe onde que está
    #Ele que vai mandar para tabela com todos os serviços o valor referente.
    

int 0x80 é a instrução análoga ao Syscall do MIPS (Isso em X86)
#Do mesmo jeito o eax e o mesmo que $V0

#"Contexto" é o nome dados para as variaveis nos registradores atualmente, então salvar o contexto é salvar o estado atual.


#O que aconteceria se não se chamar o exit no syscall?
    #Olhando na arquitetura de pipeline, a proxima instrução está sempre engatilhada
    #Então se o program não para como deveria, o comando aleatorio que vem na sequencia da memoria.
        #Normalemnte é um dado invalido, o que irá acionar a TRAP para iniciar a rotina de limpeza .(Muito extensa e chata) (Instrução inválida)
        #Se for instrução, vai rodar e vai dar um BO do caramba. Mas é raro

#MAS O COMPILADOR sempre vai colocaro exit(), para evitar isso, é padrão de todo compilador.


#Wrappers (Empacotador)
    #Atualemnte quase tudo tem isso, normalmente todas as linguas
    #É uma biblioteca do OS para criar uma interface de chamada para ser mais flexível
    #Da para escolonar eles para limitar ainda mais funcionalides (O ScanfF do C por exemplo passa por 2 para chegar no read() do SO )
        #O Trap ocorre dentro deles, mas eles em sí ficam no espaço de usuário

    #Isso evita muita coisa, nenhuma lignaugem tem que ficar mudando nome de função de acordo com a interface. Isso fica mais genérico


#interrupções
    #O kernel consegue parar o programa atual rodando, são TRAPs travadas no HARDWARE de fora do processador independente do que está lá
        #A interrupção já faz ficar no modo kernel e o SO consegue fazer o que precisa
    #Pode vir de qualquer lugar, driver, impressora, HD
    #Então o hardware tem uma lista de cosias que ele pode pedir, e o SO estará pronto para fazer (ele é feito com base nele).
        #As vezes ele olha um registrador especifico, algum lugar na memorika espeficia.
    
    #A todo momento no pipeline ele pode ser ativado para parar tudo e colocar para tratar.

    

#Trap x Interrupção
    #Trap é chamado pro software, programa, intrução ilegal (dividir por 0)
    #Interrupção é sempre fisica


#A ideia do DOS é semelhante tanto no hardware tanto em rede
    #Gera interrupções em massa para placa de rede do computador entupir o CPU com interrupções
    #Hoje em dia precisa de DDOS para alcançar uma massividade da rede com relação ao hardware


#O que será salvo do contexto quando o serviço for rodar?
    #Obrigatoraiemnte o contador de programa, mas nem sempre
    #Se ele for sobrescrito pela rotina de tratamento pode dar problema
    #Pilha do usuario entre outros


#Isso tudo foi no modelo sequencial, mas em modelos mútiplos atuais há interrupção de interrupções
    #Isso exige um encadeamento de registradores para garantir o funcionamento (Toda hora eu guardo o contexto do contexto)
    #Isso vai depender da priorirade cada driver terá o seu


#O clock também gera interrupção para garantir que o SO rode periodicamente

#Isso abre margem para dar muitos erros que serão vistos deposi


    




