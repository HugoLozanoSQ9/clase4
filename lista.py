# Para acceder al valor de los elementoes, es posible hacerlo por su número de índice entre corchetes

fruits = ["apple", "banana", "orage", "kiwi", "melon", "mango", "cherry"] 
# se pueden hacer busquedas negativas para saber los ultimos elementos en las listas
print(fruits[-1])  # cherry

print(fruits[0])  # apple

# Se maneja por rango de indices pero el ultimo ya no lo muestra (se llama slices)
print(fruits[2:5]) #orange, kiwi, melon  pero no muestr mango pq el 5 se excluye  también se pueden mezclar con numeros negativos

#si nos pasamos por ejemplo:
print(fruits[-4:8]) #Va a mostrar hasta los ultimos elementos de la lista

print(fruits[2:])#Con esto estamos haciendo que comience en indice 2 pero acabe en el ultimo elemento de la lista

print(fruits[:5])#Con esto comienza en el indice 0 y se sigue hasta el indice 5

print(fruits[-5:])#tambien se puede hacer con números negativos 

#También existen los steps que se ejecutan con ::  (x2 de 2 puntos)

print(fruits[::2]) #Salta los elementos en 2 esto imprimirá (apple, orange, melon, cherry)
print(fruits[::3])#Salta los elementos de 3 en 3 comenzando en el indice 0 (apple,kiwi,cherry)

#Para delimitar totalmente entonces sería: 

print(fruits[1:5:2]) #se imprime del indice 1 al indice 4 (el 5 es excluyente) y que lo haga de 2 en 2 (banana),(kiwi)

