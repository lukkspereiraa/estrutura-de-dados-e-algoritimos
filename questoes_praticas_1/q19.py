numeros = input('Digite uma lista de números separados por espaço: ').split()

numeros = [int(numero) for numero in numeros]

numeros_ordenados = sorted(numeros)

print(numeros_ordenados, ' lista ordenada de forma cresente')
