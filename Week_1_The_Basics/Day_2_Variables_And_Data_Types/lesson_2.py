#День 2: Переменные и типы данных.

#1. Создание переменных

age=20
height=1.6
name="Саша"
is_student=True

#2. Проверка типов

print("2 Проверка типов:")
print("age имеет тип: ", type(age))
print("name имеет тип: ", type(name))
print("is_stedent имеет тип: ", type(is_student))

#3. Вывод результата

print("3 Вывод результатов:")
print("Мой возраст: ", age)
print("Мой рост: ", height)
print("Моё имя: ", name)
print("Являюсь ли я студентом: ", is_student)

#4. Бонус: расчет года рождения

print("4 Бонус: расчет года рождения")
current_year=2025
year_of_birth=current_year-age
print("year_of_birth имеет тип: ", type(year_of_birth))
print("Мой год рождения: ", year_of_birth)