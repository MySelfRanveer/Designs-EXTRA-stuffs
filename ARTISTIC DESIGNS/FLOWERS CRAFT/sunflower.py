import turtle;

def draw_sunflower():
    screen = turtle.Screen();
    screen.bgcolor('black');
    color = ['red', 'yellow', 'magenta', 'orange', 'blue'];

    pen = turtle.Turtle();
    pen.speed(20);
    pen.color('black', 'red');
    #pen.ht();
    x = 0;
    while x < 500:
        pen.color('black', color[x % 5]);
        pen.begin_fill();
        for i in range(50):
            pen.forward(300);
            pen.left(170);
        pen.end_fill();
        x += 1;
    
    screen.exitonclick();

if __name__ == "__main__":
    draw_sunflower();