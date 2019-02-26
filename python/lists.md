Listas são apenas agrupamento de coisas com uma ordem determinada.

Podemos adicinar itens à uma lista, bem como remover itens ou checar cada item da mesma.

- Python Lists:

    As listas em python implementam bastante código por debaixo dos panos, já de maneira otimizada.

    Inserir um elemento tem complexidade O(n), enquanto operações que acessam um elemeto em um índice específico possuem complexidade O(1).

    Calcular o tamanho de uma lista utilizando a função len() tem complexidade O(1).

- Linked Lists:
    Nesta estrutura de dados, cada elemento possuí uma referência (ligação) com o próximo elemento da lista.

    Inserir um elemento entre dois outros elementos teria complexidade constante O(1). Exemplo.: Inserir o elemento X entre os elementos AB presentes em uma lista ligada:

    Elemento A possui uma propriedade next, que é uma referência para o elemento B.

    Elemento B possui uma propriedade next, que é uma referência nula, pois não existem elementos após B na lista.

    Para inserir X entre A e B, alterar a referência next de A para X. Alterar a referência next de X para B.

    Nota: Nesta operação de inserção, não foi necessário iterar ao longo da lista.

- Doubly Linked Lists
    Seguem as mesmas premissas das Linked Lists, contudo os elementos também possuem uma referência apontando para o elemento antecessor na lista.