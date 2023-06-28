'''
O bloco Try except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código. Previnindo 
assim que o programa pare de funcionar e o usuário receba mensagem de erro inesperada.

EX: 
try:
    numerador = 10
    denominador = 0
    resultado = numerador / denominador
    print(resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")

    Neste exemplo, o bloco try tenta executar a divisão entre o numerador e o denominador. 
    Como o denominador é zero, isso gerará uma exceção ZeroDivisionError. 
    O bloco except captura essa exceção e imprime uma mensagem de erro apropriada.

    try:
    numero_str = "ABC"
    numero_int = int(numero_str)
    print(numero_int)
except ValueError:
    print("Erro: Não é possível converter a string em um número inteiro.")

  Neste exemplo, o bloco try tenta converter a string "ABC" em um número inteiro usando a função int().
  No entanto, como a string contém caracteres não numéricos, ocorrerá uma exceção ValueError. 
  O bloco except captura essa exceção e exibe uma mensagem de erro adequada.

Em ambos os exemplos, o bloco except é usado para capturar exceções específicas (ZeroDivisionError e ValueError, respectivamente).
No entanto, também é possível usar um bloco except genérico, sem especificar o tipo de exceção, para tratar 
qualquer exceção que ocorra no bloco try. Por exemplo:

try:
    # Código que pode gerar uma exceção
except:
    # Tratamento para qualquer exceção que ocorra

É importante tratar as exceções de forma apropriada para lidar com erros e garantir que o programa continue sua execução de forma estável.
