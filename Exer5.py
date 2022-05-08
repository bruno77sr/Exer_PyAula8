#5- Temos um grupo de pessoas. Escreva um programa em Python que leia o sexo e a 
#altura de cada pessoa, calcule e mostre a altura média das mulheres e dos homens 
#separadamente. Utilize o comando de repetição que desejar

somaF = 0
somaM = 0
masc = 0
fem = 0
op ="s"
while op == "s":
    sexo = input("    Digite seu sexo: \n(H para homem) - (F para Mulher): ")
    altura = float(input("Digite sua altura: "))

    if sexo == "h":
        masc += 1
        somaM += altura
    elif sexo == "f":
        fem += 1
        somaF += altura

    op = input("Quer continuar ? s = sim - n = não : ")
calcM = somaM / masc
calcF = somaF / fem
print("A altura média dos homens é: %.2f" %(calcM), "\nA altura média das mulheres é: %.2f "%(calcF) )
