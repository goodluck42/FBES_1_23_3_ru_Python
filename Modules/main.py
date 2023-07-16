# f = open("task2.txt")
#
# lines = [line.replace('\n', '') for line in f.readlines()]
#
# print(lines)
#
# f.close()
import tkinter

import my_math
# import string
#
# print(string.punctuation)
###################
# word = "Hello"
#
# vowels = 0
#
# for c in word:
#     if c in "aoieu":
#         vowels += 1
#     else:
#         pass
#
# print(vowels)
# ######################
# student = {
#     "first_name": "Рамиль",
#     "last_name": "Ахминеев",
#     "father's_name": "Ренатович"
# }
#
# group = {
#     "name": "FBES_1233",
#     "students": []
# }
#
#
# group["students"].append(student)
#
# print(group)


# import json
#
# with open("data.json", 'r') as file:
#     group = json.load(file)
#
# print(group)
##############################
######
# import my_math
#
# res = my_math.div(50, 3.3)
#
# print(res)
#
# print(my_math.CONSTANT)
##############################
# from my_math import CONSTANT, mult
#
# print(CONSTANT)
#
# res = mult(20, 3.33)
#
# print(res)
##############################
# from my_math import *
#
#
# def mult(a, b):
#     print("multiplying")
#     return a * b
#
#
# res = mult(20, 3.33)
#
# print(res)
##############################

# from my_math import mult as multf, div as divide
#
#
# def mult(a, b):
#     print("multiplying")
#     return a * b
#
#
# res = multf(20, 3.33)
# res2 = mult(20, 5)
# res3 = divide(20, 5)
#
# print(res)
# print(res2)
# print(res3)
##############################
#
# import random as r
#
# rnd = r.randint(100, 200)
#
# print(rnd)

##############################

import my_math


def main():
    val = my_math.CONSTANT

    print(val)


if __name__ == "__main__":
    main()


print(f"main.py: {__name__}")
