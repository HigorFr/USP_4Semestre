#Atividade dia 24 - Entregar os Diagrama



#Modelo Entidade - Realacionamento, última aula
    #EER é uma extensão da Entidade
    #Entidade terá pelo menos umahierarquia
    #Abstração e Generalização e Especialização



#Estrutura semelhante à OOP, superlcasse e subclasses
    #Superclasse é a entidade mais genérica, e as subclasses são as mais específicas
    #Exemplo: Veículo é superclasse, Carro e Moto são subclasses
    #Atributos da superclasse são herdados pelas subclasses, mas poderão serem mais especificados
    #Relacionamentos também podem ser herdados, não apenas atributos


    #Passos na Generalização
        #Confere o que é genérico e vai identificando atributos comuns e subprime diferenças entre elas
        #Especialização (Baixo pra cima)
        #Generalização (Cima pra baixo)
        #Notação de U 
            #terá um D/O para denotar se é disjunta ou conjunta respectivamente (Se pode ser todos ao mesmo tempo ou só 1)
            #A linha (que conecta até o D/O) também indica se é parcial ou não, para ver se obrigatoriamente ele tem que ser especificado ou pode permanecer genérico
            #Semantica segue o é-um, para realizar a descrição

        
#Tipos de Herança
    #Pode ser simples ou múltipla
    #Simples: uma subclasse herda de uma única superclasse
    #Múltipla: uma subclasse herda de múltiplas superclasses
    #Dá para ter várias combinações disso, uma entidade herdar duas superclasses e ainda ter "filhas"
    #Empregado e Aluno formam Assitente Aluno, e ter duas filhas assitente Pesquisa e Assitente Ensino disjuntas


#A arquitetura da tabela vai depender dessas restrições, pois ela define como as entidades se relacionam e como os dados serão organizados no banco de dados, já que nem toda entidade vira tabela. 



#Cardinalidade em relacionamento Ternários
    #Se isola a entidade de uma e observa ela em relação as outras para dar a cardinalidade a rela, repete isso 3 vezes para achar de todas
    

#Isso tudo é o Projeto conceitual
    #Analise de requisitos (O que estou querendo)
        #Como clientes pensam
    #entidade, relacionemto, atributos, hierariquia, entidade fracas etc...
    #Restrições são importantes, (MIN/MAX), sobreprosição. Mas nem todas restrições do domínio vão poder ser capturadas por um DEER
        #Regra de negócio especifica por exemplo, Isso não deve ser levado em conta agora, será no futuro (Por exemplo, não pode haver cliente menor de idade comprando produtos de cerveja, no caso de um mercado). Coisas do gênero.


    


