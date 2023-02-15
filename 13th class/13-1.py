# import pygame

# # 초기화
# pygame.init()

# # 전역 변수 설정
# screen = pygame.display.set_mode([640, 480])

# # 게임 실행
# while True:
#     pass

import pygame, sys

# 초기화
pygame.init()

# 전역 변수 설정
screen = pygame.display.set_mode([640, 480])

# 게임 실행
while True:
  # 이벤트 설정
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()