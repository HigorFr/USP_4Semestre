#Continuação Modelo Entidade-relacionamento

    #Entregar principais funcionalidades do Sistema
    #Tangíveis, e especifica, consultas complexas
    

#Entrevistar usuario para entender o que ele precisa
    #Projetista vão começar a partir disso
    #Requisitos FUNCIONAIS (O que eu quero que a aplicação faça)
    #E depois os requisitos de dados (Que dados eu preciso para que as aplicações funcionem
    
#Projeto conceitual
    #Proxima etapa, já é fazer o modelo entidade relacionamento (MER)
    #Será usado para criar basicamente um grande diagrama (produto final) usando OS CONCEITOS do modelo entidade-relacionamento
    #Digrama é chamdo (DER)
    #Serve como contrato para ver se de fato o que está sendo construido atende as expectativas
    #Sem modelo relacional, ou chaves. Aqui o objetivo é entender o domínio
    #Levantar "regras de negocio" 
    #Isso tudo é o projeto conceitual


#Aplicação de banco de dados é dito se referendo a um BD e a um programa associado a ele.

#Como funciona o diagrama
    #Objeto básico do MER é a Entidade
        #Conectadas entre sí por relacionamentos
        #Entidades tem atributos que a descrevem
        #Atributos não podem ter mais atributos
        #Uma entidades especifica é chamado de Instância (Que nem POO)
    #EX: Objetos, pessoas, conceitos etc...

    #Atributos podem ter caracteristicas especiais
        #Atributos compostos, tipo endereço, podem ser fragmentados em vários
            #subatributos, como Rua, número, cidade e estado
            #Rua poderia se dividir ainda mais em Nome, numero apartamento etc...
            #Todo atributo tem que ser atomico

        #Multivalorados
            #Um atributo pode ter mais de um valor, formando um Conjunto, ex Telefone
        
        #Alguns Atributos podem podem ser derivdaos
            #Ou seja, não precisam de fato estar no banco pois é fácil calcular. Melhor fazer Data_Atual - Data_Nascimento

        #Atributos de Valores nulos
            #Valor especial caso não seja aplicado ou desconhecido
            #Impossível inferir algo, não se cabe

    #Tipo Entidade
        #Representa um conjunto de objetos que compartilham características comuns
        #Basciamente uma classe, e a entidade-mebrmo (?) é objeto (fazendo analogia à oop)
        #Uma entidade-membro do mesmo tipo entidade tem que compartilhar dos mesmos atributos

    #Se a entidade for "Forte", ela vai ter pelo menos um atributo "Chave", ou seja, que a torna única
        #Se não tiver chave, é uma entidade "Fraca", que depende de outra entidade para ser identificada
        #Não se usa o temor chaver primaria, estragenria etc... quando se faz o DER
            #Ele apenas indica o que é chave e o que não é


    #Tipo de relacionamento
        #Basicamente define todo conjunto de uma assoaciação especifica
        #Ou seja, cada relação unitariamente é uma intância à um Tipo de relacionamento
        #Pode ser binário (2 Graus), ternário (3 Graus) etc...
            #O grau se refere à quantidade de entidades participantes da relação
            #Normalmente relacionamento ternário da pra quebrar em 2
    
        #Relacionaemnto Recursivo
            #Quando tem basicamente uma entidade que se relaciona com ela mesma
            #Ex Funcionario - Supervisona -> Funcionario. (Em uma tabela com funcionário por exemplo)

        #restrições
            #Razões de cardinalidade
                #Define quantas instâncias de uma entidade podem ou devem se relacionar com instâncias de outra entidade
                #Ex, um aluno pode estar matricualdo apenas em uma disciplina.
                #Sempre focando no máximo, na notação N:1 por exemplo (Para qualquer N entidades, pode ter 1 da relação)
                
                #Ou por exemplo, um departamento pode ter um chefe e um chefe pode gerenciar no max 1 departamento, isso fica 1:1

                #E também "tabalha em Projeto:", que fica N:M ou N:N, que um numero qualquer de entidades pode tabralhar em um numero qualquer de outras

                #Se um máximo for estabelicido fica "X" máximo invés de N obviamente

        #Restrições de participação
            #Define se a participação de uma entidade em um relacionamento é obrigatória ou opcional, como um mínimo para relação acontecer
            #Ex, um aluno pode ser obrigado a estar matriculado em uma disciplina
        
            #Basicamente desfine se a relação é total (obrigatoria) ou parcial (Minimo 0).
                #Dependendo do dominio o total pode ter minimo 1,2,3,4 etc.. para relação existir

        #Isso é definido para cada TIPO de relacioanemtno, não todos. Para Ternários, tem uma técnica propria para conferir isso
        
        #Restrições  estruturais é a junção da cardinaldie e da participação  
        
        #Certos tipos de relacionamento podme ter atributos
            #Por exemplo, "horas de projeto", seria um dado que eu coloco no projeto ou no funcionário?
            #Nenhum, o certo é colocar na relação, pois a quantidade será proporcional
            #Acho que isso tem relação com as restrições, nesse caso é N:1, se fosse 1:1 por exemplo dificilmente terá dados para se colocar na relação em sí
        
    #Tipo Entidade Fraca
        #Entidade forte é aquela que tem pelo menos um atributo chave
        #Certas entidades que não tem atributo chave são chamadas fracas
        #As entidades fracas dependem das entidades fortes através de uma relação
        #Ex: Plano de saúde de familiares de uma empresa. Não vai ter chave única, mas vai depender do funcionário
        #A entidade forte nessa relação é chamada de proprietária, ela empreta a chave dela para entidade entidade fraca, e junta com algo para diferenciar (Tipo CPF do funcionario + nome). Esse atributo pra diferenciar é chamada de "chave parcial" da entidade fraca.

    #Vai cair isso na prova, ler diagrama e construir, visando essas relações


#Notação do Diagramas
    #slide
    #não usar outras
    #ignorar o "de", é tipo entidade, não tipo de entidade por exemplo
    #notação min,max para restrições estururais (Descrito abaixo)
    #o objeto mais macro nunca será destacada no diagrama, tipo em um BD de funcionario não tem EMPRESA, pois empresa é exatamente o que eu estou arquitetando (Só faria sentido se eu estou modelando uma rede de emrpesas)


#Max/Min
    #Numero minimo de instancias que deve aparecer e o numero máximo que ela deve participar
    #Melhor fazer notação N:1 e depois converter para (min,max)
    #Ex: (0,N) -> (0,N) ou (1,N) -> (1,N)




