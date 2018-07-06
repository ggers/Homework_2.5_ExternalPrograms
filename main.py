
import os
import subprocess

#1. создать в рабочей директории субдиректорию RESULT
#2. создать список файлов для преобразования
#3. применить к каждому файлу из списка стороннюю программу с параметрами

current_dir = os.path.dirname(os.path.abspath(__file__))

def create_subdirectory(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)
        print(f"Целевая директория {dirname} создана")

def get_files_from_directory(dir_name, file_type=".jpg"):
    return [x for x in os.listdir(os.path.join(current_dir, dir_name)) if x.endswith(file_type)]

def file_resizing(file_name, koefficient):
    image_unpack = os.path.join(current_dir, "convert.exe")
    filepath = os.path.join(current_dir, "Source", file_name)
    resultPath = os.path.join(current_dir, "Result", file_name)
    subprocess.run([image_unpack, filepath, "-resize", koefficient,  resultPath])

if __name__ == '__main__':
    print(f"Начинаем преобразование файлов в директории {current_dir}")
    create_subdirectory(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Result"))
    file_list = get_files_from_directory(os.path.join(current_dir, "Source"), file_type=".jpg")
    print(f"Будут преобразованы следующие {len(file_list)} файлов\n", file_list)
    for file in file_list:
        file_resizing(file, "200")
    print("Преобразование завершено")


