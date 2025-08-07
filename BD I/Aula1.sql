--Banco de dados I, primeira aula


--Profa Patricia, formação forte em IA

--Projeto em Grupo
--Sistema integrado com banco de dados incluso, em Grupo 4 a 5 pessoas

--Aplicação em Arquivo e no Banco
--Modelagem de Banco (Com validação)
--SQL de fato na segunda parte
--Estrutura de memoria segundária é apenas em BD II
--P1 Sem implementações, apenas definições
--Consulta e Atualização
--JBDC - Para conectar bancos
--Normalização (Avaliação, tipo da redundância)
--Permissão
--noSQL

--P1 
--P2 17/Nov
--Sub 24/Dez
--26 a 01 - Apresentação de Projeto

--P1 é peso 1 e P2 é peso 2
--Nota do projeto é peso 1 e das provas é peso 2
--P1 2,22 --P2 4,44 e --Trabalho 3,33 


--Bib Sistema de Banco de dados - Elmari Pearson
--Prof recomenda usar invés de slide





--Definição Banco de dados
    --Banco de dados
        --Coleção de dados relacionados d eum domínio especifico (Aspecto do munndo real)
        --Usado em diversos sistemas e aplicações do cotidiano
        --Requisitos - O minimo pra funcionamento, de dados etc...
        --No geral sempre há escolhas do que será levado para o banco de dados, sempre levando em conta o que será necessário ser analisado, há coisas que sempre serão deprdidas de qualquer jeito (Gap semânitco)



    --Sistema de Banco de dados
        --Todo ecosistema de utilzação do banco de dados em sí, utusário software, dados e hardware
        --Funcionalidades complexas
        --Isso se aplica á uma padaria, restarante ou qualquer coisa genérica.


    --Sistema gerenciador de banco de dados
        --Software responsável por gerenciar o armazenamento, recuperação e atualização de dados em um banco de dados
        --Exemplos: MySQL, PostgreSQL, Oracle, SQL Server etc...
    

    --Dado - Atómico por definição (Ou seja, não é para uma 'célula' conter mais que que um valor)
    
    
    
    
    --Nem sempre gerenciamento de memória é por arquivo (CSV) como visto em AED II, é  possível pelo banco, e há diferenças para Isso
        --Em arquivo normalmente é algo mais sequencial, sem verificação de integridade, nome do artista validação        
        --nenhuma empresa usa isso normalmente
    --Banco tem muito backup, controle, integridade, segurança, coerência.
    
    
    --ID - Indice de linha, tem certos adendons sobre o que é ele
    --Redundancia é quando o dado não é na agregação máxima, está fragmentado 
    --Chaves: Local é quando a chave é unica no contexto e estrangeira é para fazer ligação entre tabelas
    


    --Processo 
        --Depois do planejamento lógico vem a definição
            --Consiste em criar cada tabela e definir cada tipo e dado
            --Tem a chave primeira, ID único, chave cadndidata, que são valores únicos, e chave estrangeira, que é a ligação entre tabelas]
            --Ai ele fica no "Estado zero"
        --Construção
            --Inserir dados na tabela, popular ele usando normalmente algums script, depois disso ele fica no "Estado Inicial"
        --Manipualação é editar, fazer consulta, deletar etc...
        --Compartilhamento permitir usuários diferentes acesse o banco de dados simultaneamente
        --Proteção do sistemas Funcionamento, crashes, hardware e software
        --segurança Acessos e tudo mais
        --Manutenção para evolução dos requisitor




    --Metadado - Dado de dados, catálogo do banco de dados, descreve a estrutura do banco de dados
        

--O modelo relacional - Ele é o paradigma que é usado na matéria e mais comum hoje em dia, relação entre tabelas, dados do memso tipi (ou seja, relação = tabela)
    --A tabela é uma abstração de algo que existe, representando uma entidade ou não, ela é composta por registros, que são sinomimos de relacionamento
    --Campo é o tipo de atributo que se trata aquele registros
    --ID não necessaraimente é obrigatorio, pois em tabelas grandes já tendem a incluir algo único para registro

--Tabelas de ID mútiplo, ela normalmente é pra relacionar tabelas com redundância, ex: id artista e id album, para relacionar é melhor ter uma outra tabela falando qual artista tem qual album invés de conectar album em artista direto.
    --Pois cada artista pode ter vários albuns e cada album pode ter vários artistas (Colaboração por exemplo)

--DBA é o adminsitrador do banco de dados, usado no contexto empresarial
--Desnvolvedor ususario do banco de dado é "Usuariao final sofisticado"