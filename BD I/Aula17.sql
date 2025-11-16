#Parte final da diciplina
#Normalização



#Relacionado à qualiade do banco de dados
    #Na prática é muito dífiicl as pessoas seguirem a estrutura certa
    
#Semantica dos atributos
#Sem informação redudantes (Evita anomilia na hora de atualizar) (Cai na prova)
#Poucos valores nulos em tuplas
#Impedimento de tuplas ilegítimas


#Um banco de dados nunca está normal, isso é um adjetivo atributdo as tabelas

#Bom esquema
    #Facil de entender
    #Consultads corretas

#No nivel fisico
    #Melhor aproveito da memoria
    #Mais eficiencia nos acessos

#Ter boa divisão de tabelas, para deixar cada dominio bem definido
    #Evita redudancia, facilita atualizações etc...
    #As vezes ter dados em conjuntos é melhor do que ter tudo em uma tabela só, mas depende do caso
    #Desnormalizar (Para melhorar performance, principalmente de JOINS). Pode gerar redundancia mas fazer o que.
        #Guardar Departamento e Funcionario em uma mesma tabela, por exemplo
        #Inclusive pode gerar problemas, caso eu apague o ultimo funcionario de um departamento, o departamento some tbm
        #Além disso, se a chave for o empregado, não tem como criar um departamento novo sem funcionario dele.
            #E se for alterar o gerente? Vai ter que alterar em todas as linhas
            

#na prova pode mostrar um projeto pedindo para mostrar anomalias


#Anomalias
    # N anotei

#Se a grande maioria dos valores forem nulos em um atributo, é melhor criar uma tabela separada para esses atributos


#Noramlizar é sempre quebrar uma tabela em duas ou mais tabelas

#Dependencias funcionais
    #Usando elas você pode idenficiar em que forma normal a tabela está
    #Nada é visto pelo banco de dados físico, tudo relacionada a normalização é pelo projeto lógico e a semantica do minimundo
    


#Formas normais
    #1FN
        #Proibe atributos multivalorados, compostos e relações aninhadas
        #Todas tem que ser isso pela definição de tabela relacional
        #Fala-se "Normalizei em 1FN, 2FN etc..."

    #2FN



    #3FN
    #FNBC
    #4FN
    #5FN
    #DNF