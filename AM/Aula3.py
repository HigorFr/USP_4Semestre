#Retomando objetivos


#Objetivos
    #Classificação
        #Binária (duas classes), pode ser classe -1 ou 1 usando Tang Hip, ou Classe 0 e 1 usando função Sigmoid. Também tem o modelo com duas saídas usando um softmax. (Dá para interpretar como Softmax)
        #Multiclasse (mais de duas classes), pode ser feito usando a função Softmax/
    #Regressão
        #Função Linear


#lembrando combinação dos modelos
    #Melhorar erros
    #diminuir loss funcion



#O^(k+1) = O^(k) + α * D
    #D é a direção e alfa a taxa de aprendizado

#Loss function normalmente é erro quadradito pois é fácil diferenciar
    #


#Quando gradietne é zero, a H é pelo menos semidefinida positiva
    #Contudo, pode ser um ponto de inflexão, para ter certeza é necessário garantir que H é definida positiva. (Sobre em todas as direçoes)
    #




#Descobrindo o Alpha na função
    #Construção do H(Alpha) que zero faz com que h'(x) seja 0, ou seja, seja um mínimo.
    #Aproximando o h'(x) alterando o valor de alpha (   Uso a formula h(alpha) = GradienteF(X+D)transposto*D  )
        #O alpha zero sermpre será negativo. Depois chuto valores até achar um positivo.
        #Vou tirando média e substituindo os limites máximos e mínimos confoem eu acho
        #Uma hora acho o meio


#O gradiente é o pior dos modelos
    #Esse é usando puramente o gradiente, mas conforme el echega perto do destino ele perde magnitude
    #Tem o modelo de newton também, que usa a segunda derivada para encontrar o mínimo de forma mais eficiente.
    #Tem estimadores para  segunda derivada
    

#A largura do intervalo vai diminuindo em 2 pois é a média que estamos tirando. Logo L = (1/2)^k * (â)
    #Re arranjando fica K = log2(â/L)
    #Assumimos esse L como epison pois é como um erro que eu quero, e isso vai me dar um numero de interações.
    #O número de interações vai ser K = log2(â/ε). Isso deve ser arrendondado para cima, pois K é inteiro.

    #O Algoritmo pode seguir 3 métodos de parada diferentes então:
        #kmax = k
        #|h(0)| < episilon
        #Nint max = 10/20

    #Tem como fazer também o algorimo cortar mais que só a metade tirando a média, colocando uma proporção do numero de ouro.
        #Então se eu acho um a (o lado negativo) invés de o proximo a ser a média, será a + numero de ouro * (b-a)
        # B será B - numero de ouro * (b-a)

    #Normalmente não se encontra alpha gradiente 0, quase impossível


#Busca linear com retrocesso de Armijo
    #Com um alfa muito pequeno valdetale:
    #(f(x +alphaD) - f(x))/alpha = Deltaf(x)tD
    #f(x+alpha * d) <= f(X) + Deltaf(x)t * D * alpha Essa é a condição de checagem. Tem que ser o maior alfa possível
    #Traço uma reta gradiente que me traga qualquer alpha que diminua minha função atual. Isso mutiplicado por uma constante 10^-4

    #Começo chutando um alpha, e enquanto não satisfazer acondição você mutiplica por uma constante p


    #O C faz o trabalho de ângulo da reta, quanto maior, mais valroes ele aceita. E isso pode fazer com que ele consiga alfa grandes.

#Ou seja depende o que você quer, um alfa execelente, ou seguindo suas restrições (Que pode valorizar a velocidade)



#Um alfa em simuações não ajustadas fica variando muito



#Méotodo de Newton (Saindo dos alfas)
    #Funçẽos de perda na realidade tem muitas dimensões, não são só um X e Y
    #No méotod e utilizar apenas o delta f(x)t(x-xbarra) era ruim, pois eu tenho a premissa de que quando eu sigo a derivada caindo, a função original também está. Coisa que não necessariamente é verdade, e ela já pode ter voltado a subir.

    #No meotodo de newton adicionamos um termo de segunda ordem que é uma matriz para ter masi informações sobre a curva.
        #Ou seja, eu somo 1/2 * XHX
        #No fim eu corrijo a direção do gradiente com a matriz e melhorar  a direção dele.
        #Ficando X = XBarra - H(x)^⁻1 * Delta f(x)

    #O ruim disso é que a hessiana precisa de muito espaço, é parametro² e inverter ela
    #(Na pratica não se inverte, utiliza uma regra de sistemas lineares de grau N para resolver)
        #S.L (H(x)sigma = -Deltaf(x)) 

        #Nem sempre a matriz é inversível, e isso é uma premissa da H feita pelo méotodo. Significa que os auto-valores delas são todos negativos. Ou seja, antes de inverter eu confiro se o menor auto-valor é negativo e isso já vai me dizer se posso continuar ou não
        #(Não sei o que é auto-valor)

    #Resolve problemas quadráticos em uma iteração




#Metood de newton Modificado
    #Somo valores no auto-valores para obrigar a eles serem no minimo positivos
    #Positivação da matriz hessiana.
    #Isso garante que tanha inverso na matriz
    


#Métood de levenberg Marquardt (entendi porra nenhuma)
    #Combina o método de Newton e o gradiente descendente.
    #Adiciona um termo de regularização à matriz hessiana para garantir que ela seja positiva definida.
    #Isso permite que o método seja mais robusto e funcione melhor em problemas não lineares.
    #O parâmetro de regularização é ajustado dinamicamente com base na evolução da otimização.
    #(Escrito pelo copilot)

    #Tem se N funções r² que são referentes aos erros que eu tenho.

    #??

    #Os resíduos são negligenciados, vocẽ usa um sistema linear com o as função resultante R(x)^t * R(x)
        #




#Metódo de Davidson-Fletecher Powell
    #invés de de fato fazer conta invertendo a matriz hessiana, ele utiliza uma aproximação da inversa da matriz. (Já que vai aproximar, tenta aproximar logo a inversa).
    #Isso permite que o método seja mais eficiente em termos de memória e computação.
    #Desse forma eu podeira ir já derito aplicar os passos seguintes do newton.
    #Esses são chamados Quase-Newton, pois não utilizam informações exatas
    #Quando numero de interações passa do numero de parametros, você reseta (Pelo principicio que um vetor com 4 valores em R 3, o 4 será combinação linear dos anteriores)
    #Contudo ainda há o problema que M tem um valor grande


#Existe um que método calcula vetor gradiente e acha um D sem fazer o produto, direto.


#BFGS segue o mesmo principio, só muda como calcula a matriz


#Método de Secante de um Paso
    #MAtriz não precsia estar em memoria


#Meu deus não sobrou nada



#Atividad 3 - Numero de interações Tabela
    #Gradiente
    #Nível
    #BFGS





#Gradiente Conjugado Polark - Ribiere
    #Utiliza o graidente anteriro mais uma variação com peso e define uma nova direção. (E ainda mais). Isso já jorna melhor que o gradiente.
    #Esse peso da variação varia conforme o Polak e o Fletcher
        #Normalmente o do Polak é melhor é melhor, mas ele pode dar negativo (E ai normalmente fazer um chaveador par ao Fletcher)
    #Baixo custo, pois é produto de vetor


#problema deles princiapsi era calcular derivadas e estima-las


#Calculo numérico
    #Isso vai ajudar a estimar as derivadas de forma mais eficiente.
    #Invés da derivada ser aquela classica, será dividido por 2h para aproximar e o f(x + hei), e será ei (que é a variável i que estou derivandao)
    #Isso vale tanto para o gradiente tanto para hessiana, então você vai revezando o 0 e 1 para escolher quais variaveies estão sendo derivadas (Por aproximação)

#Exercícios propostos



    #