# importar bibliotecas
import time #Tempo

numero = int(input( "Digite o Numero a Ser Convertido Para Binario::" "Seu Numero Decimal = "))

time.sleep(2)

valor = numero
valor = bin(valor)
print((" Seu Numero Em Binario = "),valor[2:])

time.sleep(5)
