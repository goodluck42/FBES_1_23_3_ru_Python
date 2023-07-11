# my_dict = {
#     "name": "Alex",
#     "surname": "my_surname",
#     "age": 22
# }
#
# my_dict["name"] = "Fuad"
#
# # my_dict.pop("name")
#
# for key, value in my_dict.items():
#     print(f"{key}: {value}")
# def fn(*args):
#     for item in args:
#         print(item)
#     pass
#
#
# fn(10, 20)

## list generators
# from random import randint
#
# values = [randint(0, 100) for _ in range(10)]
#
# evens = [item for item in values if item % 2 == 0]
#
# print(values)
# print(evens)

###
# r - read
# w - write (creates file if not exists) (+truncate)
# a - append
# r+ - read & write
# w+ - write & read (+truncate)
# a+ - append & read


## file write
# fd = open("data.txt", 'w')
#
# fd.write("Hello C++!\n")
# fd.write("Hello Python!\n")
#
# names = ["John", "Rick", "Josh", "Alan"]
# ## variant1
# # names = [item + '\n' for item in names]
#
# ## variant2
# for i in range(len(names)):
#     names[i] += '\n'
#
# fd.writelines(names)
#
# fd.close()

## file read

# fd = open("data.txt", 'r')
#
# word1 = fd.read(5)
# fd.read(1)
# word2 = fd.read(5)
#
# line = fd.readline(3)
# # line2 = fd.readline()
#
# print(word1)
# print(word2, end='')
# print(line)
# # print(line2, end='')
#
# fd.seek(0)
#
# lines = fd.readlines()
#
# print(*'-' * 10)
#
# print(lines)
#
# fd.close()

## file append

# fd = open("data.txt", 'a')
#
# fd.write("Paul\n")
#
# fd.close()

## write dict

# item = {
#     "name": "Bread",
#     "price": 0.5
# }
#
# fd = open("items.txt", 'w')
#
# for key, value in item.items():
#     fd.write(key)
#     fd.write('\n')
#     fd.write(str(value))
#     fd.write('\n')
#
# fd.close()

## read dict


# item = {}
# fd = open("items.txt", 'r')
#
# lines = fd.readlines()
# length = len(lines)
#
# for i in range(length):
#     lines[i] = lines[i].replace('\n', '')
#
#
# for i in range(length):
#     if i % 2 == 0:
#         item[lines[i]] = lines[i + 1]
#
# print(item)
#
#
# fd.close()


## json

import json

## write json
#
# items = []
#
# items.append({
#     "name": "Beer",
#     "price": 0.5,
#     "categories": ["Alco", "Drink", "Sparkling"]
# })
#
# items.append({
#     "name": "Prawns",
#     "price": 12,
#     "categories": ["Seafood", "Frozen"]
# })
#
# fd = open("items.json", 'w')
#
# json.dump(items, fd, indent=True)
#
# fd.close()


## read json

fd = open("items.json", 'r')

items = json.load(fd)

print(items)

fd.close()
