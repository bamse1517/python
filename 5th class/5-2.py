# print(type(True))
# print(type(False))

# print(bool(1))
# print(bool(0))
# print(bool(''))
# print(bool('python'))
# print(bool(None))

# # and
# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)

# # or
# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)

# print(not True)
# print(not False)

# not True and False or not False

# ((not True) and False) or (not False)

# print("python" == "Python")
# print("python" == "python")
# print("python" != "hello")

# # 나는 대한민국 청년인가 아닌가? (나이가 34세 이하라면)
# age = int(input("나이를 입력하세요: "))
# print(age <= 34)

# # 나는 대한민국 청년인가 아닌가? (나이가 34세 이하라면) (나이가 19세 이상이라면)
# age = int(input("나이를 입력하세요: "))
# print(age <= 34)
# print(age >= 19)

# # 나는 대한민국 청년인가 아닌가?
# age = int(input("나이를 입력하세요: "))
# print(19 <= age <= 34)

# # 나는 대한민국 청년인가 아닌가?
# age = int(input("나이를 입력하세요: "))
# print((age <= 34) and (age >= 19))

# # 입력한 숫자가 홀수인가요?
# num = int(input("숫자를 입력하세요: "))
# print(num % 2 == 1)

num_1 = 1
num_2 = 1.0
num_3 = num_1
print(num_1 == num_2)
print(num_1 is num_3)
print(num_1 is num_2)
print(num_1 is not num_2)
print(id(num_1))
print(id(num_2))
print(id(num_3))
