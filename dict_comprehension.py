from math import sqrt
def run():
    #my_dict = {}

    # for i in range(1,101):
    #     if i%3 != 0:
    #         my_dict[i] = i ** 3
    # print(my_dict)


    my_dict ={i:i**3 for i in range(1,101) if i % 3 != 0 }


    print(my_dict)


    #{ key: value for value in iterable if condition}

    #1- key:value -> Representa a cada una de las llaves y valores a poner en el nuevo diccionario
    #2- Ciclo a partir del cual se extraerá elementos de cualquie iterable
    #3- Condición opcional para filtrar los elementos del ciclo
    
    #Se lee asi --> 2-1-3
    #Para cada elemento yo guardaré una clave y ese valor si se cumple la siguiente condición

 
    #dictionary = {i: i**0.5 for i in range(1, 1001) }
    #print(dictionary)

    challenge = {i: sqrt(i**0.5) for i in range(1,1001) }
    print(challenge)

       






if __name__ == '__main__':
    run()