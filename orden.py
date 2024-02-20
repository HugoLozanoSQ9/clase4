fruits = ["banana","apple",  "cherry"] 

fruits.sort()
##sort va a ordenar la lista en orden alfa numerico dependiendo del valor que tengan las posiciones
#Primero los númeos, despúes los caracteres que representen números  del > al < y al final de la A a la Z pero no a ambos
print(fruits)

fruits.sort()
#En esta situación hace lo mismo pero al revés (esta vez primero de la Z a la A, caracteres que representen numeros del mayor al menor)
#y por ultimo números de igual forma del mayor al menor

##Si se tienen elementos con mayuscula entonces va a dar prioridad y ordenará esos primero y los que no traen mayuscula después
#Se puede cambiar esto con una función dado que sort se le puede incluir una key "sort(key=)

#En donde key es una función 

def get_lower_case(value:str) -> str:
    """Returns a lower case on the value

    Args:
        value (str): Value on list 

    Returns:
        str: Value on lower case
    """
    #Esto ayuda a validar que sean realmente strings
    if isinstance(value,str):
        return value.lower() 

    return value

fruits.sort(key = get_lower_case, reverse = True) # y se puede combinar con reverse solo agregando una , 
# se puede hacer lo mismo pero sin la función get_lower_case
fruits.sort(key = str.lower, reverse = True)
print(fruits.sort(key = str.lower, reverse = True))




