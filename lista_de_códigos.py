# -*- coding: utf-8 -*-
"""Lista de códigos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EnYhbNREJ1NlvyC5G7YTxMugZH6MQEJE
"""

#Faça um Programa que mostre a mensagem "Alo mundo" na tela.

msg= 'Olá mundo'
print(msg)

#Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

user= int(input('Digite um número: '))
print(f'O número informado foi {user} ')

#Faça um Programa que peça dois números e imprima a soma.

x = int(input('Digite um número: '))
y = int(input('DIgite outro número: '))

soma = x+y
print(soma)

#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = float(input('Digite a nota do primeiro bimestre: '))
nota2 = float(input('Digite a nota do segundo bimestre: '))
nota3 =float(input('Digite a nota do terceiro bimestre: '))
nota4 = float(input('Digite a nota do quarto bimestre: '))

media = (nota1) + (nota2) + (nota3) + (nota4)/4

print(media)

#Faça um Programa que converta metros para centímetros.

metros = float(input('Informe a quantidade de metros desejado: '))
centimetros = ()
converter = (metros)/100 
print(f'O valor em centímetros convertidos é de {converter} ')

#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math 

raio = int(input('Digite o raio: '))
area = 3.14 * (raio ** 2)

print(area)

#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
import math

baseQ = int(input('Digite a base do quadrado: '))
alturaQ = int(input('Digite a altura do quadrado: '))

resultado = (baseQ)*(alturaQ)
print(resultado)

#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

salario = float(input('Quanto você ganha por hora trabalhada? '))
cargaH = int(input('Quantas horas você trabalha por mês?'))
salarioM = (salario)*(cargaH) 

print(salarioM)

#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9)
graus = float(input('Digite a temperatura: '))
F = graus
C = 5*(F - 32)/9
print(C)

#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

Fh = float(input('Digite a temperatura: '))
Calor = Fh
F = (9*((Fh +32)))/5
print(F)

#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = float(input('Digite um número: '))

A1 = (2 * n1)*(n2/2)
B2 = (n1*3)+n3
C3 = n3**3
print(A1)
print(B2)
print(C3)

#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

pesoI = float(input('Digite seu peso: '))
Altura= float(input('Digite sua altura: '))
forms = (72.7*Altura) - 58
print(forms)

#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

sexo = input('Digite o seu sexo: ')
Altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

if sexo == 'Masculino':
  forms = (72.7*Altura) - 58
  print(forms)

else: 
 forms = (62.1*Altura) - 44.7
 print(forms)

#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

pesoP = float(input('Digite a quantidade de quilos em peixes: '))
multa = float(4.00)

if pesoP > 50:
  c = pesoP - 50 
  excesso = (c*(4.00))
  print(excesso)

#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:

salario = float(input('Digite o valor do seu salário: R$'))
horas = int(input('Digite a quantida de horas trabalhadas: '))
salario_bruto = (salario) * (horas)
IR = (salario_bruto) * (0.11)#O valor total do desconto será mostrado abaixo
INSS = (salario_bruto) * (0.08)
sindicato = (salario_bruto) * (0.05)
salario_liquido = (salario_bruto) - (IR) - (INSS) - (sindicato)
mostrar = f'No final do mês seu salário será: {salario_bruto} \nO seu imposto de renda é: {IR}\nO valor desconto do INSS foi: {INSS}\nO desconto sindical foi: {sindicato}' 
print(mostrar)

#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

casa = float(input('Quantos metros quadrados tem a área a ser pintada? '))
area = (casa) 
lata = 0

while area >= 54:
  lata = lata + 1
  area = area - 54

lata = lata + 1 
valor_tinta = (lata) * 80
print( f'Os metros pintados foi: {lata} e o preço pago foi: {valor_tinta}' )

#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

arquivo = float(input('Qual o tamanho deste arquivo? '))
velocidade_net = float(input('Qual a velocidade da internet em (Mbps)'))
tempo = (arquivo) - (velocidade_net)

if tempo <= 0:
  tempo = 1 

tempo = (tempo)/60
print(f'O tamanho do arquivo em MB: {arquivo} \nA velocidade da internet para download é: {velocidade_net}')

#Faça um Programa que peça dois números e imprima o maior deles.

def soma():
  numero1 = int(input('Digite um número: '))
  numero2 = int(input('Digite um número: '))

  if numero1 >= numero2:
    numero1 = numero1 
    print(numero1)
  elif numero2 >= numero1:
    numero2 = numero2
    print(numero2)
soma()

#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

def positivo(valor_um): 
  if valor_um > 0:
    valor_um = 'positivo'
    print(f'O seu número é:{valor_um} ')
  else:
    valor_um = 'negativo'
    print(f'O seu número é: {valor_um}')
positivo(int(input('Digite um número: ')))

#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

def sexualidade():
  sexo = input('Digite uma letra: ')
 

  if sexo == 'M':
    sexo = 'Masculino'
    print('Masculino')
  
  elif sexo == 'F':
    sexo = 'Feminino'
    print('Feminino')

  
  else:
    print('sexo inválido')

sexualidade()

#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

def abc(letra):
  vogal = ['a','e','i','o','u']
  consoante = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
  numero = ['0','1','2','3','4','5','6','7','8','9']
  if letra in vogal:
    print('vogal')

  elif letra in consoante:
    print('consoante')

  elif letra in numero:
    print('numero')

  else:
    print('caracteres não aceitos')

exibir = input('Digite uma opção: ')
abc(exibir)

#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez

def media():
  nota1 = float(input('Digite a primeira nota: '))
  nota2 = float(input('Digite a segunda nota: '))
  media = (nota1 + nota2)/2
  print(media)
  if media >= 7:
    print('Você foi aprovado! Parabéns!' )

  elif media < 7:
    print('Você foi reprovado... isso é uma pena! ')

  elif media == 10:
    print('Orgulho da instituição! Parabéns!!!')

media()

#Faça um Programa que leia três números e mostre o maior deles.

def numeros():
  num1 = int(input('Digite um número: '))
  num2 = int(input('Digite um número: '))
  num3 = int(input('Digite um número: '))

  if num1 > num2 and num1 > num3:
    num1 = num1
    print(num1)
  elif num2 > num1 and num2 > num3:
    num2 = num2
    print(num2)
  elif num3 > num1 and num3 > num2:
    num3 = num3
    print(num3)

numeros()

#Faça um Programa que leia três números e mostre o menor deles.

def numeros():
  num1 = int(input('Digite um número: '))
  num2 = int(input('Digite um número: '))
  num3 = int(input('Digite um número: '))

  if num1 < num2 and num1 < num3:
    num1 = num1
    print(num1)
  elif num2 < num1 and num2 < num3:
    num2 = num2
    print(num2)
  elif num3 < num1 and num3 < num2:
    num3 = num3
    print(num3)

  if num1 > num2 and num1 > num3:
    num1 = num1
    print(num1)
  elif num2 > num1 and num2 > num3:
    num2 = num2
    print(num2)
  elif num3 > num1 and num3 > num2:
    num3 = num3
    print(num3)

numeros()

#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

def mercado():
  produto1 = input('Diga o nome do produto: ')
  preco1 = float(input('Qual o valor do produto? '))
  produto2 = input('Diga o nome do produto: ')
  preco2 = float(input('Qual o valor do produto? '))
  produto3 = input('Diga o nome do produto: ')
  preco3 = float(input('Qual o valor do produto? '))

  if preco1 < preco2 and preco1 < preco3:
    preco1 = preco1
    print('Levar o produto 1 ')

  elif preco2 < preco1 and preco2 < preco3:
    preco2 = preco2
    print('Levar o produto 2 ')

  elif preco3 < preco1 and preco3 < preco2:
    preco3 = preco3
    print('Levar o produto 3 ')

mercado()

#Faça um Programa que leia três números e mostre-os em ordem decrescente.

lista = []
for x in range(3):
  lista.append(int(input("numero: ")))
lista.sort()
lista.reverse()
for l in lista:
  print(l)

#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

def horario():
  turno = input('Digite em qual turno você estuda: ')

  if turno == 'm':
    print('Matutino')
    print(f'Bom dia! ')

  elif turno == 'v':
    print('Vespertino')
    print(f'Boa tarde! ')

  elif turno == 'n':
    print('Noturno')
    print(f'Boa noite! ')

horario()

#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.


def folha_pagamento():
  assalariados = float(input('Diga o valor do seu salário: ')) 
  salario = assalariados

  if assalariados <= 280:
    assalariados = (assalariados) *(20/100)
    print(f'O aumento do salário foi de: {assalariados}')
    
  elif assalariados > 280 <= 700:
    assalariados = (assalariados) * (15/100)
    print(f'O aumento do salário foi de: {assalariados}') 

  elif assalariados <= 700 <= 1500:
    assalariados = (assalariados) * (10/100)
    print(f'O aumento do salário foi de: {assalariados}') 
    
  elif assalariados >= 1500:
    assalariados = (assalariados) * (5/100)
    print(f'O aumento do salário foi de: {assalariados}')
  
  salario = (salario + assalariados)
  print(f'O seu novo salário será: {salario} ')

folha_pagamento()

#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.


def tributos():
  horas_trabalhadas = int(input('Diga a quantidade de horas trabalhadas: '))
  salario = float(input('Diga o valor do seu salário: '))
  salario_bruto = (horas_trabalhadas * salario)
  descontos = salario_bruto
                
  if salario_bruto <= 900:
    print('isento')

  elif salario_bruto >900 and salario_bruto <= 1500:
    salario_bruto = (salario_bruto) *(5/100)
    print(salario_bruto)
    
  elif salario_bruto >= 1500 and salario_bruto <= 2500:
    salario_bruto = (salario_bruto) *(10/100)
    print(salario_bruto)

  elif salario_bruto >= 2500:
    salario_bruto = (salario_bruto) *(20/100)
    print(salario_bruto)

    descontos = (descontos - salario_bruto)

tributos()

#Faça um Programa que peça dois números e imprima o maior deles.

def numeral():
  num1 = int(input('Digite um número: '))
  num2 = int(input('Digite um número: '))

  if num1 > num2:
    num1 = num1
    print(f'Este é o maior número da operação: {num1}')

  elif num2 > num1:
    num = num2
    print(f'Este é o maior número da operação: {num1}')

numeral()

#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

def valor():

  numero = int(input('Digite um número: '))

  if numero >= 0:
    numero = 'Positivo'
    print(f'O numero é: {numero}')
  elif numero <= 0:
    numero = 'Negativo'
    print(f'O seu número é: {numero}')

valor()

#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

def sexualidade():
  sexo = input('Digite uma letra: ')
 

  if sexo == 'M':
    sexo = 'Masculino'
    print('Masculino')
  
  elif sexo == 'F':
    sexo = 'Feminino'
    print('Feminino')

  
  else:
    print('sexo inválido')

sexualidade()

num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))

soma = (num1 + num2)
subtracao = (num1 - num2)
multiplicacao = (num1 * num2)
divisao = (num1/num2)
potencia = (num1**num2)

print(soma)
print(subtracao)
print(multiplicacao)
print(divisao)
print(potencia)

def folha_pagamento(salario):
  aumento = 0
  

  if salario <= 280:
    aumento = salario *(20/100)
    
  elif aumento > 280 <= 700:
    aumento= salario * (15/100)

  elif aumento <= 700 <= 1500:
    aumento = salario * (10/100)
    
  elif aumento >= 1500:
    aumento = salario * (5/100)
    
  
  return  salario + aumento
  

x = float(input('Digite o salário: '))
s = folha_pagamento(x)
print(f'O seu novo salário ficou em: {s} ')

print(input('Digite o número da sua conta: '))
# Modelagem alternativa usando listas
banco_lista = [
               ['001', 0],
               ['002', 100],
               ]

# Conta existe (Retorna True/False)
def conta_existe(conta):
  pass

print('Olá, você acaba de acessar a página inicial do seu banco.')
print(input('Aqui você pode teclar (0) Para iniciar uma nova conta (1) Para depositar um valor a uma conta já existente (2) Para sacar um valor da sua conta (3) Para transferir '))

# Listar contas
def listar_contas():
  pass

# Abrir conta (Retorna True/False)
def abrir_conta(conta, saldo=0):
  pass

# Depositar (Retorna True/False)
def depositar(conta, valor):
  pass
  
# Sacar (Retorna True/False)
def sacar(conta, valor):
  pass

# Transferir (Retorna True/False)
def transferir(conta_origem, conta_destino, valor):
  pass


op = 1
while op != 0:
  print('Ler/processa dados...')
  op = 0

print('Fim.')

agenda = {}
 
def main():
  
  menu = ()
  print(40*'=')
  
  print('O que deseja fazer? ')
  print('Digite 1 para adicionar um contato ')
  print('Digite 2 para editar o contato : ')
  print('Digite 3 para para excluir o contato : ')
  print('Digite 4 para ver o contato : ')
  escolha = input('Digite a opção: ')
  
  if escolha == '1':
    nome = input('Digite o nome do contato: ')
    numero = input('Digite o número do contato: ')

  elif escolha == '2':
    edit = input('Qual contanto gostaria de editar? ')
    x = nome
    print(x)
   
  elif escolha == '3':
    delete = input('Qual contanto quer excluir? ')

main()

agenda = {}

def menu():
  print(60*'#')
  print("Olá, bem vindo a agenda!")
  print("Se você deseja adicionar um contato digite 1")
  print("Se você deseja editar um contato digite 2")
  print("Se você deseja excluir um contato digite 3")
  print("se você deseja ver toda a sua agenda digite 4")
  print("se você deseja ver algum contato específico digite 5")
  print(60*'#')

def add():
  nome = input("Qual é o nome do contato? ")
  telefone = input("Qual é o telefone do contato? ")
  agenda[nome] = telefone
  return agenda

def remove():
  nome = input("Qual é o nome do contato? ")
  if nome in agenda.keys():
    del agenda[nome]
    return agenda
  else:
    print("Nome não encontrado.")
    return None

def look():
  for cont in agenda:
    print(cont)

def edit():
  nome = input("Qual é o nome do contato? ")
  if nome in agenda.keys():
    telefone = input("Qual é o telefone do contato? ")
    agenda[nome] = telefone
    return agenda
  else:
    print("Nome não encontrado.")
    return None

def see():
  nome = input("Qual é o nome do contato? ")
  if nome in agenda.keys():
    for cont in agenda.items():
      if nome == cont[nome]:
        print(cont)
  else:
    print("Não encontrado")

def opcoes(x):
  if x == '1':
    add()
  elif x == '2':
    edit()
  elif x == '3':
    remove()
  elif x == '4':
    look()
  elif x == '5':
    see()

def start():
  while True:
    menu()
    x = input("\nQual ação deseja executar? ") 
    if x in '1234':
      opcoes(x)
    elif x == 'Sair':
      return agenda
      break
    else:
      print("Opção inválida.")
      
start()

import json
import re
class Contas:
  def __init__(self):
    self.nomes = {}
    self.cpfs = {}
    self.macs = {}
    self.cods = []
    self.ativado = {}

  def gerarCOD(self, nome):
    from random import randint
    
    tam = len(nome)
    cod = randint(0, tam * tam)
    if(cod not in self.cods):
      self.cods.append(cod)
      return cod
    else:
      while(cod not in self.cods):
        cod = cod + 1
      return cod

  def MACs(self, mac):
    formato = ['a','b','c','d','e','f','0','1','2','3','4','5','6','7','8','9']
    #x = input('Digite seu Mac: ')
    if(len(mac) != 12):
      print('tamanho inválido')
      return False
    elif(not(all(mac for c in formato))):
      print('Formato inválido!')
      return False
    elif(mac in self.macs):
      print('Já possuimos esse cadastro!')
      return False
    else:
      print('MAC válido!')
      return True 

  def CPFs(self, cpf):
    formato = ['0','1','2','3','4','5','6','7','8','9']
    #x = input('Digite seu cpf: ')
    if(len(cpf) != 11):
      print('tamanho inválido')
      return False
    elif(not(all(cpf for c in formato))):
      print('Formato inválido!')
      return False
    elif(cpf in self.cpfs):
      print('Já possuimos esse cadastro!')
      return False
    else:
      print('cpf válido!')
      return True

  def inserir(self):
    mac = input("Digite seu mac.").lower()
    if(self.MACs(mac) == False):
      print("Error ao cadastrar.")
    else:
      nome = input("Digite o seu nome.")
      cod = self.gerarCOD(nome)
      cpf = input("Digite seu cpf.").lower()
      if(self.CPFs(cpf) == False):
        print("Error ao cadastrar CPF.")
      else:
        self.macs.setdefault(cod, mac)
        self.cpfs.setdefault(cod, cpf)
        self.nomes.setdefault(cod, nome)
        ativar = input("Ativar conta?").lower()
        if(ativar == "sim"):
          self.ativado.setdefault(cod, True)
        else:
          self.ativado.setdefault(cod, False)
        print("Cadastro realizado.")
        print("Cod de ID  = ", cod)
  
  def listar(self):
    print(self.nomes)
    print(self.cpfs)
    print(self.macs)
    print(self.ativado)
  
  def temCadastro(self):
    cod = int(input("Digite o cod de ID."))
    if(cod not in self.cods):
      print("Cod errado.")
    else:
      mac = input("Digite o mac para consulta.").lower()
      if(mac not in self.macs):
        print("Mac inexistente.")
      else:
        print("O mac ", mac, " possui cadastro.")
  
  def Excluir(self):
    cod = int(input("Digite o cod para excluir a conta."))
    if(cod not in self.cods):
      print("Cod de ID errado.")
    else:
      if(self.ativado.get(cod) == False):
        self.cods.remove(cod)
        self.macs.pop(cod)
        self.nomes.pop(cod)
        self.cpfs.pop(cod)
        self.ativado.pop(cod)
      else:
        print("Desative a conta")
  
  def Mudar(self):
    cod = int(input("Digite o cod para ativar/desativar a conta."))
    if(cod not in self.cods):
      print("Cod de ID errado.")
    else:
      if(self.ativado.get(cod) == False):
        self.ativado[cod] = True
        print("Ativado.")
      else:
        self.ativado[cod] = False
        print("Desativado.")

  def Atualizar(self):
    cod = int(input("Digite o cod."))
    if(cod not in self.cods):
      print("Código inexistente")
    else:
      mac = input("Digite o novo mac")
      if(self.MACs(mac) == False):
        print("Error ao verificar MAC")
      else:
        self.macs[cod] = mac
  def Exportar(self):

    arq = open('exportados.txt', 'w')
    form = str(self.nomes) +"\n"+ str(self.cpfs) +"\n" + str(self.macs)+"\n" + str(self.cods) + "\n" + str(self.ativado)
    arq.write(form)
    arq.close
  
  def Importar(self):
    arq = open('importar.txt', 'r')
    lista = arq.read()
    lista.split()
    print(lista)
    self.nomes = lista[0]
    self.cpfs = lista[1]
    self.macs = lista[2]
    self.cods = lista[3]
    self.ativado = lista[4]

# Commented out IPython magic to ensure Python compatibility.


from google.colab import drive
drive.mount('/gdrive') 
# %cd /gdrive/MyDrive 

try:
  meu_arquivo = open('file_demo.txt', 'r') # r=read, w=write
  conteudo = meu_arquivo.read()
  #meu_arquivo.write('\nNovo conteúdo')
  #meu_arquivo.save()
  print(conteudo)
except FileNotFoundError as ex:
  print('Erro ao abrir o arquivo.', ex)
finally:
  print('Fechando arquivo...')
  meu_arquivo.close()

try:
  with open('file_demo.txt', "r") as meu_arquivo: # r=read, w=write
    for linha in meu_arquivo:
      print(linha, end='')
except FileNotFoundError as ex:
  print('Erro ao abrir o arquivo.', ex)
except Exception as ex:
  print('Falha na leitura do arquivo', ex)

dias = []
http_met = []
http_cod = []
sos = []
ips = []

def ler_linhas(nome):
 
    with open(nome, 'r') as arquivo:
      for linha in arquivo:
        separar_dados(linha)

    print("Arquivo não encontrado")

def forma_http(linha):
  if 'GET' in linha:
    http_met.append('GET')
  elif 'POST' in linha:
    http_met.append('POST')
  elif 'PUT' in linha:
    http_met.append('PUT')
  elif 'DELETE' in linha:
    http_met.append('DELETE')

def forma_cod(linha):
  if '200' in linha:
    http_cod.append('200')
  elif '301' in linha:
    http_cod.append('301')

def forma_so(linha):
  if 'Windows' in linha:
    sos.append('Windows')
  elif 'Mac' in linha:
    sos.append('Mac')
  elif 'Linux' in linha:
    sos.append('Linux')

def get_infos(linha):
  dados = linha.split(' ')
  ips.append(dados[0])
  #print(dados[3])


def separar_dados(linha):
  forma_http(linha)
  forma_cod(linha)
  forma_so(linha)
  get_infos(linha)

ler_linhas('logs.txt')
print(f"Quantidade http: {len(http_met)}")
print(f"Quantidade cod: {len(http_cod)}")
print(f"Quantidade so: {len(sos)}")
print(f"Quantidade ips: {len(ips)}")
print(f"Quantidade horários: {len(dias)}")
#print(http_met)

agenda = {}

def menu():
  print(40*'#')
  print("Digite 1 para adcionar contato: ")
  print("Digite 2 para editar contato: ")
  print("Digite 3 para listar os contatos: ")
  print("Digite 4 para excluir contato: ")
  print(40*'#')
  x = int(input('Digite uma opção:'))
  return agenda

def add():
      x = input('Digite o nome do contato: ')
      y = input('Digite o número do contato: ')

def edit():
    x = input('Digite o nome do contato para editar: ')

while True:
  menu()
  add()
  edit()

#Faça um Programa que peça dois números e imprima o maior deles.

num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))

if num1 > num2:
  print(num1)
elif num2 > num1:
  print(num2)

#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

alone = int(input('Digite um número:'))

if alone >= 0:
  print('positivo')
elif alone <= 0:
  print('Negativo')

#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

unisex = input('Digite uma letra: ')

if unisex == 'm':
  print('Masculino')

elif unisex == 'f':
  print('Feminino')

else:
  print('Resultado não encontrado.')

#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letter = input('Digite uma letra:')

if letter == 'a' 'e' 'i' 'o' 'u':
  print('vogal')

else:
  print(f'A opção escolhida é uma: consoante ')

#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:

nota_um = float(input('Digite a sua nota no primeiro módulo: '))
nota_dois = float(input('Digite a sua nota no segundo módulo: '))
media = (nota_um + nota_dois) /(2)

if media == 10:
  print('Aprovado com maestria!')

elif media >= 7:
  print('Aprovado')

elif media < 7:
  print('Reprovado')

#Faça um Programa que leia três números e mostre o maior deles.

numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite um número: '))
numero3 = float(input('Digite um número: '))

if numero1 > numero2 and numero1 > numero3:
  print(f'O maior número foi: {numero1} ')

elif numero2 > numero1 and numero2 > numero3:
  print(f'O maior número foi : {numero2}')

elif numero3 > numero2 and numero3 > numero1:
  print(f'O maior número foi: {numero3}')

num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
num3 = int(input('Digite um número: '))

if num1 < num2 and num1 < num3:
    num1 = num1
    print(num1)
elif num2 < num1 and num2 < num3:
    num2 = num2
    print(num2)
elif num3 < num1 and num3 < num2:
    num3 = num3
    print(num3)

if num1 > num2 and num1 > num3:
    num1 = num1
    print(num1)
elif num2 > num1 and num2 > num3:
    num2 = num2
    print(num2)
elif num3 > num1 and num3 > num2:
    num3 = num3
    print(num3)

#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

def mercado():
  mercadoria = float(input('Digite o valor do produto: '))
  mercadoriaTwo = float(input('Digite o valor do produto: '))
  mercadoriaThree = float(input('Digite o valor do produto: '))

  if mercadoria < mercadoriaTwo and mercadoria < mercadoriaThree:
    print(f'O produto com o menor preço é: {mercadoria} ')
  
  if mercadoriaTwo < mercadoria and mercadoriaTwo < mercadoriaThree:
    print(f'O produto com o menor preço é: {mercadoriaTwo}')

  if mercadoriaThree < mercadoria and mercadoriaThree < mercadoriaTwo:
    print(f'O produto com o menor preço é: {mercadoriaThree}')

mercado()

#Faça um Programa que leia três números e mostre-os em ordem decrescente.

def numeral():
  primeiro = int(input('Primeiro numero: '))
  segundo  = int(input('Segundo numero : '))  
  terceiro = int(input('Terceiro numero: '))

  print(primeiro,'-',segundo,'-',terceiro)

  if (terceiro > segundo):
      aux = terceiro
      terceiro = segundo
      segundo = aux

  if (segundo > primeiro):
      aux = segundo
      segundo = primeiro
      primeiro = aux

  if (terceiro > segundo):
      aux = terceiro
      terceiro = segundo
      segundo = aux

numeral()

#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

def horarios():
  turno = input('Digite uma letra: ')

  if turno == 'm':
    print('Matutino\nBom dia!')

  elif turno == 'v':
    print('Vespertino\nBoa tarde!')

  elif turno == 'n':
    print('Noturno\nBoa noite!')

  else:
    print('Opção inválida! ')

horarios()

#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.


def reajuste():
  colaborador = float(input('Digite o valor do seu sálario: '))

  if colaborador <= 280:
    colaborador = colaborador *(20/100) + colaborador
    novo_salario = (colaborador) + (colaborador)
    print(f'O seu novo sálario é: {colaborador}')

  elif colaborador > 280 and colaborador <= 700:
    colaborador = colaborador *(15/100) + colaborador
    novo_salario = (colaborador) + (colaborador)
    print(f'O seu novo sálario é: {colaborador}')

  elif colaborador > 700 and colaborador <= 1500:
    colaborador = colaborador *(10/100) + colaborador
    novo_salario = (colaborador) + (colaborador)
    print(f'O seu novo sálario é: {colaborador}')

  elif colaborador >= 1500:
    colaborador = colaborador *(5/100) + colaborador
    novo_salario = (colaborador) + (colaborador)
    print(f'O seu novo sálario é: {colaborador}')

reajuste()

#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#Salário Bruto: (5 * 220)        : R$ 1100,00
#(-) IR (5%)                     : R$   55,00  
#(-) INSS ( 10%)                 : R$  110,00
#FGTS (11%)                      : R$  121,00
#Total de descontos              : R$  165,00
#Salário Liquido                 : R$  935,00


def folha_de_pagamento():
  salario_bruto = float(input('Digite o valor do seu sálario: '))
  salario = salario_bruto

  if salario <= 900:
    print('Insento!')

  elif salario_bruto > 900 and salario_bruto <= 1500:
    salario = salario_bruto - salario_bruto *(5/100)
    print('Devido aos 5% do IR')

  elif salario_bruto > 1500 and salario_bruto <= 2500:
    salario = salario_bruto - salario_bruto *(10/100)
    print('Devido aos 10% de desconto do INSS')

  elif salario_bruto >= 2500:
    salario = salario_bruto - salario_bruto *(20/100)
    print('Devido aos 11% do FGTS')
  
  salario = salario - salario_bruto *(5/100)
  salario = salario - salario_bruto *(10/100)
  salario = salario - salario_bruto *(11/100)
  print(salario)


  
folha_de_pagamento()