#    i =   0   1   2   3
# my_list = [10, 20, 42, 13]
#
# my_list[2] = 105
from builtins import input

# for item in my_list:
#     print(item)

# print('#####')

## for i in range(4):  # 0 1 2 3
# for i in range(len(my_list)):
#     print(i, my_list[i])

# print('#####')
#
# i = 0
# length = len(my_list)
#
# while i < length:
#     print(i, my_list[i])
#     i += 1
##############################################

# int, float, bool, char, str - immutable (неизменяемые)
# list - mutable (изменяемые)


# a = 42
# b = a
#
# a = 10
#
# print(a, b)
################# immutability
# a = 42
#
# print(hex(id(a)))
#
# a = 90
#
# print(hex(id(a)))
#
# a = 42
#
# print(hex(id(a)))


############# str immutability


# s = "Python"
# s1 = "Python"
#
# print(hex(id(s)))
# print(hex(id(s1)))
#
# s += '!'
#
# print(hex(id(s)))

## list mutability

# l1 = []
# l2 = l1
#
# print(hex(id(l1)))
# print(hex(id(l2)))
#
# l2.append(10)
# l2.append(20)
# l2.append(30)
#
# print(l1)
# print(l2)

## list mutability №2

# l1 = []
#
# print(hex(id(l1)))
#
# l1.append(10)
# l1.append(20)
# l1.append(20)
# l1.append(30)
#
# print(hex(id(l1)))


## mutability list №2

# l1 = []
#
# print(hex(id(l1)))
#
# l1 = []
#
# print(hex(id(l1)))


######################### METHODS

## insert
# my_list = [10, 42, 13]
#
# my_list.insert(0, 450)
# my_list.insert(2, 80)
#
# print(my_list)

## pop

# products = ["Water", "Tomato", "Bread", "Cucumber", "Cherry"]
# # 0 1 2 3
# products.pop(0)  # ["Tomato", "Bread", "Cucumber", "Cherry"]
# products.pop(1)  # ["Tomato", "Cucumber", "Cherry"]
# products.pop(2)  # ["Tomato", "Cucumber"]
#
# print(products)

## remove

# products = ["Cucumber", "Water", "Tomato", "Cucumber", "Bread", "Cherry", "Oil"]
#
# if "Oil" not in products:
#     print("Oil is not in list")
# else:
#     products.remove("Oil")
#
# print(products)

## clear

# products = ["Cucumber", "Water", "Tomato", "Cucumber", "Bread", "Cherry", "Oil"]
#
# products.clear()
#
# print(products)

## count

# products = ["Cucumber", "Water", "Tomato", "Cucumber", "Bread", "Cherry", "Oil"]
#
# cnt = products.count("Mushroom")
#
# print(cnt)

## extend

# products_stock = ["Cucumber", "Water", "Tomato"]
# products_delivered = ["Mushroom", "Limonade", "Cheese"]
#
# products_stock.extend(products_delivered)
#
# print(id(products_stock))
# print(id(products_delivered))
#
# print(products_stock)

## operator +

# products_stock = ["Cucumber", "Water", "Tomato"]
# products_delivered = ["Mushroom", "Limonade", "Cheese"]
#
# products = products_stock + products_delivered
#
# print(id(products_stock))
# print(id(products_delivered))
# print(id(products))

# print(products)


## sort

# prices = [10, 90, 13, 42, 11, 16]
#
# sort_by = int(input("Enter 1 for ascending; 2 for descending. ->"))
#
# if sort_by == 1:
#     prices.sort()
# elif sort_by == 2:
#     prices.sort(reverse=True)
#
#
# print(prices)

## copy

# a = [10, 20, 30]
# b = a.copy()
#
# b.append(-1)
#
# print("a =", a)
# print("b =", b)

## reverse

a = [10, 90, 16, 13, 42]

a.reverse()

print(a)
