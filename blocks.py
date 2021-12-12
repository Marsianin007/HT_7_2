# 2.    Написати функцію, яка приймає два параметри: ім'я файлу та кількість символів.
#   На екран повинен вивестись список із трьома блоками - символи з початку, із середини та з кінця файлу.
#       Кількість символів в блоках - та, яка введена в другому параметрі.
#   Придумайте самі, як обробляти помилку, наприклад, коли кількість символів більша,
#   ніж є в файлі (наприклад, файл із двох символів і треба вивести по одному символу, то що виводити на місці середнього блоку символів?)
#       В репозиторій додайте і ті файли, по яким робили тести.
#   Як визначати середину файлу (з якої брать необхідні символи) - кількість символів поділити навпіл,
#   а отримане "вікно" символів відцентрувати щодо середини файла і взяти необхідну кількість.
#       В разі необхідності заокруглення одного чи обох параметрів - дивіться на свій розсуд.
import json
import sys

def index_for_middle(file, number):
    with open(file, "r") as file_js:
        file_py = file_js.read()
        file_py = file_py.replace('"', '')

        if len(file_py) % 2 == 0 and number % 2 == 0:
            index_1 = int((len(file_py) - number) / 2)
            index_2 = int((len(file_py) + number) / 2)
            return file_py[index_1: index_2]


        if len(file_py) % 2 == 0 and number % 2 != 0:
            center = int(len(file_py) // 2)
            index_1 = int((center - number / 2))
            index_2 = int((center + number / 2))
            return file_py[index_1 : index_2]

        if len(file_py) % 2 != 0 and number % 2 == 0:
            index_1 = int(((len(file_py) - 1 - number) / 2))  #зміщуємо вліво
            index_2 = int(((len(file_py) + number) / 2))
            return file_py[index_1: index_2]

        if len(file_py) % 2 != 0 and number % 2 != 0:
            center = int(len(file_py) / 2)
            index_1 = int(center - (number // 2) - 1)
            index_2 = int(center + (number // 2) - 1)
            if number != 1:
                return file_py[index_1 + 1: index_2 + 2]
            else:
                return file_py[center : center + 1]

def divide_to_3_blocks(file_name, number):
    with open(file_name, "r") as file:
        text_file = file.read()
        text_file = text_file.replace('"', '')
        if str(number).isdigit():
            number = int(number)

        if  str(number).isdigit() == False:
            print("Введена строка або від'ємне число")
            SystemExit

        elif int(number) > len(text_file):
            print("Неможливо поділити з такою довжиною блока")
            SystemExit
        else:
            number = int(number)

            list_start = text_file[0:number]
            list_middle = index_for_middle(file_name, number)
            list_back = text_file[len(text_file) - number: len(text_file)]
            print("Початок: " + list_start)
            print("Середина: " + str(list_middle))
            print("Кінець: " + list_back)

divide_to_3_blocks("text.data", 0)
