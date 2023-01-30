# 문제 1
num = 0
for i in range(1, 10):
  if i % 2 == 0:    
    continue
  num = num + 1
print(num)

# 문제 1 답
res = 1
for i in range(1, 6):
  res *= i  
print(f"5! 은 {res} 입니다.")



# 문제 2
num = 0
for i in range(1, 10):
  if i % 2 == 0:
    break
  num = num + 1
print(num)

# 문제 2 답
res = 1
i = 1
while i < 6:
  res *= i
  i += 1
print(f"5! 은 {res} 입니다.")