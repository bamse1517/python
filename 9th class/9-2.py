# # abs()
# abs(-3)

# # input()
# input('숫자입력: ')

# # 인사하는 함수
# def greet():
#   print("안녕하세요")

# greet()

# # 이름을 받아서 인사하는 함수

# def greet(name):  
#   print(f"안녕하세요, {name}님")

# greet("민수")

# 두 정수의 합을 반환하는 함수
def int_sum(a, b):
  return a + b

print(int_sum(10, 20))

a = 1
print(a)

def test():
  a = 1
  print(id(a))

a = 2
print(id(a))
test()

def test():
  aa = 1
  print(aa)

test()
print(aa)

def test():
  global aa
  aa = 1
  print(aa)

test()
print(aa)