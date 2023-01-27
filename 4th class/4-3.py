# pre_word = "python"
# print(pre_word[5])
# print(pre_word[4])
# print(pre_word[3])
# print(pre_word[2])
# print(pre_word[1])
# print(pre_word[0])

# pre_word = input("단어를 입력하세요 : ")
# print("거꾸로 출력 : ", end='')
# print(pre_word[5], end='')
# print(pre_word[4], end='')
# print(pre_word[3], end='')
# print(pre_word[2], end='')
# print(pre_word[1], end='')
# print(pre_word[0], end='')

# pre_word = input("단어를 입력하세요 : ")
# post_word = ""
# post_word = post_word + pre_word[5]
# post_word = post_word + pre_word[4]
# post_word = post_word + pre_word[3]
# post_word = post_word + pre_word[2]
# post_word = post_word + pre_word[1]
# post_word = post_word + pre_word[0]
# print(f"거꾸로 출력 : {post_word}")

# pre_word = "python"
# post_word = ""
# post_word = pre_word[-1] + pre_word[-2] + pre_word[-3] + pre_word[-4] + pre_word[-5] + pre_word[-6]
# print(f"거꾸로 출력 : {post_word}")

# "python"[::-1]

# pre_word = input("단어를 입력하세요 : ")
# post_word = [pre_word[::-1]]
# print(f"거꾸로 출력 : {post_word}")

# words = "산토끼 토끼야 어디를 가느냐 깡총 깡총 뛰어서 어디를 가느냐"
# reverse_words = words[::-1]
# reverse_words.split()[::-1]
# print(reverse_words)

# str_1 = "1"
# str_2 = "2"
# str_op = "+"
# exp = str_1 + str_op + str_2
# print(eval(exp))

str_1, str_2 = input("두 개의 숫자를 입력하세요 : ").split()
oper = input("연산자를 입력하세요 : ")
result = eval(str_1 + oper + str_2)
print(f"계산 결과 : {str_1} + {str_2} = {result}")