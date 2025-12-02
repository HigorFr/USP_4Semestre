#Especificações do EP

#1 part 23/12 2 de -Rn, AD, ML, SVM, ENSEBLE (UTilizar HOG) (Dividir a imagems, marcar vetores e enviar um histograma)
#2 part 15/01 - Deep learning

#Prova 09/12



#O que vai cair na prova
    #Taxa Variavel e Taxa fixa em learning rate pro exemplo
        #Se for fixa é pequeno ou grande?

    #Numero de epocas, se é grande ou pequena (Underfitting ou OVerfitting)
        #Conjunto de validação sobiu?

    #Batch size, Batelada, ou Padrão a padrão





#SVM HARD -> Aquele que não permite erro 1/2 ||W||², yi (wxi + b) >= 1
#SVM SOFT -> Permite erro 1/2 ||W||² + C Σ F(epsiloni) , yi (wxi + b) >= 1 - εi
    #onde o erro (epsiloni) pode ser ao qudrado ou não dependendo da norma que você quer.
    #C é o fator de penalização, quanto maior o C mais você penaliza os erros, se for baixo você considera mais a generealização do modelo.


#Invés de 1 - εi  pode ser p - εi  onde p é uma margem de tolerância, ou seja, você pode errar até p pontos sem penalização.



#A função para realizar a divisão de espaço (aqueals dos pontos) deve ter uma função K(x,i) que respeita Mercer Theorem para poder garantir que o problema converge para um global.

#para testar se convergiu, utiliza as condições de Karush-Kuhn-Tucker (KKT)
    #Se αi = 0  => yi f(xi) >= 1  (ponto corretamente classificado e fora da margem)
    #Se 0 < αi < C  => yi f(xi) =
    #Se αi = C  => yi f(xi) <= 1  (ponto incorretamente classificado ou dentro da margem)

#Tem uma lista de variações do SVM para tentar solucionar problemas específicos.
    #LS-SVM por exemplo força o erro a ser = e não < que é o caso do SVM normal. por exemplo
    #Isso faz com que o problema seja resolvido por um sistema linear ao invés de um problema de otimização quadrática.

#Tecnica 1
#Então você aplica o modelo, e testa para todos os pontos de teste se respeita o KKT
    #Supondo 200 erraram e 10 acertaram, você mantem os 10 e pega 40 dos errados que estão mais próximos da margem (os que tem maior αi)
    #E treina novamente o modelo com esses 50 pontos.
    #Repete isso até que 50 pontos sejam todos classificados corretamente.


#SMO -> Otimização minima seuqencial
    #Seleciona 2 αi por vez e otimiza elas mantendo as outras fixas.
    #Um ponto de uma classe e outro de outra classe.
        #Desse modo ele vira uma equação para alpha 1 e alpha 2
        #Vai resolvendo um por um

#CHunking
    #Seleciona os pontos que violam  mais violam o KKT e resolve o problema de otimização só com esses pontos.
    #Ou seja, ele mantem os vetores de suporte (os pontos que estão na margem).
        #O problema é que isso pode extrapolar a memoria pois ele pode selecionar muitos pontos de suporte.

#SOlução para OP3
    #pelo que entendi tem um metodo que cai em uma operação de grau 3, e para isso você precisa fazer uma utilizando matrizes de D.
    #Tem uma heuristica muito longa usando matriz para resovler a equação



#SVM
    #Aplicação de SVM para fazer clusters através de uma ideia
    #joga em espaço de alta dimensão e constroi uma hiperesfera, e descobre o raio dela (De maneira que inclui todos os pontos) da menor maneira possível.
    #Quando voltar para o espaço original você volta com uma forma complexa que envolve os pontos mais externos, já clusterizados.

    #Vetores suportes vão ficar na borda (Superfice da hiperesfera)
        #QUe também vão ser extremos no clistes na dimensão original

#Primeira ideia - Par a par
    #Testa todos contra todos, ligando pontos aleatorios e testa se segue a restrição D(yj) (ditancia) <= Raio
    

#Segunda - Utilizando os vetores suprotes
    #Invés de de testar todos contra todos, você testa só com os vetores suportes na superfice.


#O problema vai ser rotular, porque resolver o problema da hiperesfera em sí é facil



#Tem outro que você só faz um Dijkstra e testa só com os mais pertos


#AGORA TROCANDO OS TIPOS DE MODELOS ================


#COmite de maquinas
    #Tem os mistura de especialistas e o Ensemble

#Nunca tem uma pessoa que sabe tudo, mas várias que sabem um pouco na vida real
    #Não seria plausivel ter vários modelos que sabem um pouco e juntá-los para fazer uma decisão melhor?
        #Isso é o comitê de máquinas

#Não é uma tecnica é em sí, é um conceito de invés de ficar ajustando parametro, você cria vários modelos com parametros diferentes e junta eles.


#Tem que ser inteligências diferentes, ao mesmo tempo que elas pessoas saber de algo. Caso o modelo for ruim ele vai contaminar o resultado final.
    #Tem que ter uma diversiade especificar na escolha


#Enseble - Estatico
    #Todo mundo vê todos os conjuntos de dados.
    #Recebem todos as entradas e fazem suas previsões, com a saida de cada um eu utilizo algum metodo para a saída ser única.

    #Precisa entender várias coisas, criação seleção e combinação dos modelos.
        #Criação -> Diferentes algoritmos, diferentes parametros, diferentes conjuntos de dados (Bag
        #Seleção -> Selecionar os melhores modelos para compor o ensemble
        #Combinação -> Como combinar as saídas dos modelos (votação, média, etc)



#A mistura de especialistas - Estatica também
    #Cada um conhece seu pedaço
    #Chaveamento é "duro", não existe extamente uma operação para combinar
        #Um modelo chaveia com base em um X, escolhido com base na parte do problema




    