# # 1부터 100까지 숫자 출력
# for i in range(1, 100 + 1, 1):
#   print(i, end=' ')

# # 1부터 100까지 숫자 중 짝수의 갯수
# count = 0

# for i in range(1, 100 + 1, 1):
#   if i % 2 == 0:
#     print(i, end=' ')
#     count = count + 1

# print(f"\n1부터 100까지 숫자 중 짝수는 {count}개 입니다.")

# # 1부터 100까지 숫자 중 n 배수의 갯수
# mul_num = int(input("multiple: "))
# count = 0

# for i in range(1, 100 + 1, 1):
#   if i % mul_num == 0:
#     print(i, end=' ')
#     count = count + 1

# print(f"\n1부터 100까지 숫자 중 {mul_num}의 배수는 {count}개 입니다.")

# # 문자 데이터에서 대문자와 소문자 갯수
# word = 'Hello Python!'
# upper_letter_num = 0
# lower_letter_num = 0

# for c in word:
#   if c.isupper():
#     upper_letter_num += 1
#     print("upper:" + c)
#   if c.islower():
#     lower_letter_num += 1
#     print("lower:" + c)  

# print(f"입력한 문자열 {word} 에서 대문자는 {upper_letter_num}개 이고, 소문자는 {lower_letter_num}개 입니다.")


# import random

# print("lotto number: ", end='')
# print(random.randint(1, 45), end=', ')
# print(random.randint(1, 45), end=', ')
# print(random.randint(1, 45), end=', ')
# print(random.randint(1, 45), end=', ')
# print(random.randint(1, 45), end=', ')
# print(random.randint(1, 45))


# import random

# print("lotto number: ", end='')

# for i in range(5):
#   print(random.randint(1, 45), end=', ')

# print(random.randint(1, 45))


# import random

# print("lotto number: ", end='')

# for i in range(6):
#   print(random.randint(1, 45), end='')
#   if i != 5:
#     print(', ', end='')


# # 반복 구조를 사용하지 않고 작성한 프로그램
# pre_word = input("단어를 입력하세요: ")
# post_word = ''

# post_word = post_word + pre_word[5]
# post_word = post_word + pre_word[4]
# post_word = post_word + pre_word[3]
# post_word = post_word + pre_word[2]
# post_word = post_word + pre_word[1]
# post_word = post_word + pre_word[0]

# print(f"거꾸로 출력한 단어: {post_word}")

# # 반복 구조를 사용한 프로그램
# pre_word = input("단어를 입력하세요: ")
# post_word = ''

# for i in range(5, 0 - 1, -1):
#   post_word = post_word + pre_word[i]
#   print(i)

# print(f"거꾸로 출력한 단어: {post_word}")

# 다양한 길이의 단어를 모두 대응하는 프로그램
pre_word = input("단어를 입력하세요: ")
post_word = ''

for i in range(len(pre_word) - 1, 0 - 1, -1):
  post_word = post_word + pre_word[i]
  print(i)

print(f"거꾸로 출력한 단어: {post_word}")