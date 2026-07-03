from lib.financeiro import *
from lib.menu import *

movimentação = []


print('\tCONTROLE FINANCEIRO', end='\n\n')
while True:
    opc = menu(['adicionar receita', 'adicionar despesa',
                'mostrar saldo', 'mostrar relatorio', 'sair'])
    if opc == 1:
        adicionar_receita(movimentação)
        print()
    elif opc == 2:
        adicionar_despesa(movimentação)
        print()
    elif opc == 3:
        mostrar_saldo(movimentação)
        print()
    elif opc == 4:
        mostrar_relatorio(movimentação)
        print()
    elif opc == 5:
        print('Saindo...')
        break




