# # 민수는 청소년인가?
# age = 20
# print(9 <= age)
# print(age <= 23)

# age = 20
# (9 <= age) and (age <= 23)

# # 암산하기
# print("3 * 5 = 15?")
# 3 * 5 == 14

# # 3의 배수인가?
# x = 10
# x % 3 == 0

# # 3과 5의 공배수인가?
# x = 9
# (x % 3 == 0) and (x % 5 == 0)

# # 민수는 청소년인가?
# age = 50

# if (9 <= age) and (age <= 24):
#   print("청소년입니다.")

# # 입력한 숫자는 3의 배수인가?
# x = int(input("x 값을 입력하세요: "))

# if x % 3 == 0:
#   print("3의 배수입니다!")

# # 어떤 숫자가 더 클까?
# #if문
# x = int(input("x 값을 입력하세요:"))
# y = int(input("y 값을 입력하세요:"))

# if x > y:
#   print(f"{x}가 {y}보다 더 큽니다.")

# # 암산하기
# import random

# num_1, num_2 = random.randint(1, 10), random.randint(1, 10)
# result = num_1 * num_2
# input_result = int(input(f"{num_1} * {num_2} = "))

# if result == input_result:
#   print("정답입니다!")

# # 민수는 청소년인가?
# age = 20
# if (9 <= age) and (age <= 24):
#   print("청소년 입니다.")
# else:
#   print("청소년이 아닙니다.")

# # 입력한 숫자는 3또는 5의 배수인가?
# x = int(input("x 값을 입력하세요: "))

# if (x % 3 == 0) or (x % 5 == 0):
#   print("3또는 5의 배수입니다!")
# else:
#   print("3또는 5의 배수가 아닙니다!")

# 암산하기
import random

num_1, num_2 = random.randint(1, 10), random.randint(1, 10)
result = int(input(f"{num_1} * {num_2} = "))

if result == num_1 * num_2:
  print("정답입니다!")
else:
  print("오답입니다!")