#Funções agregadas
    #Professora ta ligada que todo mundo meteu o loko


#Reliza operações em agregações de colunas, através de um conjunto de linhas, retornando um valor único para cada linha igual.
    #Ou seja, a média de todos os funcionarios por departamento, o total de vendas por mês, etc.
    #Exemplos:
        #COUNT() - Conta a quantidade de linhas
        #SUM() - Soma os valores de uma coluna numérica
        #AVG() - Calcula a média dos valores de uma coluna numérica
        #MIN() - Retorna o valor mínimo de uma coluna
        #MAX() - Retorna o valor máximo de uma coluna

#Como funcionam em valores nulos, elas tem comportamentos diversos
    #Count(*) por exemplo vai retornar a quantidade de linhas, independente se tem valor nulo ou não
    #Um count(coluna) vai ignorar os valores nulos e contar apenas os valores não nulos
    #Se o resultado da consulta (que o resultado é sempre uma tabela) for vazio, o resultado será 0 em um count por exemplo
        #Ou seja count nunac retorna NULL, outras funções (SOma, media, minimo, maximo) retornam NULL se o conjunto de linhas for vazio
        #Média é soma de valores não nulos dividido pela quantidade de valores não nulos
        #Do mesmo jeito soma é a soma dos valores não nulos.


#OBS na hora de formatar where, eu posos usar where <atributo1, atributo2> = tabela x com os 2 atributos, isso é válido


Pegar o Agregado de algo esecifico tem que ser no where, ou seja where slario = (select max(salario) from funcionario), da pra usar In também;
Se eu fissese select pnome, min(salario) from funcionario estaria errado, até porque o min(salario) retornaria um valor único, mas o pnome poderia ser vários, então teria que agrupar por pnome também, o que não faz sentido.





#para resolver coisas assim facilitadamente, podemos usar o Group by

#ELe agrupa as linhas que tem o mesmo valor em uma ou mais colunas, formando grupos de linhas, e então aplica a função agregada em cada grupo
    #Exemplo: Quero a média salarial por departamento
        #Select dept_no, avg(salario) from funcionario group by dept_no;
            #Isso vai agrupar todos os funcionarios por departamento, e calcular a média salarial de cada departamento


Também tem como filtrar pelo resultado do group by, usando o having
    #Exemplo: Quero a média salarial por departamento, mas só dos departamentos que tem mais de 5 funcionarios
        #Select dept_no, avg(salario) from funcionario group by dept_no having count(*) > 5;
            #Isso vai agrupar todos os funcionarios por departamento, calcular a média salarial de cada departamento, e só retornar os departamentos que tem mais de 5 funcionarios



    