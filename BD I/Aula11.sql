#Prof disse para não estudar pelos slides, mas sim pelo livro


#Demonstração do Create Table, no DDL, tudo nos slides, tem estrutura específica.

#Create table nome da tabela
#Coloca os campos e o tipo de dado, tamanho dependendo qual o dado entre (), se pode ou não ser nulo
    #Pode definir um campo como DEFAULT, ou seja, se não for passado nenhum valor, ele assume o valor default

#Define chave primaria

#Define o que é único

#Define chaves estrangeiras e pode ser definido o que fazer em caso de delete ou update
    #Na definição de delete, o padrão é RESTRICT, ou seja, não deixa deletar se tiver chave estrangeira.
        #Pode ser definido como CASCADE, ou seja, se eu deletar a tupla que é referenciada, todas as que referenciam ela também são deletadas
        #Pode ser definido como SET NULL, ou seja, se eu deletar a tupla que é referenciada, todas as que referenciam ela ficam com NULL na chave estrangeira
        #Pode ser definido como SET DEFAULT, ou seja, se eu deletar a tupla que é referenciada, todas as que referenciam ela ficam com o valor default na chave estrangeira

    #Na do update é a mesma coisa, só que se eu atualizar o valor da chave primaria, o que referencia ela também é atualizado
        #Mas é uma má prática atualizar o valor da chave primaria, então não é usado

#CONSTRAINT é para definir uma restrição qualquer, como por exemplo, um valor maior que 0


#ALTER TABLE é para alterar o esquema da tabela, não os dados em sí
    #ALTER TABLE table <Ação>
    #Tem varias ações
        #ADD COLUMN
        #DROP COLUMN
        #ADD CONSTRAINT
        #DROP CONSTRAINT
        #ALTER COLUMN
    #Pode adicionar ou dropar colunas, ou adicionar ou dropar restrições
    #Pode forçar cascade em chaves estrangeiras que já existem


#=======================================

#Agora é algebra relacional
    #Manipulação dedos, relações
    #Adptação da teorias dos conjuntos, feita por Codd 1960
    #Foi feita para ser independente do SGBD, ou seja, não importa qual SGBD você use, a teoria é a mesma

#Operadores

#Projeção, Selecção e Junção
    #Projeção é selecionar colunas
    #Seleção é selecionar linhas
    #Junção é juntar tabelas

#Operações binárias
    #União
    #Interseção
    #Diferença
    #Produto cartesiano
    #Etc...


#Operações unárias
    #Projeção
    #Seleção
    #Renomeação
    #Etc...


#Seleção seleciona linhas que satisfazem uma condição, removendo duplicadas
#Projeção seleciona colunas para serem visíveis, retornadno uma tabela com o grau referente


#Relações Intermediárias
    #Pode ser usado para fazer operações em cima de outras operações
    #Exemplo: Selecionar os nomes dos funcionários que trabalham no departamento de vendas
        #Primeiro faz a seleção do departamento de vendas
        #Depois faz a junção com a tabela de funcionários
        #Depois faz a projeção dos nomes dos funcionários



#Pode renomear uma relação com o operador ρ (Rho)
    #ρ(novo_nome, relação)


#Tem as operações de conjunto também, feitas sempre nas linhas
#Para essas operações, as relações tem que ser compatíveis, ou seja, ter o mesmo grau e os mesmos domínios
    #Damos o nome Compatibilidade de União (Veio da restrição de domínio)

    #União (∪) junta
    #Interseção (∩) pega o mesmo
    #Diferença (-) pega o que é diferente
        
    #Produto cartesiano (×)
        #Combina todas as tuplas de uma relação com todas as tuplas de outra relação
        #O grau da relação resultante é a soma dos graus das relações originais
        #O número de tuplas da relação resultante é o produto do número de tuplas das relações originais
        #Usado para fazer junção




#Join é literalmente juntar tabelas
    #Tem vários tipos
        #Natural Join (⋈)
            #Junta as tabelas pelas colunas que tem o mesmo nome
            #Remove colunas duplicadas
        #Theta Join (⋈θ)
            #Junta as tabelas por uma condição qualquer
            #Não remove colunas duplicadas
        #Equi Join
            #É um theta join onde a condição é de igualdade
            #Não remove colunas duplicadas
        #Outer Join
            #Mantém todas as tuplas de uma das relações, mesmo que não tenha correspondência na outra relação
            #Pode ser Left Outer Join, Right Outer Join ou Full Outer Join


#Operação de divisão (÷)
    #Usado para responder perguntas do tipo "Para todo"
    #Exemplo: Quais os funcionários que trabalham em todos os departamentos?
        #Tem que pegar os funcionários que trabalham em cada departamento, e ver quais funcionários aparecem em todos os departamentos
    
    
    #A operação de divisão é feita entre duas relações
        #A relação dividendo (R) tem que ter pelo menos os atributos da relação divisor (S)
        #O resultado é uma relação com os atributos de R que não estão em S, e as tuplas são aquelas que aparecem em R para todas as tuplas de S


#No geral nos slides estão melhor especificados.

