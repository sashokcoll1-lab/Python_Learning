'''
Телефонный справочник на JSON:

При запуске программа загружает контакты из файла contacts.json, если файл есть. Если нет — начинает с пустого словаря.
'''

import json
import os

'''
- Реализуйте меню:
    1. Показать все контакты (имя и телефон)
    2. Добавить новый контакт (имя, телефон)
    3. Удалить контакт по имени
    4. Найти телефон по имени
    5. Выйти (автоматически сохранить контакты в JSON)
- Все изменения должны сохраняться в файл при выходе.

- Использование модуля os (необязательно):
Проверяйте существование файла contacts.json с помощью os.path.exists() перед загрузкой, чтобы избежать ошибки.

Бонус-задача:
Добавьте возможность редактировать номер телефона существующего контакта.
'''

'''Проверка есть ли json файл и перенос данных из него в dict'''

if os.path.exists("contact.json"):
    with open("contact.json", "r", encoding="utf-8") as f:
        contacts = json.load(f)
else:
    contacts = {}

while True:
    choice=input("=== Телефонный справочник (JSON) ===\n1. Показать все контакты\n2. Добавить контакт\n3. Удалить контакт\n4. Найти контакт\n5. Редактировать номер\n6. Выйти\nВыберите действие: ")
    if choice=="1":
        if not contacts:
            print("Справочник пуст.")
        else:
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
    elif choice=="2":
        name=input("Введите имя: ")
        num=input("Введите номер: ")
        contacts[name]=num
        print(f"Добавлен новый контакт {name}!")
    elif choice=="3":
        question=input("Введите имя контакта для удаления: ")
        if question in contacts:
            del contacts[question]
            print(f"Контакт {question} удалён!")
        else:
            print(f"Контакт {question} не найден!")
    elif choice=="4":
        question=input(f"Введите имя для поиска: ")
        if question.strip() in contacts:
            print(f"{question.strip()} : {contacts[question.strip()]}")
        else:
            print(f"{question} не найден в справочнике!")
    elif choice=="5":
        edit_name=input("Введите имя для редактирования: ")
        edit_num=input("Введите новый номер: ")
        if edit_name in contacts:
            contacts[edit_name] = edit_num
            print(f"Контакт {edit_name} обновлён.")
        else:
            print(f"Контакт {edit_name} не найден.")
    elif choice=="6":
        with open("contact.json", "w", encoding="utf-8") as f:
            json.dump(contacts, f, ensure_ascii=False, indent=4)
            break
    else:
        print("Вы ввели неправильный выбор!")