import pygame
import sys
import time

# initialize Pygame
pygame.init()

# set the window size
width = 1000
height = 1000
window = pygame.display.set_mode((width, height))

# set the window title
pygame.display.set_caption("Ping Pong Game")

# create the paddles
paddle_width = 20
paddle_height = 100
paddle_speed = 5
paddle1 = pygame.Rect(0, 0, paddle_width, paddle_height)
paddle2 = pygame.Rect(width - paddle_width, height- paddle_height, paddle_width, paddle_height)

# create the ball
ball_radius = 10
ball_speed_x = 5
ball_speed_y = 5
ball = pygame.Rect(width/2 - ball_radius, height/2 - ball_radius, ball_radius*2, ball_radius*2)

# create the font object
font = pygame.font.Font(None, 36)

# create the start button
button_width = 200
button_height = 80
start_button = pygame.Rect(width/2 - button_width/2, height/2 - button_height/2, button_width, button_height)
button_color = (255, 255, 255)
button_hover_color = (200, 200, 200)

# create the start text object
start_text = font.render("Click here to start!", True, (0, 0, 0))
start_text_rect = start_text.get_rect(center=start_button.center)

# create the winner text object
winner_text = font.render("", True, (255, 255, 255))
winner_text_rect = winner_text.get_rect(center=(width/2, height/2 - 50))

# set the game state to not started
game_started = False

# set the game state to not over
game_over = False

# start the game loop
while True:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos):
                game_started = True
                game_over = False
                ball.x = width/2 - ball_radius
                ball.y = height/2 - ball_radius
                ball_speed_x = 5
                ball_speed_y = 5
                paddle1.y = 0
                paddle2.y = height - paddle_height

    # update the game if it is started
    if game_started and not game_over:
        # update the paddles
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle1.y -= paddle_speed
        if keys[pygame.K_s]:
            paddle1.y += paddle_speed
        if keys[pygame.K_UP]:
            paddle2.y -= paddle_speed
        if keys[pygame.K_DOWN]:
            paddle2.y += paddle_speed

        # keep the paddles on the screen
        if paddle1.top < 0:
            paddle1.top = 0
        if paddle1.bottom > height:
            paddle1.bottom = height
        if paddle2.top < 0:
            paddle2.top = 0
        if paddle2.bottom > height:
            paddle2.bottom = height    

        # update the ball
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # check for collisions
        if ball.top <= 0 or ball.bottom >= height:
            ball_speed_y = -ball_speed_y
        if ball.left <= 0:
            game_over = True
            winner_text = font.render("Player 2 Wins!",winner_text_rect = winner_text.get_rect(center=(width/2, height/2 - 50)))
        if ball.right >= width:
            game_over = True
            winner_text = font.render("Player 1 Wins!", True, (255, 255, 255))
            winner_text_rect = winner_text.get_rect(center=(width/2, height/2 - 50))
        if ball.colliderect(paddle1) or ball.colliderect(paddle2):
            ball_speed_x = -ball_speed_x
    
    # clear the screen
    window.fill((0, 0, 0))

    # draw the paddles and ball
    pygame.draw.rect(window, (255, 255, 255), paddle1)
    pygame.draw.rect(window, (255, 255, 255), paddle2)
    pygame.draw.circle(window, (255, 255, 255), (ball.x + ball_radius, ball.y + ball_radius), ball_radius)

    # draw the start button if the game is over
    if game_over:
        pygame.draw.rect(window, button_color, start_button)
        pygame.draw.rect(window, (0, 0, 0), start_button, 2)
        start_text_rect = start_text.get_rect(center=start_button.center)
        window.blit(start_text, start_text_rect)

    # draw the winner text if the game is over
    if game_over:
        window.blit(winner_text, winner_text_rect)

    # draw the screen
    pygame.display.flip()

    # pause for a moment
    time.sleep(0.01)

        
        
    



