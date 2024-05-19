"""escopo de variáveis"""

"""
as variáveis globais

as variáveis locais

"""

x = 5

def funcao():
    x = 3
    print('Valor da variável local: ', x)

funcao()
print('Valor da variável global: ', x)

y = 'Gabriel' # nome
z = 1.74 # altura
t = '000.000.000-00' # cpf
l = 23 # idade

# usar sempr enomes mais explicativos para as variáveis
nome = 'Gabriel'
altura = 1.74
cpf = '000.000.000-00'
idade = 23