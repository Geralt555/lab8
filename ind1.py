#!/usr/bin/env python3
# -*- config: utf-8 -*-

# Вариант 13. Использовать словарь, содержащий следующие ключи: фамилия, имя; номер телефона;
# дата рождения. Написать программу, выполняющую следующие
# действия: ввод с клавиатуры данных в список, состоящий из словарей заданной структуры;
# записи должны быть упорядочены по трем первым цифрам номера телефона; вывод на
# экран информации о человеке, чья фамилия введена с клавиатуры; если такого нет, выдать
# на дисплей соответствующее сообщение.


import sys

if __name__ == '__main__':
    # Список
    peoples = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break
        elif command == 'add':
            second_name = input("Фамилия ")
            name = input("Имя ")
            number = int(input("Номер телефона "))
            year = input("Дата рождения в формате: дд.мм.гггг ")

            if not number:
                print("Поле не заполнено")
                exit(1)

            people = {
                'second name': second_name,
                'name': name,
                'number': number,
                'year': year,
            }

            peoples.append(people)
            if len(peoples) > 1:
                peoples.sort(key=lambda item: item.get('number', '3'))

        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 20,
                '-' * 20,
                '-' * 20,
                '-' * 15
            )
            print(line)
            print(
                '| {:^4} | {:^20} | {:^20} | {:^20} | {:^15} |'.format(
                    "№",
                    "Фамилия ",
                    "Имя",
                    "Номер телефона",
                    "Дата рождения"
                )
            )
            print(line)

            for idx, people in enumerate(peoples, 1):
                print(
                    '| {:>4} | {:<20} | {:<20} | {:<20} | {:>15} |'.format(
                        idx,
                        people.get('surname', ''),
                        people.get('name', ''),
                        people.get('number', ''),
                        people.get('year', 0)
                    )
                )
            print(line)

        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=2)
            sur = (parts[1])

            count = 0
            for people in peoples:
                if people.get('second name') == sur:
                    count += 1
                    print('Фамилия:', people.get('second name', ''))
                    print('Имя:', people.get('name', ''))
                    print('Номер телефона:', people.get('number', ''))
                    print('Дата рождения:', people.get('year', ''))

            if count == 0:
                print("Таких фамилий нет !")

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить человека;")
            print("list - вывести список людей;")
            print("select <фамилия> - запросить информацию по фамилии;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print("Неизвестная команда {command}", file=sys.stderr)
