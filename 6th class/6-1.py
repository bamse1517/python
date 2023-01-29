# 삼각형 면적을 구하는 코드
# width = 10
# height = 5
# area = width * height / 2
# print(f"삼각형의 면적은 {area} 입니다.")

# 도형 면적을 구하는 코드
width = int(input("너비를 입력하세요: "))
height = int(input("높이를 입력하세요: "))
figure = input("삼각형 또는 사각형을 입력하세요: ")

if figure == "삼각형":
  area = width * height / 2
elif figure == "사각형":
  area = width * height
else:
  area = 0

if area != 0:
  print(f"{figure}의 면적은 {area} 입니다.")
else:
  print("다시 입력하세요.")