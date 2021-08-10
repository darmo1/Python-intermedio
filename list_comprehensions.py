def run():
    squares = []
    for i in range(1,101):
        squares.append(i**2)
    
    #print(squares)

    #Ahora vamos a aplicar list_comprehension
    #Estructura
    # [ element for element in iterable if condition ]
    '''
    Ahora descomposiendo seria

    1. element representa a cada uno de los elementos a poner en la lista nueva
    2. for element in iterable -> ciclo a partir del cual se extraerán elementos de otra lista o cualquier iterable
    3. if condition: condicion opcional para filtrar los elementos del ciclo

    Se lee 2 -1- 3 
    es decir:
    Para cada elemento en el iterable (3) voy a guardar el element (1) solo si se cumple (2)
    '''

    multiple_list = [ i for i in range(1, 9999) if i % 4 == 0 and i% 6 == 0 and i% 9 == 0 ]
    print(multiple_list)







if __name__ == '__main__':
    run()