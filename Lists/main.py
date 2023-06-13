# student1 = "Рамиль"
# student2 = "Али"
# student3 = "Равиль"
# # ...
# student12 = "Нателла"
############################
#              0        1        2         3
# students = ["Рамиль", "Али", "Равиль", "Нателла"]
#
# # val = students[0]
# # val = "Осман"
#
# students[1] = "Осман"
#
# print(students)
# print(students[1])
####################
## SAMPLE1
# students = []
# print("Press enter to quit the program")
#
# while True:
# 	student = input("Enter student name: ")
#
# 	if student == "":
# 		break
#
# 	students.append(student)
#
# print(students)
#########
### FOR VARAINT
# students = ["Тогрул", "Эмиль", "Осман", "Нателла"]
#
# # my_range = range(5)
# # print(list(my_range))
#
# i = 1
#
# for student in students:
# 	print(i, student)
#
# 	i += 1

### WHILE VARIANT
#           0         1      2         3          4
# students = ["Рамиль", "Али", "Равиль", "Нателла", "Аян"]
#
# i = 0
# # 0 1 2 3 4
#
# length = len(students)  # length = 5
#
# while i < length:
# 	print(i + 1, students[i])
# 	i += 1
#################################
### BAD PRACTICE
# prices = [11, 22, 30, 50, 900]
#
# for price in prices:
# 	price *= 0.81
#
# print(prices)

#####
# #         0   1   2   3   4        5
# prices = [11, 22, 30, 50, 900] # , 100
#
# prices.append(100)
#
# # print(list(range(5)))
#
# # length = len(prices)
#
# for i in range(len(prices)):
# 	prices[i] *= 0.81
#
# print(prices)

#################
# # import random
# from random import randint
#
# val = randint(1, 100)
#
# print(val)
############
from random import randint

numbers = []

for _ in range(9):
	val = randint(10, 99)
	numbers.append(val)

print(numbers)


# [-1, 2, 3, 4, 5, -10, 20, -30, -5]