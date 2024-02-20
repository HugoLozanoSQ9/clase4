x = ['apple','banana', 'cherry']

x[1] = 'watermelon'

print(x)
#['apple','watermelon', 'cherry']

#Si nosotros quisieramos cambiar multiples valores se puede hacer con un rango ¿:

fruits = ["apple", "banana", "orage", "kiwi", "melon", "mango", "cherry"] 

fruits[1:3] =['watermelon','lemon'] #recuerda que no llega al 3 (dado que el 3 lo ignora)

print(fruits)

#fruits = ["apple", "watermelon", "lemon", "kiwi", "melon", "mango", "cherry"] 
###### En caso de que el rango sea superior al elemento que vamos a sustituir por decir (1:4) = ['watermelon','lemon'] 
#Tendremos que el indice 3 se va a eliminar
#fruits = ["apple", "watermelon", "lemon", "melon", "mango", "cherry"]  así quedaría la lista
#en cambio si tenemos caso contrario (1:3) = ['watermelon','lemon','tangerine] se añade el elemento a un costado del indice 2
#fruits = ["apple", "watermelon", "lemon",'tangerine','kiwi', "melon", "mango", "cherry"]  así quedaría la lista
#Todos los elementos que se hagan de esta forma (posteriores al rango) simplemente los va a insertar

