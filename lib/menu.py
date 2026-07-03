def leiaInt(texto):
    while True:
        try:
            num = int(input(texto))
        except:
            print('Erro: por favor, digite um número inteiro válido')
        else:
            return num

def menu(lista):
    print(f' {" MENU PRINCIPAL ":=^32} ', end='\n\n')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    while True:
        opc = leiaInt('Digite a opção: ')
        if opc <= 0 or opc > len(lista):
            print('Digite uma opção válida acima!')
        else:
            return opc