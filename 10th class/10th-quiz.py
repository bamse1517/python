# 퀴즈 2번문제
# 다음 파일의 내용을 한번에 모두 읽어오기 위해서 사용할 수 있는 함수는 무엇인가요?
# 파일내용
# 이미테이션게임
# 소셜네트워크
# 마이너리티리포트


# 2번 문제 답
# writelines() & with문



# 퀴즈 3번 문제 
# 다음 파이썬 코드를 실행하면 에러가 발생합니다. 파일에 다음과 같이 내용을 저장하기 위해 해당 코드를 수정해 보세요.
# 파일내용
# 이미테이션게임
# 소셜네트워크
# 마이너리티리포트
# 오류 코드
# my_movie = open('movie_list.txt', 'r')
# my_movie.write('이미테이션게임')
# my_movie.write('소셜네트워크')
# my_movie.write('마이너리티리포트')


# 3번 문제 답
my_movie = open('movie_list.txt', 'w')
my_movie.write('이미테이션게임\n')
my_movie.write('소셜네트워크\n')
my_movie.write('마이너리티리포트\n')
my_movie.close()