# 1~10까지 모든 수를 더하는 프로그램
sum = 0
for i in range(1, 10+1, 1):
  sum = sum + i
print(sum)

# 1~100까지 모든 수를 더하는 프로그램
sum = 0
for i in range(1, 100+1, 1):
  sum = sum + i
print(sum)

# 1~1,000까지 모든 수를 더하는 프로그램
sum = 0
for i in range(1, 1000+1, 1):
  sum = sum + i
print(sum)

# 1~max까지 모든 수를 더하는 프로그램
max = 1000
sum = 0
for i in range(1, max+1, 1):
  sum = sum + i
print(sum)

# 1~x 까지 모두 더하는 프로그램
def sum(x):
  sum = 0
  for i in range(1, x+1, 1):
    sum = sum + i
  return sum

print(sum(10))
print(sum(100))
print(sum(1000))

# 2~x 까지 모두 더하는 프로그램
def sum(x):
  sum = 0
  for i in range(2, x+1, 1):
    sum = sum + i
  return sum

print(sum(10))
print(sum(100))
print(sum(1000))

# 1~x 까지 중 짝수만 모두 더하는 프로그램
def sum(x):
  sum = 0
  for i in range(1, x+1, 1):
    if i % 2 == 0:
      sum = sum + i
  return sum

print(sum(10))
print(sum(100))
print(sum(1000))