'''
5.В этом задании мы будем отслеживать дни рождения наших друзей. Создайте dictionary с
именами и датами друзей (кого угодно). При запуске программы вы должны ввести имя и
после чего программа должна вернуть Имя + дата рождения. Взаимодействие должно
выглядеть так:
>>> Welcome to the birthday dictionary. We know the birthdays of:
Albert Einstein
Benjamin Franklin

Ada Lovelace
>>> Who's birthday do you want to look up?
Benjamin Franklin
>>> Benjamin Franklin's birthday is 01/17/1706.
'''




def birthday_memory(key):
    key_name = {1: "Вася Пупкин", 2: "Петя Обломов", 3: "Саня Пушкин", 4: "Дима Билан", 5: "Боб Путин", 
            6: "Боб Марли", 7: "Сергей Есенин", 8: "Мишка Джексон", 9: "Лев Толстой", 10: "Вовка Жириновский"}
    name_birthday = {"Вася Пупкин": "02/14/1987", "Петя Обломов": "01/01/1859", "Саня Пушкин": "06/06/1799", "Дима Билан": "12/24/1981", "Боб Путин": "10/07/1952", 
                "Боб Марли": "02/06/1945", "Сергей Есенин": "10/03/1895", "Мишка Джексон": "08/29/1958", "Лев Толстой":"09/09/1828", "Вовка Жириновский": "04/25/1946"}
    print("День рождения у {} --- {}".format(key_name[key], name_birthday[key_name[key]]))




vibor_key = int(input('''
Выберите человека из списка:
1:  Вася Пупкин 
2:  Петя Обломов 
3:  Саня Пушкин 
4:  Дима Билан 
5:  Боб Путин 
6:  Боб Марли 
7:  Сергей Есенин 
8:  Мишка Джексон 
9:  Лев Толстой 
10: Вовка Жириновский

введите номер: '''))

birthday_memory(vibor_key)