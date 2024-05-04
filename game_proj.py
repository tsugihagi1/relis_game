import pygame
pygame.init()

back=pygame.transform.scale(pygame.image.load("enemy"),(500,500))
mw = pygame.display.set_mode((500,500))
mw.fill(back)
clock = pygame.time.Clock()



while not game_over:

    pygame.display.update()
    clock.tick(60)
class Area():
    def __init__(self, x=0,y=0, width=10, height=10, color=None ):
        self.rect = pygame.Rect(x,y,width,height)
        self.fill_color = back
        if color:
            self.fill_color = colo
    def color(self,new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x,y)
    def colliderect(self,rect):
        return self.rect.colliderect(rect)
class Picture(Area):
    def __init__(self,filename, x = 0, y = 0,width=10, height=10):
        Area.__init__(self, x = x, y = y, width = width, height = height, color = None)
        self.image = pygame.image.load(filename)
    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))
class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0,0,0)):
        self.image = pygame.font.SysFont("verdana" , fsize).render(text, True, text_color)
    def draw(self, shift_x, shift_y):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
        ball = Picture("ball.png", 160, 200, 50, 50)
platform = Picture("platform.png", racket_x, racket_y, 100, 30)
class Picture(Area):
    def __init__(self,filename, x = 0, y = 0,width=10, height=10):
        Area.__init__(self, x = x, y = y, width = width, height = height, color = None)
        self.image = pygame.image.load(filename)

game_over = False