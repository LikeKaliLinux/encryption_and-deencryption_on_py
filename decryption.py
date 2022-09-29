import pyAesCrypt
import os

# Функция дешифровки файла

def decryption(file, password):

    # Задаем размер буфера
    buffer_size = 512 * 1024 # с его помощью мы будем шифровать и расшифровывать

    # Вызываем метод расшифровки и перередаем в него:
    pyAesCrypt.decryptFile(
        str(file),  # файл
        str(os.path.splitext(file)[0]),
        password, # пароль
        buffer_size # буфер
    )

    # Выведим результат зашифрованного файла
    print("[Файл '" + str(os.path.splitext(file)[0]) + "' расшифрован]")

    # В конце функции удалим исходный файл с помощью метода remove

    os.remove(file)

# Фунция сканирования дерикторий

def walking_by_dirs(dir, password): # параметры для расшифровки: путь до директории и пороль

    # перебирает все поддиректории в указанной директории

    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # если находим файл, то расшифрует его

        if os.path.isfile(path):
            try:  # обернем функцию в блок try на всякий случай
                decryption(path, password)
            except Exception as ex:
                print(ex)
        else:  # иначе продолжаем искать
            walking_by_dirs(path, password)


password = input("Введите пароль для расшифровки: ")
walking_by_dirs("C:/Users/Bogdan/Desktop/test", password)