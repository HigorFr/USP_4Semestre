#Não teve a ultima auxiliar
    #Basciamente o que será visto é gerenciamento de memória

#Lembremos que os programas pensam que tem memoria infinita, e o OS define um local para ficar na memória. A partir dai o hardware consegue realziar uma soma de todos os endereços.

#Contudo surge um problema, fica buracos quando um programa cai e precisamos ir preenchendo para evitar desperdicío, mas nem tudo tem o mesmo tamanho.

#Para resolver isso, decidiu dividir a memória
    #Uma parte do programa pode inclusive não estar na memoria, e só uma parte rodando.
    #Cada parte é uma moldura (Que normalmente é do mesmo tamanho de uma página)



#Desse modo tem uma memŕoia virtual e um endereço de memória física.
    #Uma moldura será mapeada pela página virtual haverá uma divisão no endereço com um ID de moldura seguido pelo bits da memoria mesmo.
        #(Pelo q entendi uma moldura pode mapear uma página real)
    #Essa forma, os bits da memoria vão incrementando e quando batem no limite aumentam o ID da moldura.


#??? - Não entendi legal toda parte aqui no miolo

#No fim, você terá uma moldura mapeando uma página real



#Problema dessa abordagem é que pode disperdiçar memória, fica meio framentado já que um processo pode acabar não utilizando tudo.
    #Tem além disso que existir um gerenciamento, pois páginas de pouco bytes vão exigir muita requisição ao HD e paginas muito longas vão framentar muito

#O resto da aula n entendi legal



#Quando troca contexto a TLB também é alterada, pois isso o custo é alto



#Gerenciamento de memoria associativa TLB
    #Feito normalemnte pro Hardware, pois é mais rápido, exemplo do x86
    #Um processo pode ser bloqeuado se der page fault, o proprio SO toma conta, faz a requsição para o HD e bloqeuia
    #
    