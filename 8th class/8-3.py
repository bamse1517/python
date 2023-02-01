# 리스트가 저장된 메모리 위치 확인
pl_list = ['python', 'java', 'c']
print(pl_list)
print(id(pl_list))
print(id(pl_list[0]))

# 리스트의 데이터 변경 후 메모리 위치 확인
print(pl_list)
pl_list.remove('java')
pl_list.append('javascript')
print(pl_list)
print(id(pl_list))
print(id(pl_list[-1]))
print(id(pl_list[0]))

# 튜플이 저장된 메모리 위치 확인
pl_tuple = ('python', 'java', 'c')
print(pl_tuple)
print(id(pl_tuple))
print(id(pl_tuple[0]))

# 튜플에 저장된 데이터 변경 시도
print(pl_tuple)
# pl_tuple.remove('java')
pl_tuple.append('javascript')

pl_tuple = ('python', 'c', 'javascript')
print(pl_tuple)
print(id(pl_tuple))

# 0부터 9사이의 홀수 값을 튜플로 저장하기
a = (1, 3, 5, 7, 9)
print(a)
print(type(a))

# 0부터 9사이의 홀수 값을 튜플로 저장하기 - 튜플 표현식
b = tuple(i for i in range(10) if i % 2 != 0)
print(b)
print(type(b))

# 튜플의 최대, 최소, 합 계산
print(max(b) + min(b))
print(sum(b))

# 튜플을 리스트로 변환하기
c = list(b)
print(c)
print(type(c))
c.append(11)
print(c)

# 리스트를 튜플로 변환하기
d = tuple(c)
print(d)
print(type(d))

# 리스트로 메뉴와 가격 정보 저장하기
menus = ["김치찌개", "김밥", "떡국", "칼국수", "냉면", "떡볶이"]
prices = [6000, 3000, 5000, 5000, 6000, 3000]
print(menus)
print(prices)

# 메뉴에 따른 가격 출력하기 - 리스트
print(prices[1])
print(prices[menus.index("김밥")])

# 딕셔너리로 메뉴와 가격 정보 저장하기
menus = {"김치찌개": "6000", 
         "김밥": "3000", 
         "떡국": "5000", 
         "칼국수": "5000", 
         "냉면": "6000", 
         "떡볶이": "3000"}
print(menus)
print(menus["김밥"])

# 사람 정보를 딕셔너리로 저장하기
person = {"name": "김이준",
          "age": 20,
          "gender": "남성"}
print(person)
print(person["age"])

# 딕셔너리에 새로운 데이터 추가
person["혈액형"] = "B"
person["거주지"] = "서울"
print(person)

# 딕셔너리에 기존 데이터 변경 및 검색
blood = {"ABO": "B",
         "Rh": "+"}
person["혈액형"] = blood
print(person)
print(person["혈액형"]["Rh"])

# 딕셔너리의 모든 키 출력
for i in person:
  print(i)

# 딕셔너리의 모든 값 출력
for i in person:
  print(person[i])