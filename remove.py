fruits = ["apple", "banana", "cherry"] 

fruits.remove('banana')

print(fruits) #Si existen más de un elemento con el mismo nombre se va a eliminar el que tiene el menor indice.

#['apple','cherry']

#####
#También se pueden eliminar elementos de un indice con el método pop()

fruits1 = ["apple", "banana", "cherry"] 
fruits1.pop(1)

print(fruits1)

#['apple','cherry']

##############
#El método index nos va a ayudar a saber el indice de un valor que queremos conocer.

print(fruits1.index('apple')) # va a devolver el indice numérico