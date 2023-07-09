# def main():
#     import random
#
#     print(random.randint(1, 11))
#
#
# if __name__ == "__main__" and 0:
#     main()
# ################
# # +, -, /, *, %, //, **
# # >=, <=, >, <, ==, !=
# # =, +=, -=, ...
# ################
# # a = 5
# #
# # if a % 2 == 0:
# #     print(a, "is even")
# # else:
# #     print(a, "is odd")
#
# ################
# # a = "50"
# # b = "10"
# #
# # a1 = int(a)
# # b1 = int(b)
# #
# # print(a1 - b1)
# ################
# # list, dict, set
# # str, int, bool, float, char, tuple
#
#
# ################
#
# # l = [10, 20, 30, 42]
# #
# # i = 0
# #
# # while i < len(l):
# #     print(l[i])
# #
# #     i += 1
#
# # s = "Hello Python"
# #
# # s = s.upper()
# #
# # print(s)
#######################
# CRUD
# C - CREATE
# R - READ
# U - UPDATE
# D - DELETE

students = []


def add_student(student):  # parameters
    student = student.title()

    students.append(student)


def remove_student(student):
    student = student.title()

    if student in students:
        students.remove(student)


def get_student_by_name(name):  # name = "Аян" "Гусейнли Аян Фаган"
    for student in students:
        if name in student:
            return student
    return None

def update_student_by_name(name, new_fullname):
    for i in range(len(students)):
        if name in students[i]:
            students[i] = new_fullname
            break


def check_int(number):
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0


def avg(a, b):
    result = (a + b) / 2

    return result


add_student("Искендерли Амин Ильхам")  # arguments  # student = "Amin"
add_student("Гусейнли Аян Фаган")  # student = "Ayan"
add_student("Сигарёв Вадим ...")
add_student("Мусаев Рауф Матлабович")
add_student("Байрамов Али Юсиф")
#
# students.sort()

# remove_student("Сигарёв Вадим ...")

student = get_student_by_name("Вадим")

if student is not None:
    new_fullname = student.replace("...", "Генадьевич")
    update_student_by_name("Вадим", new_fullname)

print(students)


# s = input()


# res = avg(10, 15)

# print(res)
######
# s = check_int(-90)

# print(s)


# print(10, 20, 30, "Text")

# A = -42
#
# if A > 0:
#     value = True
#
#
# print(value)

l = [0, 0, 1, 2]

s = None

print(type(s))
