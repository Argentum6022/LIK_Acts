import os
file_path=str(input('Введите путь папки: '))
number=str(input('Введите входящий номер раствора:'))
file_path=file_path.replace('\\','\\\\')
os.chdir(file_path)
os.mkdir(number)