import pygame

### Colors
WHITE = (255, 255, 255)
BLACK = (0,0,0)

### Constants
W = 1000
H = 600
pygame.font.init()
comic = pygame.font.SysFont('Comic Sans MS', 30)

### Variables
wt = 20
mplay = False

p1x = W/30
p1y = H/2 - ((W/60)**2)/2

p1score = 0

w_p = False
s_p = False
wsr = False

dm = H/40

paddle_width = W/70
paddle_height = paddle_width**2

bsd = 1

bx = W/2
by = H/2
bw = W/65
bxv = H/60
bxv = -bxv
byv = 0
class Ball:
  def __init__(self, x, y):
    self.x = x
    self.y = y

    def myfunc(self):
      print("Hello my x is " + self.x)
ball = Ball(bx, by)
## Functions
def drawpaddle(x, y, w, h):
    pygame.draw.rect(screen, WHITE, (x, y, w, h))

def drawball(x, y):
    pygame.draw.circle(screen, WHITE, (int(x), int(y)), int(bw))

def uploc():
    global p1y
    if w_p:
        if p1y-(dm) < 0:
            py1 = 0
        else:
            p1y -= dm
    elif s_p:
        if p1y+(dm)+paddle_height > H:
            p1y = H-paddle_height
        else:
            p1y += dm

def upblnv():
    global bx
    global bxv
    global by
    global byv
    global p1score

    if (bx+bxv < p1x+paddle_width) and ((p1y < by+byv+bw) and (by+byv-bw < p1y+paddle_height)):
        bxv = -bxv
        byv = ((p1y+(p1y+paddle_height))/2)-by
        byv = -byv/((5*bw)/7)
    elif bx+bxv < 0:
        bx = W/2
        bxv = H/60
        by = H/2
        byv = 0
    if by+byv > H or by+byv < 0:
        byv = -byv
    if bx+bxv > W:
        bxv = -bxv

    bx += bxv
    by += byv

def drawscore():
    score = comic.render(str(p1score), False, WHITE)
    screen.blit(score, (W/2,30))

### Initialize
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption('Pong Relativistico')
screen.fill(BLACK)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_UP:
                w_p = True
                if s_p == True:
                    s_p = False
                    wsr = True
            if event.key == pygame.K_DOWN:
                s_p = True
                if w_p == True:
                    w_p = False
                    wsr = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                w_p = False
                if wsr == True:
                    s_p = True
                    wsr = False
            if event.key == pygame.K_DOWN:
                s_p = False
                if wsr == True:
                    w_p = True
                    wsr = False
    ball.myFunc()
    screen.fill(BLACK)
    uploc()
    upblnv()
    drawscore()
    drawball(bx, by)
    drawpaddle(p1x, p1y, paddle_width, paddle_height)
    pygame.display.flip()
    pygame.time.wait(wt)
