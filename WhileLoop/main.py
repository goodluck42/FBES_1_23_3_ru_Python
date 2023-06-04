# i = 0
# # [0, 100]
# end = int(input("Enter number of iterations -> "))
#
# while i < end:
#     x = 1
#     if i % 2 == 0:
#         print("even:", i)
#     else:
#         print("odd:", i)
#
#     # i += 1  # increment
#     i += 1  # decrement

# print("i=", i, sep="|")
# print(1, 2, 3, end=" ")
# print(4, 5, 6)

# iteration

## WHILE & BREAK
# id = int(input())  # id = 7654 - Вагиф
# i = 0
#
# while i < 10000:
#     if i == id:
#         print("user found")
#         break
#     print(i)
#     i += 1
#
#
# print("i =", i)
## WHILE & CONTINUE

# [0, 30)
# [15, 20]
# i = 0
# while i < 30:  # i = 15
#     if 15 <= i and i <= 20:
#         i += 1
#         continue
#
#     print(i)
#     i += 1
# # [15, 20]
# value = 15
#
# if 15 <= value and value <= 20:
#     print("in range")
# else:
#     print("not in range")


begin = 10
copy = begin

print("first: ")
while begin > 0:

    print(begin)
    begin -= 1

print("second: ")
while begin > 0:
    print(begin)
    begin -= 1

