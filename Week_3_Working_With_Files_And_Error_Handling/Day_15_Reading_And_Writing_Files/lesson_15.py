'''Задание 15'''

'''Запросите у пользователя его имя и возраст. Запишите эти данные в файл user_info.txt в формате:
# Имя: {имя}, Возраст: {возраст}'''

name=input("Ваше имя: ")
age=input("Ваш возраст: ")
with open("user_info.txt","w",encoding="utf-8") as f:
    f.write(f"Имя: {name}, Возраст: {age}\n")

'''2. Чтение из файла:
# Прочитайте файл user_info.txt и выведите его содержимое на экран.'''

with open("user_info.txt","r",encoding="utf-8") as f:
    data=f.read()
    print(f"Содержимое файла:\n{data}")

'''3. Добавление в файл (режим a):
Спросите у пользователя его любимый город и добавьте эту информацию в тот же файл на новой строке:
Город: {город}'''

with open("user_info.txt","a",encoding="utf-8") as f:
    city=input("Введите свой любимый город: \n")
    f.write(f"Город : {city}")

'''4. Список дел'''

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