# #@title 어떤 숫자가 더 클까?
# # 중첩 if문
# x = int(input("x 값을 입력하세요:"))
# y = int(input("y 값을 입력하세요:"))

# if x == y:
#   print(f"{x}와 {y}는 똑같습니다.")
# else:
#   if x > y:
#     print(f"{x}는 {y}보다 더 큽니다.")
#   else:
#     print(f"{y}는 {x}보다 더 큽니다.")

# #@title 어떤 숫자가 더 클까?
# x = int(input("x 값을 입력하세요:"))
# y = int(input("y 값을 입력하세요:"))

# if x == y:
#   print(f"{x}와 {y}는 똑같습니다.")
# elif x > y:
#   print(f"{x}는 {y}보다 더 큽니다.")
# else:
#   print(f"{y}는 {x}보다 더 큽니다.") 

# #@title 민수는 청소년 또는 청년인가?
# age = 20

# if (9 <= age) and (age <= 24):
#   print("청소년입니다.")
# elif (19 <= age) and (age <= 34):
#   print("청년입니다.")
# else:
#   print("청소년 또는 청년이 아닙니다.")

# #@title 민수는 청소년 또는 청년인가?
# age = 20

# if 9 <= age <= 18:
#   print("청소년입니다.")
# elif 19 <= age <= 24:
#   print("청소년 이면서 청년 입니다.")
# elif 25 <= age <= 34:
#   print("청년입니다.")
# else:
#   print("청소년 또는 청년이 아닙니다.")

# #@title 음료 주문하기
# print("메뉴: 커피, 녹차, 주스, 물")
# order = input("음료를 주문하세요: ")

# if order == "커피":
#   print("커피는 2,500원 입니다.")
# elif order == "녹차":
#   print("녹차는 3,000원 입니다.")
# elif order == "주스":
#   print("주스는 3,500원 입니다.")
# elif order == "물":
#   print("물은 2,000원 입니다.")
# else:
#   print("주문 가능한 메뉴가 아닙니다.")

age_str, temp_str = input("나이와 현재 온도를 입력하세요: ").split()
age, temp = int(age_str), float(temp_str)
result = ''

if age <= 2:
  if 36.4 <= temp <= 38.0:
    result = "정상 체온"
  else:
    result = "비정상 체온"
elif age <= 10:
  if 36.1 <= temp <= 37.8:
    result = "정상 체온"
  else:
    result = "비정상 체온"
elif age <= 64:
  if 35.9 <= temp <= 37.6:
    result = "정상 체온"
  else:
    result = "비정상 체온"
else:
  if 35.8 <= temp <= 37.5:
    result = "정상 체온"
  else:
    result = "비정상 체온"


print(f"{age}세, {temp}도는 {result}입니다.")