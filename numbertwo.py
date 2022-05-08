
'''def preencherLista1(tamanho):
   vetor = [""] * tamanho
   for i in range(tamanho):
    vetor[i] = int(input("digite um valor: "))
    return vetor

 def preencherLista2(tamanho):
    vetor = [""] * tamanho
    for i in range(tamanho):
     vetor[i] = int(input("digite um valor: "))
     return vetor

 def unirListas(vetor1, vetor2):
    return vetor1 + vetor2

 def removeRepetidos(vetor):
   lista = []
   for i in vetor:
     if i not in lista:
         lista.append(i)
   lista.sort()
   return lista

tamanhoVetor1 = int(input("informe o tamanho do vetor 1."))
tamanhoVetor2 = int(input("informe o tamanho do vetor 2."))

print("vetor 1:")
vetor1 = preencherLista1(tamanhoVetor1)
print("vetor 2:")
vetor2 = preencherLista2(tamanhoVetor2)

vetor3 = unirListas(vetor1, vetor2)
vetorunido = removeRepetidos(vetor3)
print(vetorunido)'''