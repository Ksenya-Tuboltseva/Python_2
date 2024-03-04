##Напишите функцию группового переименования файлов. Она должна:
##a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
##b. принимать параметр количество цифр в порядковом номере.
##c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
##d. принимать параметр расширение конечного файла.
##e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

import os
import pathlib

path_of_files = "C:\\reports\\"

def a (path, name):
    with open(path, "r+", encoding="utf-8") as files:
        files = Path(Path().cwd())
        for i, f in enumerate(files.iterdir()):
            new_name = name+str(i)+f.split(".")[-1]
            f.os.rename(f, new_name)
        
def b (path, integer):
    with open(path, "r+", encoding="utf-8") as files:
        files = Path(Path().cwd())
        for i, f in enumerate(files.iterdir()):
            if len(str(i)) != integer:
                num = f.split(".")[1][-len(str(i))]
                null = "0" * (integer-num)
                new_name = f.split(".")[1][len(f.split(".")[1]-len(str(i))] + null + num + f.split(".")[-1]
                
def c (path, extention):
    with open(path, "r+", encoding="utf-8") as files:
        files = Path(Path().cwd())
        for f in os.listdir(files):
            if f.split(".")[-1] == extention:
                f.os.rename(f, "new_name")
                
def d (path, extention_new):
    with open(path, "r+", ecoding="utf-8") as files:
        files = Path(Path().cwd())
        for f in os.listdir(files):
            if f == "new_name":
                new_name = f.split(".")[1]+extention_new
                f.os.rename(f, new_name)
    
def e (path, start=start, end=end):
    with open(path, "r+", encoding="utf-8") as files:
        files = Path(Path().cwd())
        for i, f in enumerate(files.iterdir()):
            f.os.rename(f, f[start, end]+str(i)+f.split(".")[-1])
