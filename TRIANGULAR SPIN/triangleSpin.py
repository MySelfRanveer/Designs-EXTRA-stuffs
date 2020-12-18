import turtle;

def draw_triangle(pen, size):
    for i in range(3):
        pen.forward(size);
        pen.right(120);

def draw_spin():
    screen = turtle.Screen();
    screen.bgcolor('black');
    #colors = ['red', 'yellow', 'green', 'magenta', 'blue', 'orange'];
    red = 255;
    green = 0;
    blue = 0;

    pen = turtle.Turtle();
    pen.speed(0);
    pen.pensize(2);
    size = 40;
    for i in range(255*2):                          #Total Rotations
        screen.colormode(255);                      #setting color for screen
        if(i < 255//3):                             #why divisible by 3 ? --> because we have only red, green, blue (3 colors combinations);
            green += 3;
        elif i < 255 * 2 // 3:
            red -= 3;
        elif i < 255 :
            blue += 3;
        elif i < 255 * 4 // 3:
            green -= 3;
        elif i < 255 * 5 // 3:
            red += 3;
        else :
            blue -= 3;
        pen.forward(size + i);                      #drawing of one side of square with increasing size
        pen.right(120.5);                           #Rotation of square at each four angle with 0.5 --> total rotation = 0.5 * 4 = 2
        pen.pencolor(red, green, blue);
    
    pen.ht();
    screen.exitonclick();

if __name__ == "__main__":
    draw_spin();
