# # 나연이의 정보
# name = '이나연'
# age = 20
# height = 170
# weight = 50
# gender = '여성'
# location = '서울'
# user_id = 'nayeoni@abc.d.y'
# user_pw = '1234'
# test_1 = 57
# test_2 = 65

# # 나연이는 여성인가요?
# gender == '여성'

# # 나연이는 김씨 인가요?
# name[0] == '김'

# # 나연이는 서울에 살면서 키가 160 이상인가요?
# (location == '서울') and (height >= 160)

# # 나연이는 대한민국의 청년인가요?
# # 청년은 19세 이상, 34세 이하
# (age >= 19) and (age <= 34)

# # 나연이는 과체중인가요?
# # bmi 계산은 자신의 몸무게(kg)를 키(m)의 제곱으로 나누는 것
# # bmi 가 18.5 이하면 저체중 / 18.5 ~ 22.9 사이면 정상 / 23.0 ~ 24.9 사이면 과체중 / 25.0 이상은 비만

# bmi = weight / (height / 100) ** 2
# (bmi >= 23.0) and (bmi <= 24.9)

# # 나연이가 본 시험의 평균 점수가 60점 미만인가요?
# test_mean = (test_1 + test_2) / 2
# test_mean < 60

# # 나연이가 본 시험 점수 중 60점 이상이 있나요?
# (test_1 >= 60) or (test_2 >= 60)

# # 나연이 id는 이메일 형식이 맞나요?
# user_id.find('@') > 0

# # 나연이가 로그인 했나요?
# input_id = input("id: ")
# input_pw = input("pw: ")
# (user_id == input_id) and (user_pw == input_pw)

# #좌표평면에서 점의 위치 판단하기

# # (2, 2)는 1사분면(+, +) 인가요? 
# x, y = 2, 2
# x > 0 and y > 0

# # (-3, 2)는 3사분면(-, -) 인가요? 
# x, y = -3, 2
# x < 0 and y < 0

# # (-2, -2)는 1사분면(+, +) 또는 3사분면(-, -) 인가요? 
# x, y = -2, -2
# #(x > 0 and y > 0) or (x < 0 and y < 0)
# x * y > 0

# # 2004년도는 윤년인가요?
# year = 2004
# year % 4 == 0 and year % 100 != 0 or year % 400 == 0

# 2010년 21세기 인가요? 
import math
year = 2010
math.trunc(year / 100 + 1) == 21