#Algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
num = int(input("Digite um número: "))
dobro = num*2 #Multiplicar o valor por 2
triplo = num*3 #Multiplicar o valor por 3
raiz = num**(1/2) #Elevar o valor a meio (1/2), ou exponenciação/potenciação
print("O número que você digitou é {}\nO dobro: {}\nO triplo: {}\nA raiz quadrada: {:.2f}".format(num, dobro, triplo, raiz))
