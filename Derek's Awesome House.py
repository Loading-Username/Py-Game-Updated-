import pygame
import math
import random

# Initialize Game Engine
pygame.init()


# Window
SIZE = (800,600)
TITLE = "First Drawing"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
GREEN = (9, 234, 28)
BLUE = (106, 162, 252)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 123, 0)
YELLOW = (255, 250, 0)
PINK = (255, 0, 144)
BROWN = (102, 66, 0)
DGREEN = (0, 150, 58)
GRAY = (71, 70, 66)

# Functions
def draw_cloud(x, y):
    pygame.draw.ellipse(screen, WHITE, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, WHITE, [x + 20, y + 20, 60, 40])

def draw_door(x, y):
    pygame.draw.rect(screen, GRAY, [x, y, 50, 100])

def draw_doorknob(x,y):
    pygame.draw.ellipse(screen, WHITE, [x, y, 5, 5])

def draw_window(x, y):
    pygame.draw.rect(screen, BLUE, [x, y, 50, 75])
    
''' Make stars '''

stars = []

for i in range(200):

    x = random.randrange(0, 800)

    y = random.randrange(0, 400)

    r = random.randrange(1, 5)

    s = [x, y, r, r]

    stars.append(s)   

# Game Loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Drawing Code (Describe the picture.)
    
    ''' sky '''
    screen.fill(BLACK)

    ''' stars '''

    for s in stars:

        pygame.draw.ellipse(screen, YELLOW, s)

    ''' moon '''
    pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])

    ''' grass '''
    pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])

    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        post = [x+5, y], [x+10, y+5], [x+10, y+40], [x, y+40], [x, y+5]
        pygame.draw.polygon(screen, WHITE, post)
    
    pygame.draw.rect(screen, WHITE, [0, y+10, 800, 5])
    pygame.draw.rect(screen, WHITE, [0, y+30, 800, 5])

    ''' house '''
    pygame.draw.rect(screen, RED, [375, 400, 400, 400])

    ''' roof '''
    roof = [350, 400], [800, 400], [575, 275]
    pygame.draw.polygon(screen, GRAY, roof)

    ''' clouds '''
    draw_cloud(50, 150)
    draw_cloud(250, 75)
    draw_cloud(350, 125)
    draw_cloud(450, 175)
    draw_cloud(650, 100)

    ''' tree stump ''' 
    y = 500
    for x in range(50, 350, 100):
        trunk = [x, y], [x+30, y], [x+30, y+30], [x, y+30]
        pygame.draw.polygon(screen, BROWN, trunk)

    ''' leaves'''
    y = 500
    for x in range(50, 350, 100):
        leaves = [x+15,y-150], [x+60,y], [x-30,y] 
        pygame.draw.polygon(screen, DGREEN, leaves)

    ''' door '''
    draw_door(550, 500)
    
    ''' doorknob '''
    draw_doorknob(590, 550)

    ''' windows '''
    draw_window(450, 450)
    draw_window(650, 450)
