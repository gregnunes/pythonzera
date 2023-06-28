''''
# Levantando os próprios erros co Raise

Raise -> Lança execução

OBS: O raise não é uma função. É uma palavra reservada, assim com def ou quaelquer outra em python

Para simplificar, pense no raise como útil para que possamos criar próprias execuções e mensagens.

A forma geral de utilizar  é:

raise TipoDoErro('Mensagem de erro')

Ex 1.
def color(texto.cor):
  if type(texto) is not str:
    raise TypeEerror('texto precisa ser string')
  if type(cor) is not str:
    raise TypeError('cor precisa ser uma string')
print(f'O texto(texto) será impresso na cor')

OBS: Raise assim como return, finaliza uma função. Ou seja, nada após o raise é executado


   

