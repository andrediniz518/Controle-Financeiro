def leiaFloat(texto):
    while True:
        try:
            num = float(input(texto))
        except:
            print('Erro: por favor, digite um número válido')
        else:
            return num

def adicionar_receita(movimentação):
    receita = dict()
    descrição = str(input('Qual a descrição? '))
    while True:
        valor = leiaFloat('Qual valor? R$')
        if not valor > 0:
            print('Digite um valor maior que R$0')
        else:
            break
    receita['tipo'] = 'receita'
    receita['descrição'] = descrição
    receita['valor'] = valor
    movimentação.append(receita)
    print('Receita criada com sucesso.')

def adicionar_despesa(movimentação):
    despesa = dict()
    descrição = str(input('Qual a descrição? '))
    while True:
        valor = leiaFloat('Qual valor? R$')
        if not valor > 0:
            print('Digite um valor maior que R$0.')
        else:
            break
    despesa['tipo'] = 'despesa'
    despesa['descrição'] = descrição
    despesa['valor'] = valor
    movimentação.append(despesa)
    print('Despesa criada com sucesso.')

def calcular_saldo(movimentação):
    receita = despesa = total = 0
    for item in movimentação:
        if item['tipo'] == 'receita':
            receita += item['valor']
        else:
            despesa += item['valor']
    total = receita - despesa
    return total

def mostrar_saldo(movimentação):
    if len(movimentação) > 0:
        saldo = calcular_saldo(movimentação)
        print(f'Saldo atual R${saldo:.2f}')
    else:
        print('Adicione movimentações para consultar saldo.')

def mostrar_relatorio(movimentação):
    if len(movimentação) > 0:
        print(f'{" RELATÓRIO ":=^32}')
        for item in movimentação:
            print(f'{item['tipo']}\t|\t{item['descrição']}\t|\tR${item['valor']:.2f}')
        mostrar_saldo(movimentação)
    else:
        print('Adicione movimentações para consultar relátorio.')