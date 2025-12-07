#Coisas a serem estudadas.


#Tipos de Aprendizados de máquians

# === Erro verdadeiro.
#Tipos de estratificação de dados
#Tipos de Testes de Hipotese

#Trabalho

#POde usar HOG, LBP etc como função de biblioteca, não pode USAR UM MODELO PRONTO (TIPO OS DO SKLEARN)
#Extrair rotulo, testar parametro

#POde aplicar Wavelet transform, que retorna LL, LH, HL, HH dividodo em 4 partes
    #Filtro passa baixa (Elimina alta frequencia) e passa alta (Elimina baixa frequência)
    #SUavisa a imagem
    #Da para aplicar inumeras vezes, e jogar fora o que não precisar (EXemplo, caso você só precisa diminuir a resolução)

#Acho que HOG é obrigatorio. Pode jogar features de caracteristicas da imgem também

    #Identificação biometrica (1:N , ou seja, você tem n pessoas e quer identificar quem é)
        #Rotula, treina dando uma imagem e respondendo quem é aquela pessoa
        

    #Autenticação biometrica (1:1, ou seja, você tem uma pessoa e quer autenticar se é ela mesmo)
        #Dobro de features
        #Treina mostrando duas imagens da mesma pessoa (1), depois com pessoas diferenes (0)
        #Depois no teste você pega duas imagens e vê se é a mesma pessoa ou não.



    #Relatorio no modelo da IEEE
    #Também em Vídeo

    #Exemplo de questão
    #Suponha o exemplo, tem que fazer análise óbitos (doenças respiratorio) por queimadas
    #Achar uma Relação causal.
    #Informações, é leitos, região, queimadas, população. 
    #Só dois anos de dados (24 amostras)

    #Um modelo linear não seria bom, pois não seguiria o erro normal, até porque os valores são discretos
        #Você pode transformar isso em uma taxa, e será continuo
        #Linear é ruim para contagem
        #etc.. etc...




#Comite de Maquinas
    #Enseble espera que o resultado será melhor em média dos que os componentes individuais
        #Contudo não garante que seja melhor que todos modelos especificos.
        #Até porque não se conhece o teste.

    #Mudar a inicialização não é suficiente para criar diversidade, arquitetura diferente é melhor
    #E se cada um receber uma parte diferente do dado de treino, melhor ainda. Você especializa cada modelo em uma parte diferente do dado.

    #Mistura de esepcialisata tem um acomplamento entre os seletor/combinador
        #Todos tem que ser treinado simultaneamente, de maneria que o seletor dá peso para cada modelo para ele ir escolhendo
        #Ele chaveia entre os modelos

    #Rede de gating é um exemplo de mistura de especialistas, que tem como saida uma probabilidade de cada modelo ser o melhor para aquele X, ele recebe parte do X e decide qual modelo usar.
        #"Dado esse entrada qual o especilista que está acertando? vou amentar o peso dele na proxima interação"


#Redução de erros de generalização
    #Tem maneiras de combinar o modelos no ensemble
        #Uma delas é tirando uma mérdia simples de cada modelo, 
        #O mesmo vale para clusterização através de votação

    #Em mistura de especialsita, ele corta, e coloca partes de um modelo e partes de outras, como se fosse funções não continuas


#Gerando Ensembles
    #Popular nos anos 2000
    #Devem cometer erros distintos
    #Trade entre bias e variância
        #Similar entre o tempo de treino e overfitting
        #Suaviação é um exemplo qeu demonstra overfitting, você pode até usar mas, tem quepenalizar esse modelo no ensemble


#Teoria de ambiguidade
    #O que é uma combinação convexa?
        #A soma dos pessos é 1
    #A formula no slide faz muito sentido



#Como saber qual compenente escolher?
    #não tem como, não tem como prever comnjutno de teste


#Onde usar? Caso você não tenha certeza de um modelo muito bom, você pode usar ensemble para melhorar o resultado. Se você ja tem um modelo muito bom, não tem porque usar ensemble, já que ele garante uma média


#Esse método não leva em consideração outras coisas sem ser combinações complexas
    #A questão era "até que ponto combinar". Não tem forma milagrosa
    #Tem que medir diversidade.



#COmo medir diversidade?
    #Não tem jeito universal, cada caso é um caso
    #Pode usar correlação entre os modelos
    #Pode usar entropia etc...


#Etapas de construção de um ensemble não é deifinido
    #Gerar modelos
    #Seleção de modelos (Alguma tecnica)
    #Finalmente combinação (Média, modelo)

#O problema é que tem que ter conjuntos de dados para cada uma dessas partes (Além de testar). As vezes a seleção é pulada.


#Técnicas de seleção
    #Muitas, no slide. (Algumas baseam se podar, algumas em seelcionar o melhor e ir testando cada um que melhora. Algum testa aleatorio)
    #Se tiver 4 modelos tem um total de 2^4 = 16 combinações possíveis. ou seja, n²
    #Todas estrategias para isso são gulosas para testar todas, mas economziam em algo.
    #Cross-over é genetico, ele vai tendo mutações e cruzamentos, e vai testando o melhor conjunto.



#Tecnicas de construção
    #Implicitos é mudar dados de entrada, inicialização, arquitetura etc...
        #Atua no espaço de hipótese

    #Bosting é melhor que o bagging pois ele foca em erros anteriores.
        #Contudo diferente do bagging não pode ser treinado paralelamente


    
    #Manipular arquiteura (Tipo numero de neuronio) é ruim, são não é tão ruim como mudar inicialização

    #Algortiimo evolutirovo
        #semelhante aqueles 10110, mas nesse caso esse 0 e 1 muda toadas as propriedades do modelo, tipo arquitetura, dados, função de custo etc...
        #"métrica de diversidade"


    #Tem como variar o Kernel (C) também.
    

    #Explícitos é adicionar termos de regularização que forcem a diversidade
        #Atua na função de custo




#Mistura de Esepecialistas
    #Terá uma gating para fazer divisão
    #AGora o que quer se maximiar é probabilidade do especialista estar certo dado que eu o escolhi.
    