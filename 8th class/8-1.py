# # 사람의 정보를 이름, 나이, 성별 3가지의 데이터로 저장하기 위한 코드
# name = "김이준"
# age = 20
# gender = "남성"

# print(name)
# print(age)
# print(gender)

# # 또 다른 사람의 정보를 이름, 나이, 성별 3가지의 데이터로 저장하기 위한 코드
# name1 = "이서아"
# age1 = 21
# gender1 = "여성"

# print(name1)
# print(age1)
# print(gender1)

# 리스트로 3가지의 데이터 저장하는 코드
person = ["김이준", 20, "남성"]
print(person)

print(person[0])
print(person[1])
print(person[2])

# 리스트에 데이터 추가 append()
person = ["김이준", 20, "남성"]
person.append("B")
person.append("서울")
print(person)

# 리스트의 마지막 데이터 출력
print(person[4])
print(person[-1])

# 이름과 나이만 출력
print(person)
print(person[0:2])
print(person[:2])

# 혈액형과 거주지만 출력
print(person)
print(person[3:4+1])
print(person[-2:])

# 리스트에 데이터 추가 insert()
print(person)
person.insert(2, 180)
print(person)
