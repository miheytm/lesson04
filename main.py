#Задача 22:
import random

list_1 = []
n_1 = int(input('Введите количество элементов первого списка: '))
for i in range(n_1):
        list_1.append(random.randint(-20,20))
print('Первый набор')
print(list_1)
set_1 = set(list_1)

list_2 = []
m_1 = int(input('Введите количество элементов второго списка: '))
for i in range(m_1):
        list_2.append(random.randint(-20,20))
print('Второй набор:')
print(list_2)
set_2 = set(list_2)
set_3 = set_1.union(set_2)
list_3 = list(set_3)
list_3.sort()
print('Объединенный отсортированный набор, без повторений:')
print(list_3)

#Задача 24:
list_4 = []
n_4 = int(input('Введите количество кустов на грядке: '))
for i in range(n_4):
        list_4.append(random.randint(0, 40))
print(list_4)
coun_i = -1
max_k = list_4[coun_i-1]+list_4[coun_i]+list_4[coun_i+1]
for i in range(len(list_4)-1):
        if (list_4[i-1]+list_4[i]+list_4[i+1]) > max_k:
                max_k = list_4[i-1]+list_4[i]+list_4[i+1]
                coun_i = i
print('С куста номер', coun_i + 1, 'и двух соседних,', max_k, 'это максимум')



