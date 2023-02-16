# import pygame, sys

# # 초기화
# pygame.init()

# # 전역 변수 선언
# size = [700, 500]
# screen = pygame.display.set_mode(size)

# # 게임 실행
# while True:
#   # 종료 이벤트 설정
#   for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#       sys.exit()
  
#   # 화면 설정
#   screen.fill([0,0,0])
#   pygame.draw.line(screen, [255,255,255], [349,0], [349, 500], 5)
#   pygame.display.flip() 

# pygame.quit()

# import pygame, sys

# # 초기화
# pygame.init()

# # 기본 색 정보 정의
# BLACK = [0, 0, 0]
# WHITE = [255, 255, 255]

# # 전역 변수 선언
# size = [700, 500]
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("Pong")

# # 게임 실행
# while True:
#   # 종료 이벤트 설정
#   for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#       sys.exit()
  
#   # 화면 설정
#   screen.fill(BLACK)
#   pygame.draw.line(screen, WHITE, [349,0], [349, 500], 5)

#   pygame.display.flip() 

# pygame.quit()

# import pygame

# class Paddle(pygame.sprite.Sprite):
#   def __init__(self, color, width, height):
#     super().__init__()

#     self.image = pygame.Surface([width, height])
#     self.image.fill([0,0,0])
#     self.image.set_colorkey([0,0,0])

#     # 사각형 막대 그리기
#     pygame.draw.rect(self.image, color, [0,0,width, height])
#     self.rect = self.image.get_rect()

#   def move_up(self, pixels):
#     self.rect.y -= pixels
#     if self.rect.y < 0:
#       self.rect.y = 0

#   def move_down(self, pixels):
#     self.rect.y += pixels
#     if self.rect.y > 400:
#       self.rect.y = 400

# # 퐁 게임 막대 만들기
# # pygame 라이브러리 가져와서 게임 엔진 초기화하기
# import pygame, sys
# from paddle import Paddle

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

# # 모든 스프라이트 모으기
# sprites_list = pygame.sprite.Group()
# sprites_list.add(paddle_A)
# sprites_list.add(paddle_B)

# # 화면 업데이트 속도 제어를 위한 시간 변수 설정
# clock = pygame.time.Clock()

# # 메인 프로그램
# while True:
#   # 종료 이벤트 설정
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
    
#   sprites_list.update()

#   # 화면 설정
#   screen.fill(BLACK)
#   pygame.draw.line(screen, WHITE, [349,0], [349,500], 5)
#   sprites_list.draw(screen)

#   pygame.display.flip()

#   # 화면 업데이트 시간 설정(초당 60 프레임)
#   clock.tick(60)

# pygame.quit()

# 퐁 게임 막대 만들기
# pygame 라이브러리 가져와서 게임 엔진 초기화하기
import pygame, sys
from paddle import Paddle
from ball import Ball

pygame.init()

# 기본 색 정보 정의
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]

# 게임 윈도우 설정
size = [700, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

# 오른쪽 막대 객체 생성
paddle_A = Paddle(WHITE, 10, 100)
paddle_A.rect.x = 20
paddle_A.rect.y = 200

# 왼쪽 막대 객체 생성
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

  # 공이 벽에 닿으면 튕기기
  if ball.rect.x > 690 or ball.rect.x < 0:
    ball.left_right_turn()
  if ball.rect.y > 490 or ball.rect.y < 0:
    ball.up_down_turn()

  # 모든 스프라이트 상태 업데이트
  sprites_list.update()

  # 게임 화면 구성  
  screen.fill(BLACK)
  pygame.draw.line(screen, WHITE, [349,0], [349,500], 5)
  sprites_list.draw(screen)

  pygame.display.flip()

  # 화면 업데이트 시간 설정(초당 60 프레임)
  clock.tick(60)

pygame.quit()