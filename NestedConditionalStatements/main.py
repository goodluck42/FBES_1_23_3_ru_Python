# arithmetic
# +, -, /, *, **, //, %

# assignment
# =
# shorthand operators
# +=, +=, -=, /=, *=, **=, //=, %=

# logical
# and, or, not

# comparison

# >, <, >=, <=, ==, !=

# Unary (1): not, -, +, ~
# Binary (2):
# Ternary (3):

# a = 42
# b = True
#
# print(a, b)
# print(not a)
#
# if 1 and "" or 0:
#     print("First")
# elif 1:
#     print("Second")
# elif " ":
#     print("Third")
#
# # int, float, bool, str
#
# a = 42.13
# b = str(a)  # "42.13"
#
# print(type(a))
# print(type(b))
# print(b)

# print("1. Start")
# print("2. Settings")
# print("3. Exit")
#
# choice = int(input("-> "))
#
# if choice == 1:
#     print("Starting...")
# elif choice == 2:
#     print("1. Audio settings")
#     print("2. Video settings")
#     print("3. Monitor settings")
#
#     settings_choice = int(input("Select setting -> "))
#
#     if settings_choice == 1:
#         print("Audio settings changed")
#     elif settings_choice == 2:
#         print("Video settings changed")
#     elif settings_choice == 3:
#         print("Monitor settings changed")
#     else:
#         print("Incorrect action!")
# elif choice == 3:
#     print("Exit...")
# else:
#     print("Incorrect action!")


# declaration

a = None

# definition

text = None

value = 41

if value % 2 == 0:
    text = "even"

if text is None:  # text == None
    print("text is None")

print(text)


# val = 15
#
# if val // 3 == 0:
#     print("OK")

val = 300

percent = val * 0.08

print(percent)

m1 = 400
m2 = 200
m3 = 300


if m1 > (m2 + m3) / 2:
    print("m1 is top")

if m3 > (m2 + m1) / 2:
    print("m3 is top")

if m2 > (m1 + m3) / 2:
    print("m2 is top")



secs = 121

mins = secs // 60

print(mins)

if secs % 60 >= 1:
    mins += 1

print(mins * 0.03, "AZN")