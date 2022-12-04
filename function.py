import csv

def insert(name, nickname, age, city, comics):
    with open('database.csv', 'at', newline='') as file_out:
        fieldnames = ['name', 'nickname', 'age', 'city', 'comics']
        writer = csv.DictWriter(file_out, fieldnames=fieldnames)
        writer.writerow({'name': name, 'nickname': nickname, 'age': age, 'city': city, 'comics': comics})

def remove(i):
    i += 1
    with open('database.csv', 'r') as file_in:
        lines = file_in.readlines()
        pointer = 1
        with open('database.csv', 'w') as file_out:
            for line in lines:
                if pointer != i:
                    file_out.write(line)
                pointer += 1
    return

def alternate(i, name, nickname, age, city, comics):
    remove(i)
    insert(name, nickname, age, city, comics)
    return