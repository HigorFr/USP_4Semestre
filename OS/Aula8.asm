#Aula 8

P1 07/10
P2 ???


#Controle muticiclo
    #Instruções complexas precisam de mais de um ciclo de clock, e para isso é necessário um registrador
    #Então entre cada etapa serã armazenados valores para o proximo ciclo
    #no geral divisão é feita em 5 passos, e com os registradores eu posso pular etapas inúteis.
        #Um branch vai ser agora 3 passos


#As operações tem um nome especifico dentro do diagrama. (ALUOUT, IR[], PC etc...)

#Para isso funcionar é necessário uma máquina de estado para esturuturar o processo, isso ta no slide

# Lw 5
# Lw 5
# Beq 3
# Add 4
# SW 4

#21

#Está O load word está somando deslocamento na memoria

# 16










#Pipeline
    #Também já visto em oacI, vocẽ carrega através de buffers (Registradores fetios de flipflops) todos os comandos, e separa em 5 etapas todo processo
    #Dessa forma cada clock pode ir "andando" com as opeações.





