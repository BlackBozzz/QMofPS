import os
import shutil

global HomePath
HomePath = os.getcwd() + "/Admin"
os.chdir(HomePath)
print(HomePath)


def Help():
    return ("""
    CreateNewFolder     param1: (file name or path)                                               - создать пустой каталог (папку)
    DeleteFolder        param1: (file name or path)                                               - удалить папку
    FolderLevelUp       param1: (no parameters)                                                   - вернуться в предыдущую директорию
    MoveToFolder        param1: (path)                                                            - перейти в другой каталог
    CreateNewFile       param1: (file name)                                                       - создать новый текстовый файл
    WriteInFile         param1: (file name or path) param2: (text)                                - записать текст в файл
    ShowFile            param1: (file name or path)                                               - вывести содержимое файла
    DeleteFile          param1: (file name or path)                                               - удалить  файл
    CopyFile            param1: (file name or path) param2: (file name or path)                   - копировать файл
    MoveFile            param1: (file name or path) param2: (file name or path)                   - заменить (переместить) этот файл в другой каталог
    RenameFile          param1: (file name or path) param2: (file name or path)                   - переименовать файл или каталог
    reset               param1: (no parameters)                                                   - очистка терминала
    help                param1: (no parameters)                                                   - вывод доступных команд
    """)


# Проверка пути на валидность
def CheckPath(path):
    global HomePath
    if len(path.split("/")) == 1:
        if HomePath in os.getcwd():
            return True
    else:
        if HomePath in path[:len(HomePath)]:
            return True
    return False


# создать пустой каталог (папку)
def CreateNewFolder(folder):
    try:
        if not os.path.isdir(str(folder)) and CheckPath(folder):
            os.mkdir(str(folder))
            print(os.getcwd())
            return "Выполнено"
    except FileExistsError:
        return None


CreateNewFolder("123")


# удалить папку
def DeleteFolder(folder):
    if CheckPath(folder):
        os.rmdir(str(folder))
    else:
        print("Нет разрешения")


# вернуться в предыдущую директорию
def FolderLevelUp():
    try:
        if os.getcwd() != HomePath:
            os.chdir("..")
            return "Операция выполнена"
        else:
            return "Нет разрешения"
    except:
        return "Нет разрешения"


# перейти в другой каталог
def MoveToFolder(path):
    try:
        if CheckPath(path):
            os.chdir(path)
            print(os.getcwd())
        else:
            print(os.getcwd())
            print("Нет разрешения")
    except:
        return False


# создать новый текстовый файл
def CreateNewFile(file):
    try:
        if CheckPath(file):
            text_file = open(f"{file}", "w")
            text_file.close()
        else:
            print("Нет разрешения")
    except FileExistsError:
        print("Файл с таким именем уже существует")


# записать текст в этот файл
def WriteInFile(file, text):
    if CheckPath(file):
        with open(f"{file}", "a") as file:
            file.write(text)
    else:
        print("Нет разрешения")


# вывести содержимое файла
def ShowFile(file):
    if CheckPath(file):
        with open(f"{file}", "r") as file:
            for line in file:
                print(line)
    else:
        print("Нет разрешения")


# удалить этот файл
def DeleteFile(file):
    if CheckPath(file):
        os.remove(f"{file}")
    else:
        print("Нет разрешения")


# копировать файл
def CopyFile(file, path):
    if CheckPath(file) and CheckPath(path):
        shutil.copy(fr"{file}", f"{path}")
    else:
        print("Нет разрешения")


# заменить (переместить) этот файл в другой каталог
def MoveFile(file, path):
    if CheckPath(file) and CheckPath(path):
        os.replace(fr"{file}", f"{path}/{file.split('/')[-1]}")
    else:
        print("Нет разрешения")


# переименовать
def RenameFile(file, new_file):
    if CheckPath(file):
        if len(file.split("/")) == 1:
            if len(new_file.split("/")) == 1:
                os.rename(f"{file}", f"{new_file}")
        else:
            if len(new_file.split("/")) == 1:
                os.rename(f"{file}", f"{file[:-len(file.split('/')[-1])]}/{new_file}")
    else:
        print("Нет разрешения")


CreateNewFolder(HomePath)
