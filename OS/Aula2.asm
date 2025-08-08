#Aula2

#Tipos e estruturas de um SO - Continuando um Overview


    #Mutias classificações
        -Hardware compartilhado 
            - Monotarefa/Monoprogramado (Hardware antigo ainda usado)
                -Facil de ser implementado
                -Um programa por vez na memória
                -Não aproveita todos os recursos (Pois gera gargalo entre hardware)
                    -Na pratica uma tarefa tem os estados: nova, executando ou terminando
            -Multitarefa/Multiprogamado (Atual)
                -Mantém vários programas na meória principal, compartilhando o tempo e recursos
                -Uma roda enquanto outra está parada aguardando algo
                -Complexo de implementar
                -Surgiu já no hardware, a memória era literalmente parcionada e cada programa ocupava um bloco (Físico mesmo)
                    -SO ia trocando e revezando (Criava a impressão de paralelismo para o usuário)
                    -Isso através de um algoritimo (Round Robin)
                -Aproveita muitos os recrusos, isso aumenta a produtividade
                -Pode ser Multiusuario (Ou seja, vários usuarios em um mesmo sistema) ou Mono (Apenas 1)
                -Estados de Nova (Não começou), pronta (Pode voltar para o processador, nada impede ele), Suspensa (Aguardando entrada ou saída), Executando e ou terminada.
                    -Logo tem meio que um loop entre pronta, executando e suspensa
                -Tem varios algortimos para definir quem roda (pode usar prioridade, aleatorio, etc...) caso tem varias tarefas prontas

                -Surtos de CPU acontecem tamém nisso, em modelagem de dados, há um grande periodo de entrada e saída, e depois vem uma onda muito grande de uso de CPU
                    -Tem tipos processos que são mais ou menos. (CPU-BOUND ou I/O - BOUND)
                    -Ideal é equilibrar , jogar coisas fora de processos I/O bound junto do CPU bound para manter ele ocupado

                - SO também pode interromper o processo, e limpar ele da memória, por ele ter terminado, ou por algum erro
                    -Toda vez que ele for fazer entrada e saída ele tem que chamar o SO, nenhum programa tem acesso direto ao hd
                        -Com chamada ao sistema
                    -Tudo com algoritimos

        
        -Classificação quanto à interação permitida
            -Batch
                -Primeiros à surgir, antigamente cada "Job" (programa) era um cartão perfurado, e isso era muito ineficiente para processamentos em sequencia (como impressora), pois não dava pra fazer tudo ao mesmo tempo
                    -Pra isso foi criado o sistema em lote (originou o .bat), que permitiria uma ordem de execução de linhas código sem interação com o usuário
                    -Processo chamado Spooling de impressão
                

            -Pode ser iterativo ou não (Ou seja, com precença do usuário)
            -Tempo compartilhado
                -


            -Tempo rela
                -Tempo de respostas limitadas
                -Usado para fins especificos, como sensores em fábricas
                -É uma corrida conta o tempo para o processo
                -Tem os "Hard Real Time", que é um modelo obrigado os processos a estarem no prazo
                -Tem os "Soft Real Time", o inverso, que é usado para vídeo e aúdio, que não são críticas mas podem ser ignorados se não cumprirem o prazo (O audio e o video por exemplo são continuos, não faz sentido travar em um frame)
                    -Tem algoritimos apra cada um deles

            -Modo Usuario ou Modo Kerven (São modos de acessos)
                -Kernel tem acesso a tudo, usuário não (Principalemnte coisa relacionada diretamente aos Inputs e Saídas)
                    -São bits de registrador que verifica se a instrução pode ser feita ou não no hardware
                    -Privilegio é do kernel
                -Garante segurança do Hardware
                -A bios quando roda no boot sempre roda no kernel
                -No fim o "Kernel" é um bit do hardware, é o suprasumo do poder, que o SO sempre tem e gerencia. Isso é diferente do root (root está dentro do SO). Mas os comandos em sí é o SO. Ele já inicia com o esse bit ativado, e gerencia quem vai ter também além dele.

        -Organizações
            -Monolito
                -Forma primitiva
                -Interface absoluta, um grande bloco de ponto para qualquer coisa
                -Na pratica é mais fragmentado, o linux e o windoes são exemplos
                    -UNIX por mais que se seja módulos, ainda no geral é uma grande interface, pois não há hierarquia obrigatoria
                -No geral é o hardware em uma ponte e chamada dos sistema em outra
                -Como tudo está compilado junto, é extremamente rápido seu funcionamento, mas em desvantagem fica desorganizado
            -Em Camadas:
                -Chamadas vão descendo, não fica vários modulos em uma mesma camada, elas só conseguem subir ou descer conforme a hierarquia
                -O nucleo do NT é assim
            -MicroKernel
                -Nucleo minimo, para que ele seja usado o minimo possíve
                -Ele funciona só para enviar mensagem para o hardware mesmo, mais nada
                -Memoria, Tratamento de arquivo, tudo isso roda em modo usuário e convers com o kernel
                -Normalmente tem mais chamadas, pois fica quase um ping pong entre um programa e outro usando kernel de ponte
                -Usado no Minix e Symbian.
                -Muito resistente quanto a falhas, é extremamente modulável e pequeno. Mesmo se for módulo de memória por exemplo caindo, ele consegue levantar novamente. (Sim, até o gerenciamento de memória fica com o usuário)
            
        -Lembrando que o SO é formado por partes tanto no modo kernel tanto no modo usuario. Não é porque que está no modo usuário que não é SO

            -Maquina virtual
                -Criado pela IBM
                -Conceito d enuvem se baseia nela
                -Replica o hardware várias vezes, para que cada replica utiliza um SO diferente. Desse modo o SO interage com um Hardware falso.
                -Bom para criar ambientes isolados, mas ao custo de complexidade e processamento devido o gerenciamento d erecurso

            -Cliente e Servidor
                -É um microkernel, com módulos separados em várias máquinas
                -Totalmente distribuido, funciona com base em chamadas
                -Literalmente mutios resistente a falhas, muito fácil criar redundancias
                -LENTO
            
        -Obs existe uma discussão muito grande entre Monolitico e Microkernel. Existe um pouco até hoje, e inclusive tem uma briga do Andrew Tanenbaum e do Linus sobre.
                

                


        

