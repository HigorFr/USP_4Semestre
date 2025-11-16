#Correção do exercicio da aula anterior.
#Em consutla aninhada, para cada tupla, está rodando a consulta interna, isso talvez torne o processmento muito lento, mas o tópico de tempo de consulta é assunto de BD II.
    #Importante é entender que existem diferentes maneiras de fazer a mesma consulta


#Diferentes tipos de JOINS


#INNER JOIN: Retorna apenas as tuplas que possuem correspondência em ambas as tabelas.
    #Não pode valor nulo nem de um lado nem de outro.
    #Exemplo: SELECT Funcionario.nome, Departamento.nome FROM Funcionario INNER JOIN Departamento ON Funcionario.departamento_id = Departamento.id
        #Isso vai listar os nomes dos funcionários junto com o nome do departamento que eles trabalham, mas apenas para os funcionários que estão alocados em algum departamento.


#Natural Join: É uma forma simplificada de fazer um INNER JOIN, onde o banco de dados automaticamente faz a junção com base nas colunas que possuem o mesmo nome em ambas as tabelas.
    #Não recomendado, pois não está explicito quais colunas estão sendo usadas para a junção, o que pode levar a erros se as tabelas forem alteradas.


#LEFT JOIN: Retorna todas as tuplas da tabela à esquerda e as tuplas correspondentes da tabela à direita. Se não houver correspondência, os valores da tabela à direita serão nulos.

#RIGHT JOIN: Retorna todas as tuplas da tabela à direita e as tuplas correspondentes da tabela à esquerda. Se não houver correspondência, os valores da tabela à esquerda serão nulos.

#FULL JOIN: Retorna todas as tuplas quando há uma correspondência em uma das tabelas. Se não houver correspondência, os valores da tabela sem correspondência serão nulos.

#Outer pode ser adicionado a LEFT, RIGHT e FULL JOIN para enfatizar que são joins externos, ou seja, que retornam todas as tuplas de uma das tabelas, mesmo que não haja correspondência na outra tabela, (Valores nulos por exemplo).
    #Por padrão é sempre inner join

    #Em resumo, tudo que é outer mantem todos os valores de uma das tabelas, mesmo que não tenha correspondência na outra tabela, preenchendo com null os valores que não tem correspondência.


#Asterisco em select * é para selecionar todas as colunas de uma tabela, mas não é uma boa prática, pois pode trazer colunas desnecessárias e impactar a performance da consulta. É melhor especificar apenas as colunas que você realmente precisa.


#Um full join não é um produto cartesiano, ele retorna todas as tuplas de ambas as tabelas, mas apenas uma vez para cada combinação de tuplas que possuem correspondência, e preenche com null os valores que não tem correspondência.
    #Produto cartesiano é quando você combina todas as tuplas de uma tabela com todas as tuplas de outra tabela, resultando em um número muito grande de combinações.

    #Em produto catersiano não há valores nulos
        #Ele não vai tentar juntar "nada com nada"