##Напишите функцию для транспонирования матрицы
def transpose(m):
    m = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    return m

matrix = [[0, 1, 2], [3, 4, 5]]
print(matrix)
print(transpose(matrix))

##Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.
def kwarg_dict(**kwargs):
    rez_dict = {}
    for kw in kwargs:
        rez_dict[kw] = kwargs[kw]
    return rez_dict

print(kwarg_dict(name="Alex", age=30, city="Moscow"))

##Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. Дополнительно сохраняйте все операции поступления и снятия средств в список.
def main():
    balance = 0
    count = 0
    lst = []
    print("Добро пожаловать")
    while True:
        while True:
            user_input = input("Выберите действие: 1 - пополнить, 2 - снять, 3 - показать все операции, 4 - выйти" : )
            if user_input not in ("1", "2", "3", "4"):
                print("Неверно")
            else: break
        match user_input:
            case "1":
                balance, count, lst = add_money(balance, count, lst)
                print(f"Ваш баланс {balance}")
            case "2":
                balance, count, lst = get_money(balance, count, lst)
                print(f"Ваш баланс {balance}")
            case "3":
                print(f"Список Ваших операций: {lst}")
            case "4":
                print(f"Ваш баланс: {balance}. До свидания")
            
def add_money(balance, count, lst):
    if balance > 5000000:
        balance *= 0.9
    while True:
        try:
            summ = int(input("Введите сумму пополнения, кратную 50: "))
        except:
            ex = input("Хотите выйти? (Да/нет)")
            if ex.lower() == "да":
                return balance, count, lst
            else: continue
        if summ % 50 == 0:
                break
    balance += summ
    count += 1
    if count % 3 == 0:
        balance *= 1.03
    lst.append(f"добавлено с учетом налога {summ} у.е.")
    return balance, count, lst
    
def get_money(balance, count, lst):
    if balance > 5000000:
        balance *= 0.9
    while True:
        try:
            summ = int(input("Введите сумму снятия, кратную 50: "))
        except:
            ex = input("Хотите выйти? (Да/нет)")
            if ex.lower() == "да":
                return balance, count, lst
            else: continue
        if summ % 50 == 0:
            perc = summ * 0.015
            if perc < 30:
                perc = 30
            elif perc > 600:
                perc = 600
            if summ + perc > balance:
                print("Недостаточно средств")
                continue
            else: break
    balance -= (summ + perc)
    count += 1
    if count % 3 == 0:
        balance *= 1.03
    lst.append(f"Снято с учетом процентов: {summ+perc}")
    return balance, count, lst
    
if __name__ == "main":
    main()