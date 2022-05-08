#3- Faça um programa em Python que leia um valor n, inteiro e positivo, calcule e mostre 
#a seguinte soma:
#S = 1 + 1/2 + 1/3 + 1/4 +...+ 1/n



# processamento
tab = [1]
while True:
   n = int(input('Digite um numero inteiro: '))
   for a in range(5,n):
     s = 1+ (1/2) + (1/3) + (1/4) + (1/a)
     print("%.2f"%(s))

     p = input("Quer continuar ? (s) para sim (n) para não ? ")
     if p == "n":
       break 


#anunciado confuso '-'