import pygame
pygame.init()
WIDTH, HEIGHT = 500, 500
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
class sprite:
    def __init__(self, x=50,y=50,w=50,h=50,speed=5,imege=None,color=WHITE):
        self.color = color
        self.imege = imege
        self.rect = pygame.Rect(x,y,w,h)
        self.speed = speed
        self.load_img(imege)
    def load_img(self, path):
        if not path:
            return
        self.imege = pygame.image.load(path)
        self.imege = pygame.transform.scale(self.imege, (self.rect.w, self.rect.h))
    def draw(self, window):
        if self.imege:
            window.blit(self.imege, (self.rect.x, self.rect.y))
        else:
            pygame.draw.rect(window, self.color, self.rect)
    def move(self,window):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.x > self.speed:
            self.rect.x -= self.speed
        if key[pygame.K_RIGHT] and self.rect.right <= window.get_width()- self.speed:
            self.rect.x += self.speed
        if key[pygame.K_UP] and self.rect.y > self.speed:
            self.rect.y -= self.speed
        if key[pygame.K_DOWN] and self.rect.bottom <= window.get_height()- self.speed:
            self.rect.y += self.speed
        
         
Window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
plaer = sprite()
run = True
while run:
    Window.fill(BLUE)
    plaer.draw(Window)
    plaer.move(Window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    pygame.display.flip()
    clock.tick(50)
