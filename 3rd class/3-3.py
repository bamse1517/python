# a, b = input().split()
# print(a)
# print(b)

# a, b = input("두 개의 숫자를 입력하세요 : ").split()
# print(a + b)
# print(type(a))

# a, b = input("두 개의 숫자를 입력하세요 : ").split()
# print(int(a) + int(b))

# str_a, str_b = input("두 개의 숫자를 입력하세요.").split()
# num_a, num_b = int(str_a), int(str_b)

# sum_result = num_a + num_b
# diff_result = num_a - num_b
# product_result = num_a * num_b
# quotient_result = num_a / num_b

# print(f"{num_a} + {num_b} = {sum_result}")
# print(f"{num_a} - {num_b} = {diff_result}")
# print(f"{num_a} * {num_b} = {product_result}")
# print(f"{num_a} / {num_b} = {quotient_result}")

str_a, str_b, str_c = input("세 개의 숫자를 입력하세요.").split()
num_a, num_b, num_c = int(str_a), int(str_b), int(str_c)

sum_result = num_a + num_b + num_c
diff_result = num_a - num_b - num_c
product_result = num_a * num_b * num_c
quotient_result = num_a / num_b / num_c

print(f"{num_a} + {num_b} + {num_c} = {sum_result}")
print(f"{num_a} - {num_b} - {num_c} = {diff_result}")
print(f"{num_a} * {num_b} * {num_c} = {product_result}")
print(f"{num_a} / {num_b} / {num_c} = {quotient_result}")