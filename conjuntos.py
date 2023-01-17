# - Conjuntos em qualquer linguagem de programação, estamos fazendo referência a teoria de conjuntos
# - da matmatica.

#Conjuntos são chamados de sets 
# Sets não possuem valores duplicados.
#Não possuem valores ordenados. 
# Eelemntos não são acessados via indice, conjuntos não são indexados.

#Conjunto são bons para armazenamento de elementos, mas não importa a ordenação.
# Quando não se preocupa com chaves, valores e itens duplicados.

# Os Sets são referênciados em Python com chaves {}
# Diferença entre conjunto e mapas:
#Dicionário tem chave e valor.
# Conjunto tem apenas Valor.

# Definindo conjunto:

# forma 1
#s = set({1 , 2 , 3 , 4, 5 , 5 , 6 , 7 , 2 , 3}) # Valores Repetidos.
#print(s)
#print(type(s))
# OBS: Ao criar o conjunto,  os valores repetidos serão ignorados.

# Forma 2 (mais comum )
# s = {1, 2 , 3 , 4 , 5 , 5}
#print(s)
#print(type(s))

#if 3 in s:
 #   print('Tem o 3')
#else:
 #   print('Não tem o 3')
 
 #OBS: podemos verificar se determinado elemento está está contido no conjuunto.
 

""""""
#Importante que além de não termos valores duplicados, não temos ordem.

#lista = [99, 2, 24, 23, 12, 44, 1, 44]
#print(f'lista: {lista}')
    
#tupla = (99, 2, 24, 23, 12, 44, 1, 44, 1)
#print(f'Tupla: {tupla}')

#dicionario = (lista , 'dict')
#print(f'Dicionário: {dicionario}')

#conjunto = {99, 2, 34, 23, 12, 44, 1, }
#print(f'Conjunto: {conjunto}')

#Rmovendo elementos de um conjunto

#forma1

# s={1, 2, 3, 4}
#s.remove()

#Se o valor não existir = keyerror

#forma2
#s.discard()

#OBS: Se o valor não for encontrado, nenhum erro é gerado

#Nenhum valor é retornado 


#Copiando uum conjunto para outro

# s= {1, 2, 3}
#forma1 Deep Copy
#novo = s.copy()

#Forma 2 Shallow Copy
#novo = s
#novo.add(4)


# Podemos remover todos os itens de um conjunto
# s.clear()


# Métodos Matemáticos de conjunto

#forma 1 .union

# Forma 2 utilizando (Pipe |)

# Forma 3 Ambiguidade (.intersection)

# Formma 4 Utilizando (&) 



# Apenas em um conjunto, utilizar .difference 




