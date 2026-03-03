#Exercício B1 - Número Positivo ou Negativo

num = int(input("Digite um numero: "))

if num >= 0:
    print("Numero positivo")
else:
    print("Numero negativo")



#Exercício B2 - Maior de Idade

idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print("És maior de idade")
else:
    print("Ainda nao és maior de idade")


#Exercício B3 - Número Par ou Ímpar

valor = int(input("Digite um valor: "))

if valor % 2 == 0:
    print("Numero par")
else:
    print("Numero impar")


#Exercício B4 - Comparação de Dois Números

num_1 = int(input("Digite o primeiro numero: "))
num_2 = int(input("Digite o segundo numero: "))

if num_1 > num_2: 
    print("O primeiro numero é maior que o segundo ")
else:
    print("O segundo numero é maior que o primeiro")

#Exercício B5 - Password Simples   

password = str(input("Digite a sua password: "))
password_correta = "python"

if password == password_correta : 
    print("Acesso permitido ")
else:
    print("Acesso negado")

#Exercício I1 - Classificação de Nota

nota = int(input("Digite a sua nota :"))

if nota >= 18:
    print("Excelente")
elif nota >= 14:
    print("Bom")
elif nota >= 10:
    print("Suficiente")
else:
    print("Reprovado")

#Exercício I2 - Classificação de Idade    

idade_1 = int(input("Insira a sua idade: "))

if idade_1 < 13:
    print("És considerado(a) um(a) criança")
elif idade_1 >= 13 and idade_1 <= 17:
    print("És considerado(a) um(a) jovem")
elif idade_1 >= 18 and idade_1 <= 64:
    print("És considerado(a) adulto(a)")
else: 
    print("És considerado(a) um(a) sénior")



#Exercício I3 - Múltiplo de 3 e 5

numero = int(input("Digite um numero: "))

if numero % 3 == 0 and numero % 5 == 0:
    print("Múltiplo de 3 e de 5")
elif numero % 3 == 0:
    print("Múltiplo de 3")
elif numero % 5 == 0:
    print("Múltiplo de 5")
else:
    print("O número não é múltiplo de 3 nem de 5")  


#Exercício I4 - Login com Utilizador e Password

user = str(input("Digite o username: "))
password = int(input("Digite a password: "))
               
user_correto = "admin"
pass_correta = 1234

print(user == user_correto and password == pass_correta)



#Exercício I5 - Número dentro de intervalo
num = int(input("Digite um numero: "))

if num >= 10 and num <= 20 :
    print("Está dentro do intervalo")
else:
    print("O número não está dentro do intervalo")



#Exercício A1 - Sistema Multibanco Simples

saldo = 1000
valor = int(input("Digite o valor que deseja levantar: "))
saldo_restante = saldo - valor
if valor <= saldo :
    print(f"Autorizado! O saldo restante é {saldo_restante} euros")
else:
    print("Rejeitado!")
    print(f"Não consegues levantar {valor} euros , ficarias com {saldo_restante} euros")



#Exercício A2 - Maior de Quatro Números

num_1 = int(input("Digite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))
num_3 = int(input("Digite o terceiro número: "))
num_4 = int(input("Digite o quarto número: "))

if num_1 >= num_2 and num_1 >= num_3 and num_1 >= num_4:
    print("O maior número é: ",num_1)
elif num_1 <= num_2 and num_2 >= num_3 and num_2 >= num_4:
    print("O maior número é: ",num_2)
elif num_1 <= num_3 and num_3 >= num_2 and num_3 >= num_4:
    print("O maior número é: ",num_3)
else:
    print("O maior número é: ",num_4)



#Exercício A3 - Classificação de IMC (Simplificado)

peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite a sua altura (m): "))

imc = peso / (altura * altura)

print("IMC:", (imc, 2))

if imc < 18.5:
    print("Baixo peso")
elif imc < 25:
    print("Normal")
elif imc < 30:
    print("Excesso de peso")
else:
    print("Obesidade")



#Exercício A4 - Sistema de Desconto

valor_compra = int(input("Digite o valor da compra: "))
desconto = 0

if valor_compra >= 100:
    desconto = valor_compra * 0.1
    valor_final = valor_compra - desconto
    print(f'O seu desconto é de {desconto} e o valor final e {valor_final}')
elif valor_compra >= 50:
    desconto = valor_compra * 0.05
    valor_final = valor_compra - desconto
    print(f'O seu desconto é de {desconto} e o valor final e {valor_final}')
else:
    print("Não tem direito a desconto")

    

#Exercício A5 - Verificação de Ano Bissexto (Simplificado)

ano = int(input("Digite um ano: "))

if ano % 4 == 0: 
    print("Ano bissexto")
else:
    print("Ano normal")

