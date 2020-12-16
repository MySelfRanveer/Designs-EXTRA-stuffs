import turtle;
from pygame import mixer;
#import playsound;
#import os;

#playsound.playsound('backgroundSoundOfDesigns.mp3');
#os.system("backgroundSoundOfDesigns.mp3");
mixer.init();
mixer.music.load(r"C:\Users\RANVEER\Desktop\PYTHON\Game using python\Design Projects\backgroundSoundOfDesigns.mp3");
mixer.music.play();

def draw_square(pen) :
    for i in range(1,5):
        pen.forward(200);
        pen.right(90);

def draw_art():
    screen = turtle.Screen();
    screen.bgcolor('black');
    turt = turtle.Turtle();
    turt.shape('turtle');
    turt.color('yellow');
    turt.speed(10);
    turt.pensize(2);
    for i in range(1,37):
        draw_square(turt);
        turt.right(10);
    nextTurt = turtle.Turtle();
    nextTurt.shape('turtle');
    nextTurt.color('blue');
    nextTurt.speed(20);
    nextTurt.pensize(2);
    size = 1;
    x = 700;
    while x > 0 :
        nextTurt.forward(size);
        nextTurt.right(91);
        size += 1;
        x -= 1;
    nextTurt.ht();
    screen.exitonclick();


def drawSquareSpiral() :
    screen = turtle.Screen();
    screen.bgcolor('black')
    pen = turtle.Turtle();
    pen.shape('turtle');
    pen.color('red');
    pen.speed(20);
    pen.pensize(1);
    size = 1;
    while True :
        pen.forward(size);
        pen.right(91);
        size += 1;
    pen.ht();
    screen.exitonclick();


#drawSquareSpiral();
draw_art();
mixer.music.stop();

"""
from turtle import *;
color('red', 'yellow');
begin_fill();
while True :
    forward(200);
    left(170);
    if abs(pos()) < 1 :
        break;
end_fill();
done();
"""
"""
import turtle;
pen = turtle.Turtle();
n = 10;
for i in range(n * 3):
    pen.forward(i * 10);
    pen.right(120);

turtle.done();
"""
