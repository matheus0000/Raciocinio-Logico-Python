# importar bibliotecas
import time #Tempo

numero = int(input( "Digite o Numero a Ser Convertido Para Binario::" "Seu Numero Decimal = "))

time.sleep(2)

valor0 = numero
valor1 = numero
valor0 = hex(valor0)
valor1 = bin(valor1)
print((" Seu Numero Em Hexadecimal = "),valor0[2:])
print((" Seu Numero Em Binario = "),valor1[2:])

time.sleep(5)
