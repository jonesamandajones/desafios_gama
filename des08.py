import sys


lista = list(sys.argv)
lista.pop(0)
def lista_inteiros(lista):
    lista_int = []
    for i in lista:
        lista_int.append(int(i))
    return lista_int

lista_int = lista_inteiros(lista)
lista_int.sort(key=int, reverse=True)
print(lista_int)