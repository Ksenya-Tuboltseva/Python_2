##В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку
from datetime import datetime
import calendar

def check_date():
    date = input("Введите дату в формате DD.MM.YYYY: ")
    if len(date.split(".")[2]) == 4 and len(date.split(".")[1]) == 2 and len(date.split(".")[0]) == 2:
        format = "%d.%m.%Y"
        try:
            date = datetime.strptime(date, format)
            return date
        except:
            return "Даты не существует"
    else:
        return "Неправильный формат"

def check_year(year: int) -> bool:
    return calendar.isleap(year)
       
print(check_date(), check_year(2024))


##Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь
def chess (points: list ):
    for point1 in points:
        for point2 in points:
            if point1[0] == point2[0] or point1[1] == point2[1] or abs(point1[0] - point2[0]) == abs(point1[1] - point2[1]):
                return False
            else:
                return True
            
print(chess(points=[(1,6), (3,7), (2,8), (4,1), (8,5), (7,4), (6,3), (5,2)]))

##Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки
import random

def chess_check ():
    desk = []
    for i in range(0,8):
        desk.append((random.randint(1,8), random.randint(1,8)))
    return desk

def check ():
    i = 0
    while i < 4:
        if chess(points=chess_check()) == True:
            return chess_check()
            i += 1
        else: continue
    
print(check())