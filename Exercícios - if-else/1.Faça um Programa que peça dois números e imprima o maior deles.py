A = int(input('Primeiro Numero = '))
B = int(input('Segundo Numero = '))
C = int(input('Terceiro Numero = '))
# 'Procurando quem e menor'
if A < B and A < C:
    menor = A
if B < C and B < A:
	maior = B
if C < A and C < B:	
    menor = C
# 'Procurando quem e maior'	
if A > B and A > C:
    maior = A
if B > C and B > A:
	menor = B
if C > A and C > B:	
    maior = C
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))	
