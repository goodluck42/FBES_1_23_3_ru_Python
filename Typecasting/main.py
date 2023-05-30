# int, float, str, bool

# number: int = int(input())
#
# print(number + number)

# str to int

# text: str = "+42"
# number: int = int(text)
#
# print(number * 2)

# str to float

# text: str = "42.0"
# number: float = float(text)
#
# print(number * 2)

# str to bool

# text: str = ""
# value: bool = bool(text)
#
# print(value)


# float to int
# a: float = 42.13
# b: int = int(a)
#
# print(b)

# int to bool & float to bool
# a = 0
# b = bool(a)
#
# print(b)

# bool to int & bool to float
# a = True
# b = float(a)
#
# print(b)

# bool to str

# a = True
# b = str(a)
#
# print(a)
# print(b)
# print("True")

# arithmetic
# +, -, /, *, %, //, **

# assignment
# =, +=, -=, /=, *=, %=, //=, **=
# :=

# coins = 100
#
# coins //= 5  # coins = coins // 5
#
# print(coins)

# comparison
# >, <, >=, <=, ==, !=

# a = 12
# b = 10
#
# result: bool = a != b
#
# print(result)

# logical
# and, or, not

# and
# 0 - False
# 1 - True
# print(False and True)  # 0 * 1 = 0 = False
# print(True and False)  # 1 * 0 = 0 = False
# print(False and False)  # 0 * 0 = 0 = False
# print(True and True)  # 1 * 1 = 1 = True

# or
# print(False or True)  # 0 + 1 = 1 = True
# print(True or False)  # 1 + 0 = 1 = True
# print(False or False)  # 0 + 0 = 0 = False
# print(True or True)  # 1 + 1 = 2 = True

# not (unary)
# print(not True)
# print(not False)

# value = -5
#
# a = 10
# b = 5
#
# result = a - b

# unary
# binary
# ternary

# number = int(input("Enter a number: "))
#
# if number > 0:
#     print("positive")
# elif number == 0:
#     print("zero")
# else:
#     print("negative")

number = 25

if number / 2:
    print("even")
else:
    print("odd")


print("1. Add")
print("2. Subtract")
print("3. Multiply")

choice = int(input("Enter choice -> "))

if choice == 1:
    print("Adding two numbers")
elif choice == 2:
    print("Subtracting two numbers")
elif choice == 3:
    print("Multiplying two numbers")