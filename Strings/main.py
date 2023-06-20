#    012345
s = "Python is the best language for AI"



# s_len = len(s)
#
# print(s[s_len - 1])
# print(s[-1])
# print(s[5])

## slices
# word = s[:6]
# word2 = s[19:27]
# word3 = s[-2:]
# word4 = s[:]
#
# print(word)
# print(word2)
# print(word3)
# print(word4)


## methods

## replace
# s = s.replace("Python", "C++")
# s = s.replace("AI", "gamedev")
#
# print(s)

## index

# text = input()
#
# if text in s:
#     idx = s.index(text)
#     print(idx)
# else:
#     print(f"'{text}' not found")

## find & rfind

# text = input()
#
# idx = s.find(text)
#
# if idx == -1:
#     print(f"'{text}' not found")
# else:
#     print(idx)


## count

# cnt = s.count('a')
#
# print(cnt)

## is methods

## isnumeric & isdigit

# text = "42"

# if text.isnumeric():
#     print(f"'{text}' is numeric")
# else:
#     print(f"'{text}' is not numeric")

## isascii

# text = "C++"  # 67 43 43

# for i in text:
#     print(ord(i))

# if text.isascii():
#     print(f"'{text}' is ascii")
# else:
#     print(f"'{text}' is not ascii")

# c = chr(67)

# print(code)

## isalpha

# text = "hello"
#
# if text.isalpha():
#     print(f"'{text}' is isalpha")
# else:
#     print(f"'{text}' is not isalpha")


## isalnum

# text = "hello123"
#
# if text.isalnum():
#     print(f"'{text}' is isalnum")
# else:
#     print(f"'{text}' is not isalnum")

## lower & upper

# text = "Python!"
#
# text = text.lower()
# # text = text.upper()
#
# print(text)
#
# c = chr(97 - 32)
# print(c)

## split & join

##  ["Python", "is", "the", "best", "language", "for", "AI"]
# print(s)
# words = s.split(' ')
#
# words_len = len(words)
# print(f"len = {words_len}")
# print(words)
#
# text = '|'.join(words)
#
# print(text)

## startswith & endswith

# print(s)
#
# if s.startswith("Python"):
#     print("starts with")
# else:
#     print("not starts with")
#
# if s.endswith("I"):
#     print("ends with")
# else:
#     print("not ends with")


## Escape sequences

print("C\nC++\nC#")
print("\\n")
print("\\\\\\\\")

print("C++\tC#")

print("C++\b\b")

print("Python is the \"best\" lang")