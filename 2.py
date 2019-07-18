"""
1. Задание на закрепление знаний по модулю CSV . Написать скрипт, осуществляющий выборку
определенных данных из файлов info_1.txt , info_2.txt , info_3.txt и формирующий новый
«отчетный» файл в формате CSV . Для этого:
a. Создать функцию get_data() , в которой в цикле осуществляется перебор файлов с
данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения
каждого параметра поместить в соответствующий список. Должно получиться четыре
списка — например, os_prod_list , os_name_list , os_code_list , os_type_list . В этой же
функции создать главный список для хранения данных отчета — например, main_data
— и поместить в него названия столбцов отчета в виде списка: «Изготовитель
системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data (также для
каждого файла);
b. Создать функцию write_to_csv() , в которую передавать ссылку на CSV-файл. В этой
функции реализовать получение данных через вызов функции get_data() , а также
сохранение подготовленных данных в соответствующий CSV-файл;
c. Проверить работу программы через вызов функции write_to_csv() .
"""

# 1

import csv
import os
import sys

# print(sys.getdefaultencoding())
# os.walk(path)
# <generator object walk at 0x7f5e5acbd4b0>
# os.walk(path).next()
# This will return:
#    [0] -> The path you passed
#    [1] -> list of All the first level directories in your path
#    [2] -> list of All the first level files
# len(next(os.walk(path)[2])) - number of files in dir
# OR len(os.listdir(path)) - 2
# subtract 2 becase dirs (., ..) are also counted
# os.getcwd() = os.path.abspath(__file__)
def get_data():
    path_to_data = os.getcwd() + '\\data_2'
    # cycle through all the files in subdir
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы'],
                os_prod_list,
                os_name_list,
                os_code_list,
                os_type_list
                ]
    files_in_subdir = len(next(os.walk(path_to_data))[2])
    for i in range(1, files_in_subdir + 1):

        with open(path_to_data + '\\info_' + str(i) + '.txt', 'rb') as tempfile:
            # We need to decode Russian files in non-Russian OS
            temp_content = tempfile.read().decode('cp1251').encode('utf-8')
            # We resave files in temp utf-8 files because __next__ method
            # is gone in str variable after decoding. When we iterate over a str
            # we receive individual letters and not lines, which are needed
            # in csv.reader method below
            f = open(path_to_data + '\\tempfile' + str(i) + '.txt', 'wb')
            f.write(temp_content)
            f.close()
            # manual recommends use of newline='' for csv files
            # utf-8 is the default encoding in python
            with open(path_to_data + '\\tempfile' + str(i) + '.txt', newline='', encoding='utf-8') as csvfile:
                content = csv.reader(csvfile, delimiter=':')
                for row in content:
                    if row[0] == 'Изготовитель системы':
                        os_prod_list.append(row[1].lstrip())
                    if row[0] == 'Название ОС':
                        os_name_list.append(row[1].lstrip())
                    if row[0] == 'Код продукта':
                        os_code_list.append(row[1].lstrip())
                    if row[0] == 'Тип системы':
                        os_type_list.append(row[1].lstrip())
            # remove temp files
            os.remove(path_to_data + '\\tempfile' + str(i) + '.txt')
    return main_data

def write_to_csv(out_file='csv_out.txt'):
    data = get_data()
    with open(out_file, 'w', newline='', encoding='utf-8') as fn:
         fn_writer = csv.writer(fn, quoting=csv.QUOTE_NONNUMERIC)
         fn_writer.writerows(data)

"""
2. Задание на закрепление знаний по модулю json . Есть файл orders в формате JSON с
информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными. Для
этого:
a. Создать функцию write_order_to_json() , в которую передается 5 параметров — товар
( item ), количество ( quantity ), цена ( price ), покупатель ( buyer ), дата ( date ). Функция
должна предусматривать запись данных в виде словаря в файл orders.json . При
записи данных указать величину отступа в 4 пробельных символа;
b. Проверить работу программы через вызов функции write_order_to_json() с передачей
в нее значений каждого параметра.
"""
import json
import random
import datetime
def write_order_to_json(item, quantity, price, buyer, date):
    order_record = {'item': item,
    'quantity': quantity,
    'price': price,
    'buyer': buyer,
    'date': date
    }
    with open('orders.json', 'w') as fn:
        json.dump(order_record, fn, sort_keys=True, indent=4)


"""
3. Задание на закрепление знаний по модулю yaml . Написать скрипт, автоматизирующий
сохранение данных в файле YAML-формата. Для этого:
a. Подготовить данные для записи в виде словаря, в котором первому ключу
соответствует список, второму — целое число, третьему — вложенный словарь, где
значение каждого ключа — это целое число с юникод-символом, отсутствующим в
кодировке ASCII (например, €);
b. Реализовать сохранение данных в файл формата YAML — например, в файл
file.yaml . При этом обеспечить стилизацию файла с помощью параметра
default_flow_style , а также установить возможность работы с юникодом:
allow_unicode = True ;
c. Реализовать считывание данных из созданного файла и проверить, совпадают ли они
с исходными
"""
import yaml


def save_yaml(data):

    with open('file.yaml', 'w', encoding='utf-8') as fn:
        yaml.dump(data, fn, default_flow_style=False, allow_unicode=True)

def read_yaml():
    with open('file.yaml', encoding='utf-8') as fn:
        # original yaml.load() method is not safe!
        return yaml.full_load(fn)

if __name__ == '__main__':
    print('Homework 1')
    write_to_csv('csv_out_file.txt')

    print('Homework 2')
    r = random.randint(1, 1000)
    write_order_to_json('item'+str(r), r, 1000-r, 'buyer'+str(r), str(datetime.datetime.now()))

    print('Homework 3')
    dict_to_yaml = {'uno': ['one', 2, 'three', 2.0],
                    'dos': 100500,
                    'tres': {'1€': 'euro', '2₤': 'pound', '3₽': 'ruble'}
                    }
    save_yaml(dict_to_yaml)
    print('Original dict:')
    print(dict_to_yaml)
    print('Restored from yaml')
    print(read_yaml())
