#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    # Список самолетов.
    planes = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о самолете.
            destination = input("Пункт назначения: ")
            num = input("Номер рейса: ")
            typ = input("Тип самолета: ")

            # Создать словарь.
            plane = {
                'destination': destination,
                'num': num,
                'typ': typ,
            }

            # Добавить словарь в список.
            planes.append(plane)
            # Отсортировать список в случае необходимости.
            if len(planes) > 1:
                planes.sort(key=lambda item: item.get('destination', ''))

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 15
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                    "No",
                    "Пункт назначения",
                    "Номер рейса",
                    "Тип самолета"
                )
            )
            print(line)

            # Вывести данные о всех самолетах.
            for idx, plane in enumerate(planes, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>15} |'.format(
                        idx,
                        plane.get('destination', ''),
                        plane.get('num', 0),
                        plane.get('typ', '')
                    )
                )

            print(line)

        elif command.startswith('select '):

            # Разбить команду на части для выделения пункта назначения.
            part = command.split(' ', maxsplit=1)
            com = part[1]

            # Инициализировать счетчик.
            count = 0
            # Проверить сведения самолетов из списка.
            for plane in planes:
                if com == plane.get('typ', ''):
                    count += 1
                    print(
                        '{:>4}. Пункт: {}; Номер: {}'.format(count, plane.get('destination', ''),
                                                             plane.get('num', ''))
                    )

            # Если счетчик равен 0, то самолеты не найдены.
            if count == 0:
                print("Заданный тип не обнаружен.")

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить самолет;")
            print("list - вывести список самолетов;")
            print("select <тип> - запросить самолеты заданного типа;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)