#Agora é DML e não DDL



#DML é Data Manipulation Language
    #É a linguagem de manipulação de dados
    #São os comandos que manipulam os dados dentro das tabelas
    #Exemplos: SELECT, INSERT, UPDATE, DELETE


#Já sei de quase tudo isso
    # SELECT lista atributos
    #FROM lista tabelas
    #WHERE condições
    #GROUP BY agrupa por atributos
    #HAVING condições de grupo
    #ORDER BY ordena por atributos
    #LIMIT limita o número de resultados
    #OFFSET pula um número de resultados
    #DISTINCT remove duplicadas
    #AS renomeia um atributo ou tabela
    #JOIN junta tabelas
    #ON condições de junção


#Já sei de tudo isso, não preciso anotar


    #usar várias tabelas no from é como um produto cartesiano, no filto eu escolho como vai ser a restrição
#Tem como renomear durante o FROM, isso é para facilitar o WHERE
    #Exemplo: FROM Funcionario AS F, Departamento AS D
        #Ai no WHERE eu uso F e D para referenciar as tabelas
        #Isso é útil quando tem várias tabelas com o mesmo nome de atributo


#(provavel que isso cia na prova)
#Tem operadores de atributos também aqui
    #Tem condições para funcionar: MEsmo numeros de atributos, mesmos domínios (par a par) (Compatíveis na união)
    #UNION - Junta resultados de duas consultas (Também some com duplicadatas)
    #EXEPT - Remove resultados de uma consulta que estão em outra consulta
    #INTERSECT - Pega só os resultados que estão nas duas consultas


#COnsulta aninhadas