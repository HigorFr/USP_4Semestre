#Continuação de redes neurais (que eu perdi T-T)
    #Classifcação entradas
    #Classificação saídas
    #Camadas (Que não são nem entradas nem saídas)
    


#Cada nó é uma função de ativação, pode ser usando sigmoide (normalmente na camada), e na saída (normalmente com softmax)
    #Em problemas de classificação noramlmente não há memoria, é foward
    #Em de tempo (RNN) há memoria, é foward e backward, então saídas voltam como entradar em um feedback, isso é muito mais díficil trerinar e pode gerar comportamentos instáveis
        #Ai dizemos que é recorrência total (Tem a local e a global)
        #Local é quando só a camada tem feedback

#Cada seta tem uma nomenclatura baseada de onde vai e de onde vem (nessa ordem). E uma letra que é em qual camada está (A é entrada, B é primeira camada, C é segunda camada, e assim por diante)
    

#Depois se faz uma matriz para cada "a" camada, sendo cada aij
    #A primeira coluna da matriz será o ai0. O resto é tudo que chega nela     
    #A altura da matriz é dada pela quantidade de nós referente
    

#Então a formula para um nó especifico é Zin1(n) = a10 *1 + a11X1(n) + a12X2(n) + ... + a1mXm(n)
    #Que fica Zin1(n) = Σ ai0 + Σ aijXj(n)

    #A função de sinapse será aplicada ao Zin, ou seja, Zout1(n) = f(Zin1(n) ) (Invés de zout é chamado só de Z1(n)) mesmo

#O neuronio em sequencia será aplicado não mais ao X, mas sim ao Z do anterior,se for o final ela soltará o YinK e não outro ZinK

#O erro vai ser a diferença do Y esperado e da saída, e o erro total será a soma dos erros ao quadrado (para evitar negativos)
    #j(n) = 1/2 Σ (Yd - Y)^2, o 1/2 é só um fator para faciltiar a derivada
    #O erro então será Jt = 1/2 Σ Σ J(n) 
    #Essa é a função que queremos minizmar atraves do MSE

#Derivando o    derivdad de Jt = e(n) * e(n) derivado de Bkj, ou seja o n vai variar
#Derivar e(n) em Bkj é mais complicado que parece
    #e(n) = Yd - Y
    #Derivada de e(n) em Bkj = derivada de Y em Bkj (Pois o Yd é constante)
    #Y = f(ZoutK(n)) = f(Σ Bk0 + Σ Bkj Zj(n))
    #Derivada de Y em Bkj = f'(ZoutK(n)) * derivada de ZoutK(n) em Bkj
    #Derivada de ZoutK(n) em Bkj = Zj(n) (Pois o resto é constante)
    #Logo, derivada de e(n) em Bkj = f'(ZoutK(n)) * Zj(n)


#Substituindo na derivada de Jt
    #Derivada de Jt em Bkj = 1/2 * Σ (  e(n) * f'(ZoutK(n)) * Zj(n)   )
    #Gradiente vai desparecendo a medida que você vai voltando para trás
#Dá para implemntar em forma matricial
#ekn é N x ns, o f(ZoutK(n)) é N x ns, e Zj(n) é N x (H+1) (Supondo que já tenha bias)
#A matriz Ns x (H+1) = 1/n * e^x * g') x Z

#Com isso eu vou achar o do último, e com ele eu uso para achar o do penúltimo, e assim por diante, propagando para trás

#O processo se repete até você ter todo mundo
    #Contudo deve se tirar o bias, pois ele não tem peso vindo de trás (Antes do nó)
    #Na hora a matriz vai ficar Ns x H



#Como criar uma rede neural

#Entrada X matriz (N, ne+1), Yd (N, ns), h (numero de amostras)
    #Yd já é a raida esperada, se for sigmoide ou tangente hiperbolica já tem que estar tudo normailziado (Entre 0 e 1 ou -1 e 1)
    
# 1 Passo é  Gerar A e B (Pesos iniciais)
    #A é (ne+1, H), B é (H+1, ns)
    #Noramlmente A e B ambos com valores entre -0.2 e 0.2


#2 função que calcula a saída da rede
    # Zin = X * A' (A transposto)
    #Z = f(Zin)
    #Yin = Z*B' (B transposto)
    #Y = f(Yin)

    #isso vai se repetir várias vezes para cada camada ex:
    #Pin = Y * C'
    #P = f(Pin)
    #E assim por diante

    #Apesar que o Y normalmente é sempre a última       


    #se for sigmoide:
        #f' = f(x) * (1 - f(x))
        #g' = g(x) * (1 - g(x))


#3 Calcular o erro
    #E = Yd - Y


#4 Calcular o gradiente
    #derivada de j em B:
        #dj/dB = 1/N * E * f'(Yin) * Z
        #dj/dZ = 1/N * E * f'(Yin) * B (Tirando a linha de bias, 1:)
        #dj/dA = (djdZ * fl)'*X
        #grad = [djdA(:); djdB(:)] (Empilha tudo em um vetor só)   ( o (:) é como se fosse um .flat() )

        #Lembrnado que a mutiplicação ali é elemento a elemento, não a matricial
    
    #O B tem que tirar o bias, pois ele não tem peso vindo de trás (Antes do nó)
    #O f'(Zin) é uma matriz diagonal, então dá para fazer a multiplicação elemento a elemento
      
    #A sigmoide reduz o erro para trás, e se tiver muita camadas pode ser que o erro suma e os pesos não sejam alterados

    #dB = 1/N * E * f'(Yin) * Z
    
#5 Enquanto Norm(Grad) > 1e-5 and nepocas<nepocasmax
    #5.1 calcular a taxa de aprendizado
    #5.2 atualizar A e B
        #A = A - lr * djdA
        #B = B - lr * djdB

    #Repete tudo, como o A mudou, Y também muda, e o erro também, e o gradiente também
    
    # Aaux = A- lr * djdA
    # Baux = B - lr * djdB

    #Calcula saída para o conjunto de vlaidação

    #Zin = Xval * Aaux'
    #Z = f(Zin)
    #Yin = Z*Baux'
    #Y = g(Yin)
    #erro = Ydval - Y
    #EQM = 1/n * sum(erro.^2)
    

    #Se EQM < EQMmin  (Ou seja, se a atualização for boa)
        #Af = Aaux
        #Bf = Baux
        #EQMmin = EQM
    #nepocas = nepocas + 1

    #Se o erro for maior, é possível que esteja ocorrendo um overfitting, então não atualiza os pesos, só aumenta a época e continua testando para ver se acha um melhor
        #Pois também é possível que subiu só um pouco, mas já já volta a descer


    #AGora eu calculo para o conjunto de treinamento
        #Resto ta no edisciplinas


#EM softmax se usa uma medida de erro diferente do MSE, que é a entropia cruzada
    #J = - 1/N * Σ Σ Yd(n,k) log Y(n


#Tem as com base radial, que são utilizando funções gaussianas (copilot)
    #A entrada é a distância euclidiana entre o ponto e o centro da gauss
    #A saída é a soma ponderada das saídas de cada neurônio
    #maldição da dimensionalidade, então não é muito usada, pois se vocẽ tiver 5 divisões de dados, vocÊ precisa 5^n neurônios, onde n é a quantidade de dimensões. Isso é muito custoso.
        #Existem técnicas para reduzir esse problma criando clusters nos dados, mas é muito específico
        #Técnica que aloca as guassianas, onde o sigma e o centro são definidos por outra técnica supervisionada
    #Pode ser resumida em uma unica mutiplciação matricial, sem iteração. W = (H^T H)^-1 H^T S
    #No fim você pondera várias guassianas e soma para chegar em uma função final
        #Um pouco parecido com KNN, mas aqui é uma guassiana por ponto, e no KNN é só a média dos k mais próximos


#============================



#Rede de Hopfield
    #Rede recorrente, onde cada nó é ligado a todos os outros (Inclusive ele mesmo)
    #Usada para memória associativa, ou seja, você dá um pedaço da informação e ela completa o resto
    #Cada nó é binário (1 ou -1),

    #Atratores, funcionam que nem um voronói, onde caa ponto puxa para o centro mais próximo



    #Redes com recorrências são aquelas que dependem do tempo, tipo idenficar voz ou bolsa
        #Camada de contexto, pesos travados randomicos
        #Derivar isso é um inferno







    
