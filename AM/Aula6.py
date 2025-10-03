#Podar porque?
    #Evitar Overfitting

#Pre-pode exige limiar, e é ruim ficar testetando
#Poda pós-poda é melhor, mas mais custosa
    #Dexa ela crescer e depois poda
    #Pode ou não usar um conjunto de validação


#Tem a formula de poda com erro minimo no slide 40.
#Notação |S|t, t é o nó filho referente à um pai que eu travei, para cada um deles eu aplico a formula do e.
#o |S| é a quantidade de amostras que chegam naquele nó.
#Cada folha é um c, a classe. O que eu defini
#o resultado e'(t) é o erro estimado, que é o erro aparente + a correção
    #ou seja, eu pego o 1 - o maior acerto

#A probabilidade ParP(y=c|x) é a probabilidade de um x ser da classe c, isso é priori, normalmente considera uma distribuição uniforme (1/k), isso é meio exagerado se a distribução não for uniforme

#O L é um parametro de poda, que eu defino, vou testanto. Quanto maior ele for, mais agressiva é a poda. Normalmente colocam valor K, para cortar com a probabilidade

#essa formula é meio ruim quando se tem muitas classes, pois o valor do E vai tender a ficar muito grande já que o max vai ficar muito pequeno (por conta do denominador). Isso faz que ele pode muito mais agressivamente



#Depois ainda você tem que ponderar o erro pela quantidade de amostras que caiu enm cada T, (ou seja, é uma medizinha ponderada pela quantidade).

#E então é só olhar, se o erro (e') do pai sozinho for maior do que o erro soma erros dos filhos deles, vale a pena deixar os filhos.

#Esse processo é reptido para todo nó sem ser folha, sempre feito de baixo para cima.




#E se eu não quiser conjunto de validação?

    #ntão eu uso uma poda pessimista.


#NEsse caso, eu pego o erro de fato e() (Que eu caculo, vendo o que eu classifiquei com base namaioria da folha) e somo um peso de complexidade dela que é a folha/2*|S|, ou seja, eu somo meio erro por folha, para cada amostra que cai ali.
        #Essa soma sera a estmiativa do meu erro, para evitar que ele coloque folhas demais.

        #Eu pego esse erro e guardo. Agora eu pego o nó pai, calculo como se ele fosse folha (ou seja, faço a mesma coisa vendo qual classe é maior) e compar o erro dele também somado com a complexidade. Se o erro do pai como folha for menor, vale a pena podar.

        #O ponto é que ainda existe um desvio de erro que ai anda somo para o não podado (Dando desvantagem para ele). É basciamente um desvio padrão, Formula no slide 42.


        #No C4.5 ainda é utilizada um coeficiente alpha Z (Nivel de significancia) que é basicamente um erro extra, feito com 1/Z (Ou seja um pouco maior qu 1), mutiplicando pelo desvio padrão 




#Algoritimo é conferir quais das 3 opções é melhor, e ir comparando erros

#1 Como fica se deixar a arvore toda sem mudar nada (Como arvore, entende-se um pedaço dela, ou seja, um nó e todos os seus filhos)
#2 Como fica se pegar se eu trnasformar esse nó em folha (E consequentmeente fodase os filhos desse nó que vira folha)
#3 Como fica se pegar o filho mais frequente do pai e jogar no lugar do pai

#Eu faço o menor das três, ou seja, escolho a opção que deu o menor erro.

#(Interessante notar que se não tivesse a correção na formula o 1 sempre ganha, já que informação extra vai sempre melhorar o resultado, o que nem sempre é bom pelo overfitting)

#=============================

#Certo, mas isso é meio custoso computacionalmente, então existe maneiras de otimizar.

#uma maneira é deixar varias árvores surgirem e tirar uma média entre eles, da mesma maneira que se tira a média de várias funções.

#Esse é o Random Forest.


#Você utiliza seu conjunto de dados para gerar várias árvores (Por padrão é 100), mas cada árvore é gerada com um conjunto de dados diferente (Feito por amostragem com reposição, ou seja, o mesmo dado pode ser pego mais de uma vez, e alguns dados podem nem ser pegos).
    #Ou seja, é literalmente reposição para cada LINHA, uma arvore pode ser formada pela mesma linha reptidada vezes se você der azar.

#Isso é o Bagging (Bootstrap Aggregating).

#Tem também uma outra estratégia chamada Boosting, que é um pouco diferente.
    #Nesse, para gerar o conjunto de dados, eu escolho uma distribuição, treino ela, e no conjunto seguinte eu olho os resultados do anterior, e dou mais chance de ser escolhido para os erros, ou seja, eu escolho mais vezes os dados que foram errados.
    #Isso se repte para todos os Xn, mas sempre pego do mesmo conjunto de dados original, só que com distribuições probabilisticas diferentes.
    #O ruim é o treinamento é sequencial, ou seja, não da para paralelizar, mas dá melhor desempenho normalmente

#O chamado disso é Convenção de Máquina


#Dá para fazer com conjunto de atributos também.


#Nesse caso não há poda, pois o overfitting é evitado por conta da média de várias árvores.



#Estratégias no slide.


#PCA é um método de redução de dimensionalidade linear, que tenta encontrar as direções de maior variação nos dados e projetá-los em um espaço de menor dimensão, preservando o máximo possível da variância.

    #Combinar atributos é chamado de "Extração de Atributos"
    #Seleção de atributos é escolher um subconjunto dos atributos originais, enquanto a extração de atributos cria novos atributos combinando os originais.

    #Tem 3 tipos de seleção de atrivutos, filtro, embutido e wrapper
        #Filtro é baseado em características estatísticas dos dados, como correlação, variância,
        #Embutido realiza a seleção de atributos durante o processo de treinamento do modelo, integrando a seleção de atributos com a construção do modelo.
        #Wrapper usa uma técnica (um outro modelo) preditivo para avaliar a importância dos atributos, selecionando aqueles que melhoram o desempenho do modelo. (Ou seja, é um modelo suporter para o outro)
            #O Wrapper fica em um loop com o modelo, testando várias combinações de atributos e vendo qual combinação dá o melhor resultado.
            #Pode ser para frente (OU seja, eu vou adicionando atributos começando com nada) ou para trás (Eu vou tirando atributos começando com tudo). Para trás é meio ruim pois ela dificilmente ira um atributo muito correlacionado com outro.


#Ele também precisa discretizar os dados, ou seja, transformar dados contínuos em categóricos através de ranges.
    #Entropia é uma boa métrica para isso, pois ela mede a incerteza dos dados. Caoticidade.

    #Utiliza-se os proprios dados como candidados de parametro para realizar o split, e será o dado da entropia que irá ditar
        #Para cada candidato, testa os erros que acontecerão com base na classe target e soma os erros ponderados ou utiliza outra métrica para definir qual utilizar.
        #Quando meis perfeitamente ele dividir, ou seja, menos erros, menor e a entropia, melhor o split. Ou seja, entropia é o quanto falta de informação para classificar perfeitamente, uma proproção de organização.
            #Se a entropia é 0, está perfeitamente classificado

        #No geral utiliza-se outra métrica, está no slide, info(D) = |d1|/|D|*Entropy(D1) + |d2|/|D|*Entropy(D2)
            #Quando a divisão é meio, a entropia é máxima, e é minima quanddo está perfeitamente dividido, ou seja, probabilidade/proporção 0 ou 1
            #Para calcular a entropia é uma formula utilziando um critério que respeita isso. No slide.

#No geral, os testes quando podem ser feitos utilizando vários atributos em conjunto.
    #Logo pode ser 2^n, onde n é a quantidade de atributos, o que é inviável se for testar todos.
    #Existem Algortiimos Genéticos que podem ser utilizados para isso, ou seja, eu combino elementos para que o os filhos melhorem a performance dos pais, e assim por diante.
        #Para isso criamos uma matriz binária, onde 1 é o atributo selecionado e 0 o não selecionado, que são os Genes.
        #Pega linha distinta e faz o cruzamento entre elas (Crossover e mutação), fazendo uma nova população, e assim por diante. E então você vai indentificando os atrbituos são mais importantes (Ou seja, aqueles genes que ficam com 1 mais vezes).
        #Nem sempre o genetico compensa, pode ser que o 2^n, não tenha um n tão grande assim para precisar disso. (Genetico também nem sempre encontra o ótimo)


#==========

#AS outras medidas para descobrir se a escolha de features é boa:
#Informação Ganha
#Razão de Ganh  
#Gini 


#Entropia = -pi*log2(pi) no geral.


#Comçando por Ganho de informação
    #É basicamente a diferença entre a entropia antes e depois do split. Ou seja, antes do atribute
    #Ganho(A) = Info(D) - InfoAnterior(D)  (Notação de ganho normalmente 'delta G)
    #E ai eu uso isso como medida, calculo de uma classe pai InfoAnterior e vou testando com todos atributos como filhos, e vejo qual deles me dá o maior ganho de informação, ou seja, a maior redução de entropia.

    #A info de fato será Info = E(t1) + E(t2) + ... + E(tn), mas tenho que mutiplicar cada uma dessas entropias pela proporção de dados que caíram ali, ou seja, |ti|/|D|, para ponderar o erro.

    #VOu registrando cada melhoria e vou escolhendo o maior ganho de informação, ou seja, a maior redução de entropia.
        #Os primeiros na arvore (topo) são os que mais reduzem a entropia, ou seja, os com maior ganho


    #O problma desse méotod é que ocrre risco dele escolher um atributo que diferencia muito e não siginifica nada, tipo CPF
        #Para resolver isso tem um calculo feito penalizando o numero de Split, chamado Razão de ganho, que é Ganho(A)/SplitInfo(A)
        #Formula do splitinfo 68 ou 67 não lembro


    #gini não entnedi porra nenhuma, é grau de impureza seja o que for isso






















