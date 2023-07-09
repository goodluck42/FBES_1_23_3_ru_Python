# def get_person():
#     with open("data.txt", "r") as f:  # чтение из файла
#         name = f.readline()
#
#     return name
#
#
# persons = []
#
# person = get_person()
# persons.append(person)
#
# with open("out.txt", "w") as f:  # запись из файла
#     f.writelines([person])
import uuid

## tuple

# def get_user():
#     name = "Vadim"
#     age = 21
#
#     return name, age
#
#
# my_tuple = get_user()
#
# for item in my_tuple:
#     print(item)
#
# print(type(my_tuple))
# print(my_tuple)
# print(len(my_tuple))

## args

# def my_sum(*args):
#     length = len(args)
#
#     if length == 0:
#         return
#
#     for item in args:
#         print(item / 2)
#
#
# with open("nums.txt", "r") as f:
#     numbers = [int(value) for value in "".join(f.readlines()).split('\n')]
#
#     print(numbers)
#
#
# my_sum(10, 20, 30)  # my_sum(10, 20, 30)
# print(*'-' * 10)
# # my_sum(numbers)  # my_sum([10, 20, 99])
# my_sum(*numbers)  # my_sum(10, 20, 99)
#
# print(*"C++")  # print('C', '+', '+')


## dict

# coins, diamonds, name, surname

# coins = 90
# diamonds = 165
# name = Амин
# surname = Искендерли
# _id = ...

## tuple variant

# student = (90, 165, "Амин", "Искендерли", str(uuid.uuid4()))
#
# print(student[0])
# print(student[1])
# print(student[4])

## dict

stud = {
    "coins": 90,
    "diamonds": 165,
    "name": "Амин",
    "_id": str(uuid.uuid4()),
    "grades": [10, 12, 13, 41]
}

# keys = stud.keys()
# for key in keys:
#     print(key)
#
# print(*'-' * 10)
# values = stud.values()
#
# for value in values:
#     print(value)


def print_student(student):
    for k, v in student.items():
        print(f"{k}: {v}")


def input_student():
    student = {}

    student["coins"] = int(input("Enter coins: "))
    student["diamonds"] = int(input("Enter diamonds: "))
    student["name"] = input("Enter name: ")
    student["_id"] = str(uuid.uuid4())

    return student


stud1 = input_student()

print_student(stud1)

game = {
    "name": "Rainbow Six: Siege",
    "price": 5,
    "genres": ["shooter", "coop", "online"],
    "developer": "Ubisoft",
    "description": "Cool game",
}

