##Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
def split(p):
    folder = ""
    name = ""

    for i in range(1, len(p)):
        if p[-i] == "/":
            folder = p[:-i+1]
            name = p[-i+1:]
            break

    name, format = name.split(".")
    return folder, name, format

path = "C:/Users/User/Desktop/ФТноменклатура.docx"
print(split(path))

##Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int, премия str с указанием процентов вида “10.25%”. В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии
nm = ["Alex", "Max"]
st = [10000, 20000]
per = ["5%", "10%"]

def bonus(name, rate, percent):
    salary_dict = {name[i]: rate[i]/100*float(percent[i][:-1]) for i in range(len(name))}
    yield salary_dict

##Создайте функцию генератор чисел Фибоначчи
def fib(n):
    a, b = 0, 1
    for __ in range(n):
        yield a
        a, b = b, a + b

for i, num in enumerate(fib(8), start=0):
    print(f"F{i} = {num}")