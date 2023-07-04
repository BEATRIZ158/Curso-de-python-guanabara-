#Tipo primitivo e informações
a = input("Digite qualquer coisa: ")
print(f"Tipo primitivo: {type(a)}") #Função que retorna o tipo primitivo de 'a'
print(f"Todos os caracteres são letras? {a.isalpha()}") #Usado para verificar se todos os caracteres são alfabéticos
print(f"Todos os caracteres são minúsculos?{a.islower()}") #Metodo que verifica se todos os caracteres são minúsculos, retorna TRUE ou FALSE.
print(f"Todos os caracteres são maiúsculos? {a.isupper()}")#Verifica se são maiúsculos 
print(f"Tem espaços? {a.isspace()}") #Metodo que retorna TRUE se todos os caracteres forem espaços em branco
print(f"É numérico? {a.isnumeric()}") #Retorna TRUE se todos os caracteres forem numéricos
print(f"É alfanumérico?{a.isalnum()}") #Verifica se todos são alfabéticos ou numéricos
print(f"É decimal? {a.isdecimal()}") #Retorna TRUE se todos os caracteres forem decimais
print(f"Está capitalizado? {a.istitle()}") #Verifica se a primeira letra da string é maiúscula e as demais minúsculas, retorna TRUE ou FALSE
