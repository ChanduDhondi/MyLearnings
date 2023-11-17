import pygame
import random
import time
import sys

class Snake:

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load('movement.mp3')
        pygame.mixer.music.play(-1)
        self.length = 1
        self.snake_position = [200,200]
        self.snake_body = [[200,200]]
        self.fruit_x = 300
        self.fruit_y = 300
        self.window_width = 600
        self.window_height = 600
        self.score = 0
        self.direction = 'RIGHT'
        self.screen = pygame.display.set_mode((self.window_width,self.window_height))
        pygame.display.set_caption('Chandu Dhondi - Snake Game')
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()

    # def fruit(self):
    #     self.image = pygame.image.load('egg.bmp')
    #     self.screen.blit(self.image,(self.fruit_x,self.fruit_y))

    def move(self):
        self.fruit_x = random.randint(0,40)*10
        self.fruit_y = random.randint(0,40)*10

    def show_score(self):
        self.score_font =pygame.font.SysFont('arial',25,False,False)
        self.score_draw = self.score_font.render('Score : '+str(self.score),True,'white')
        self.score_rect = self.score_draw.get_rect()
        self.screen.blit(self.score_draw,self.score_rect)
        pygame.display.flip()

    def game_over(self):
        self.over = pygame.font.SysFont('arial',50,False,False)
        self.over_draw1 = self.over.render('-: GAME OVER :- ',True,'red')
        self.over_rect1 = self.over_draw1.get_rect()
        self.over_rect1.center = self.screen_rect.center
        self.screen.blit(self.over_draw1,self.over_rect1)

        self.over1 = pygame.font.SysFont('arial',4,False,False)
        self.over_draw2 = self.over.render('Your Score : '+str(self.score),True,'violet')
        self.over_rect2 = self.over_draw2.get_rect()
        self.over_rect2 =self.screen_rect.move(185,330)
        self.screen.blit(self.over_draw2,self.over_rect2)
        pygame.display.flip()
        self.music('crash')
        pygame.mixer.music.pause()

    def music(self,sound):
        sound =pygame.mixer.Sound(f'{sound}.mp3')
        pygame.mixer.Sound.play(sound)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.direction = 'right'
                elif event.key == pygame.K_LEFT:
                    self.direction = 'left'
                elif event.key == pygame.K_UP:
                    self.direction = 'up'
                elif event.key == pygame.K_DOWN:
                    self.direction = 'down'
                elif event.type == pygame.K_q:
                    sys.exit()
    	
        #moving continuously
        if self.direction == 'right': 
            self.snake_position[0] += 10
        if self.direction == 'left':
            self.snake_position[0] -= 10
        if self.direction == 'up':
            self.snake_position[1] -= 10
        if self.direction == 'down':
            self.snake_position[1] += 10

        #snake collide with fruit
        self.snake_body.insert(0,[self.snake_position[0],self.snake_position[1]])
        if self.snake_position[0] == self.fruit_x and self.snake_position[1] == self.fruit_y:
            self.music('ding')
            self.score += 10
            self.move()
        else: 
            self.snake_body.pop()
            
        self.color = random.choice(['violet','indigo','blue','green','yellow','orange','red'])

        for i in self.snake_body:
                pygame.draw.rect(self.screen,self.color,pygame.Rect(i[0],i[1],15,15))
        
        #game over condition
        if self.snake_position[0] < 0 or self.snake_position[0] > self.window_width:
            self.game_over()
            time.sleep(3)
            pygame.quit()
        elif self.snake_position[1] < 0 or self.snake_position[1] > self.window_height:
            self.game_over()
            time.sleep(3)
            pygame.quit()

        #if snake touches the body
        for j in self.snake_body[1:]:
            if self.snake_position[0] == j[0] and self.snake_position[1] == j[1]:
                self.game_over()
                time.sleep(3)
                pygame.quit()

    def run_snake(self):
        while True:           
            self.screen.fill('black')
            self.check_events()
            self.show_score()
            self.snake = pygame.draw.rect(self.screen,'green',pygame.Rect((self.snake_position[0],self.snake_position[1]),(15,15)))
            self.fruit = pygame.draw.rect(self.screen,'yellow',pygame.Rect((self.fruit_x,self.fruit_y),(15,15)))
            pygame.display.flip() 
            self.clock.tick(10)


if __name__ == '__main__':
    snake = Snake()
    snake.run_snake()