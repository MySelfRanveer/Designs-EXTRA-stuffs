#Spiral Circle Designs

import turtle, math, random;

#drawConcentrics() method draw concentic circles of different radii
def drawConcentrics(name, size, rotation, x, minus):
    def drawCircles(t, size, x):                                        #Drawing of 4 circles with varrying sizes
        for i in range(4):
            t.circle(size);
            size -= minus + x;
    
    def drawSpecial(t, size, repeat, x):                                #number of repetitions of each concentric circles
        for i in range(repeat):
            drawCircles(t, size, x);
            t.right(360/repeat);
    drawSpecial(name, size, rotation, x);



"""
def circleName(name, i):
    name.speed(0);
    name.color('{}'.format(ar[i]))
    return name;


first = circleName(nameS, 0)
second = circleName(nameS, 1);
third = circleName(nameS, 2);
forth = circleName(nameS, 3);
fifth = circleName(nameS, 4);
sixth = circleName(nameS, 5);
"""

#Main Method
def drawCircleSpiralGenerator(): 
    screen = turtle.Screen();
    screen.bgcolor('black');
    ar = ['white', 'yellow', 'blue', 'orange' , 'magenta', 'red'];

    FIRST = turtle.Turtle();                                            #First White Pen
    FIRST.speed(0);
    FIRST.color('{}'.format(ar[0]));

    SECOND = turtle.Turtle();                                           #Second Yellow Pen
    SECOND.speed(0);
    SECOND.color('{}'.format(ar[1]));

    THIRD = turtle.Turtle();                                            #Third Blue Pen
    THIRD.speed(0);
    THIRD.color('{}'.format(ar[2]))

    FORTH = turtle.Turtle();                                            #Fourth Orange Pen
    FORTH.speed(0);
    FORTH.color('{}'.format(ar[3]));

    FIFTH = turtle.Turtle();                                            #Fifth Magenta Pen
    FIFTH.speed(0);
    FIFTH.color('{}'.format(ar[4]));

    SIXTH = turtle.Turtle();                                            #Sixth Red Pen
    SIXTH.speed(0);
    SIXTH.color('{}'.format(ar[5]));

    minus = random.randint(-10, 10);
    x = 5;
    while x > 0 :
        size = 100;
        drawConcentrics(FIRST , size, random.randint(1, 10), 62, minus);
        drawConcentrics(SECOND, size, random.randint(1, 10), -2*minus, minus);
        drawConcentrics(THIRD, size, random.randint(1,10), -3, minus);
        #drawConcentrics(FORTH, size, random.randint(1,10), 2, minus);
        drawConcentrics(FIFTH, size, random.randint(1,10), 0, minus);
        #drawConcentrics(SIXTH, size, random.randint(1,10), -45, minus);
        x -= 1;
    turtle.ht();
    screen.exitonclick();
    
if __name__ == "__main__":
    drawCircleSpiralGenerator();
