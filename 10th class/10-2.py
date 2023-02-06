# # 파일 읽기
# my_todo = open('todo.txt', 'r')
# lines = my_todo.readlines()
# print(lines)

# # 파일 닫기
# my_todo = open('todo.txt', 'r')
# lines = my_todo.readlines()
# print(lines)
# my_todo.close()

# 파일 내용을 한 줄씩 읽어오기
my_todo = open('todo.txt', 'r')
first_line = my_todo.readline()
second_line = my_todo.readline()
third_line = my_todo.readline()
print(f"1: {first_line}")
print(f"2: {second_line}")
print(f"3: {third_line}")
my_todo.close()