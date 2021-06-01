'''
A soma dos quadrados dos primeiros dez números naturais é,
1² + 2² + ... + 10² = 385

O quadrado da soma dos dez primeiros números naturais é,
(1 + 2 + ... + 10)² = 55² = 3025

Portanto, a diferença entre a soma dos quadrados dos primeiros dez números naturais e o quadrado
da soma é 
3025 - 385 = 2640.

Encontre a diferença entre a soma dos quadrados dos primeiros cem números naturais e o quadrado da
soma.
'''

def soma_quadrada(num):
	soma = 0
	for x in range(1,num+1):
		soma = soma + (x**2)
	return soma

def quadrado_soma(num):
	quadrado = 0
	for x in range(1,num + 1):
		quadrado = quadrado + x
	quadrado = quadrado**2
	return quadrado

diferenca = quadrado_soma(100) - soma_quadrada(100)

print(diferenca)
