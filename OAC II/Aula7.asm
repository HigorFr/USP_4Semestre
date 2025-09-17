#Aula 7, agora estamos vendo os comandos, já vistos em OAC instrução

#Exericcio de fazer MDC em assembly


ADDIU $r0 35
ADDIU $r1 15

Maior:
SLT $r2 $r0 $r1 #SE  r0 < r1 ele já ta certo
BEQ $r2 $0 Loop
ADD $t0 0 $r1
ADD $r1 0 $r0
ADD $r1 0 $t0

Loop:
ADD $r3 $r1 $0
SUB $r1 $r1 $r0
SLT $t0 $0 $r1  #Se ainda é maior que zero eu não pualo
BEQ $t0 $0 Final
BEQ $r1 $0 Final
J Maior


Final:
#O $r3 que é o máximo divisor comum

