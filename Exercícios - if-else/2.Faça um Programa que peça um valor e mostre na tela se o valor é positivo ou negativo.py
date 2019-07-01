n1=int( input('Digite o primeiro numero: ') )
n2=int( input('Digite o segundo numero: ') )

if n1 > n2 :
    print('O primeiro, {} , é maior' .format(n1))
else:
    if n1 == n2 :
        print('Os números são iguais')
    else:
        print('O segundo, {} , é maior' .format(n2))