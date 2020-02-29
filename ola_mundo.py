var1 = 50
var2 = 100
conta = (var1 * var2) * var1

def faz_conta():
    return 0

def oi():
    print('oi')

def soma_dois_valores(valor1, valor2):
    return valor1 + valor2

def raiz(valor, base):
    return valor ** (1 / base)

def e_par(valor):
    return (valor % 2) == 0  #para teste lógico, usa-se dois sinais de igual

def div_por_seis(valor):
    return ((valor % 2) == 0) and ((valor % 3) == 0)

def testes():
    print(div_por_seis(7))
    print(div_por_seis(9))
    print(div_por_seis(12))

    x = soma_dois_valores(3, 4)
    print(x)
    x = soma_dois_valores(2, 8)
    print(x)
    x = raiz(9, 2)
    print(x)

    print(e_par(4))
    print(e_par(5))

def testa_par():
    '''Lê um valor inserido pelo usuário, verifica se o valor é par e retorna uma mensagem.'''
    parada = False
    while parada == False:
        valor = input('Insira um valor numérico, ou aperte ENTER para encerrar...\n') #input sempre retorna um valor de texto, então tenho que transformar em número, integer, no caso.
        if valor =='':
            parada = True
        elif e_par(int(valor)) == True:
                print('O valor inserido é par.')
        else:
                print('O valor inserido é ímpar.')

testa_par()

def dez_mult_tres():
    '''Imprime os primeiros 10 números não negativos múltiplis de 3.'''
    cont = 0
    numero = 1
    while cont < 2:
        if numero % 3 == 0:
            print(numero)
            cont = cont + 1  #posso colocar cont += 1
        numero += 1

dez_mult_tres()

















