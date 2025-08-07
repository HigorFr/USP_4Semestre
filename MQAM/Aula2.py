# Aula 2

    #Curiosidade: Termo "Regressão" veio de uma analogia com a ideia de que os filhos tendem a ter características mais próximas dos pais, ou seja, uma regressão à média.
        #Veio do Francis Galton, que estudou a hereditariedade e notou que as características dos filhos tendem a ser uma média das características gerais. FIlhos de pais altos tendem a serem um pouco menores, e filhos de pais baixos tendme a ser um pouco maiores isso ele escreveu como "regressão à média".ou "regressão à mediocridade".

    #Exemplo, nota em ensino médio e nota na faculdade

    #Para utilização, tem-se algumas presmissas
        #Deve ser utilizar relações com tendêncais de fato lineares, tendências quadrdáticas ou cúbicas não são adequadas para regressão linear simples.
        #Os resíduos, ou seja, os erros (diferença entre o valor real e o valor predito) devem ser aproximadamente normalmente distribuídos. Isso significa que a maioria dos erros deve estar próxima de zero, com poucos erros grandes.
        #Os erros, se forem tratados como variáveis aleatórias, devem ser independentes entre si. Ou seja, o erro de uma observação não deve influenciar o erro de outra observação, isso se deve pela própria indpendência das observações.
            #Isso é muito interessante de se observar, pois se eu sei que o erro de uma observação influência o outro, então há algo mais que não está sendo capturado pelo modelo. Na estatistica normlmente se considera tudo como indepentente, mas na vida real isso 'emuito difícil
            #Em séries temporais, por exemplo, os erros podem ser correlacionados ao longo do tempo, o que viola essa presmissão, por exemplo, volume pluvial em dias consectivos. Se choveu hoje, é mais provável que chova amanhã.

        #Variãncia dos resíduos deve ser constante ao longo de todas as observações. Isso significa que a variância dos erros não deve mudar à medida que os valores de X mudam. Se a variância dos erros aumenta ou diminui com os valores de X, isso é chamado de heterocedasticidade e pode afetar a precisão das estimativas do modelo.
            #Ou seja, é como se fosse a mesma distribuição de erros para todos os valores de X

    #Notação do Erro
        # R ~ N(0, σ²) (ou seja, "Resíduos seguem uma distribuição normal com média zero e variância σ²")
        #Também da pra considerar Y|X ~ N(μ, σ²) (ou seja, "Y dado X segue uma distribuição normal com média μ e variância σ²")
        #Isso é Y|X ~ N(B0 + B1X, σ²) (é beta zero + beta 1 vezes X, ou seja, a média da distribuição normal é uma função linear de X)


    #Heterocedasticidade - Quando a variância dos erros não é constante ao longo de todas as observações. Isso pode ocorrer, por exemplo, quando a variabilidade dos dados aumenta com o valor de X.

    #Homocedasticidade - Quando a variância dos erros é constante ao longo de todas as observações. Isso é uma suposição importante na regressão linear, pois garante que os erros não variem sistematicamente com os valores de X.(Premissa da regressão linear)



    #Distribuição Normal
        #Variância é feita pela média dos quadrados dos desvios em relação à média, contudo é sobre n-1 e não n, isso se deve pelos graus de liberdade, ou seja, a variância é uma estimativa não tendenciosa da variância populacional.

    #Exemplo no Python pelo PROF no EDisciplinas 




    #Coeficiente de Determinação (R²)
        #Formado pelo SSTO, SSE e SSR
        #SSTO (Total Sum of Squares) - Soma total dos quadrados
        #SSE (Sum of Squared Errors) - Soma dos erros ao quadrado
        #SSR (Sum of Squared Residuals) - Soma dos resíduos ao quadrado

        #O R é dado por R² = 1 - (SSE/SSTO), ou seja, é a proporção da variância total que é explicada pelo modelo de regressão.
        #OU (SSO/SSTO) já que eles são complementos, que explicam a distancia entre a média e os valores observados.
        #QUanto melhor o modelo, mais próximo de 1 o R² estará, ou seja, mais do modelo é explicado pela variável preditora X.

        #Na correção linear simples, existe uma correção do coeficiente r e o R², que literalmente é o quadrado do coeficiente de correlação, ou seja, R² = R²
            #r é o coeficiente de correlação entre X e Y, (O angulo da reta de regressão com o eixo X)

