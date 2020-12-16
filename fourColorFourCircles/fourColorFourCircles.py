import turtle;

def draw_FourColors(rad, limit):
    vel = 50;
    screen = turtle.Screen();
    screen.bgcolor('black')
    pen = turtle.Turtle();
    pen.pencolor('red');
    pen.pensize(3);
    pen.speed(vel);

    for i in range(limit):
        pen.pencolor('red');
        pen.circle(rad + i*3);
    pen.circle(rad, 90);
    pen.right(180);
    for i in range(limit):
        pen.pencolor('blue');
        pen.circle(rad + i*3);
    pen.circle(rad, 90);
    pen.right(180);
    for i in range(limit):
        pen.pencolor('yellow');
        pen.circle(rad + i*3);
    pen.circle(rad, 90);
    pen.right(180);
    for i in range(limit):
        pen.pencolor('green');
        pen.circle(rad + i*3);


def drawCircle(rad, limit):
    pen = turtle.Turtle();
    pen.pensize(3);
    pen.speed(2);
    for i in range(limit):
        pen.pencolor('red');
        for j in range(2):
            pen.circle(rad, 120);
            pen.circle(rad, 90);

x = 1;
while x < 10:
    draw_FourColors(20, 50);
    #drawCircle(100,10);
    x += 1;




"""

    for i in range(2):
        pen.circle(rad, 90);
        pen.circle(rad, 90);
    pen.circle(rad, 90);
    pen.right(180);
    for i in range(2):
        pen.pencolor('blue');
        pen.circle(rad, 90);
        pen.circle(rad, 90);
    pen.circle(rad, 90)
    pen.right(180);
    for i in range(2):
        pen.pencolor('yellow');
        pen.circle(rad, 90);
        pen.circle(rad, 90);
    pen.circle(rad, 90);
    pen.right(180);
    for i in range(2):
        pen.pencolor('green');
        pen.circle(rad);
    


"""