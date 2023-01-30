# # 1부터 100까지 숫자 출력 (for)
# for i in range(1, 100 + 1):
#   print(i, end=' ')

# # 1부터 100까지 숫자 출력 (while)
# i = 1
# while (i < 101):
# # 표
#   i = i + 1

# # 1부터 무한대 숫자 출력하기
# n = 1

# while True:
#   print(n, end=' ')
#   n = n + 1

# # 코드를 무한으로 실행하기
# i = 1
# while (i <= 100):
#   print(i, end=' ')

# # 입력한 숫자 만큼 별 출력하기
# while True:
#   num = int(input("출력할 별 갯수: "))
#   if num == 0:    
#     break
#   for i in range(num):
#     print("*", end='')
#   print("\n프로그램을 종료하고 싶으면 0을 입력하세요.")

# print("프로그램을 종료합니다.")

# # 1부터 100까지 숫자 중에서 5의 배수를 제외하고 출력하기(for)
# mul_num = 5
# count = 0

# for i in range(1, 100 + 1):
#   if i % mul_num == 0:
#     continue
#   print(i, end=' ')
#   count += 1

# print(f"\n1부터 100까지 숫자 중 {mul_num}의 배수를 제외한 숫자는 {count}개 입니다.")

# 1부터 100까지 숫자 중에서 5의 배수를 제외하고 출력하기(while)
mul_num = 5
count = 0

i = 1
while i < 101:
  if i % mul_num == 0:
    i += 1
    continue
  print(i, end=' ')
  count += 1
  i += 1
  
print(f"\n1부터 100까지 숫자 중 {mul_num}의 배수를 제외한 숫자는 {count}개 입니다.")