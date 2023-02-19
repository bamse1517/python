# # 문제
# # 파이썬에서 pygame 라이브러리를 이용하여 간단한 퐁 게임을 만들고 있습니다. 
# # 게임의 난이도를 높이기 위해 공을 두 개 만들려고 합니다. 
# # 다음의 공 객체 하나를 정의하는 코드를 이용하여 공 객체 두 개를 만드는 코드로 수정해 보세요.
# ball = Ball(WHITE, 10, 10)
# ball.rect.x = 345
# ball.rect.y = 195

# 답
from ball import Ball
WHITE = [255, 255, 255]
ball_1 = Ball(WHITE, 10, 10)
ball_1.rect.x = 345
ball_1.rect.y = 195

ball_2 = Ball(WHITE, 10, 10)
ball_2.rect.x = 345
ball_2.rect.y = 195