def run():
    my_list = [1, 'Hello', True, 4.5]
    my_dict = {"first_name" : "Danilo" , "last_name" : "Morales"}


    super_list = [
        {"first_name" : "Danilo" , "last_name" : "Morales"},
        {"first_name" : "Santiago" , "last_name" : "Morales"},
        {"first_name" : "Mateo" , "last_name" : "Montoya"},
        {"first_name" : "Julian" , "last_name" : "Montoya"},
        {"first_name" : "Susana" , "last_name" : "García"}
    ]

    super_dict = {
        "natural_nums" : [1,2,3,4,5],
        "integer_nums": [-1,-2,0,1,2],
        "floating_nums" : [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, '-', value)



if __name__ == '__main__':
    run()
    print('entre')