import pygame;
pygame.init();

WIN_WIDTH = 900;
WIN_HEIGHT = 615;
window_screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT));
pygame.display.set_caption('LIPSTICK FOUNDATION');

lipstick_base = pygame.image.load(r"C:\Users\RANVEER\Desktop\PYTHON\Game using python\Design Projects\ARTISTIC DESIGNS\standing lipstick base.jpg");
upper_head = pygame.image.load(r"C:\Users\RANVEER\Desktop\PYTHON\Game using python\Design Projects\ARTISTIC DESIGNS\HEAD2.jpg");
#lower_head = pygame.image.load(r"C:\Users\RANVEER\Desktop\PYTHON\Game using python\Design Projects\ARTISTIC DESIGNS\lipstick head.jpg")
backOfHead = pygame.image.load(r"C:\Users\RANVEER\Desktop\PYTHON\Game using python\Design Projects\ARTISTIC DESIGNS\back of head.jpg");
clock = pygame.time.Clock();

def draw_background():
    window_screen.blit(lipstick_base, (0, 0));

def draw_Head(new_head , x, y):
    window_screen.blit(upper_head, (x, y));
    #window_screen.blit(new_head, (x, y));

def move_Head(x, y, velocity):
    for i in range(100):
        draw_Head(x, y + i*velocity);

def draw_Up(x, y):
    window_screen.blit(backOfHead, (x , y));

def lips_move():
    
    run = True;
    pos_x = WIN_WIDTH//2;
    pos_y = WIN_HEIGHT//4;
    velocity = 1;
    pos = 1;
    y_inc = 80;
    while run :
        draw_background();
        clock.tick(20);
        #draw_Head(pos_x - 40, pos_y - 70);
        #new_head = pygame.transform.rotate(upper_head, -45);
        #if pos == 1:
        #    for i in range(90):
        #new_head = pygame.transform.rotate(upper_head, -45 + i/2);
        #window_screen.blit(new_head, (pos_x - 55, pos_y + i * velocity - 70 - y_inc));
        draw_Head(upper_head, pos_x - 55, pos_y + pos * velocity - 70 - y_inc);
        
        if pos < 202+y_inc:
            pos += 1;
        if pos > 100 and pos <= 202 + y_inc:
            draw_Up(pos_x - 55, pos_y + pos*velocity - 197 - y_inc);
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = False;
                pygame.quit();
                quit();
        pygame.display.update();
        pygame.display.flip();

if __name__ == "__main__":
    lips_move();
