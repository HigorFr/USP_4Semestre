#Aula 1

#Professor Norton
#Sistema Operacionais

    #Graduado em Física, mestrado e doutorado em ciência da computação
    #Não tão focado em epsquisa de SO, mais em foco em visão de programador

    #Gosta de devaneios (muito)

    #Bib:. Não seguiu a risca pra fazer slide mas é "Andrew Modern Operating System"
    #P1 02/10
    #P2 14/11
    #Psub 27/11 (Só caso você não fez prova)

    #2 EPs - Grupo de até 5 Pessoas

    #Cad ep é 2, P1 é 2,4 e P2 e 3,6 da média

    #Fórun do eDisciplinas

#Multithread e Escalonamento e outros assuntos






#Conceitos Overview

#Sistema Computacional
    #Consiste de muito equipamentos
    #Programador precisava saber como lidar com todas as partes, SO faz esse serviço agora
        #Hardware era cru, não tinha driver
    #É uma camada que conversa com o programa para o usuário não precisar fazer mais doq devaneios
    #Organiza memória, programa, usuários da máquina
        #Quando o SO te dá um endereço de memória, não é na memória fisica, ele gerencia memórias para cada programa para que não ocorra erros

    #Isso tornou o coneceito de máquina mais flexível, você pode trocar pessas, trocar períférios entre outros, além de organizar melhor os recursos
        #Principal comunicador com os programas, mas interage com o usuário diretamente através dos comandos
    

    #DOS E Unix tem comandos proprio (DOS que criou o Windows), antigamente era mais variado mas na atualidade afunilou nos 2 kernel
    #LS / DIR
    #CP / COPY
    #RM / DEL


    #Veremos chamada ao SO, que é mais complexa do que se aparece, interrupção do SO no processador entre outros
        #Não necessariamente é para um computador, pois ele gerencia dispositivos
    
    #Importante entender comprotamento dele e ponte com outros componentes, tipo cache, pois isso faz diferença na programação, por mais que no papel e abstratamente seriam coisas iguais



    #Tipos de memória
        #ROM - Read Only Memory
        #Armazenada BIOS (Programa basico de entrada e saida)
        #Post
        #CMOS (Baterizinha na placa mãe)
            #Grava data e hora, na teoria ela dura muito tempo
        
    
    #O que rola quando aperta o botão de ligar de fato
        #Processador roda a bios, jogada na hora no processador sem conferir navegador
        #Power-ON self test (post) vai conferir os dispositivos conectados, e comparar com o que já estava na CMOS, e vai atualizar eles (Ver se conectou algo novo, se algum saiu etc...)
        #A bios depois vai chegar qual disco de boot no cmos, copiar e jogar pra rodar, também nem vai conferir, só jogar no processador
        #Boot coloca na ram o kernel do SO que estava no hd
        #Dai o kernel assume a partir de então o computador

    #programa não é processo

    #Tem dispostiivos de Entrada e saída
        #SO tem uma assinatura para cada função
        #Os dispostivios tem que vir com um driver, programa de ponte fornecido pelo fabricante
        #Isso está no nucleo, os drivers. Como é algo de fora, isso em segurança é bem perigoso
        #Varia de SO pra SO


    #Em suma, tem mutias complexidades em uma máquina e o sitema operacional gerencia tudo isso através de algoritimos
        #chamadas ao SO são caras em tempo
    












