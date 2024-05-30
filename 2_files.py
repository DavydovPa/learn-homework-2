"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""
import shutil
def main():


    with open('referat.txt', 'r', encoding='utf-8') as ref:

        content = ref.read()
        ref_2 = len(content)
        print('Длинна строки:', ref_2)

        ref_3 = len(content.split())
        print(f"Количество слов: {ref_3}")

    shutil.copyfile('referat.txt', 'referat2.txt')

    with open('referat2.txt', 'r', encoding='utf-8') as f:
        f_str = f.read()
        f_str = f_str.replace('.', '!')

    with open('referat2.txt', 'w', encoding='utf-8') as f:
        f.write(f_str)




























if __name__ == "__main__":
    main()
