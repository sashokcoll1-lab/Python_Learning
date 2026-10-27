#Задание 10

#1. Создать 3 листа по требованиям

num=[1,2,3,4,5]
fruits=["Яблоко", "Банан", "Дыня"]
mixed=[666, "Дьявол", 1.05]

#2. Работа с листом

print(f"Вывод первого элемента списка: {num[0]},{fruits[0]},{mixed[0]}")
print(f"Вывод последнего элемента списка: {num[0]},{fruits[0]},{mixed[0]}")
print(f"Вывод среднего элемента списка: {num[len(num)//2]},{fruits[len(fruits)//2]},{mixed[len(mixed)//2]}")
fruits.pop(1)
fruits.insert(1,"Манго")
fruits.append("Киви")

#3. Срезы

print(num[0:3:1])
print(num[1:-1:1])
print(num[::-1])

#4. Методы списков

fruits.sort()
num.pop(-1)
num.insert(0,0)

#5. Бонусная задача

numbers=0
count=0
numbs_list=[]

while numbers!=5:
    count+=1
    numbs=int(input(f"Введите число {count}:"))
    numbs_list.append(numbs)
    numbers+=1
print(numbs_list)

print(f"Сумма: {sum(numbs_list)}")

print(f"Максимальное значение: {max(numbs_list)}")
print(f"Минимальное значение: {min(numbs_list)}")