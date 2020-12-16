import turtle;

def rainbowBenzene():
    colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red'];
    pen = turtle.Pen();
    pen.speed(20);
    turtle.bgcolor('black');

    for x in range(360):
        pen.pencolor(colors[x % 7]);
        pen.width(x / 100 + 1);
        pen.forward(x);
        pen.left(59);
    
    pen.ht();
    turtle.exitonclick();

def rainbowBenzeneOnly():
    colors = ['red','purple','cyan','green','magenta','yellow'];
    pen = turtle.Pen();
    pen.speed(20);
    turtle.bgcolor('black');

    for x in range(360):
        pen.pencolor(colors[x % 6]);                               #This makes choice of colors
        pen.width(x / 100 + 1);
        pen.forward(x);
        pen.left(59);
    
    pen.ht();
    turtle.exitonclick();

def rainbowBenzeneSpiral():
    colors = ['red','green','blue','red','green','blue'];
    pen = turtle.Pen();
    pen.speed(20);
    turtle.bgcolor('black');

    for x in range(360):
        pen.pencolor(colors[x % 6]);                               #This makes spiral good
        pen.width(x / 100 + 1);
        pen.forward(x);
        pen.left(59);
    
    pen.ht();
    turtle.exitonclick();

if __name__ == "__main__":
    #rainbowBenzeneOnly();
    #rainbowBenzene();
    rainbowBenzeneSpiral();
