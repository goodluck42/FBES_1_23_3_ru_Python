# n = int(input())


# FOR VARIANT
# for i in range(1, 10 + 1):
# 	print(n, "*", i, "=", n * i)


#### WHILE VARIANT
# i = 1
# while i <= 10:
# 	# print(n, "*", i, "=", n * i)
# 	print(f"{n} * {i} = {n * i}")
# 	i += 1

#######################

# begin = int(input("Enter begin -> "))
# end = int(input("Enter end -> "))

# for i in range(begin, end + 1):
# 	for j in range(1, 10 + 1):
# 		print(f"{i} * {j} = {i * j}")
# 	print("-" * 10)

# i = begin
#
# while i <= end:
# 	j = 1
#
# 	while j <= 10:
# 		print(f"{i} * {j} = {i * j}")
# 		j += 1
# 	i += 1
###########################################
#i = 0

# i = 3
# j = 4

# break_required = False
#
# while i < 5:  # i = 1
# 	j = 0     # j = 0
#
# 	while j < 5:
# 		if i == 3 and j == 2:
# 			break_required = True
# 			break
# 		print(f"i = {i}; j = {j}")
# 		j += 1
# 	i += 1
#
# 	if break_required:
# 		break
#############################
# for i in range(5):
# 	for j in range(5):
# 		if i >= 1 and i <= 3 and j >= 1 and j <= 3:
# 			print("  ", end="")
# 		else:
# 			print("* ", end="")
# 	print()


for _ in range(0):
    for _ in range(0):  # spaces
        pass
    for _ in range(0):  # stars
        pass
