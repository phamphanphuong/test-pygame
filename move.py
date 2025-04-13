import math
import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

playerImage = pygame.image.load("green.png")
playerX = WIDTH /2
playerY = HEIGHT /2
playerSpeed = 5

enemyImage = pygame.image.load("red.png")
enemyX = 100
enemyY = 100
enemySpeed = 1

clock = pygame.time.Clock()

running = True
blinkActive = False
blinkStart = 0
score = 0

def resetPositions():
    global playerX, playerY, enemyX, enemyY, score
    playerX = WIDTH /2 + 200
    playerY = HEIGHT /2 + 200
    enemyX = 100
    enemyY = 100


while running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check for key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerX = playerX - playerSpeed
        print(playerX, playerY)
    if keys[pygame.K_RIGHT]:
        playerX = playerX + playerSpeed
        print(playerX, playerY)
    if keys[pygame.K_UP]:
        playerY = playerY - playerSpeed
        print(playerX, playerY)
    if keys[pygame.K_DOWN]:
        playerY = playerY + playerSpeed
        print(playerX, playerY)

    # Check for boundaries
    if playerX < 0:
        playerX = 0
    if playerX > WIDTH - playerImage.get_width():
        playerX = WIDTH - playerImage.get_width()
    if playerY < 0:
        playerY = 0
    if playerY > HEIGHT - playerImage.get_height():
        playerY = HEIGHT - playerImage.get_height()
        
    # Mouse position
    mouseX, mouseY = pygame.mouse.get_pos()
    # Mouse click
    mouseClick = pygame.mouse.get_pressed()
    if mouseClick[0]:  # Left click
        print("Mouse clicked at:", mouseX, mouseY)
    if mouseClick[2]:  # Right click
        print("Player at:", playerX, playerY)
        
    
    # Player di chuyển theo chuột nếu chuột trong screen
    if 0 < mouseX < WIDTH and 0 < mouseY < HEIGHT:
        if mouseX > playerX:
            playerX += playerSpeed
        elif mouseX < playerX:
            playerX -= playerSpeed    
        if mouseY > playerY:
            playerY += playerSpeed
        elif mouseY < playerY:
            playerY -= playerSpeed
        
    # Enemy đuổi theo player (phiên bản đơn giản)
    if enemyX < playerX-5:
        enemyX += enemySpeed
    elif enemyX > playerX+5:
        enemyX -= enemySpeed

    if enemyY < playerY-5:
        enemyY += enemySpeed
    elif enemyY > playerY+5:
        enemyY -= enemySpeed

    # Check for collision
    if abs(playerX - enemyX) < 32 and abs(playerY - enemyY) < 32:
        # print("Collision detected!")
        score += 1  # Mỗi lần tránh được enemy hoặc sau thời gian
        blinkActive = True
        
        blinkStart = pygame.time.get_ticks()
        print("blinkStart = ", blinkStart)

        # Reset game state if score reaches 10
        resetPositions()
       

    # Vẽ điểm lên màn hình
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, BLACK)

    
    if blinkActive and pygame.time.get_ticks() - blinkStart > 100:
        blinkActive = False

    # Fill the screen with white and draw the player image
    if blinkActive:
        screen.fill(BLACK)
    else:
        screen.fill(WHITE)
    
    screen.blit(playerImage, (playerX, playerY))
    screen.blit(enemyImage, (enemyX, enemyY))
    screen.blit(score_text, (10, 10))

   
    # Update the display
    pygame.display.update()
    
    
pygame.quit()