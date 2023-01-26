# print(10 + 5)
# print(10 - 5)

# print(10 + 5 + 1)
# print(10 + 5 - 1)

# num_1 = 10
# num_2 = 5
# num_3 = 1
# print(num_1 + num_2 + num_3)
# print(num_1 - num_2 - num_3)
# print(num_1 + num_2 - num_3)

# print(10 * 5)
# print(10 / 4)

# num_1 = 10
# num_2 = 5
# print(type(num_1))
# print(type(num_1 / num_2))

# num_1 = 10
# num_2 = 5
# num_3 = 3
# res_1 = num_1 * num_2
# res_2 = num_1 / num_2
# res_3 = num_1 * num_2 / num_3
# print(res_1)
# print(res_2)
# print(res_3)

# print(type(10 + 5))
# print(type(10 / 5))
# print(type(10.0 + 5.0))
# print(type(10 + 5.0))

# birth_day = 25
# birth_month = 2
# step_1 = birth_month * 4
# step_2 = step_1 + 2
# step_3 = step_2 * 25
# step_4 = step_3 + birth_day
# print(step_4 - 50)

# 5 / 3 몫 1, 나머지 2
# print(5 / 3)
# print(5 // 3)
# print(5 % 3)

# print(5 / 3)
# print(round(5 / 3))
# print(round(5 / 3, 2))

# num = int(input("숫자를 입력하세요 : "))
# remainder = num % 2
# print(f"입력한 숫자는 {num} 이고, 2로 나눈 나머지 값은 {remainder} 입니다.")

# print(3 ** 3)
# print(pow(3, 3))

# num = 100 ** 100
# print(num)

# print(2 ** (3 * 1))

# print(2 ** (3 * 2))

# print(2 ** (3 * 10))

# hour = 10
# cell_count = 2 ** (3 * hour)
# print(f"{cell_count:,}")

hour = int(input("시간을 입력하세요 : "))
cell_count = 2 ** (3 * hour)
print(f"1마리의 대장균은 {hour}시간이 지나면 {cell_count:,}마리로 분열합니다.")
