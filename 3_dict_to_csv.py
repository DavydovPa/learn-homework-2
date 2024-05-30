"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

import csv
def main():

    lines = ['name', 'age', 'job']

    peoples = [
        {'name': 'Victor', 'age': 34, 'job': 'Driver'},
        {'name': 'John', 'age': 29, 'job': 'Teacher'},
        {'name': 'Zack', 'age': 19, 'job': 'Student'},
        {'name': 'Pavel', 'age': 31, 'job': 'Brewman'},
        {'name': 'Anna', 'age': 30, 'job': 'Lawyer'},
        {'name': 'Julia', 'age': 44, 'job': 'chef'},
    ]

    with open('Users.csv', 'w', encoding='utf-8') as file_csv:
        writer = csv.DictWriter(file_csv, lines, delimiter=';')
        writer.writeheader()
        for people in peoples:
            writer.writerow(people)


if __name__ == "__main__":
    main()
