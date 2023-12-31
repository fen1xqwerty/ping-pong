from pygame import*



class GameSprite(sprite.Sprite):

    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       
        sprite.Sprite.__init__(self)

       
        self.image = transform.scale(
            image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Racket(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

speed_x = 3
speed_y = 3

win_width = 700
win_height = 500
display.set_caption("Ping-pong")
window = display.set_mode((win_width, win_height))
back = (200, 255, 255)
window.fill(back)
racket_l = Racket("racket.png", 10, win_height /2-40, 20, 80, 10)
racket_r = Racket("racket.png", 700-10-20, win_height /2-40, 20, 80, 10)
ball = GameSprite("tenis_ball.png", 325,225 , 50, 50, 5)
clock = time.Clock()
FPS = 60
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
           game = False
    ball.rect.x += speed_x
    ball.rect.y += speed_y
    window.fill(back)
    racket_l.update_l()
    racket_r.update_r()
    racket_l.reset()
    racket_r.reset()
    ball.reset()
    display.update()
    clock.tick(FPS)