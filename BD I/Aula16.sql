#Comparação de string

# O _ e o % podem ser usados em conjunto para fazer comparações mais complexas
    #Exemplo: Quero selecionar todos os produtos cujo nome começa com 'A', seguido de qualquer caractere, e termina com 'C'
        #Select * from produto where nome like 'A_C%';
            #Isso vai selecionar todos os produtos cujo nome começa com 'A', seguido de qualquer caractere, e termina com 'C', seguido de qualquer sequência de caracteres


#Ou seja o _ representa um único caractere, e o % representa qualquer sequência de caracteres (inclusive nenhuma)


#Dá para inverter a lógica do like usando o not like


#Usado um caractere escapado
#Voce pode definir um caractere especial para ser usado como escapamento em uma string, usando a cláusula ESCAPE
    #Exemplo: Quero selecionar todos os produtos cujo nome contém o caractere '%'
        #Select * from produto where nome like '%\%%' escape '\';
            #Isso vai selecionar todos os produtos cujo nome contém o caractere '%', usando '\' como caractere de escapamento

#Por padrão o escapamento é '\', mas pode ser definido outro caractere qualquer            


#Isso é útlil quando você quer buscar por caracteres especiais que são usados como curingas no LIKE, como '%' e '_'
    #Se você não usar o caractere de escapamento, o banco vai interpretar esses caracteres como curingas, e não como caracteres literais



#IN e BETWEEN
#O IN é usado para verificar se um valor está dentro de um conjunto de valores
    #Exemplo: Quero selecionar todos os produtos cujo preço seja 10, 20 ou 30
        #Select * from produto where preco in (10, 20, 30);
            #Isso vai selecionar todos os produtos cujo preço seja 10, 20 ou 30
#BETWEEN é usado para verificar se um valor está dentro de um intervalo de valores
    #Exemplo: Quero selecionar todos os produtos cujo preço esteja entre 10 e 20
        #Select * from produto where preco between 10 and 20;
            #Isso vai selecionar todos os produtos cujo preço esteja entre 10 e 20, inclusive 10 e 20


#O ANY e o ALL são usados para comparar um valor com um conjunto de valores retornados por uma subconsulta
    #Exemplo: Quero selecionar todos os produtos cujo preço seja maior que o preço médio dos produtos
        #Select * from produto where preco > any (select avg(preco) from produto);
            #Isso vai selecionar todos os produtos cujo preço seja maior que o preço médio dos produtos
    
    #Exemplo: Quero selecionar todos os produtos cujo preço seja maior que todos os preços dos produtos em promoção
        #Select * from produto where preco > all (select preco from produto where promocao = true);
            #Isso vai selecionar todos os produtos cujo preço seja maior que todos os preços dos produtos em promoção



#Definir tuplas em comparações é usando <>

#Order By ordena o resultado de uma consulta
    #Tem prioridade em uma ordem, ou seja, NUMERO ASC, NOME DESC etc...


#Divisão em SQL
#Não existe uma operação de divisão direta em SQL, mas podemos simular essa operação usando sub
#Será utilizado not exists e except
#Exemplo no slide




#Inserção em DML
    #AS tuplas que vão popular a tabela podem ser definidas diretamente no insert, ou podem ser o resultado de uma consulta


    #Não prestei atenação aqui
