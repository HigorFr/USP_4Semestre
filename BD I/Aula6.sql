#Colocar conceitos em dias (Espero que não seja uma possível prova surpresa)




#conceitos
    #Projeto Conceitual -> Entrega diagrama de entidade-relacionamento. (Não há tabela, não há relação, isso é do projeto lógico)
    #Projeto Lógico -> Entrega Esquema do banco de dados


#Modelos SGBDs que utilziam MR são chaamdos SGBDs Relacionais

#MR representa os dados do BD como relações.

#Relacionamento é conceito do Projeto conceitual, Relação é uma lista, que vem do projeto lógico.




#Modelo Lógico
    #Tabela, cada coluna se refere à um Atributos
    #Cada linha da tabela é denominado tupla
    #Defino o domínio de cada dado. (Tipo, tamanho, etc)
        #SGBD vai conferir isso

    #Tem um esquema para definir relação
        #   Nome(atributo1,atributo2 ... etc)
        #Grau de relação é a quantidade de atributos que compõem a relação.

    #Domínios também tem que ser definidos por um padrão
        # dom(nome do domínio/atributo): descrição
        # Ex: dom(cpf): número de 11 dígitos

    
#Notação do banco de dados em sí
    #Como os a teoria do COD foi bazeada em algébra de conjuntos, assim se baseou a teoria do banco de dados. Foi pensado em termos de teoria.
    #Contudo será uma algebra modificada para mexer em relações, "Algebrá realcional"

    #Primeiro será consultas da algebra relacional, para depois fazer consultas (Que serão traduzidas) para SQL

    #Tabela na notação relacional é R(A1, A2, An). A ordem dos atributos tem uma definição lógica.

    #Uma tuplas t (T minusculo) em um estado de ralação r(R) é feito com t = <v1,v2 ... vn>
        #Vi é valor do atributo Atributos
        #Exemplo <'12345678901', 'João da Silva', '1990-01-01'>

    #Recuperar valore é com []
        t[nome do atributo]


    #SuperChave
        #t1[cpf] diferente de t2[cpf]
        #Ou seja, são um subconjunto de valores com valores obrigatoriamente distintos em uma realação.
        #Então é diferente de "Chave", pois pode ser um conjunto. (Endereço + ID) é único, (Porque obivamente ID é único), logo é "Superchave" pois o conjunto é distinto.
        
        #Para ser "Chave" precisa ser mínimo. Elas são candidatas e arbritariamente uma pode ser definida como primaria, fazendo as outras serem secundárias.
            #Toda realação por definção precisam de uma chave primaria.
            #Toda tabela por definição também não pode ter linha dupla

        #Superchave deafult é a junção de toda a tupla

        #Uma chave pode ser composta por 2 ou mais  atributos para existir, ou seja, porque o "mínimo" para identificar a tupla precisa de duas colunas
            #Exemplo: (Id do trabalho + id do funcionario )

        #O sgbd vai sempre usar chave para recuperar uma tupla da relação


        #Os atributos que formam a chave primaria fiacam sublinhados


#Restrições de integridade
    #Por definição uma dentro de cada tupla o valor do atributo Ai deve ser atômico em seu domínio.
        #Por isso que atributos compostos são marcados, para ser feito em uma tabela

    #Restrição de chave
        #Valor de chave precisa ser único

    #Restriçãod e Entidade
        #Valor não pode ser NULL


#Chave estrangeira vai fazer referência à uma chave primaria em outra tabela
    #Tem que ter compatibilidade de domínio, ou seja, a definição do atributo igual.
    #Ou ela ocorre e existe em outra tabela ou é NULL (OU corresponde ou não)
    #Chave estrangeira é sempre aquela que sai, e vai pra uma chave primaria de outra tabela.

    #Relação fraca no modelo conceitual tem uma chave parcial, e por isso noramlmente utiliza chaves agrupadas como chave estrangeira para a entidade principal.



#Exercício no slide
    #Com o resultado formatado que nem no exemplo. Esquema do banco de dados
    #Isso será uma das entegas do trabalho







