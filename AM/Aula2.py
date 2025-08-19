#Reprise

#Ou seja, no final a curva ROC é para me ajudar a verificar a confibialidade da diferença quadrática
#Então é a sensibilidade do modelo em relação ao teta (Quanto mais perto a area debaixo da curva for 1)
    #

#Overfit - Muito acerto no treino, pouco acerto no teste.


#Resubstituiton


#Holdount - Divisão
    #Train - Normalmente o maior ~ 60 a 70% do total
    #Validation - Para cada época, será apresentado esses dados, o modelo também vai diminuir o erro dele com o passar do tempo, mas o erro dele pode aumentar conforme o parametros (O que indica overfiting pelo teste), e se isso acontece você para. Isso é para garantir a generalização 
    #Test - Usado para ver se o modelo de fato está bom

    #Como a divisão dele é aleatoria, o modelo pode acabar sendo enviesado. Para paper deve ser tirado a média entre várias aplicações com diferentes divisões. Ou seja, é aplicado "Mutiplos Holdout".

    #Se o problema for desbalanceado, também o holdout puro é ruim, já que pode enviesar a divisão dos blocos


#ObsEpoca - Tempo apara passar (apresentar) todo o conjunto de dados


#Random
    #melhor que o holdout rodado uma vez
    #Aletorio a divisão de K


#K-Fold Cross Validation
    #Revesamento de teste e treino
    #Divisão do conjunto de dados em K partes (folds)
    #Para cada iteração (K Split), um fold é usado como teste e os outros como treino
    #Isso é repetido K vezes, garantindo que cada parte seja usada para teste
    #No final você tem 5 modelos, então você tira uma média entre cada um deles

    #Muito caro para conjunto grandes (K vezes mais)
    #Estratificado, Invés de dividido aleatoriamente, ele divide também em classes, ou seja, 5 para cada por exemplo. Isso é bom para impedir viés em desbalanceamentos.


#Leave-One-Out (LOO)
    #Especifico para conjuntos pequenos (100)
    #Para cada iteração, um único exemplo é usado como teste e os outros como treino
    #Isso é repetido para cada exemplo, garantindo que cada parte seja usada para teste
    #No final você tem 100 modelos, então você tira uma média entre cada um deles

#Kx2 Fold 
    #Usado para conjuntos grandes ou para comparar modelos
    #Divide em 50% para treino e 50% para teste, treina, inverte, e testa novmanete (Garante que todo mundo passa pelo treino)
    #Repete K vezes o processo variando a divisão de 50%.
    #Isso meio que resolve o problem do K fold para conjunto grandes e garante melhor resolução


#Na doc do Scikit-lean tem vários modelos de cross validation

#https://scikit-learn.org/stable/modules/cross_validation.html




#Bootstrap
    #Usado para conjuntos grandes
    #Cria subconjuntos aleatórios com reposição
    #Para cada subconjunto, treina um modelo e repete, ele pode repetir isso até 200 vezes
    #No final, combina os resultados de todos os modelos
    #Divisão de 0,38 das amostras não escolhidas e consequentemtnete 0.632 serão escolhidas (Por isso holdut é mais ou menos 70/30)
    #Na hora d ejuntar os conjuntos ele aplica um peso também
    #Tem a versão estratificada também para dados desbalanceados



#=========== Fim da Reprise da aula passada ==================


#Em modelos com intersecção grandes, comparrar modelos apeanas por acurácia é muito errado, o certo é fazer um teste de hipótese.
    #Isso porque a acurácia pode ser enganosa em conjuntos desbalanceados, onde um modelo pode ter alta acurácia simplesmente por prever a classe majoritária.
    #Então o objetivo é provar que não existe sobreposição suficiente para existir uma diferença significativa entre os modelos, essa será  H0, hipótese nula
    #Assim a afirmação é "Considerando alpha nivel de significancia, esse é o melhor modelo", normalmente é 5% de Alpha

#P valor será a probabilidade de obter um resultado tão extremo quanto o observado, dado que a hipótese nula é verdadeira, se for maior que Alpha, a afirmação nula permanece

#São dois teste, o primeiro considera que vem de uma distribuição guassiana T-test
    #Eles noramlmente assumem independência, o que de fato não é verdade, mas para evitar complexidade
    #T-Test, normalmente usado o Pareado (Você compara o com maior acuracia contra todos os outros modelos, e tira o significado de cada teste)
        #Basicamente você está tentando provar que o de melhor média é de fato o melhor
    #Será usado o scipy para achar o p_valor
    #Tem o teste de Wilcoxon, que é uma alternativa não paramétrica ao T-Test, também pelo scipy usando argumento (Antes, Depois)

    #Tem que ter todas essas informações para de fato algo ser publicado hoje em dia, é exigido muito fundamento estatístico

#Obs*Precision e Recall


#Adendo,nada é feito com dados de testes. manipualções tem que ser lógicas para não afetar o treino
#Underfitting é quando algum parametro faz com que a taxa de acertio mesmo no conjunto igual de trainamento fique com uma baixa taxa de acerto.


#Influencia -> GPU, Muito dado, etc...


#-> Aprendizado Supervisionado 
    #Tenho X e Y, quero chegar no f(x) -> y, ou seja, achar a função
    #Primeiro se cria um espaço de hipotese com todos os F possíveis, e então contra-se a F que melhor representa.
    #Exemplo nos slide (Conjunto de dados e conjunto de funções possíveis)
    #A melhor f será aquela com maior numero de acertos no conjunto



#Regressão aproximando pontos
    #Imaginando um gráfico de função, será "chutado" várias funções usando diferentes polínomios que passe mais próxima de todos os pontos que eu quero
    #Quanto mais polnómios, menos suave a curva de previsão fica, e mais overfit terá (Ou seja, vocẽ vai obrigar ele a passar pelos pontos)
    #Contudo mesmo assim, funções de polinomios altos são escolhidos, pois é fácil penalizar polinomiso prejudicias ao modelo de maneira que suavisa ela.
        #Contudo, em situações estáticas, onde não tem muita diferença, usa-se o principio da pasemonia, usa o mais simples (Grau 3 no exemplo) para explicar

    #Definição de simples é suavidade por exemplo, é um conhecimento a priori.




#Problema principal então é escolher uma função no espaço de hipótese
    #Avaliar cada uma
    #Escolher
    #Modelar aplicações como problema de machine learning

#Hipotese sufciente
    #Tem foco somente valores rotulados em 1

#Hipotese necessária
    #Tem foco somente valores rotulados em 0

#Hipotese constante
    #Foco em ambos



#Tipos de erros (Teoria Dilema bias-variancia de PAC)
    #Erro verdadeiro e erro sobre conjunto de treino (bias)
    #Fórmula é no slide.

    #|H| é a cardinaldiade do espaço de hipotese, quanto maior, maior o erro
    #M é a qtd de amostras, quanto maior, melhor
    #Dilema de bias e variancias, são inversamente proporcionais de acordo com o tamanho do espaço de hipótese. Isso deve ser escolhido de acordo, exemplo de gráfico no slide

    #Assume que o espaço de hipotese é finito e contável, contudo nem sempre isso é verdade


#Risco empírico e Risco esperado, outra forma de entender o problema
    #Esperado é feito Integrando para todos os pontos
    #Risco empirico é o erro quadratico médio



#Dimensão VC
    #Mede a compleixdade de um tipo de função
    #Alta capacidade -> Aproxima bem os dados
    #Dilema Capacidade e generalização
    #Separação de pontos através de parametros, isso define compleixdade, exemplo no slide
        #Se eu consigo serpara 2 pontos (Rotulando dados de todas as forma possíveis), dizemos que é compleixdade 2

    #Uma linha por exemplo, separa até 3, então tem complexidade 3. (Tudo isso falando em R2
        #E tudo analago para as dimensões, planos serão compleixdade 4 em R3. Isso se estende para sempre, a capacidade de "linha" em R^n será n+1
        #Isso é útil, eu posos pegar os dados e jogar em dimensões altissimas, para então traçar uma "linha" para calssificar


    #Numero de parametros não está relacionado à complexidade diretamente, (óbvio que tem relação, mas não é diretamente proporcional)


    #Então agora o objetivo é diminuir o erro de treino e simultaneamente a dimenção VC, e para isso tem que se achar um meio termo
        #O problema que isso exige dimensão VC como parametro, e isso é aproximado, mas não existe algo preciso para realizar isso para os modelo complexos.
        #A parte matematica explora isso, mas não há nada estabelecido por padrão, é um dos gargalos da área.

    #No final isso basicamente me descreveria qual arquitetura utilizar.



#Modelo parametricos e não parametricos
    #Modelos parametricos são os que se atribui sentido uma função especifica, seja geometrico ou que for. (Tipo ax + b, isso é uma reta)
    #Modelos não parametricos são os que não há explicação lógica, os pesos de uma rede neural por exemplo não são explicáveis, é simpelsmente uma otmiziação do que é melhor


#Não parametricos normalmente mapeam qualquer coisa, e são mais genericos, rede neural é proxima (Pois eu defino a quantidade de nós, ela não mapeia todas funções possíveis). Uma puramente não paramétrica eixigiria que ela fosse capaz de representar qualquer função.
    #KNN por exemplo exige que tenha um K existente definido.


#Ou seja, quanto menos interpretável, menos parametrico é.

#Maldição da dimensionalidade
    #Quanto mais dimensões, mais complexo fica o modelo, e mais dados são necessários para treinar ele caso eu qeurira manter a mesma distribuição
    #Se eu teinha 5 prontos em X, quero adicionar outro atributo em Y, isso exige invés de 5, 25 pontos, se for 3, pode ser 125. Então as veszes o gargalo não é atributo e sim dados.

    #Isso pode ser um pouco desviado conhecendo a concentração de pontos no espaço, que me permitirá excluir certos pontos não relevantes para o treinamento

