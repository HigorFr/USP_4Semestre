#Era para ser inferência sobre os parametros
    #Teste de hipótese e intervalos de confiança etc...

#contudo devido aos palnos do professor será uma aula de regressão linear simples
    #Caso prático para visualização




#Extesção da regressão linear simples
    #Invés de apenas um coeficiente mutiplicativo, tenho um coeficiente para cada variável
    # Y = B0 + B1*X1 + B2*X2 + ... + Bn*Xn + erro
    #Os betas são parametros, ou seja, se eu soubesse cada um dos valors eu teria uma função de regressão perfeita

#No fim isso 'eo mesmo que Ỹ = E(Y|X1,X2,x3...)
    #problema do orçamento familia e do solo


#Preparar os dados
    #Soma dos valores para criação do total
    #divisão por ele para obter a proporção (Ex, qtd do dinheiro gasto em alimentação)
    #Cuidado com peculiaridades do dominio, como em proporções podem acabar prevendo resultados negativos dependndo do X
        #Por isso é bom fazer análise exploratória para normalizar esses tipos de erros que podem se encontrados

    #Aplicação de transformações (Tipo log para fazer com que a linha siga melhor a curva em assimetrias)
    #Porque log10? Noramlmente é mais interpretativa no resutlado (QUe nesse caso é X em 10^X, numero de unidades)
        #Log também ajuda a exitar valores menores que 0


    #One Hot Encode
        #Transforma variáveis classificatórias em variáveis dummy
        #Colunas correlacioandas são excuidas, pois é redundante
            #Isso pode ser feito para K variaveis, e K-1 colunas dummy são criadas


    #No fim em variaveis categorias terá um elemtno a mais nos valores 1,que não ocorrerá em categorias 0 (Já que o beta vai estar mutiplicando por 0)
        #Então é como se fosse dois modelos, e você tivesse separando eles e explicando a diferença através de uma soma (Que pode ser "ligada ou desligada")
    #contudo ocorre efeitos de "saturação". (Quanto menos algúem gasta com alimentação, menos ela tende a diminuir o gasto), Ou seja, a "velocidade de variação" vai diminuindo ou aumentando.)
        k#Isso pode ser capturado por curvas em formato de S para pegar esse comportamento para dar mais precisão



    #Como voltar a escala original? (Tipo depois de fazser o log)
        #Expressão LogitY
        

    #Mesmoa ssim pode acabar gerando uma disperção alta, pois se assume um "Angulo" igual para ambas
        #Isso ocorre às vezes pois é necesasrio uma variação conjunta em variáveis invés de uma analise separada
        #Isso é feito utilizando uma nova variável que sera o produto de ambas X3 = X1 * X2. (No exemplo é X3 = Total * SexoM)
            #Note que o SexoM continua sendo binário



    #Resultado fica bom no final


    



