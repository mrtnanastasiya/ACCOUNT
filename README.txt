Домашнее задание к лекции 1. «Import. Module. Package»

1. Разработана структура программы «Бухгалтерия»:
main.py;
application/salary.py;
application/db/people.py.
Main.py — основной модуль для запуска программы.
В модуле salary.py функция calculate_salary.
В модуле people.py функция get_employees.

2. Импортированы функции в модуль main.py и вызываны эти функции в конструкции.
if __name__ == '__main__':


3. При вызове функций модуля main.py выводится текущая дата.

4. Найден пакет requests на pypi и в файле requirements.txt указана его актуальная версия. 

*5. Создан рядом с файлом main.py модуль dirty_main.py и импортированы все функции с помощью конструкции.
