# ipsum = '''
# Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
# Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
# Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
# Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
# '''
# print(ipsum)

# # 총 글자수
# print(f"총 글자수는 {len(ipsum)}자 입니다.")

# # 대문자 변환
# print(ipsum.upper())

# # 소문자 변환
# print(ipsum.lower())

# # 첫글자만 대문자 변환
# sentence = "hello, and welcome to my world."
# print(sentence.capitalize())

# str_1 = "HELLO"
# str_2 = "world"
# print(str_1.isupper())
# print(str_2.islower())

# str_3 = str_1 + str_2
# print(str_3)
# print(str_3.isupper())
# print(str_3.islower())

# txt = "I love apples, apple are my favorite fruit"
# print(txt.count("apple"))

# "hello"[0]

# txt = "I love apples, apple are my favorite fruit"
# print(txt.find("apple") + 1)

words = '''
20
22
PSY coming back
(이리 오너라)
Long time no see huh?
오래간만이지 huh?
우리 다시 웃고, 울고, 지지고, 볶고
Let's get loco
Pandemic's over uh
그래, 기분이 오져 uh
다시 그분이 오죠 uh
Everybody say
뻑적지근해
걸쩍지근해
시끌벅적거리네
너무 좋아 북적거리네
동서남북 ay
강남, 강북 ay
싹 다 모여 throw yo hands in the air
I say, "Yeah"
Can you feel it?
Can you feel it?
Whoa-yeah, whoa-whoa
Can you feel it?
Can you feel it?
Whoa-yeah
Ayy
준비하시고 (go)
쏘세요 (oh)
That, that, I like that (like that)
기분 좋아 babe (babe)
흔들어 좌우, 위아래로 (sing it)
One, two, three to the four (sing it)
That, that, I like that
That, that, I like that babe
That, that, I like that
It's like that, that yo
That, that, I like that
That, that, I like that babe
That, that, I like that
It's like that
야, 내가 뭐 하는 사람인지 까먹었지?
That, that, I like that (like that)
시간이 지나도 변함없이
That, that, I like that (like that)
I don't care, I don't care that I like that
That, that, I like that (like that)
내가 바라보고 바래왔던 사람들아
모두 다 ready, set, go!
되려 늘어난 맷집, 때리던 분이 불편하겠지
너네 바램대로 망할 거라 고사 지낸
사람들을 모아다가 가볍게 때찌
적당히 하라고 oh, oh, oh
그냥 닥치고 다 같이 놀아보자고 oh, oh, oh
민윤기와 박재상
Can you feel it?
Can you feel it?
Whoa-yeah, whoa-whoa
Can you feel it?
Can you feel it?
Whoa-yeah
Ayy
준비하시고 (go)
쏘세요 (oh)
That, that, I like that (like that)
기분 좋아 babe (babe)
흔들어 좌우, 위아래로 (sing it)
One, two, three to the four (sing it)
That, that, I like that
That, that, I like that babe
That, that, I like that
It's like that, that yo
That, that, I like that
That, that, I like that babe
That, that, I like that
It's like that, that yo
Do what you wanna (ay, ay, ay)
Say what you wanna (ay, ay, ay)
Do what you wanna (say what?)
That, that, I like that babe
Do what you wanna (ay, ay, ay)
Say what you wanna (ay, ay, ay)
Do what you wanna (say what?)
That, that, I like that babe
That, that, I like that
'''

# print(words.count("that"))

# find_word = input("검색할 단어를 입력하세요 : ")
# word_count = words.count(find_word)
# print(f"{find_word} 은(는) 총 {word_count} 번 등장합니다.")

# find_word = input("검색할 단어를 입력하세요 : ")

# word_count = words.count(find_word)
# print(f"{find_word} 은(는) 총 {word_count} 번 등장합니다.")

# word_first_index = words.find(find_word) + 1
# print(f"{find_word} 은(는) 총 {word_first_index} 번 등장합니다.")

# find_word = input("검색할 단어를 입력하세요 : ")

# word_count = words.count(find_word)
# print(f"{find_word} 은(는) 총 {word_count} 번 등장합니다.")

# word_first_index = words.find(find_word) + 1
# print(f"{find_word} 은(는) 총 {word_first_index} 번 등장합니다.")

# find_cap_word = find_word.capitalize()

# cap_word_count = words.count(find_cap_word)
# print(f"{find_cap_word} 은(는) 총 {cap_word_count} 번 등장합니다.")

# cap_word_first_index = words.find(find_cap_word) + 1
# print(f"{find_cap_word} 은(는) 총 {cap_word_first_index} 번 등장합니다.")

words_lower = words.lower()

find_word = input("검색할 단어를 입력하세요 : ")

word_count = words_lower.count(find_word)
print(f"{find_word} 은(는) {word_count} 번 등장합니다.")

word_first_index = words_lower.find(find_word) + 1
print(f"{find_word} 은(는) {word_first_index} 번 등장합니다.")