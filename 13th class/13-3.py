# # 퐁 게임 막대 만들기
# # pygame 라이브러리 가져와서 게임 엔진 초기화하기
# import pygame, sys
# from paddle import Paddle
# from ball import Ball

# pygame.init()

# # 기본 색 정보 정의
# BLACK = [0, 0, 0]
# WHITE = [255, 255, 255]

# # 게임 윈도우 설정
# size = [700, 500]
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("Pong")

# # 오른쪽 막대 객체 생성
# paddle_A = Paddle(WHITE, 10, 100)
# paddle_A.rect.x = 20
# paddle_A.rect.y = 200

# # 왼쪽 막대 객체 생성
# paddle_B = Paddle(WHITE, 10, 100)
# paddle_B.rect.x = 670
# paddle_B.rect.y = 200

# # 공 객체 생성
# ball = Ball(WHITE, 10, 10)
# ball.rect.x = 345
# ball.rect.y = 195

# # 모든 스프라이트 모으기
# sprites_list = pygame.sprite.Group()
# sprites_list.add(paddle_A)
# sprites_list.add(paddle_B)
# sprites_list.add(ball)

# # 화면 업데이트 속도 제어를 위한 시간 변수 설정
# clock = pygame.time.Clock()

# # 메인 프로그램
# while True:
#   # 이벤트 발생 함수
#   for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#       sys.exit()

#   # 게임 구조 작성
#   # 키 입력에 따른 막대 이동 정의
#   keys = pygame.key.get_pressed()
#   if keys[pygame.K_w]:
#     paddle_A.move_up(5)
#   if keys[pygame.K_s]:
#     paddle_A.move_down(5)
#   if keys[pygame.K_UP]:
#     paddle_B.move_up(5)
#   if keys[pygame.K_DOWN]:
#     paddle_B.move_down(5)

#   # 공이 벽에 닿으면 튕기기
#   if ball.rect.x > 690 or ball.rect.x < 0:
#     ball.left_right_turn()
#   if ball.rect.y > 490 or ball.rect.y < 0:
#     ball.up_down_turn()

#   # 공이 막대에 닿으면 튕기기
#   if pygame.sprite.collide_mask(ball, paddle_A) or pygame.sprite.collide_mask(ball, paddle_B):
#     ball.bounce()

#   # 모든 스프라이트 상태 업데이트
#   sprites_list.update()

#   # 게임 화면 구성  
#   screen.fill(BLACK)
#   pygame.draw.line(screen, WHITE, [349,0], [349,500], 5)
#   sprites_list.draw(screen)

#   pygame.display.flip()

#   # 화면 업데이트 시간 설정(초당 60 프레임)
#   clock.tick(60)

# pygame.quit()

# # 퐁 게임 막대 만들기
# # pygame 라이브러리 가져와서 게임 엔진 초기화하기
# import pygame, sys
# from paddle import Paddle
# from ball import Ball

# pygame.init()

# # 기본 색 정보 정의
# BLACK = [0, 0, 0]
# WHITE = [255, 255, 255]

# # 점수 변수 초기
# score_A = 0
# score_B = 0

# # 게임 윈도우 설정
# size = [700, 500]
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("Pong")

# # 왼쪽 막대 객체 생성
# paddle_A = Paddle(WHITE, 10, 100)
# paddle_A.rect.x = 20
# paddle_A.rect.y = 200

# # 오른쪽 막대 객체 생성
# paddle_B = Paddle(WHITE, 10, 100)
# paddle_B.rect.x = 670
# paddle_B.rect.y = 200

# # 공 객체 생성
# ball = Ball(WHITE, 10, 10)
# ball.rect.x = 345
# ball.rect.y = 195

# # 모든 스프라이트 모으기
# sprites_list = pygame.sprite.Group()
# sprites_list.add(paddle_A)
# sprites_list.add(paddle_B)
# sprites_list.add(ball)

# # 화면 업데이트 속도 제어를 위한 시간 변수 설정
# clock = pygame.time.Clock()

# # 메인 프로그램
# while True:
#   # 이벤트 발생 함수
#   for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#       sys.exit()

#   # 게임 구조 작성
#   # 키 입력에 따른 막대 이동 정의
#   keys = pygame.key.get_pressed()
#   if keys[pygame.K_w]:
#     paddle_A.move_up(5)
#   if keys[pygame.K_s]:
#     paddle_A.move_down(5)
#   if keys[pygame.K_UP]:
#     paddle_B.move_up(5)
#   if keys[pygame.K_DOWN]:
#     paddle_B.move_down(5)

#   # 공이 왼쪽 또는 오른쪽 벽에 닿는 경우 다시 시작하기
#   if ball.rect.x > 690:
#     score_A += 1
#     ball.new()
#   if ball.rect.x < 0:
#     score_B += 1
#     ball.new()    

#   # 공이 벽에 닿으면 튕기기    
#   if ball.rect.y > 490 or ball.rect.y < 0:
#     ball.up_down_turn()

#   # 공이 막대에 닿으면 튕기기
#   if pygame.sprite.collide_mask(ball, paddle_A) or pygame.sprite.collide_mask(ball, paddle_B):
#     ball.bounce()

#   # 모든 스프라이트 상태 업데이트
#   sprites_list.update()

#   # 게임 화면 구성  
#   screen.fill(BLACK)
#   pygame.draw.line(screen, WHITE, [349,0], [349,500], 5)
#   sprites_list.draw(screen)

#   # 화면에 점수 표시
#   font = pygame.font.Font(None, 40)
#   text = font.render(str(score_A), True, WHITE)
#   screen.blit(text, [250,10])
#   text = font.render(str(score_B), True, WHITE)
#   screen.blit(text, [420,10])

#   pygame.display.flip()

#   # 화면 업데이트 시간 설정(초당 60 프레임)
#   clock.tick(60)

#   # 점수가 10점이 되면 게임 종료하기
#   if score_A == 10 or score_B == 10:
#     ball.stop()

# pygame.quit()

# 퐁 게임 막대 만들기
# pygame 라이브러리 가져와서 게임 엔진 초기화하기
import pygame, sys
from paddle import Paddle
from ball import Ball

pygame.init()
pygame.mixer.init()

# 기본 색 정보 정의
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]

# 점수 변수 초기
score_A = 0
score_B = 0

# 게임 윈도우 설정
size = [700, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

# 왼쪽 막대 객체 생성
paddle_A = Paddle(WHITE, 10, 100)
paddle_A.rect.x = 20
paddle_A.rect.y = 200

# 오른쪽 막대 객체 생성
paddle_B = Paddle(WHITE, 10, 100)
paddle_B.rect.x = 670
paddle_B.rect.y = 200

# 공 객체 생성
ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

# 모든 스프라이트 모으기
sprites_list = pygame.sprite.Group()
sprites_list.add(paddle_A)
sprites_list.add(paddle_B)
sprites_list.add(ball)

# 화면 업데이트 속도 제어를 위한 시간 변수 설정
clock = pygame.time.Clock()

# 사운드 설정
hit_file = "ping_pong_8bit_beeep.ogg"
hit_sound = pygame.mixer.Sound(hit_file)

# 배경음악 설정
bg_file = "8bit_Bossa.mp3"
pygame.mixer.music.load(bg_file)
pygame.mixer.music.play()

# 메인 프로그램
while True:
  # 이벤트 발생 함수
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

  # 게임 구조 작성
  # 키 입력에 따른 막대 이동 정의
  keys = pygame.key.get_pressed()
  if keys[pygame.K_w]:
    paddle_A.move_up(5)
  if keys[pygame.K_s]:
    paddle_A.move_down(5)
  if keys[pygame.K_UP]:
    paddle_B.move_up(5)
  if keys[pygame.K_DOWN]:
    paddle_B.move_down(5)

  # 공이 왼쪽 또는 오른쪽 벽에 닿는 경우 다시 시작하기
  if ball.rect.x > 690:
    hit_sound.play()
    score_A += 1
    ball.new()
  if ball.rect.x < 0:
    hit_sound.play()
    score_B += 1
    ball.new()    

  # 공이 벽에 닿으면 튕기기    
  if ball.rect.y > 490 or ball.rect.y < 0:
    hit_sound.play()
    ball.up_down_turn()

  # 공이 막대에 닿으면 튕기기
  if pygame.sprite.collide_mask(ball, paddle_A) or pygame.sprite.collide_mask(ball, paddle_B):
    hit_sound.play()
    ball.bounce()

  # 모든 스프라이트 상태 업데이트
  sprites_list.update()

  # 게임 화면 구성  
  screen.fill(BLACK)
  pygame.draw.line(screen, WHITE, [349,0], [349,500], 5)
  sprites_list.draw(screen)

  # 화면에 점수 표시
  font = pygame.font.Font(None, 40)
  text = font.render(str(score_A), True, WHITE)
  screen.blit(text, [250,10])
  text = font.render(str(score_B), True, WHITE)
  screen.blit(text, [420,10])

  pygame.display.flip()

  # 화면 업데이트 시간 설정(초당 60 프레임)
  clock.tick(60)

  # 점수가 10점이 되면 게임 종료하기
  if score_A == 10 or score_B == 10:
    ball.stop()
    pygame.mixer.music.fadeout(2000)

pygame.quit()