#Revisão da aula passsada





#Várias D entradas com D pesssos.
    #Isso passa por uma função S que depois passa por uma função logisitca, com saída 0 ou 1


#Rastie Net
    #A função de perda é o erro quadrádico médio (Igual ao linear)
    # L(w) = 1/n Soma n=1 até N (yn - ydn)² + λ1||w||² + λ2||w||  ( λ2||w||  é o mesmo que sign(w) ) quando formos derivar
#Problema é que esse modelo é apeans para 2 classes, binário, como transformar para multiplas classes?
    #Estrategia One vs All
        #Treina um modelo para cada classe, onde a classe é 1 e as outras
        #Ou seja, eu escolho uma classe para ser 1 e as outras (2,3), depois 2 vs (1,3), depois 3 vs (1,2), uma você escolhe para ser 1 e as outras -1
        #Cada modelo vai ter um X valore de saída para um Y, e você classificar ele como o maior X.
        #Problema é que piora os desbalanceamentos de classe, já que se tiver 50 A e 1000 A e B, o teste será injusto
        #Você sempre tera N modelos, onde N é o número de classes

    #Estrategia One vs One
        #Vocẽ testa 1 contra 2, depois 1 e 3, depois 2 e 3... e assim por diante
        #Isso até contemplar todas as combinações
        #Problema é que se tiver 5 classes, você vai ter 10 modelos, seguindo uma ordem de Nc(Nc-1)/2
        #Então o custo computacional aumenta muito
        #E para escolher a classificação, você faz uma votação, onde cada modelo vota em quem ele acha que é a classe correta
            #Se empatar você adota um critério, que normalemnte é o com maior correlação


    #MOC (Codificação de saída mínima)
        #A ideia é usar uma codificação binária para cada classe, onde a classe é 1 e as outras 0
        #Ou seja, é o 1 contra os zeros e faço a divisão, então eu sempre terei log2(N) modelos, onde N é o número de classes
        #Isso transforma o problema em um de múltiplas saídas, onde cada saída é um classificador binário
        
        #Cada um dos classificadores vai sair um valor de 1 ou 0, e você escolhe o valor com base na combinação binária
            #Problema é que pode sair classes que não existem, tipo 11 quando só tem 3 classes (00, 01, 10)


#Tranformando modelo em multiclass
    #Invés de sigmoide, usa-se softmax
        #Softmax é uma generalização do sigmoide para múltiplas classes
        #Onde a soma de todas as saídas é 1
        #y = exp(zj) / Σ exp(zk)  (k=1

    #Na lousa o professor escreveu uma notação função de 3 classes, com 3s (que acho que são as saída das regrssões)

    #Isso irá gerar uma matriz W, onde cada coluna é um dado e cada linha é uma classe

    #Também o X terá uma dimensão de NxD+1, onde N é o número de dados (Exemplo), D é o número de atributos e +1 é o bias

    #Terá uma matriz S, onde cada linha é um dado e cada coluna é uma classe

    #Tera a matriz Y, onde cada linha é um dado (Exemplo) e cada coluna é uma classe, mas só terá 1 em cada linha

    #Para chegar em S, é X*W, mas W tem que estar transposto para mutiplicar "bater". Então S = X*W^T

    #Agora para chegar no Y através desse S, precisamos aplicar o softmax em cada linha de S
        #P(C1n | xn) = Softmax =  exp(s1n) / (exp(s1n) + exp(s2n) + exp(s3n))  (Onde C1 é a classe 1, e xn é o dado n)


    #Agora na hora de maximiziar a classe Y1, é notavel que a Y2 e Y3 vão ser 0.

    #Na formula, para levar a probabildiade única então é feito um produtoróio de P(Cmn | xn)^ydn, e ydn (como é 1 ou 0) eu consigo escolher quem é o máximo
        #isso facilita na hora de derivar

    #Depois, esses resultados eu tiro produto entre eles novamente, para considerar todos os dados, ficando produtório de produtórios

    #Função de perda é a log-verossimilhança
        #L(W) = - Σ Σ ydn log P(Cmn | xn)

        #Agora achar o gradiente exige que eu derive em todos os W possíveis

        #Derivada da soma é soma das derivadas então isso é  Σ Σ ydn * d/dwm P(Cmn | xn)
        #Abrindo o somatório de dentro eu vejo que é a soma soma da derivdas das classes.
            #Isso acontece pois, mesmo que w1 influencia apenas S1, o softmax faz com que todas as S sejam interligadas.

        #Eu também volto o P(Cmn | xn) para a formula do softmax para ficar evidente o que estou derivando
            #Então eu tenho que derivar uma fração, onde o numerador é exp(smn) e o denominador é a soma de todos os exp(sk)

    #Ao final de toda essa derivação, o resultado vai dar o 1 -Softmax (G1mn) * Xn0
        #Sim, muito interessante que o softmax não mudou depois de derivado

    #Isso fica d/dw ln(Gmn) = (1 - Gmn) Xn0 se m = k (No parte que estou derivando é igual aonde estou olhando)
        #E d/dw ln(Gmn) = - Gmn * Xn0 se m != k (No parte que estou derivando é diferente aonde estou olhando)

    #Ao aplicar todas essas formulas naquele produtos derivado que deu somatório, a formula fica Σ Xn0 (ydn - Gmn), e serve para qualquer K
        #Ou seja, no fim é mutiplciar o erro pelo X
        #Se tivesse sigmoide, derivar ia ficar mais díciel realizar a derivada.
            #Isso tem relação com casos entropia cruzada (seja lá o que isso for), o softmax ajuda nesses casos, sigmoide atrapalha

        #Ele foi feito aplicando gradiente, mas teria como aplicar newton também, mas é mais complicado

        # P/Casa se eu tiver muito tempo mesmo, Calcular DT(w)/DwIj SOmatorio n=1 até N (ydn - Gmn)Xi0     (Tudo é constante exceto o Gmn, que depende de W)
            #Dica é usar 1 0, depois 0, 1 e você vai fazendo uma expressão para diagonal da matriz heassian outra nas colunas.
            #É pra chegar em algo bem mais simples até que o gradiente (por mais monstruosa que a derivada que is   so pareça)


    #Regressão logistica Multinomial passo a passo
        #Vocẽ vai receber uma matriz X de NxD+1 (N dados, D atributos + bias) e uma matriz Y de Nxk (N dados, K classes)

        # 1 Passo é gerar N Kx(d+1) com valores aleatorios normalmente entre -0.5 e 0.5 (Onde K é o número de classes, D é o número de atributos e +1 é o bias)
        # 2 Calcular a saída S = X*W^T (W é a matriz de pesos)
        # 3 Calcular a saida ychapeu que é a Exp(S) / Σ Exp(S) (O Softmax)
        # 4 Calcular o erro E = Y - Ychapeu
        # 4.1 Calcular o graidente Somatorio n=1 até N (Erro)Xi0 
            #Nessa etapa, invés de fazer um for para achar o gradiente, você pode fazer a multiplicação de matrizes E^T * X, e ai você já tem a matriz gradiente prontinha (Que matematematicamente é a mesma coisa)
        # 5 Transforma essa matriz gradiente em um vetor (Flatten) e  então calcula a norma
        # 6 Enquanto a norma for maior que um gradiente de tolerancia epsilon ou o numero max de iterações não for atingido
            # 6.1 Atualiza W = W + η * gradiente (η é a taxa de aprendizado, um alpha que você escolhe como funciona)
        #Então repete para o passo 2            

#Lembra que agora você quer maximizar um Y especifico, então você vai na direção do gradiente


#Pra lição de casa fica fazer isso para base IRIS, mas usando sigmoide invés de softmax para dia 28
#A derivada de newton é para amanhã    
#A da semana passada fica para dia 21


#FALTA MATERIAL DA aula passada (ou seja, o que eu li ontem n serviu para nada)



#Revãisão da aula passada (KNN)
    #Modelo núcleo, distribuição gaussiana ao redor de cada ponto
    #KNN, pega os k vizinhos mais próximos e faz uma votação
        #KNN (K-Nearest Neighbors)

    #Calcula a distancia entre o ponto e a guassiana e vejo qual contribui mais

    #$oma todas as contribuiçãoes de probabilidade ponderadas e pego a maior. (Eu voto na maior)

    #Se for regressão é a média ponderada, eu uso a distancia de X até X4 como peso, e somo, depois divido pela soma dos pesos
        #E então você ter aum Y aproximado

    #Nota que KNN não tem treinamento, ele só armazena os dados
        #Então o custo de memória é alto, mas o de treinamento é nulo
        #O problama é saber o desvio padrão apra definir a abertura da gaussiana
            #Se for muito pequeno, o modelo fica muito ruidoso
            #Se for muito grande, o modelo fica muito genérico

    #Por isso o KNN é mais usado como baseline




#Árvores de decisão

#Cada nó será uma pergunta sobre um atributo, que levará para amis nós até chegar em um nó folha que é a decisão final, podendo ser binária ou não, as ramificações também.
#Quanto maior o nó, mais separa os dados, ou seja, mais informação ele tem, mais crítico.
#Muito fácil vizualizar, pois você já sabe o que cada nó significa.
#Quanto mais atributo tiver, mais profunda fica a árvore, e mais difícil de interpretar.
#A vizualiação dele também é facilmente transmitida para um conjunto de regras.
#Vantagem, não precisa de muito conhecimento prévio, é fácil de interpretar, pode lidar com dados categóricos e numéricos
#A acurácia se relaciona mais com o domínio do problema, ás vezes são boas, as vezes são ruins. (No geral é ruim)


#An é o conjunto de N atributos que existem
#Cardinalidade é o número de valores que um atributo pode ter, X o espaço das instâncias (O produto de todos os domínios)
#Na literatura tem os algoritimos ID3, C4.5, CART (Esse é o mais usado)
    #O que varia é o critério para escolher um nó raiz de outros.


#Méotodo (mais simples)
    #No slide está bem explicado, não preciso copiar
    #A maneira que vamos definir o nó que vai mudar, essa é a parte que ele vai ficar fazendo cálculo

#Da nós que são "pertecentes à conjuntos" ou pode fazer a contagem de quantos são de cada classe, e escolher o que tem mais etc...


#Condição de parada é quando todos os dados são da mesma classe, então vira folha

#Tem alguns principios de pré-poda, que é parara o treinamento antes de chegar na condição de parada.
    #Exemplo, cada nó me da um certo X de ganho, se X< 0.01 eu paro pois é um ganho baixo e pode śo atrapalhar.

#Lembrando que ávore sempre tem que ter a informações pois ela é supervisionada.


#Como medir os erros
    #Existe uma formula generica para englobar todos os erros
    # Somatorio x,y D(x,y) * L(y,DT(S)(X))
    # É uma chance D e um L que é o que perdi, nesse caso da arovre considero D como 1/n pois eu não tenho a probabilidade de cada classe (Considero uniforme)
    #E o L que é a quantidade é uma soma de 0 e 1, onde 1 é erro e 0 é acerto


#Não se pode deixar a árvore crescer demais, pois vai gerar overfitting
    #Então normalemnte se adota um limiar para impedir o aumento, o problema é como calcular esse limiar, essa é a pre póda.
    #Pode ser uma "Pre-poda" ou uma "Pós-poda" (deixa ela crscer e depois corta, normalmente é a melhor estratégia do que definir limiar)

#Como tem muitos atributos que podem ser modificados para fazer a pré-pode, escolher eles adequadamente da muito trabalho

#Em pos poda, o que sera podadado será baseadao em um alpha, que são aquelas que produzem o menor aumento na taxa de erro por filha podada

#Para calcular o alpha eu calculo a diferença do erro entre uma arvore podada e a orginal, isso me da uma variação de erro. Isso eu divido pelo número de folhas que foram podadas.
    #ou seja, eu calculo um erro por folha podada

# a formual é e(pruned(T,t),S) - e(T,S) / |leaves(T)| - |leaves(pruned(T,t))|
    #Onde "e" é o erro, T é a árvore, t é o nó que estou


#porra do jogo do garfield lembrar