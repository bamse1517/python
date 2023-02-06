# # 파일 내용 추가
# my_todo = open('todo.txt', 'a')
# my_todo.write("\n일기쓰기")
# my_todo.write("\n운동하기")
# my_todo.close()

# # 새로운 파일 만들기
# my_wish = open("wish.txt", "w")
# my_wish.write("아이슬란드 오로라 보기\n")
# my_wish.write("남극 펭귄 보기\n")
# my_wish.write("아프리카 사자 보기\n")
# my_wish.close()

# # 사람의 실수를 줄이기
# # 파일 닫기를 실수로 빼먹는다면?
# # with 문으로 실수를 미리 차단해 봅시다.
# # with expression [as variable]:
# #     block

# # 새로운 파일 만들기 - with문
# with open("wish_1.txt", "w") as my_wish:
#   my_wish.write("아이슬란드 오로라 보기\n")
#   my_wish.write("남극 펭귄 보기\n")
#   my_wish.write("아프리카 사자 보기\n")

# # 파일 내용 랜덤 뽑기
# import random

# my_wish = open("wish.txt", "r")
# my_wish_list = my_wish.readlines()
# my_wish.close()

# random_num = random.randint(0, len(my_wish_list)-1)
# print(my_wish_list[random_num])

# # 파일 내용 랜덤 뽑기 - with문
# import random

# with open("wish.txt", "r") as my_wish:
#   my_wish_list = my_wish.readlines()

# random_num = random.randint(0, len(my_wish_list)-1)
# print(my_wish_list[random_num])

# # 파일 복사하기
# old_file = open("wish.txt", "r")
# new_file = open("wish_new.txt", "w")

# old_list = old_file.readlines()
# for i in old_list:
#   new_file.write(i)

# old_file.close()
# new_file.close()

# # 파일 복사하기 - with문
# with open("wish.txt", "r") as old_file:
#   old_list = old_file.readlines()

# with open("wish_new_1.txt", "w") as new_file:
#   for i in old_list:
#     new_file.write(i)

# # 파일 복사하기 - writelines()
# old_file = open("wish.txt", "r")
# new_file = open("wish_new_2.txt", "w")

# old_list = old_file.readlines()
# new_file.writelines(old_list)

# old_file.close()
# new_file.close()

# 파일 복사하기 - writelines() & with문
with open("wish.txt", "r") as old_file:
  old_list = old_file.readlines()

with open("wish_new_1.txt", "w") as new_file:
  new_file.writelines(old_list)