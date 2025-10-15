#Consulta aninhanda é aquela que usa uma consulta dentro de outra consulta para realizar um filtro.
    #Exemplo: SELECT nome FROM Funcionario WHERE salario > (SELECT AVG(salario) FROM Funcionario)
        #Isso vai listar os nomes dos funcionários que ganham mais que a média dos salários dos funcionários


    #Exemplo 2: SELECT nome FROM Funcionario WHERE departamento_id IN (SELECT id FROM Departamento WHERE nome = 'TI')
        #Isso vai listar os nomes dos funcionários que trabalham no departamento de TI


#Null é um valor especial, ele não tem valor e nem definicação clara. Usar algo do tipo = "NULL" é errado pois filosoficamente ele é não é nada
    #O certo é usar IS NULL ou IS NOT NULL, funções definidas para lidar com null