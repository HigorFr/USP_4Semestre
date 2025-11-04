# Aula 11


-#Recursividade dos resultados Z
    #Não anotei muita coisa






#Evolução do modelo linear: (O Kernel)
    #Nos modelos lineares, temos W =  (X^T * X) ^-1 * X^T * y
    #Podemos escrever a função sendo f(x) = Phy(x)^T * W
    #Onde Phy(x) é a função de base (polinomial, gaussiana, sigmoide, etc)
    #Dessa forma, W = (Phi^T * Phi) ^-1 * Phi^T * y (Com o W do tamanho Qx1, Q = número de funções de base)

#Assim podemos trazer um espaço de alta dimensão, onde os dados podem ser linearmente separáveis em menos espaço    

#No fim a gente não conhece o Phi, mas podemos usar o truque do kernel:
    #K(x_i, x_j) = Phy(x_i)^T * Phy(x_j)
    #Ou seja, o produto interno no espaço de alta dimensão pode ser calculado diretamente no espaço original


#para funcionar a função deve cumprir algumas condições, como por exemplo poder ser decomposta em phi e phi^t
    #o phi em sí nem é necessário conhecer
    #Como você não conhece a dimensão de phi, você assume um D e procura qual o que melhor se ajusta.


#Matriz kernel
    #K(x_i, x_j) = Phy(x_i)^T * Phy(x_j)
    

#Realizando manipualções algebricas chegamos que
    #(Phi^T * phi) * phi^t * K⁻1 = phy^t
    #Logo phi^t * K⁻1 = (phi^t * phi)⁻1 * phi^t



#Passos:
#Definir um kernel
    #Polinomial, você escolhe o grau de D em K(x_i, x_j) = (x_i^T * x_j + c)^d
    #Gaussiano (RBF): K(x_i, x_j) = exp(-||x_i - x_j||^2 / (2*sigma^2))
        #sigma controla a largura da gaussiana

#Calcula K, para todas entradas se calcula a função kernel definida, resultando em uma matriz NxN (N = número de amostras)
#Então é necessário calcular alpha, que será a = K⁻1 * y (Basciamente você pega da dimensão alta para a dimensão original)
#Finalmente é calcular K para os testes




#Hiperplano de seperação de margem ótima
#Vapnik


#Consiste em encontrar um hiperplano que maximize a margem entre as classes
#Margem = distância entre o hiperplano e os pontos mais próximos de cada classe (vetores de suporte)
#Maximizar a margem ajuda a melhorar a generalização do modelo

#Calcula distancia entre pontos, dividindo pontos acima da reta e pontos abaixo
#O seu ro vai ser a soma dos pontos mais pertos
#Não exatamente é uma reta, mas qualquer variação em mais dimensões (Plano, hiperplano etc...)



#                  
