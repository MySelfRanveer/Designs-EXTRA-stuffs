import turtle, math;
color = ['red', 'green', 'blue', 'yellow', 'magenta', 'cyan'];

#draw_square() method creates one single square
def draw_square(pen, size):
    for i in range(1,5):
        pen.forward(size);                  #length of side of square
        pen.right(90);

#draw_star() method creates one paired spikes of star
def draw_star(pen, size):
    val = float(3 * math.sqrt(2));          #angle between two spikes of outer circle --> angleOfBTWSpikes = angle * sqrt(2);
    pen.right(val/2);
    pen.forward(size);
    pen.right(180 - val/2);                 #reversing spikes
    pen.forward(size);
    pen.left(180 - val/2);                  #reReversing spikes

#Main method
def drawColorfulSquare(size):
    screen = turtle.Screen();               #Screen for Project
    screen.bgcolor('black');
    turt = turtle.Turtle();                 #turtle (pen)
    turt.shape('turtle');
    turt.speed(20);
    turt.pensize(2);
    j = 0;
    for i in range(1,121):                  #looping 120 times --> why ? --> angle btw each inner spikes = 3 --> 360 / 3 = 120;
        turt.color(color[i % 6]);
        draw_square(turt, size);            #drawing single squares
        turt.right(3);                      #angle btw each inner spikes
        j = i % 6;
    
    turt.color(color[j + 1]);               #Next coloured pen
    #Reaching outside the bigger circle
    turt.forward(size);
    turt.right(90);
    turt.forward(size);
    turt.color(color[3]);
    turt.left(45);                          #making pen staright
    size = size * math.sqrt(2);             #size of spikes should be radius of outer circle
    for i in range(1, 171):                 #looping 170 times --> why ? --> angle btw each outer spike = 3 * sqrt(2) --> angle taken for one spike making = 3 * sqrt(2) / 2 --> 360 * sqrt(2) / 3 = 170;
        draw_star(turt, size);              #drawing one single pair of spikes
    
    turt.ht();                              #hide turtle (pen);
    screen.exitonclick();
#size (argument passed) = length of side of each squares;
if __name__ == "__main__":
    drawColorfulSquare(130);
