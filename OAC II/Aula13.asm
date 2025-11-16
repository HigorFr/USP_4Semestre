#Agendamento
    #Bascaimente o compilador agenda isntruções para poder colcoar uma na frente da outra no Superpipline

#Storyboard ou Tomazulu??

#Solução 1 - Storyboard, Execuções fora de ordem se possível (Ou seja, não há conflito e há recursos)
    #Divido em:
    #Despacho (Decofificação e Confere por Conflitos)
    #Leitura de Operando (Onde ela espera se tiver conflito e onde o operando vai ser lido (O Op code) )
    #Execução agora pode variar mesmo em uma mesma instrução
        #isso gera novos tipos de conflito
    #E escrever o resultado


#Conflitos
    #WAW - Escrita após Escrita
        #Só vai permitir despacho enquanto a primeira escrita não tiver terminado (Ou seja, fica parado no despacho)

    #RAW - Leitura após Escrita (Quero ler algo que ainda não foi lido)
        #Segura a instrução na leitura de operando

    #WAR - Escrita após leitura
        #Seguro na execução


#O que será anotado no SCOREBOARD de fato:
    #Estado de instução (Indica se está no depacho, leitura, execução ou escrita)
    
    #Estado das unidades funcionais, (9 Valores distintos que ajudam no controle)
        #É a principal parte, cada um dos valores está especificado no slide
        #Unidades funcionais = ULAs  (que agora são mais de uma), e a memoria
        #Cada uma delas será uma linha, e cada nove valores serão uma coluna

    #Resultado de cada registrador


    #Ou seja:
    #Estados da instruções, estados da unidade funcional e estados de resultados de registradores




#Despacho
    #Buffer guarda instruções, se encher o PC para
    #Ele já vai alterando os valores dos registradores da unidades funcionais

#Ler operando
#N anotei

#Execução compelta
#N anotei

#Escrtita de resultado

#Pode ocorrer conflito na RAM, pois o endereço (Depois de soamr o deslocamento) pode ser o mesmo. (Tomazulu resolve isso)
    #Perceber conflitos em memória ram é muito difícil no geral. (Até porque é imposível mapear com flags todos os gigas de RAM)
    #bli

