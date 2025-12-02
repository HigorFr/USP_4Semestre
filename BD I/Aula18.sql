#atributo
    #Primario ou não (Se tiver na chave primaria é primaria)


#Determinação
    #Falamos que X determina Y (X->Y) se para cada valor de X, houver um único valor de Y associado
    #Exemplo: CPF -> Nome, Endereço, Telefone

#Dependencia funcional trivial
    #Dependencias triviais é quando Y é subconjunto de X em X->Y (X->Y significa "X determina Y"
    #Não trivial é quando Y não é subconjunto de X
    
    
    
#Regras de inferêncai (Não cai na prova)
    #A partir de algumas inferencias você pode descobrir outras dependencias funcionais
    #Reflexividade: Se Y é subconjunto de X, então X->Y
    #Aumento: Se X->Y, então XZ->YZ
    #Transitividade: Se X->Y e Y->Z, então X->Z
    #Pseudotransitividade: Se X->Y e YZ->W, então XZ->W
    #Decomposição: Se X->YZ, então X->Y e X->Z
    #ADitiva: Se X->Y e X->Z, então X->YZ


#Segunda forma normal
    #Para isso precisa entender dependencias funcionais totais
    #Dependencia total é quando um atributo depende de toda a chave primaria, e uma vez que eu removo um atributo da chave primaria, a dependencia deixa de existir

    #ISSO VAI CAIR.


    #Um esuquema na segunda forma normal então é quando ele está em 1FN e todos os atributos não primarios são dependentes totalmente da chave primaria.
        #Ou seja, não tem como exitir dependencia parcial.

    #Para isso novamente será necessário quebrar a tabela novamente, deixando só atributos que dependem totalmente da chave primaria em uma tabela, e os que dependem parcialmente em outras tabelas (Uma para cada dependencia parcial)


    #Anomalias se não for comprida
        #Inconsitencia na insersção (Se não tiver todos os dados, não tem como inserir)
        #Inconsitencia na remoção (Se for o ultimo registro de um dado, ele some os dados de outra)
        #Inconsitencia na atualização (Se tiver redundancia, pode esquecer de atualizar algum lugar)

        #SGBD vai deixar, não tem como ele saber que isso ta errado.


    #Vai cair na prova justificando qual tipo de problema e onde ele se encontra. Também como resolver.

    

    #Terceira forma normal
        #Tem relação com a dependencia funcional transitiva
            #Ou seja, isso acontece se X->Z que foi decomposta em X->Y e Y->Z na mesma tabela.
            #Misturar dados de empregado com dados de departamento, por exemplo
                #É como se eu tivesse adiantando informações do deparatamento na tabela do empregado, invés de simpelsmente usar o o DNUMERO para referenciar o departamento

        #Se Y for chave candidata, não é considerado transitivo (logiciamente)

        #Logo uma Terceira forma normal é quando está em 2FN e não existe dependencia funcional transitiva entre atributos não primarios.
            #Ou seja, todos os atributos não primarios dependem somente da chave primaria e não possuem transitividade.
            #OBS: para estar na forma N+1, é necessario primeiro estar na forma N.



#Definições das fromas normais levam em conta qualquer chave candidata na real, não só as primarias como mostrada. O que foi feito foi simplificar o entendimento usando só a chave primaria.

    #Definição 2FN: Um esquema R está em 2FN se, para toda depedencia funcional com chaves candidatas, não forem parciais.

    #Definição 3FN: Um esquema R está em 3FN se, para toda dependencia funcional não trivial X->A que pertence a R, X for uma superchave de R ou A for um atributo primario de R.

    #Mas ainda tem reduncância, bem pouca, mas tem.
    #Pra resovler temos a forma de Boyce-Codd



#Foroma de Boyce-Codd (BCNF)
    #É uma forma mais restritiva que a 3FN
    #Um esquema R está em BCNF se, para toda dependencia funcional não trivial X->A que pertence a R, X for uma superchave de R.
        #Ou seja, todos os atributos determinantes são superchaves.
    #Logo, todo esquema em BCNF está em 3FN, mas o contrário não é verdadeiro.
    #Pode ser necessário decompor mais ainda a tabela para chegar na BCNF.

    #Ou seja, ele não permite a segunda possibilidade da 3FN, onde o atributo determinado pode ser um atributo primario.
        #Exemplo: Em uma tabela onde a chave primaria é composta por (Aluno, Curso), e o atributo "Coordenador do curso" depende do "Curso", que é um atributo primario.
        #Nesse caso, para estar em BCNF, seria necessário criar uma tabela separada para os cursos e seus coordenadores.

    #Atributo primario é aquele que faz parte de alguma chave candidata.


        

        
#Exercicios:
#1-   
    #Não está na 2FN pois existem dependencias parciais de IDAluno, uma com nomreAulo e outra com endereço.
    #Para resolver, criar uma tabela com IDAluno, idDisciplina, semestre, ano e nota. E outra tabela com endereço e nome e IDaluno

#2- #F1: Areaconhecimento, Ano -> nomePremiado e Nacionalide
    #F2: nomePremiado -> nacionalidade 
    
    
    #Não está na 3FN, pois existe uma dependencia transitiva entre nomePremiado e nacionalidade.
    #Para resolver, criar uma tabela com Areaconhecimento, Ano e nomePremiado. E otura com nomePremiado e nacionalidade.

#Conceito de dependencia funcional é que as tuplas sempre terão os mesmos valores correspondentes, ou seja, se existe A com B em um lugar, B sempre acompanhárá A em outras tuplas também.


#Falar anomalias



#3- Exercício no ediciplinas
#a
#B
#c
#d
#e





