""" 
Designs and Architechtures

"""

import turtle;

#draw_circle() method draws a single elliptical circle
def draw_circle(pen, radius):
    for i in range(2):
        pen.circle(radius, 90);                                     #drawing a quarter of circle
        pen.circle(radius//2, 90);                                  #pulling circular arc inward

#Main Method for Elliptical Ring
def circularCircleMovement(radius):
    screen = turtle.Screen();
    screen.bgcolor('black');
    colors = ['violet', 'indigo', 'blue', 'green',  'yellow', 'orange', 'red'];

    pen = turtle.Turtle();
    pen.speed(100);
    angle = 10;
    
    for i in range(100):                                            #number of rounds = 360 / change of elliptical angle( 10 ) = 36 But we are writing 100 for checking for long
        pen.seth(-angle);
        pen.pencolor(colors[i % 7]);
        draw_circle(pen, radius);
        angle += 10;
    pen.ht();
    screen.exitonclick();

if __name__ == "__main__":
    circularCircleMovement(80);




























"""
import pygame, random, math, time;
pygame.init();

HEIGHT = 700;
WIDTH = 700;
win = pygame.display.set_mode((WIDTH, HEIGHT));
win.fill((0, 0, 255));

x = 2;
y = 2;

clock = pygame.time.Clock();
def start() :
    cnt = HEIGHT / 2 - 80;
    t = 5;
    while(cnt <= 430) :
        #event = pygame.event.wait();
        clock.tick(t);
        #win.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)));
        #pygame.draw.circle((win), (255, 0, 0), (HEIGHT // x , WIDTH // y), 80, 5);
        #circular rotation of circles
        
        radius = 80;
        radiusC = 40;
        cnty = int(WIDTH / 2 - math.sqrt( (radius)*(radius) - ( cnt - HEIGHT / 2) * ( cnt - HEIGHT / 2)));
        pygame.draw.circle(win, (255, 0, 0), (cnt, cnty), radiusC, 8);
        cnty1 = int(WIDTH / 2 + math.sqrt( (radius)*(radius) - ( cnt - HEIGHT / 2) * ( cnt - HEIGHT / 2)));
        pygame.draw.circle(win, (255, 0, 0), (cnt, cnty1), radiusC, 8);
        cnt += 20;
        #time.sleep(1);

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT :
                pygame.quit();
                quit();
                break;
        pygame.display.update();
        pygame.display.flip();
"""
    
"""
    cnt = HEIGHT / 2 - 80;
    while(cnt <= 430) :
        #event = pygame.event.wait();
        clock.tick(t);
        #win.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)));
        #pygame.draw.circle((win), (255, 0, 0), (HEIGHT // x , WIDTH // y), 80, 5);
        #circular rotation of circles
        
        radius = 80;
        cnty = int(WIDTH / 2 + math.sqrt( (radius)*(radius) - ( cnt - HEIGHT / 2) * ( cnt - HEIGHT / 2)));
        pygame.draw.circle(win, (255, 0, 0), (cnt, cnty), radius, 8);
        cnt += 10;
        #time.sleep(1);

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT :
                pygame.quit();
                quit();
                break;
        pygame.display.update();
        pygame.display.flip();
"""
"""
while True :
    start();
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit();
            quit()
            break;

quit();
"""