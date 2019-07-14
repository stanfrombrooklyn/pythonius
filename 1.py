"""
Практическое задание
1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и
проверить тип и содержание соответствующих переменных. Затем с помощью
онлайн-конвертера преобразовать строковые представление в формат Unicode и также
проверить тип и содержимое переменных.
2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в
последовательность кодов (не используя методы encode и decode ) и определить тип,
содержимое и длину соответствующих переменных.
3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в
байтовом типе.
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из
строкового представления в байтовое и выполнить обратное преобразование (используя
методы encode и decode ).
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из
байтовового в строковый тип на кириллице.
6. Создать текстовый файл test_file.txt , заполнить его тремя строками: «сетевое
программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""

# 1
words = ['разработка', 'сокет', 'декоратор']

for i in words:
    print(type(i), i)
    print(type(i.encode('utf-8')), i.encode('utf-8'))

# 2
print('-' * 80)
words1 = [b'class', b'function', b'method']

for i in words1:
    print(type(i), i, len(i))

# 3
print('-' * 80)
words2 = ['attribute', 'класс', 'функция', 'type']
for i in words2:
    x = "b'" + i + "'"
    try:
        eval(x)
    except:
        print(f"{i} cannot be written in a b'...' form")

# 4
print('-' * 80)
words3 = ['разработка', 'администрирование', 'protocol', 'standard']
for i in words3:
    x = i.encode()
    print(x)

    y = x.decode()
    print(y)

# 5
print('-' * 80)
import requests
import os
import subprocess

response = requests.get('http://youtube.com')
print(response)

os.system('ping youtube.com')

sub = subprocess.Popen(['ping', 'yandex.ru'], stdout=subprocess.PIPE)
for line in sub.stdout:
    print(line.decode('cp866'))

# 6
print('-' * 80)

with open('test_file.txt', 'w', encoding='utf-8') as fn:
    fn.write('сетевое программирование')
    #fn.write('сокет')
    #fn.write('декоратор')
    fn.write('hellohello')

import chardet
with open('test_file.txt', 'rb') as fn:
    content = fn.read()
detect = chardet.detect(content)
print(detect)


with open('test_file.txt', encoding='utf-8') as fn:
    for line in fn:
        print(line)
