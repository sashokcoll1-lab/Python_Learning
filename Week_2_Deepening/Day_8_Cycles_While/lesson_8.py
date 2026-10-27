#День 8: Циклы.

import random

#1. Счётчик от 1 до 5 (с помощью while)

i=1

print("=== Счётчик от 1 до 5 ===")

while i<=5:
    print(i, end=" ")
    i+=1

print("\n")

#2. Счётчик от 5 до 1 (с помощью while)

i=5

print("=== Счётчик от 5 до 1 ===")

while i>=1:
    print(i, end=" ")
    i-=1

print("\n")

#3. Сумматор чисел

total_sum_num=0

print("=== Сумматор чисел ===")

while True:
    sum_num=int(input("Введите число (0 для выхода): "))
    if sum_num==0:
        break
    else:
        total_sum_num+=sum_num

print(f"Сумма: {total_sum_num}\n")

#4. Бонус-задача. Угадай число

print("=== Угадай число ===")

random_num=random.randint(1,10)
count=1

while True:
    num=int(input("Угадайте число от 1 до 10: "))
    if num==random_num:
        break
    elif num>10 or 1>num:
        print("Число должно быть от 1 до 10!")
    elif num>random_num:
        print("Меньше!")
        count+=1
    else:
        print("Больше!")
        count+=1

if count==1: #Корректное название попыток для каждого кол-ва
    print(f"Угадали за {count} попытку!")
elif count==1:
    print(f"Угадали за {count} попытки!")
else:
    print(f"Угадали за {count} попыток!")