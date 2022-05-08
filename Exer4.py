#4- Escreva um algoritmo que leia um grupo de valores reais e determine quantos valores 
#são positivos e quantos são negativos. Determine, também, qual é o menor desses 
#valores. Utilize o comando de repetição que desejar.
from asyncio.windows_events import NULL


neg = 0
posi = 0
varNeg = 0

op = "s"
while op == "s" or op == "S":
    a = float(input("Digite um valor: "))
    if a < 0:
        neg += 1
        if a < varNeg:
            varNeg = a
    elif a > 0:
        posi += 1
        varPos = a
    op = input("Quer continuar ? \n((s)sim ou (n)não):  ")

print("A quantidade de negativos é: ", neg, "\nA Quantidade de positivo é: ", posi, "\nO menor valor é: ", varNeg)
    