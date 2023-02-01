# # 리스트에 데이터 삭제 remove()
# person = ["김이준", 20, "남성"]
# person.append("B")
# person.append("서울")
# person.insert(2, 180)
# print(person)
# person.remove("B")
# print(person)
# blood = ["B", "+"]
# person.insert(4, blood)
# print(person)

# # 혈액형 데이터 출력하기
# person[4]

# # 혈액형 데이터 중 Rh 데이터 출력하기
# person[4][1]

# 메뉴 및 가격 정보를 리스트로 저장하기
menus = ["김치찌개", "김밥", "떡국", "칼국수", "냉면", "떡볶이"]
prices = [6000, 3000, 5000, 5000, 6000, 3000]
print(menus)
print(prices)

# 리스트의 위치값 찾기 index()
menus.index("김밥")

# 김밥의 위치값과 동일한 위치의 가격 출력하기
prices[menus.index("김밥")]

# 리스트 항목 갯수(길이) len()
len(menus)

# 리스트의 특정 항목의 갯수 세기 count()
prices.count(5000)

# 메뉴 및 가격 정보 저장하기
menus = ["김치찌개", "김밥", "떡국", "칼국수", "냉면", "떡볶이"]
prices = [6000, 3000, 5000, 5000, 6000, 3000]

# input() 함수를 이용하여 음식 이름과 가격 추가
menu = input("음식 이름을 입력하세요: ")
price = int(input("해당 음식의 가격을 입력하세요: "))

# 입력한 정보 출력
print(f"입력한 음식은 {menu}, 가격은 {price}원 입니다.")

# 입력한 메뉴와 가격을 리스트에 추가
menus.append(menu)
prices.append(price)

# 전체 리스트 출력
print(menus)
print(prices)

# 현재 메뉴 정보 출력하기
print(menus)

# 가격을 알고 싶은 메뉴 이름 입력하기
menu = input("메뉴 이름을 입력하세요: ")

# 입력한 메뉴의 가격을 찾아서 출력하기
price = prices[menus.index(menu)]
print(f"{menu}의 가격은 {price}원 입니다.")

# 현재 메뉴 및 가격 정보 출력하기
print(menus)
print(prices)

# 삭제할 메뉴 입력받고 해당 가격 출력하기
menu = input("삭제할 음식 이름을 입력하세요: ")
price = prices[menus.index(menu)]
print(f"{menu}, {price}원을 리스트에서 삭제합니다.")

# 메뉴와 가격 정보 삭제하기
menus.remove(menu)
prices.remove(price)

# 변경된 메뉴 및 가격 정보 출력하기
print(menus)
print(prices)

# 현재 메뉴 및 가격 정보 출력하기
print(menus)
print(prices)

# 삭제할 메뉴 입력받기
menu = input("삭제할 음식 이름을 입력하세요: ")

# 입력받은 메뉴가 기존 메뉴에 있는지 여부에 따라 삭제하거나 확인 메시지 출력하기
if menu in menus:
  price = prices[menus.index(menu)]
  print(f"{menu}, {price}원을 리스트에서 삭제합니다.")
  menus.remove(menu)
  prices.remove(price)
else:
  print(f"{menu}는 메뉴 리스트에 없습니다. 다시 확인하세요.")

# 변경된 메뉴 및 가격 정보 출력하기
print(menus)
print(prices)

# 리스트에 저장된 데이터 뒤집기 reverse()
menus.reverse()
print(menus)

# 리스트에 저장된 데이터 정렬하기 sort()
menus.sort()
print(menus)

# 내림차순 정렬
menus.sort(reverse=True)
print(menus)