import math

# Isto é uma calculadora super basica

def isFloat(n):
    try:
        float(n)
        return True
    except:
        return False

def turnIntoNumber(n):
    try:
        return  int(n)
    except:
        return float(n)

def operacaoValida(componentes):
    if(components.__len__() == 3 and (componentes[1] == '+' or componentes[1] == '-' or componentes[1] == '*' or componentes[1] == '/')):
        if(componentes[0].isnumeric() or isFloat(componentes[0])):
            if(componentes[2].isnumeric() or isFloat(componentes[2])):
                return True

    return False

def calcular(componentes):
    n1 = turnIntoNumber(componentes[0])
    n2 = turnIntoNumber(componentes[2])

    if(componentes[1] == '+'):
        result = n1 + n2

    if (componentes[1] == '-'):
        result = n1 - n2

    if(componentes[1] == '*'):
        result = n1 * n2

    if (componentes[1] == '/'):
        if(n2 != 0):
            result = n1 / n2
        else:
            result = 'Impossivel n / 0'

    print(f'Resultado = {result}\n')

if __name__ == '__main__':
    print('----------------------------')
    print('| Calculadora Super Basica |')
    print('----------------------------')

    components = [' ', ' ', ' ']
    novaoperacao = True

    while (not operacaoValida(components)) or novaoperacao:
        print('\nInsira uma operação basica (+ - * /)')
        print('(numero) (opreação) (numero)')
        print('Exemplo: 2 * 5')

        print('> ', end =' ')
        operacao = input()

        components = operacao.split(' ')

        if(operacaoValida(components) or components.__len__() == 3):
            calcular(components)

            print("Quer fazer mais operações? s->Sim, n->Não")
            print('> ', end =' ')
            escolha = input()

            if(escolha != 's'):
                novaoperacao = False

        else:
            print('Operação não válida!!!\n')

    print('----------------------------')
    print('----------------------------')
