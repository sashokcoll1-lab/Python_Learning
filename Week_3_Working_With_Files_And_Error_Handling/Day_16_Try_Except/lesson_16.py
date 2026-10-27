'''1. Деление с защитой:
Запросите два числа у пользователя, выведите результат деления. Обработайте:
    ValueError — если ввели не число
    ZeroDivisionError — если второй ноль'''

while True:
    try:
        num_1 = int(input("=== Деление ===\nВведите первое число: "))
        num_2 = int(input("Введите второе число: "))
        print(f"Результат деления: {num_1/num_2}")
        break
    except ValueError:
        print("Это не число!")
    except ZeroDivisionError:
        print("Делить на ноль нельзя!")

'''2. Чтение файла с проверкой:
Попросите пользователя ввести имя файла. Попробуйте прочитать и вывести его содержимое. 
Если файла нет — сообщите об этом и не дайте программе упасть.'''

try:
    name_file=input("=== Чтение файла ===\nВведите имя файла: ")
    with open(name_file,"r", encoding="utf-8") as f:
        print(f"Содержимое файла:\n{f.read()}\nКонец содержимого файла")
except FileNotFoundError:
    print("Файл не найден. Проверьте имя.")
except PermissionError:
    print("Нет прав для чтения файла.")

'''3. Список дел с обработкой ошибок:
Доработайте вчерашний список дел: добавьте обработку FileNotFoundError при чтении и PermissionError (на всякий случай).'''

from datetime import datetime

while True:
    choice=input("=== Список дел ===\n1. Показать все задачи\n2. Добавить новую задачу\n3. Очистить список задач\n4. Выйти\nВыберите действие: ")
    if choice=="1":
        try:
            with open("tasks.txt","r",encoding="utf-8") as f:
                task_data=f.read()
                if not task_data:
                    print("Список задач пуст.")
                else:
                    lines = task_data.splitlines()
                    for i, line in enumerate(lines, start=1):
                        print(f"{i}. {line.strip()}")
                    print("\n=== Конец списка задач ===")
        except FileNotFoundError:
            print("Список задач пуст (файл не найден).")
        except PermissionError:
            print("Нет доступа к файлу.")
    elif choice=="2":
        task_new=input("Введите задачу: ")
        now = datetime.now().strftime(" %Y-%m-%d %H:%M:%S")
        with open("tasks.txt","a",encoding="utf-8") as f:
            f.write(f"{task_new} | {now}\n")
            print("Задача добавлена!")
    elif choice=="3":
        with open("tasks.txt","w",encoding="utf-8") as f:
            pass
            print("Список задач очищен!")
    elif choice=="4":
        print("До свидания!")
        break
    else:
        print("Выберите правильный вариант!")

'''4. Бонус-задача:
Создайте функцию safe_int_input(prompt), которая запрашивает у пользователя целое число,
обрабатывает ValueError и повторяет запрос до тех пор, пока не будет введено корректное число. Возвращает int.'''

def safe_int_input(prompt):
    while True:
        try:
            num_int = int(input(prompt))
            return num_int
        except (ValueError, ZeroDivisionError):
            print("Некорректный ввод. Попробуйте снова.")

num=safe_int_input("Введите целое число: ")
print(f"Вы ввели число: {num}")