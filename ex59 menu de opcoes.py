from time import sleep
v1 = int(input('Digite o primeiro valor:'))
v2 = int(input('Digite o segundo valor:'))
op = 0

maior = v1 > v2
maior2 = v2 > v1
while op != 5:
    print('=-'*20)
    print('''
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos numeros
    [ 5 ] Sair do programa''')
    op = int (input(('Qual sua opção?')).strip())
    if op == 1:
        s = v1 + v2
        print('A soma dos valores é {}'.format(s))
    elif op == 2:
        m = v1 * v2
        print('Os valores multiplicados são iguais à {}'.format(m))
    elif op == 3:
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print('Entre {} e {} o maior é {}'.format(v1,v2,maior))
    elif op == 4:
        print('Digite os novos números')
        v1 = int(input('Digite o primeiro valor:'))
        v2 = int(input('Digite o segundo valor:'))
    elif op == 5:
        print('Você saiu do programa!')
    else:
        print('Opção inválida. tente novamente!')
    print('-='*20)
    sleep(1.5)
print('Fim do programa!')
