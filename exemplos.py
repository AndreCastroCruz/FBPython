import os
os.system("cls")

#listas

lista = []
letras = list("EPAMINONDAS")
numeros = list(range(10))
print(lista)
print(letras)
print(numeros)

print("Ultimo caracter da lista numeros ",numeros[-1])
listanova = letras + numeros
print(listanova)
print("Tamanho da lista nova é ",len(listanova))
listanova.pop()
print(listanova)
print("Tamanho da lista nova é ",len(listanova))
del listanova[10]
print(listanova)
print("Tamanho da lista nova é ",len(listanova))
listanova.append("EXEMPLO NA LISTA") #o comando APPEND coloca o novo item na ultima posição
print(listanova)
print("Tamanho da lista nova é ",len(listanova)) 
listanova.insert(10, "s") #o comando INSERT serve para acrescentar um item na posicao que determinou
print(listanova)
print("Tamanho da lista nova é ",len(listanova))
listanova[10] = "S" #forma para apenas alterar o valor que está nessa posição na lista
print(listanova)
print("Tamanho da lista nova é ",len(listanova))



for indice, item in enumerate(listanova):
    print(indice, item)