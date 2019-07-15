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
© geekbrains.ru 16
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
# os.path.abspath(__file__)
path_to_data = os.getcwd() + '\\data_2'
for i in range(1, len(next(os.walk(path_to_data))[2]) + 1):
    # docs recommend use of newline='' for csv files
    with open(path_to_data + '\\info_' + str(i) + '.txt', newline='') as csvfile:
        content = csv.reader(csvfile)
        for row in content:
            print(row)
