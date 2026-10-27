#День 9: Циклы for

#1. Простой перебор от 1 до 10 (с помощью for in range)

print("=== Простой перебор от 1 до 10 ===")
for i in range(1,11):
    print(i, end=" ")
print("\n")

#2. Чётные числа от 2 до 20

print("=== Чётные числа от 2 до 20 ===")
for i in range(2,21,2):
    print(i,end=" ")
print("\n")

#3. Таблица умножения

num=5
print("=== Таблица умножения на 5 ===")
for i in range(1,11):
    print(f"{num} * {i} = {num*i}")
print("\n")

#4. Сумма чисел от 1 до 100

sum_num=0
print("=== Сумма чисел от 1 до 100 ===")
for i in range(1, 101):
    sum_num+=i
print(sum_num, "\n")

#5. Бонус-задача. Переворот строки

print("=== Переворот строки ===")
varieble=input("Введите строку: ")
res=""
for i in range(len(varieble)-1,-1,-1):
    res+=varieble[i]
print(f"Результат: {res}")