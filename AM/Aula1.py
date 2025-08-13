#Aula 1
#Prof Clodoaldo

    #Machine Learning


#Várias BIB
# Vanpik descrição mais matematica
# 

#2 EPs
#E1 - 2 Técnicas de aprendizado tradicional e 01 de aprendizado profundo
#E2 - Atividades Individuais semanais (Extra, não obrigatório)

#1 Prova, valendo 6, trabalho velndo 4 e o E2 vale 1 extra

#Entender a técnica e saber realiza-la, não é superificial tipo usar o python


#Exemplo biometria, exige isso (FOrmação do clodoaldo)

    #Tradicional:
    #Aquisição de dados
    #Processa, filtra tudo
    #Caracteristicas, medidas que importam para análise (Tipo distancia do olho na biometria)
    #Classificação
    #Avaliação (É você ou não)

    #No deep lerning não tem a extração e classificação em sí, é tudo um grande bloco com várias camadas

#TUdo surge a partir de um banco de dados, com relação

#GANS - Gerador e Discriminador,
    #Discrminador recebe imagines reais e fakes do gerador e tenta julgar
    #Tem resultado no final, que dá feedback para ambos
    #O Erro então começa a deslocar do gerador para o discrminador
    #No final ele irá começar a gerar imagens próximas as verdadeiras


    #No Gerador, os mais modernos utilizam um vetor randamico, para qualquer entrar te retornar um valor
    #Semelahnte à uma função, você entra com um X numa norma, e ele retorna uma gaussiana referente aleatoria
    #Imagen é a mesma coisa, eu coloco um X e tem que retornar um gato aleatorio


#Função objetivo fica 

#Se uso pytorch

#Épocas é quantas vezes será atualizado o valor




#Grafico de perda
    #Todos os métodos de gradiente são muito difíceis encontrar minimo global, é praticamente impossível
    #SEmpre tem uma loss, que tem que ser minimizado, então o objetivo é encontrar os parametros que fazem o erreo diminuir
    #As vezes o modelo é ruim pois caiu em um local com pessímo minimo local
    #Contudo é parametros multifimensionais

    #Tem dois métodos principais, um que utiliza a média da derivada de todos parametros e outro que caminha um por um
        #O primeiro é o melhor, mas normalmente não cabe na memoria, e o segundo é muito ruim pois fica aleatorio.
        #Nomamlemnte faz um meio termo chamado Batch_size que são pacotes de parametros

#Basciamente um G cria
#um D define se é ou não
#Atualiza G para enganar D

#O problema é que a GANS normalemnte não se tem muito controle, e elas são travadas na definição na criação
#cGANS meio que são GANS condificiais para resolver esse problema, vocẽ coloca uma entrada para delimitar
    #Isso vai tanto para o Discrminador e para o Gerador, dessa forma ele durante o treino para essa calsse já delimitar o que será gerado


#Isso foi o Geral

    #O que se procura é uma maquina copaz de realizar uma tarefa através de experiência
    #Arendizado indutivo, é dito que ele aprende quando se temuma T tarefa e E experiencias e uma medida M, que vai melhorando conforme a quantidade de E vai aumentado



    #Indutivo é conhecer a partir do comportamento de um dado. Ou seja, ele testas resultados, aprende e cria conhecimento
        #Todos modelos tem que seguir isso, ou seja, ele está induzindo conhecimento apra dados que el enão tem
    #Ele extrai um conhecimento implicito, mas ele também já existe    

    #Abdutivo é diferente, raro, é baicamente um relção de "Se" inquirida para "Se Somente se", ou seja, você generaliza uma afirmação que pode ou não ser de fato uma verdade
    #Ou seja, se A->B eu observo o B e tendo inquirir o A, tento inquirir a entrada do modelo (Algorimos genericos seguem isso)
    #Ele tenta des

    #Usar o modelo já feito é dedutivo, pois a função já está pronto e basta aplica-lo, assim como uma função f(x) -> y
    #Dou entrada e tiro a saída, tirando um conhecimento explicito


    #Aqui só terá Indutivo e Dedutivo.
    #Abudtivo é um tipo mais caótico


#Paradigmas (os basicos, mas existem muitas)
    #Aprendizado Supervisionado, entrada X e saída Y, e tanto X e Y tem que ser explicitos para máquin
        #Intancias (linas) e colunas (características), ele vai testando
        #Classificação é valores Discretos (É sim ou não por exemplo)
        #Regressçao valores continuos como saída

    #Aprendizado por reforço, não será abordado, é um modelo que tem uma pontuação, ele ganha recompensas se fazer algo certo e é punido se fazer algo errado. Então é uma metrica de desmpenho que é escolhida e vai variando. Jogos normalmente usam isso
        #Tudo onde não se tem possibilidade de falar todas as probabilidades possíveis    

    #Aperindizado não supervisionado
        #Clustering ou redução de dimensionalidade
    
        #Semi-superfizionado é quando se utiliza o modelo para rotular uma base não rotulada inciailmente e mandar rotular com uma base já rotulada, e depois nos processo seguintes eu repito o processo atualizando os resultados em conjunto com os inicialmente rotulados e os feitos pela máquina
        #Reconhecimento de fala, visão computacional, classificaçaõ de páginas


        #Auto-Supervisionado
        #Basciamente através da entrada do modelo já pronto ele consegue se adaptar internamente e aprender conforme o uso. Então basicamente ele troca a ordem da entrada para conferir se faria um resultado diferente. Se tiver, dá para aprender pois a saída deveria ser a mesma. 
        #Inicialmente ele irá gerar os dados, ele cria. Depois desse processo já estar estruturado ele então passa por um fine-turing
        #NLP, visão computacional

#Todos esses modelos podem seguir através de uma base de banco de dados ou online

    #Aprendizado multitarefa
        #unico modelo que realiza varias tarefas pequenas não tão relacionadas

    #Meta-Leaning
        #Aprnede com poucos dados para ser genérico, e depois conforme a aplicação é feito um fine-turning
    

    #Aprendizado por Transferência
        #Muito popular hoje em dia
        #GANS hoje em dia são muito dificeis de serem treinadas do zero pelo custo computacional
        #Pego um modelo mais existente, pré-treinada. Aproveito o conhecimento dele para reduzir treainemnto extras, base menor


    #Aprendizado Trandutivo
        #Parecido com o semi-supervisionado
        #Contudo os dados de teste nesse caso são jogados no treinamento, e não separado em outra base (Aqui eu pego o resultado e jogo no treino)
        #no semi, eu o treino e o teste continuam separados
        #Vai ficar com víes, não será muito geral

#Diagrama útil nos slides


#Classificação -> Binaria é a mais classica, sim ou não (É Gato ou não)
#Multiclasse -> A mais complicada, sai um vetor de "probabildiades", que somadas dão 1
    #Tem muitas nuancias nesse caso, tipo distancia de humming que precia ser aberto em várias colunas


#Conceitos
#Capacidade de generelização é a capacidade de dar o valor correto em cenários diferentes
    #Media e informação do geral tem que ser separada do treino sempre


#Overfitting
    #Erro baixo no treinamento e o teste tem erro alto
    #isso quando uma distribuição é a MESMA, só porque o de cima aconteceu não signifca que é overiftting de fato

#Underfitting
    #Refernete aepans ao treinamento, independe do teste
    #Modelo mais simples que os dados isso acontece
    #Baisicamente um modelo ruim mesmo


#3 Separações normalmente
    #Treainmento (calculo do gradiente)
    #Validação ()
    #Teste


#Desbalanceamento de classe
    #Quando uma classe tem muito mais exemplos do que outra, o modelo pode ter dificuldade em aprender a classe minoritária.
    #Isso afeta o valor desempenho do modelo, usando erro quadratico médio ou erro absoluto médio
    #Então é sempre bom usar a matriz de confusão caso não seja balanceado


#1 / 2
#3 / 4
#1 é TP
#2 é FP
#3 é TN
#4 é FN

#Dependendo do dominio tem métricas diferentes para classificação (Ex, doençã tem que ter pouco falso negativo)
#Na matriz multiclasse é o quadrado do numero de colunas


#Varios calciulos no slide
#F1 Score é um geral que usa de ambos
#MCC Coeficiente de correlação de matheus é uma media geral entre todas as classes


#Threshold é basicamente o ponto de corte para decidir entre as classes
#Modelo robusto é aquele que dá para sofrer alteração no Threshold sem perder performance
    
    #Curva Roc é bascamente uma curva do eixo da FP e da TP, que indica basicamente o comportamento de troca entre positivo e negativos
    #Quanto mais porto da curva pior, pois quer dizer que ele apenas está trocando os positivos para negativos, então não é robusto
        #Limiar = Threshold
    #ou seja, quanto mais perto de um melhor a variaçãoem relação a curva RCOK


#Em multiclasse, depende, fica one Vs All
    #um com o resto, ou seja, em uma matriz de 3 classes, eu escolho uma classe para ser sozinha e outras para ser conjunti
    #desse modo volta a ser algo binario, então tem a calsse 1, e 2,3 versus a 1 e 2,3 que da na mesma da verdaeiro falso



#Metodos de avaliação
    #Resubstitution
    #Random Split - Suavisa overfiting caso alguma tenha dado
    #Holdout - Treinamento e teste sem osbreposição (30/70 normalmente), normalmente a literatura pede que isso seja aplicado 30x em sequencia para ser aceito, pois é muito fácil enviezar, tem que rodar varias vezes
    #K-FOld Estratificado Cross validation. Você divide o conjunto em K partes iguais, treina 1,2,3 terina na 4. Testa 1,2,4 treina 3 e assim por diante até todos tenham sido testados.No final eu tiro uma média. Deposi eu posso reptiri o processo todo para ter ainda mais acuracia estatistica (Tudo que é estratificado é por classe)
    #K-FOld sem ser estratitifcado é randomico, sem classe
    #Leave-one-out, mesma filosofia para conjunto bem pequeno, que invés de eu dividir em K partes eu pego um por 1
    #Bootstrap - Seleciona varios para treinar aleatoriasmente, todas as vezes. Os que sobrarem vão para o teste. Depois mutiplico por um coeficiente para tirar um erro medio do treino e do teste
    #Kx2 K-Fold - Problema dele é que ele fica lento, nesse caso fica 50% treino e 50% teste randomico e troca depois repetindo. Todo processo repetido K vezes
    #Variações de K-FOld - Repetido ou estratifificado

