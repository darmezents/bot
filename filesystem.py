# Работа с файлами

import os 

# информация о текуще файле
print(
    os.getcwd()
)
# result:
# C:\Users\User\Desktop\bot


# получить список файлов в директории
print(
    os.listdir()
)
# result:
#['arr.py', 'dict_01.py', 'filesystem.py', 'hello_world.txt', 'homework_1.py', 'homework_2.py', 'main.py', 'README.md', 'str.py']


# проверка есть ли директория
print(
    os.path.isdir('homeworks')
)

for f in os.listdir():
    print(
        f'is dir: {f}', os.path.isdir(f)
    )
# result:
# is dir: arr.py False
# is dir: dict_01.py False
# is dir: filesystem.py False
# is dir: hello_world.txt False
# is dir: homeworks True
# is dir: homework_1.py False
# is dir: homework_2.py False
# is dir: main.py False
# is dir: README.md False
# is dir: str.py False
    

# создание директорий
    
# os.makedirs('home')
    
# if not os.path.isdir('home_01/work_1'):
#     os.makedirs('home_01/work_1')

def make_dirs(path):
    if not os.path.isdir(path):
        os.makedirs(path)

# make_dirs('home_01/work_1')
        

# План переноса файлов в директорию
# 1. Проверка существует и директория
    # 1.1 Если существует, то ничего не делать
    # 1.2. Если не существует, то создать 
# 2. Ищем файлы, которые будем переносить
    # 2.1. Ищем файлы с форматом .txt
    # 2.2. Ищем файлы название которого содержит "homework"
# 3. Перемещение
    # 3.1. Выбор файла
    # 3.2. Копируем
    # 3.3. Перходим в директорию
    # 3.4. Добавляем файл
         # 3.4.1. Проверка исходного и скопированного файлов 
    # 3.5. Удаляем исходный файл       

        