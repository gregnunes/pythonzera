#len() -> Retorna o tamanho

#print(len('Geek University'))
#print(len([1, 2 , 3 , 4 , 5]))
#print(len((1, 2, 3, 4, 5)))
#print(len({1 ,2  , 3 , 4 , 5}))
#print(len({'a' : 1 , 'b': 2, 'c' : 3, 'd' : 4 , 'e' : 5}))
#print(len(range(o , 10)))

#por debaixo dos panos, quando utilizamos a função len()

#Dunder len
#print('Geek University'._len_())

""""""
#Abs

#abs() -> Retorna o valor absoluto de um numero ineiro ou real.

#print(abs(-5))
#print(abs(5))
#print(abs(3.14))
#print(abs(-3.14))

#Sum

# sum() ->Recebe como parâmetro umiteráve, podendo receber um valor inicial,e retornara soma total dos elementos.
#OBS: O valor incial default = 0

#Exemploes Sum

#print(sum([1, 2, 3, 4, 5]))
#print(sum([1, 2, 3, 4, 5],5))
# Possível usar com tuplas, set, float

#Round
# round() -> Retorna um número arredondado para n dígito de precisão a cada decimal.
#Exemlplos round

#print(round(10.2))
#print(round(10.5))
#print(round(1.2121212121, 2))
#print(round(1.2199999, 2))