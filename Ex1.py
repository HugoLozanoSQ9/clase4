def funcion(value: str)-> str:
    if isinstance(value,int) or isinstance(value,float):
        return str(value)
    elif isinstance(value,str):
        return str(value)

fruits = ["banana", "orage", "kiwi", "Melon",1,20, 8.7, "Cherry", 'mango', 'apple'] 

#fruits.sort(key=funcion)


#######################
#La mejor forma de hacerlo era:
def get_value(value) -> str:
    return str(value).lower()

fruits.sort(key=get_value)
print(fruits)
