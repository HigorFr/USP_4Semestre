--Sistema baseasdo em Banco de dados X Arquivo

--Arquivo
    --Quem faz aplicação se responsabiliza por tudo
    --Baixa complexidade
    --Baixa segurança
    --Cada usuário implesmente e utiliza
    --Falta de sincronização, ex em corporação (E dá muitp trabalho sincronizar)
    --Redundância e Inconsistência
    --Vai disperdiçar meméoria

    --Contudo tem a vantagens que nem sempre vale a pena usar banco de dados
        --Coisas simples
        --Necessidade de eficiência (SBD é mais lento)
        --Acesso em Tempo Real
        --Custo
        --Mono usuário

--Redudância pode gerar inconsistência, isso será abordado no futuro
    --Isso parte do pressuposto que um dado alterado, deve ser propragado e alterado em todos


--Prova tem questões práticas e teóricas


--Esquema de BDs
    --Definido durante o Proejto do banco de dados
    --Muito semelhante à computação orientada à objetos
    --Definição de classe, atributos e métoodos
    --Contrutores definem como os dados serão inseridos, cada tabela sem o seu contrutor

    --Diagramas definem o esquema, sem dados, apenas colunas
        --Também chave primeira e estragenria ficam destacadas

    --Estado do banco de dados ou Instancia do Banco de dados
        --Conjunto de dados armazenados no banco de dados em um determinado momento

    --Depois de realizar o esquma de fazer os create table, rodar o script, o banco de dados fica no estado inicial


    --SGBD Garante que todo estado do banco de dados satisfaça todas as restrições de integridade, ou seja, seja válido
        --Normalmente na hora de definir no projeto lógico já se pensa nas restrições de integridade para isso sequer ser necessaŕio

    --Catálogo e Metadados
        --O construtor de esquema, quando está sendo feito além das restrições da tabelas, compõe os metadados simultaneamente
        --Os metadados vão para um local chamado catálogo no SGBD

    --Estutura distribuida
        --Modulo cliente / servidor (Ambos vão operar no meu notebook)

    --Cliente 
        --É o normalmente acessado, por programa e interfaces que acessam o bd
        --Requisita, e o SGBD entrega o dado
        --

    --3 Esquemas de artquitetura
        --Separação programa e dados
        --Suporte a mutipls visões de usuario (Sò usa o que precisa)
        --Catálogo para conceito além dos dados (Metadados)

        --Desenho do esquema no slide


    --No nível interno está os algoritimos de ordenção em memoria secundária, ele é operado pelo DBA, e não afeta o usuário externo, ele foca em como os dados são armazenados, busca, exclusão etc... (Usuário não vê isso)
    --No nível conceitual, está o catálogo, apenas descrevendo como os dados estão, chaves etc..., estutura do banco de dados, restrições
    --E no nível externo é as visões de usuário, onde dá pra saber o que cada usuário tem acesso, cada visão externa tme uma descrição

    --*Na hora de estudar n confundir esquema conceitual com "modelo conceitual". Modelo conceitual é uma representação abstrata do banco de dados, enquanto o esquema conceitual é a estrutura real implementada no SGBD.

    --Essa arquitetura é exatamente para separar estrutrua física da lógica, já tornar a operação mais flexível, permitindo alteração em qualquer parte sem ter que fazer retrabalho
        --Tipo mudar algortimos de busca internamente



    --Linguagens
        --VDL - Linguagem de definição de visões, para definir as visões externas
        --DDL - Linguagem de definição de dados, para definir o esquema conceitual, (Create table por exemplo)
        --SDL - Linguagem de definição de dados, para definir o esquema físico, (Create index por exemplo)
        --DML - Linguagem de manipulação de dados, para manipular os dados, inserir, deletar, atualizar etc... conferir
        --O SQL meio que é uma linguagem "wrapper" que envolve todas essas linguagens (Não sei se oficialmente o nome é "wrapper")

        --Exemplo no slide

    
    --Usuario de banco
        --Programadores
        --Usuario de alto nível (PEssoal que não programa)

    
    --Projeto do Bando de Dados
        --Primeira coisa a ser feita, coleta e análise de requsiitos
        --Nada a ver com implementações
        --Os chamados "projetistas", acham a necessidade do cliente, (quem te contratou), dizem os requisitos e o que ele vai precisar

        --Modelo Entidade-relacionamento
            --Modelo das ligações, funciona como um contrato entre o cliente e o projetista
            --Isso meio qeu vai especificar como o banco de dados vai ser

