#1 Создать словарь student (name, age, city, hobby)

student_dict={"name":"Саша", "age":20,"city":"Москва","hobby":"Программирование"}

#2 Вывести name, все ключи словаря, все значения, все пары

print(f"=== Вывод name, keys, value, items === \nName: {student_dict["name"]}")
print(f"Keys: {student_dict.keys()}")
print(f"Values: {student_dict.values()}")
print(f"Items: {student_dict.items()}")

#3 Изменяем возраст студента (+1)

student_dict["age"]=21

#4 Добавляем новую х-ку оценки (новым dict)

evaluations_dict={"mathematics":5,"physics":3,"informatics":5}

#5 Бонус-задача: создание dict телефонный справочник с циклом ввода имена и вывода номера с именем до команды стоп

phone_directory_dict={"Саша":"123-4567","Иван":"234-5678","Маша":"345-6789"}

print(f"=== Телефонный справочник ===")
for name,phone in phone_directory_dict.items():
    print(f"{name} : {phone}")

while True:
    question=input("=== Телефонный справочник ===\nВведите имя для поиска (или 'стоп' для выхода:): ")
    if question.lower() == "стоп":
        print("До свидания!")
        break
    elif question.strip() in phone_directory_dict:
        print(f"{question.strip()} : {phone_directory_dict[question.strip()]}")
    else:
        print(f"{question} не найден в справочнике!")