#Sirve para adicionar una lista a otra
fruits = ["apple", "banana", "cherry"] 
tropical_friuts = ['mango', 'pineapple','papaya']

fruits.extend(tropical_friuts)

print(fruits)
#"apple", "banana", "cherry",'mango', 'pineapple','papaya'
#tambien se puede tener de la siguiente forma: 
all_fruits = fruits + tropical_friuts
#Se podría decir que es una combinación de ambas pero creando una nueva lista