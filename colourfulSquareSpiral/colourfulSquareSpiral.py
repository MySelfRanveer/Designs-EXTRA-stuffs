import turtle;


"""
**LOGIC EXPLANATION**

color : 0, 1, 2, 3, 4, . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ., 255
start pos : red=255, green=0, blue=0;
end pos : red=255, green=0, blue=0;

So, We have to go first :
from 0 to 255
then back
from 255 to 0;

FIRST ITERATION
distribute 0 to 255 into 3 parts --> 
1. 0 to 255//3          --> red remains constant; green increase by 3; blue remains constant;
2. 255//3 to 255*2//3   --> red decrease by 3; green remains const; blue remains const;
3. 255*2//3 to 255*3//3 --> red remains const; green remains const; blue increase by 3;

SECOND ITERATION
go back same step but instead of increase use decrease;

"""


def round_spirals():
    screen = turtle.Screen();
    screen.bgcolor('black');

    pen = turtle.Turtle();
    pen.speed(100);
    #starting with red color in center
    red = 255;                                      #as maximum value = 255 --> so red value needs to be decreased;
    green = 0;                                      #needs to be increased;
    blue = 0;                                       #needs to be increased;

    for i in range(255*2):                          #Total Rotations
        screen.colormode(255);                      #setting color for screen
        if(i < 255//3):                             #why divisible by 3 ? --> becoz we have only red, green, blue (3 colors combinations);
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
        pen.forward(50 + i);                        #drawing of one side of square with increasing size
        pen.right(90.5);                            #Rotation of square at each four angle with 0.5 --> total rotation = 0.5 * 4 = 2
        pen.pencolor(red, green, blue);
    
    print(str(red) + " " + str(green) + " " + str(blue));
    pen.ht();
    screen.exitonclick();

if __name__ == "__main__":
    round_spirals();
