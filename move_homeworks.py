import os
import shutil

from helper import make_dirs

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


# 1
homework_dir = 'homeworks'

make_dirs(homework_dir)

# 2
files = os.listdir()
new_files_list = [] # список файлов, которые будем перемещать

for file in files:
# 2.1 и 2.2
    if '.txt' in file and 'homework' in file:
        new_files_list.append(file)

# print(new_files_list)
        
for file in new_files_list:
    shutil.copy(file, f'{homework_dir}/{file}')

for file in new_files_list:
    os.remove(file)