# alglign2
O código apresentado simula uma versão digital simplificada da máquina Enigma, utilizando conceitos de álgebra linear, principalmente matrizes. Nesse código, fizemos uma implementação que usa matrizes de permutação e codificação one-hot para cifrar e decifrar mensagens.
O código é dividido em duas partes principais: funções de criptografia e funções de manipulação de strings e matrizes.
1. Funções de Criptografia
Estas funções são responsáveis por cifrar e decifrar mensagens utilizando operações matriciais.
Função cifrar(msg: str, P: np.array) -> str:
Descrição: Esta função cifra uma mensagem usando uma matriz de permutação P.
Processo: A mensagem msg é convertida em uma matriz one-hot M usando a função para_one_hot. Em seguida, a matriz de permutação P é multiplicada por M (P @ M), resultando na matriz cifrada M_cifrada. Finalmente, a matriz cifrada é convertida de volta para string usando para_string.
Álgebra Linear: A matriz de permutação P reordena as colunas da matriz one-hot M, essencialmente aplicando uma transformação linear que embaralha as letras da mensagem original.
Função de_cifrar(msg: str, P: np.array) -> str:
Descrição: Esta função decifra uma mensagem cifrada usando a inversa da matriz de permutação P.
Processo: Similar à cifragem, a mensagem cifrada é convertida para uma matriz one-hot M_cifrada. A matriz inversa de P (np.linalg.inv(P)) é multiplicada por M_cifrada, resultando na matriz original M_original. A matriz original é então convertida de volta para string.
Álgebra Linear: A matriz inversa de P reverte a transformação linear aplicada durante a cifragem, retornando a mensagem original.
Função enigma(msg: str, P: np.array, E: np.array) -> str:
Descrição: Simula o funcionamento da máquina Enigma, cifrando uma mensagem caracter por caracter e alterando a matriz de permutação P a cada iteração.
Processo: Para cada caractere da mensagem, aplica-se a função cifrar usando a matriz P atual. Após cifrar cada caractere, P é atualizada multiplicando-a por uma matriz de evolução E (P = P @ E), que altera a matriz de permutação para a próxima iteração.
Álgebra Linear: A matriz E modifica a permutação aplicada a cada caractere, simulando a complexidade das rotações dos rotores na máquina Enigma original.
Função de_enigma(msg: str, P: np.array, E: np.array) -> str:
Descrição: Decifra uma mensagem cifrada usando o procedimento inverso ao da função enigma.
Processo: Para cada caractere cifrado, aplica-se a função de_cifrar e, em seguida, atualiza-se P usando a matriz de evolução E.
Álgebra Linear: Assim como na cifragem, a matriz P evolui a cada caractere para reverter a sequência de transformações aplicadas durante a cifragem.
2. Funções de Manipulação de Strings e Matrizes
Estas funções convertem entre representações de strings e matrizes, essenciais para aplicar operações matriciais.
Função para_one_hot(msg: str) -> np.array:
Descrição: Converte uma string em uma matriz one-hot, onde cada coluna representa um caractere da string.
Álgebra Linear: A matriz one-hot é uma forma conveniente de representar vetores canônicos, onde cada caractere é mapeado para uma base ortonormal em um espaço vetorial.
Função para_string(M: np.array) -> str:
Descrição: Converte uma matriz one-hot de volta para uma string.
Álgebra Linear: Este processo inverte a conversão de vetor canônico para string, extraindo a base dominante em cada coluna.
Este código demonstra como conceitos de álgebra linear podem ser aplicados à criptografia. As operações de multiplicação de matrizes e inversão de matrizes são centrais para a transformação de mensagens, espelhando o funcionamento de máquinas de criptografia históricas, como a Enigma. A compreensão dessas operações oferece insights valiosos sobre a aplicação prática da álgebra linear em áreas como segurança da informação.

