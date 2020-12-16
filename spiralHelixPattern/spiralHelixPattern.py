import turtle;
screen = turtle.Screen();
t = turtle.Pen()
colors = ['red', 'purple', 'orange', 'blue', 'yellow'];
t.speed(50);
for i in range(100) :
    t.pencolor(colors[i % 5]);
    t.circle(5 * i);
    t.circle(-5 * i);
    t.left(i);
t.exitonclick();