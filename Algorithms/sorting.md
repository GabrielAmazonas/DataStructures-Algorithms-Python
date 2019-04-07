Ordenaḉão (Sorting):

 - Bubble Sort:
        - É uma das abordagens mais simples, no entanto não é eficiente. Sua eficiência é O(n²).
        Consiste em comparar cada elemento com seu elemento adjacente, trocando-os de ordem caso necessário.
        - É chamada de "Bubble" pois a cade interação o maior elemento da array vai para a sua posição correta após ordenado 
        (considerando uma ordenação crescente de números inteiros)
        - Complexidade Espacial (Space Complexity) : O(1), pois Bubble Sort ẽ realizada in-place e não são necessárias outras
        estruturas de dados.
        
 - Merge Sort:
    - Utiliza a estratégia "divide and conquer": Quebra a lista em múltiplas partes e re-organiza estas partes, antes de
    reconstruir a lista Ex.: Divide uma array de 7 posições em 4 arrays, 3 de 2 posições e uma de tamanho 1, ordenam-se
    os elementos de cada um desses novos arrays, e posteriormente, criam-se dois novos arrays, um de 3 posições e outro 
    de 4 posições, comparando os arrays ordenados no passo anterior. O primeiro item do novo array será o menor entre os
    primeiros itens de cada array utilizada para originar um novo, e assim sucessivamente.
    - Complexidade n . log (n) (mais eficiente do que a bubble sort), porém possui maior complexidade espacial por criar
    diversas novas etruturas de dados.
    
 - Quick Sort:
    - Em muitos cenários, é o algoritmo mais eficiente de ordenação. Consiste em dividir a lista em duas, selecionando
    um elemento de cada, e ordená-lo de forma que este elemento fique no meio da nova lista.
    - Complexidade Espacial: O(1)