#Aula de sexta de noite a qual com certeza estou muito animado

#Lembrando scoreboarding
    #Dispacha todas em ordem mas pode acabar fora de ordem dependendo das instruções
    #Ele tinha uma maneira diferente de tratar cada conflito, os WAW, RAW e WAR.
    #Se duas instruções forem escrever ao mesmo tempo, então considera sempre a mais antiga



Exemplo conflitos:

#Considerando:
L 1
A 2
M 2
D 6



Sem Conflitos
I div $r4, $r4, $r5
I or $r1, $r0, $r5
I add $r2, $r3, $r5
I lw $r7, 120($r6)

#Não vai dar nenhum conflito, todos os registradores estão de acordo e vão rodar idealmente.

Read after Write
I div $r4, $r4, $r5
I lw $r1, 120($r4)
I add $r2, $r3, $r5
I or $r8, $r6, $r7


IF  ID  OPR  D1  D2  D3  D4  D5  D6  WB
    IF  ID   OPR OPR OPR OPR OPR OPR OPR? OPR? D1 D2 WB
        IF   OPR D1  D2  WB
             IF  ID  OPR D1  WB


#Aqui travou no OPR, pois ningué, está usando a memoria, mas ela ainda precisa de dados pendentes
#Note também que ele sempre roda mais uma vez um ciclo repetido (mesmo que já esteja livre o que ele espera), para descobrir que ele pode continuar em OPR
                        
Conflito Estrutural
I div $r4, $r4, $r5
I add $r2, $r3, $r9 (Esse 9 era 4, mas para facilitar observar, foi trocado)
I add $r0, $r5, $r6
I or $r8, $r6, $r7


IF  ID OPR  D1  D2  D3  D4  D5 D6 WB
    IF ID   OPR D1  D2  WB
       IF   ID  ID  ID  ID ID  OPR D1   D2 WB 
            IF  IF  IF  IF IF  ID  OPR  D1 D2  WB
                                
#Note que aqui travou em ID pois como o comando é o mesmo, ele sequer pode entrar no OPR
#Note também que ele sempre roda mais uma vez um ciclo repetido (mesmo que já esteja livre o que ele espera), para descobrir que ele pode continuar em ID

WAW e WAR
I div $r4, $r4, $r5
I or $r8, $r6, $r7
I add $r9, $r4, $r8
I lw $r8, 120($r6)


IF  ID  OPR  D1  D2  D3  D4  D5  D6  WB
    IF  ID   OPR D1  WB
        IF  ID  OPR OPR OPR OPR OPR OPR D1  D2  WB
            IF  ID  OPR OPR OPR OPR OPR OPR OPR OPR OPR D1  D2  WB                       (Essa linha ta errada eu acho)



#===========Tomasulo================
    #Invés de utilizar variaveis definidas e obrigar o assembly a montar de uma maneira, você utiliza $X por exemplo para especificar "Utilize um registrador novo qualquer"
    #Dessa maneira, ele pode evitar redundancias feitas pelo código, já que mesmo variáveis que estão sendo utilizadas podem travar desnecessaraimente o pipeline.
    #Isso é "Renomear" registradores Exemplo slide.

#Aqui terá adiantamento
#Se um registrador será sobrescrito, ele simplesmente não escreve o valor antigo em um registrador, ele só vai passar o valor lá dentro quando for usado por outro registrador.

#Memoria RAM não será renomeada, só registradores.

#Estações de reserva amrazenam comandos (Qi, através de um numero)

#Isso vai funcioanr como uma outra tabela extra 

