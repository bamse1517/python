# # 1. 로또 번호 자동 생성하는 함수
# import random

# rand_num = random.randint(1, 45)
# print(rand_num)

# # 1. 로또 번호 자동 생성하는 함수
# import random

# lotto_list = []
# rand_num = random.randint(1, 45)
# lotto_list.append(rand_num)
# rand_num = random.randint(1, 45)
# lotto_list.append(rand_num)
# rand_num = random.randint(1, 45)
# lotto_list.append(rand_num)
# rand_num = random.randint(1, 45)
# lotto_list.append(rand_num)
# rand_num = random.randint(1, 45)
# lotto_list.append(rand_num)
# rand_num = random.randint(1, 45)
# lotto_list.append(rand_num)
# print(lotto_list)

# # 1. 로또 번호 자동 생성하는 함수
# import random

# lotto_list = []
# for i in range(6):
#   rand_num = random.randint(1, 45)
#   lotto_list.append(rand_num)

# print(lotto_list)

# # 1. 로또 번호 자동 생성하는 함수
# import random

# def lotto_num_gen():
#   lotto_list = []
#   while len(lotto_list) < 6:
#     rand_num = random.randint(1, 45)
#     if rand_num not in lotto_list:
#       lotto_list.append(rand_num)
#   lotto_list.sort()
#   return lotto_list

# print(lotto_num_gen())

# # 2. 내가 선택한 번호를 저장하는 함수

# input_list = []

# while len(input_list) < 6:
#   input_num = int(input())
#   if input_num in input_list:
#     print("중복된 번호입니다. 다시 입력하세요.")
#     continue
#   input_list.append(input_num)
#   print(f"현재까지 입력한 번호: {input_list}")

# input_list.sort()

# print(input_list)

# # 2. 내가 선택한 번호를 저장하는 함수

# def user_input_list():
#   input_list = []
#   while len(input_list) < 6:
#     input_num = int(input())
#     if input_num in input_list:
#       print("중복된 번호입니다. 다시 입력하세요.")
#       continue
#     input_list.append(input_num)
#     print(f"현재까지 입력한 번호: {input_list}")
#   input_list.sort()
#   print(f"최종 입력된 번호: {input_list}")
#   return input_list

# print(user_input_list())

# 3. 두 개의 리스트를 입력받아 몇 개의 항목이 일치하는지를 알려주는 함수
def compare_two_list(list_1, list_2):
  count = 0
  for i in list_2:
    if i in list_1:
      count = count + 1
  return count 

alist = [1, 2, 3]
blist = [2, 3, 4]
print(compare_two_list(alist, blist))

import random

def lotto_num_gen():
  print("----로또 번호 생성을 시작합니다.----")
  lotto_list = []
  while len(lotto_list) < 6:
    rand_num = random.randint(1, 45)
    if rand_num not in lotto_list:
      lotto_list.append(rand_num)
  lotto_list.sort()
  print("----로또 번호 생성을 종료합니다.----")
  return lotto_list

def user_input_list():
  print("----번호 입력을 시작합니다.----")
  input_list = []
  while len(input_list) < 6:
    input_num = int(input())
    if input_num in input_list:
      print("중복된 번호입니다. 다시 입력하세요.")
      continue
    input_list.append(input_num)
    print(f"현재까지 입력한 번호: {input_list}")
  input_list.sort()
  print("----번호 입력을 종료합니다.----")
  return input_list

def compare_two_list(list_1, list_2):
  print("----비교를 시작합니다.----")
  count = 0
  for i in list_2:
    if i in list_1:
      count = count + 1
  print("----비교를 종료합니다.----")
  return count 

# 메인함수
new_lotto_list = lotto_num_gen()
new_input_list = user_input_list()
new_count = compare_two_list(new_lotto_list, new_input_list)
print(f"입력한 번호는 {new_input_list}, \n로또 번호는 {new_lotto_list}, \n{new_count}개 일치합니다.")