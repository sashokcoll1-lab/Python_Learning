#Задание 12

#1. Написать фунция greet(), которая принимает имя и выводит "Привет, {имя}!"

def greet(name):
    print("=== Функции ===")
    print(f"Привет, {name}!")

greet("Саша")

#2. Написать функцию square(), которая принимает число и возвращает его квадрат

def square(num):
    print(f"Квадрат числа {num}: {num*num}")

square(5)

#3. Написать функцию is_even(), которая проверяет на чётность число

def is_even(num):
    if num%2>0:
        print(f"Число {num} чётное? False")
    else:
        print(f"Число {num} чётное? True")

is_even(7)

#4. Написать функцию sum_range(start, stop), которая суммирует числа от start и до end

def sum_range(start, end):
    sum_num=0
    for i in range(start, end+1):
        sum_num+=i
    print(sum_num)

sum_range(1,10)

#5. Бонус-задача. Создайть функцию calculator(a, b, operation), которая принимает два числа и строку с операцией (+, -, *, /)
    #Возвращает результат операции
    #В основной программе запросите данные у пользователя, вызовите функцию и выведите результат. Обработайте деление на ноль и неверную операцию

def calculator(a,b,operation):
    if operation=="+":
        print(f"Результат: {a} + {b} = {a+b}")
    elif operation=="-":
        print(f"Результат: {a} - {b} = {a-b}")
    elif operation=="*":
        print(f"Результат: {a} * {b} = {a*b}")
    elif operation=="/" and b!=0:
        print(f"Результат: {a} / {b} = {a/b}")
    elif b==0:
        print(f"Делить на {b} нельзя!")
    else:
        print(f"Неверная операция!")

print(f"=== Калькулятор ===")
a=int(input("Введите первое число: "))
b=int(input("Введите второе число: "))
operation=input(f"Введите операцию (+, -, *, /): ")
calculator(a,b,operation)