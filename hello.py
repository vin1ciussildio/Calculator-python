#Agradecimento por usar o programa:
print ("Olá bem vindo a minha calculadora em python ^W^")

#Input do nome do usuario:
nome = input("Qual é o seu nome ?: ")
print(f"Muito prazer em conhecer {nome} ^W^")

#Input do Primeiro numero: 
print ("vamos começar com o basico ^W^")
print ("Digite um numero qualquer (Usar (.) em caso de numeros com virgula): ")
num1= float( input())

#Imput do segundo numero:
print ("Digite um segundo numero qualquer (Usar (.) em caso de numeros com virgula): ")
num2= float( input())

#Funçoes
soma = float (num1 + num2)
multiplicacao = float (num1*num2)
divisao = float (num1/num2)
subitracao = float (num1-num2)

#Resultados
print (f"O primeiro numero usado para os cauculos e:  {num1}")
print (f"O segundo numero usado para os cauculos e:  {num2}")
print (f"A soma dos dois numeros e:  {soma}")
print (f"A multiplicacao dos dois numeros e::  {multiplicacao}")
print (f"A divisao dos dois numeros e:  {divisao}")
print (f"A subitracao dos dois numeros e:  {subitracao}")