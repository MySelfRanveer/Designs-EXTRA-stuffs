import turtle;

def draw_tri(pen, size):
    for i in range(3):
        pen.forward(size);
        pen.right(120);
    pen.left(60);

def draw_spatterns():
    screen = turtle.Screen();
    screen.bgcolor('black');
    colors = ['red', 'yellow', 'green', 'magenta', 'blue'];

    pen = turtle.Turtle();
    pen.speed(0);
    dir = 1;
    pen.ht();
    for i in range(400):
        dir = dir * -1;
        #pen.pencolor(colors[i % 5]);
        pen.color('black', colors[i % 5]);
        pen.begin_fill();
        draw_tri(pen, dir*(40 + i));
        pen.end_fill();
    pen.ht();
    screen.exitonclick();

def draw_amazingPattern(size):
    screen = turtle.Screen();
    screen.bgcolor('black');
    colors = ['red', 'yellow', 'green', 'cyan', 'magenta', 'orange', 'blue'];
    pen = turtle.Turtle();
    #pen.pencolor('yellow');
    pen.pensize(3);
    pen.speed(0);
    x = 0;
    i = 1;
    while x < 60:
        for i in range(6):
            pen.color('black', colors[i % 7]);
            pen.begin_fill();
            #for j in range(6):
            draw_tri(pen, size);
            pen.end_fill();
        if i % 2 == 0:
            pen.forward(size*(-1)**i);
            pen.right(60 * (-1)**i);
        else:
            pen.forward(size*(1)*2);
            pen.left(60 * (-1)**i);
        if(x % 6 == 5):
            pen.left(360//30*i);
            pen.forward(size*2);
        x += 1;
    pen.ht();
    screen.exitonclick();

if __name__ == "__main__":
    #draw_spatterns();
    draw_amazingPattern(40);