"""""""""
Listas

Listas em python funcional como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem Dinâmico e também de podermos colocar qualquer tipo de dado.

Linguagens C/Java: Arrays 
    - Possuem tamanho e tipo de dado fixo:
    Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array
    será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.

-   Dinâmico: Não possuem tamanho fixo; ou seja, podemos criar a listae simplesmente ir adicionando elementos;
-   qualquer tipo de dado; Não possuem tipo de dado fixo; Ou seja, podemos colocar qualquer tipo de dado;
As listas em Python são representadas por colchetes: []
"""""""""

type([])

lista1 = [1, 90, 40, 50, 80, 10, 30]

lista2 = ['g', 'e', 'b', 'k', 'f', 'o']

lista3 = []

lista4 = list(range(11))

lista5 = ('Hello World ')

# Podemos checar se determinado valor está na lista

#num = 50
#if num in lista4:
 #       print(f'Encontrei número {num}!')

#else:
      
#        print(f'Não encontrei o {num} !')
        
# Podemos facilmente ordenar uma lista 
#lista1.sort()
#print(lista1)


##print(lista1[::-1])
##print(lista2[::-1])
## Reverse Lista 
##lista1.reverse()
##lista2.reverse()

#utilizando while 
#carrinho = []
#produto = ''

# while produto != 'sair:
#print("Adicione um produto na lista ou digite 'sair' para sair:")
#produto = input()
# if produto != 'sair':
    #carrinho.append(produto)
    
#for produto in carrinho:
#print(produto)