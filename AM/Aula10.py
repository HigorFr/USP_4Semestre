#Faltei na última e na antepenúltima. 
    #na penultima foi o negociod e redes neurais

#Teve alguma coisad e ajuste sincrono



#Exemplo mostrando rede com imagens (letras)
    #A precisão é melhor quanto mais pixels tem, ou seja, mais detalhes.
    #Outra coisa é que se a quantidade de possíveis entrada/saidas for mairo (ou seja, mais letras), a precisão cai.
    #A rede neural aprende a reconhecer padrões, então se tiver mais detalhes, ela consegue aprender


#Octane e Matlab são os programas usados.

#Aqui mostrou a convergência do alpha, e se vale a apena calcular o gradiente para fazer alfa dinamico
    #Mostrou que o alfa dinamico é melhor, mas demora mais pra calcular
    #Em redes neurais muito profundas, isso pode ser custoso



#exercicio, previsão em séries temporais, IBOVESPA
    #normalmente é por triplice barreira, ou seja, cria-se um retangulo de previsão que dependendo de onde a linha encosta define uma operação (Subida, descida, mantem)
    #mas no exercicio será feito diferente, será uma regressão linear ponto à ponto
        #problema é que treino usa passado e o teste irá prever o futuro, então a rotulação fica mais complexa (dirigir olhando pro retrovisor)
    #saida é a taxa de acerito do teste
    #lembrando que é só prever o label, (Subir, descer, manter)


    #Definir auto-correlação tem um periodo com os anteriores e formar os gráficos
    #Como ponto de partida usar um laço com regressão linar, e usar a saída disso para rede.

    #Cada neuronio vai recbcer a saída dele com 1 atraso e 2 atrasos e a saída dos outros neuronios com 1 e 2 atrasos tbm



    #Propagação drieta, ou seja, a saída de um neurônio vai para o próximo, só essa formula fica diferente




#Agora N derivações sobre como realizar a previsão usando redes que recebem Z(n-1), Z(n-2) e etc como entrada
    #Muito estranho, não entendi nada se eu rever talvez eu entenda. (Isso foi até o final da aula)




