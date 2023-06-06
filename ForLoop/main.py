

# 0 1 2 3 4
# i = 0
# while i < 5:
# 	if i == 3:
# 		i += 1
# 		continue
# 	print("Hello")
# 	i += 1
########################################
# begin = int(input("Begin -> "))
# end = int(input("End -> "))

# my_range = range(5)  # 0 1 2 3 4
# my_range = range(begin, end + 1)  # 10, 11, 12
# my_range = range(10, 2, -1)  # 10, 11, 12

# print(list(my_range))
###########################

# i = 0
#
# while i < 5:
# 	print(i)
# 	i += 1


###########################
# my_range = range(0, 5)  # 0 1 2 3 4
#
# for i in my_range:
# 	i += 100
# 	print(i)
#
# # 100, 101, 102, 103, 104
#
# for i in my_range:
# 	print(i)
##########################
# int, float, bool, str - immutable

# a = 10
# b = a
#
# a = 42
# b = a
#
# print(b)

# my_list = [10, 15, 20, 30]
#
# for i in range(0, 10):
# 	print(i)

# a = 5
# b = 6
# temp = a
# a = b
# b = temp
#
# print(a, b)
#
# a = 0.5


print(0.1 + 0.2)


x = 1.0

print(11 / 1)

x = 10

while True:
	if x == 1:
		break

	if x == 5 or 4 or 3:
		x -= 1
		continue

	print(x)
	x -= 1