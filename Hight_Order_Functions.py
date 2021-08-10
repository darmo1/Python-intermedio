# High Order Function

#Es una función que recibe en su parámetro a otra función. 
#Lo que en JS se llama callback

    # Filter, map and reduce

my_list = [1,2,4,5,6,9]

odd = list(filter(lamda x: x%2 !=0 , my_list))

#filter es una HOC y recibe dos parámetros, una es la expresion lambda
#Y la otra es la lista que es un iterable
#filter( función , iterable  ) esto retorna un iterador que es un objeto especial
#en python y poniendo list() como wrapper obtendremos nuestro resultado

ahora para map

list_map = [1,2,3,4,5]

map_result = list(map(lambda item : item**2 , list_map))
print(map_result)


Reduce

from functools import reduce

list_Reduce = [2,2,2,2,2]
# a--> primer elemento  b--> segundo elemento y luego se va iterando
all_multiplied = reduce(lambda a,b : a*b , list_Reduce)

print(all_multiplied)