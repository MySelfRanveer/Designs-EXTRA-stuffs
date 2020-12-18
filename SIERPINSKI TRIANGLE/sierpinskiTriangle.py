import turtle;

def draw_tri_levels(pen, side, levels, colors, index):
    """
    docstring
    """
    if(levels == 1):
        pen.color(colors[index % 5]);
        pen.begin_fill();
        for i in range(3):
            pen.forward(side);
            pen.left(120);
            pen.speed(10000);
        pen.end_fill();
    else:
        draw_tri_levels(pen, side//2, levels - 1, colors, index + 1);
        pen.forward(side//2);
        index += 1;
        pen.pencolor(colors[index % 5]);
        draw_tri_levels(pen, side//2, levels - 1, colors, index + 1);
        pen.back(side//2);
        pen.left(60);
        pen.forward(side//2);
        index += 1;
        pen.pencolor(colors[index % 5]);
        pen.right(60);
        draw_tri_levels(pen, side//2, levels - 1, colors , index + 1);
        pen.left(60);
        pen.back(side//2);
        index += 1;
        pen.pencolor(colors[index % 5]);
        pen.right(60);
        pen.speed(100000);

def draw_sierpinskiTri():
    bg = 'black';
    screen = turtle.Screen();
    screen.bgcolor(bg);
    colors = ['red', 'cyan', 'green', 'magenta', 'blue'];
    index = 0;

    pen = turtle.Turtle();
    pen.pencolor(bg);
    pen.goto(-350, -350);
    side = 800;
    draw_tri_levels(pen, side, 7, colors, index);
    pen.ht();
    screen.exitonclick();

if __name__ == "__main__":
    draw_sierpinskiTri();