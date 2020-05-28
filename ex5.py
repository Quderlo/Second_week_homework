import random

def marks():
	mark = []
	for _ in range(5):
		mark.append(random.randint(2,5))
	return mark

def fun(tmp):
	x = 0
	for j in tmp:
		x += j
	return x

def average_class(tmp):
	return str((fun(tmp) / len(tmp)))

def average_school(sum, total_lenght):
	return str(sum / total_lenght)

roster = []
letter = 'АБВГ'
sum = 0
total_lenght = 0
for i in letter:
	for z in range(1,5):
		tmp = marks()
		roster.append({'school_class': str(z) + i, 'scores': tmp})
		print('Средний балл в классе ' + str(z) + i + ' равен ' + average_class(tmp))
		sum += fun(tmp)
		total_lenght += len(tmp)

print('Средний балл по школе равен ' + average_school(sum, total_lenght))


#Задание
#Создать список из словарей с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
#Посчитать и вывести средний балл по всей школе.
#Посчитать и вывести средний балл по каждому классу.
