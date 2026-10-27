#День 5: Условные операторы

#1. Запрашиваем число у пользователя

number=int(input("Введите любое число: "))

#2. Начинаем проверять число и выводить результят

if number>0:
    print("Число положительное!")
elif number<0:
    print("Число отрицательное!")
else:
    print("Это ноль!")
print()

#3. Дополнительная задача. Спрашиваем у пользователя возраст

age=int(input("Сколько вам лет? "))

#4. Начинаем проверять возраст и определять группу пользователя по нему

if age<13:
    print("Ребёнок")
elif age<18:
    print("Подросток")
elif age<60:
    print("Взрослый")
else:
    print("Пенсионер")
print()

#5. Бонусная задача. Спрашиваем пользователя два числа

print("=== Калькулятор ===")
number_calculator_1=int(input("Введите первое число: "))
number_calculator_2=int(input("Введите второе число: "))

#6. Спрашиваем пользователя какую операцию он хочет сделать и выводим результат

operation=input("Введите операцию (+, -, /, *): ")
if operation=="+":
    print(f"Результат: {number_calculator_1} {operation} {number_calculator_2} = {number_calculator_1+number_calculator_2}")
elif operation=="-":
    print(f"Результат: {number_calculator_1} {operation} {number_calculator_2} = {number_calculator_1-number_calculator_2}")
elif operation=="/":
    if number_calculator_2!=0:
        print(f"Результат: {number_calculator_1} {operation} {number_calculator_2} = {number_calculator_1/number_calculator_2}")
    else:
        print("Ошибка! Деление на ноль!")
elif operation=="*":
    print(f"Результат: {number_calculator_1} {operation} {number_calculator_2} = {number_calculator_1*number_calculator_2}")
else:
    print("Ошибка! Вы ввели неверную операцию!")