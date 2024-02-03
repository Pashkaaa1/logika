#Створи власний Шутер!
import pygame
import random
pygame.init()
W,H = 700,500

fps = pygame.time.Clock()


class main():
    def __init__(self,x,y,w,h,img):
        self.x = x
        self.y = y
        self.w = w
        self.h  =h
        self.img = img
        self.img_new = pygame.transform.scale(pygame.image.load(self.img),(self.w,self.h))

        self.rect = self.img_new.get_rect(center = (self.x,self.y))
        self.rand = random.randint(1,3)
player = main(350,450,50,100,'rocket.png')


bullet_list  = []
def addbullet():
    bullet_list.append(main(player.rect.x,player.rect.y,10,35,'bullet.png'))
def add(img):

    a = []
    y =19
    for el in range(5):
        a.append(main(random.randint(10,W-30),y,70,70,img))
    return a
list_enemy = add('asteroid.png')

pygame.mixer.init()
pygame.mixer.music.load('space.ogg')
pygame.mixer.music.play(loops = -1)
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption('Shooter')
fon = pygame.transform.scale(pygame.image.load('galaxy.jpg'),(W,H+30))
run = True

score_number=0
health_number=5
while run:
    score = "Kills:" + str(score_number)
    health="Health:" + str(health_number)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run =False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                addbullet()


    screen.blit(fon, (0,-30))
    text_score = pygame.font.Font(None, 30)
    text_new = text_score.render(score, True, (255, 100, 255))
    screen.blit(text_new, (50, 50))
    text_health = pygame.font.Font(None, 30)
    text_new = text_health.render(health, True, (255, 100, 255))
    screen.blit(text_new, (550, 50))
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]  and player.rect.right<=W:
        player.rect.x +=5
    if key[pygame.K_LEFT]  and player.rect.left>=0:
        player.rect.x -=5

    screen.blit(player.img_new,player.rect)

    for el in list_enemy:
        screen.blit(el.img_new,el.rect)
        el.rect.y += el.rand
        if el.rect.bottom >=H:
            el.rect.x,el.rect.y = random.randint(0,W-30),-50
            el.rand = random.randint(1,3)
            health_number -=1
        for bullet in bullet_list:
            screen.blit(bullet.img_new, (bullet.rect.x +20, bullet.rect.y))
            bullet.rect.y -=1
            if bullet.rect.colliderect(el.rect):
                bullet_list.pop()
                el.rect.x,el.rect.y = random.randint(0,W),-50
                score_number+=1


    if health_number<=0:
        break
    fps.tick(70)
    pygame.display.update()


