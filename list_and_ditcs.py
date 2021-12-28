def run():
    my_list = [1,"hello",True,4.5]
    my_dict = {"Firstname": "Jeronimo", "lastname": "Bedoya"}

    super_list = [
        {"Firstname": "Jeronimo", "lastname": "Bedoya"},
        {"Firstname": "Miguel", "lastname": "Torres"},
        {"Firstname": "Pepe", "lastname": "Rodelo"},
        {"Firstname": "Susana", "lastname": "Martinez"},
        {"Firstname": "Facundo", "lastname": "Garcia"}
    ]

    super_dict = {
        "natural_nums": [1,2,3,4],
        "integer_nums":[-1,-2,0,1,2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)
    
    for items in super_list:
        print(items)

if __name__ == '__main__':
    run()