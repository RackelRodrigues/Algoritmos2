
n=int(input('Informe a ordem da matriz:'))

matriz=[]
for i in range(n):
  matriz.append([0] * n)

for i in range(n):
  for j in range(n):
    print('M[',i+1,',',j+1,']:',sep='',end='')
    matriz[i][j]=int(input())


for i in range(n):
  for j in range(n):
     print(matriz[i][j] ,end='')
    print()


  soma = 0
  for i in range(n):
    soma = soma + matriz[i][i]

    print('A soma dos elementos da diagonal principal é', soma)