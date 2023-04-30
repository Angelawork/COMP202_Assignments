#name: Angela(Qingchen) Hu, McGill student ID: 261075832
import turtle
def circle(radius, x, y, color):
    '''(float, int, int, str) -> NoneType
    Draws a circle of the given radius at the
    given coordinates: x and y, with the given color.
    '''
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.circle(radius)
    turtle.end_fill()
    
def eyes(x,y):
    '''(int, int) -> NoneType
    Draws 2 circles to represent eyes at the
    given coordinates: x and y.
    A small circle is drawn within the
    large circle to represent the pupil.
    '''
    circle(45.0, x, y, 'grey4')
    circle(45.0 * 0.45, x+15, y+40, 'azure')

def nose():
    '''() -> NoneType
    Draws a shape to represent the nose.
    '''
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor('grey18')
    
    turtle.left(45)
    turtle.forward(25)
    turtle.left(90)
    turtle.circle(25,90)
    turtle.left(90)
    turtle.forward(25)
    turtle.end_fill()

def face(x,y):
    '''(int, int) -> NoneType
    Draws a pentagram to represent cheek
    at the given coordinates: x and y.
    '''
    turtle.color('brown1')
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor('brown2')
    
    i=1
    while i<=5:
        turtle.forward(100)
        turtle.right(216)
        i+=1
    turtle.end_fill()

def curve(parameter1, parameter2, step_length, angle):
    '''(float, int, float, int) -> NoneType
    Draws a curve with the given conditions:
    parameter1, parameter2, which determine the curve's size;
    as well as step_length, angle, which determine
    the amount of distance and angle the turtle travels
    in each iteration.
    '''
    a=parameter1
    for i in range(parameter2):
        a+=step_length
        turtle.right(angle)
        turtle.forward(a)

def lips_and_mouth():
    '''() -> NoneType
    Draws 2 lines and a shape to
    represent the lips and mouth.
    '''
    turtle.color('grey13')
    turtle.penup()
    turtle.goto(0,-20)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor('firebrick3')
    
    turtle.left(240)
    turtle.forward(90)
    turtle.circle(-30,60)
    turtle.circle(-30,-60)
    turtle.backward(90)
    turtle.right(212)
    turtle.forward(90)
    turtle.circle(30,60)
    turtle.circle(30,-60)
    
    turtle.right(-260)
    turtle.forward(180)
    curve(1.0, 11, 0.5, 12)
    turtle.forward(160)
    turtle.end_fill()

def tongue():
    '''() -> NoneType
    Draws a shape to represent the tongue.
    '''
    turtle.penup()
    turtle.color('firebrick4')
    turtle.backward(70)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor('firebrick2')
    
    curve(3.0, 20, 0.47, 8.4)
    turtle.forward(2)
    turtle.right(60)
    turtle.forward(110)
    curve(1.0, 11, 0.5, 12)
    turtle.forward(95)
    turtle.end_fill()

def firstname():
    '''() -> NoneType
    Draws the the first letter of the
    author's first name:"A" to sign the artwork.
    '''
    turtle.penup()
    turtle.color('HotPink')
    turtle.goto(-30,205)
    turtle.right(36)
    turtle.pendown()
    
    turtle.forward(100)
    turtle.right(148)
    turtle.forward(100)
    turtle.backward(50)
    turtle.right(104)
    turtle.forward(25)

def polygon(n,side_length):
    '''(int, float) -> NoneType
    Draws a polygon with n sides which have
    the given side_length.
    '''
    i=0
    while i<=n:
        turtle.forward(side_length)
        turtle.left(360/n)
        i+=1
    
def triangle():
    '''() -> NoneType
    Draws a triangle.
    '''
    turtle.penup()
    turtle.color('orange')
    turtle.goto(45,190)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor('orange')
    
    turtle.right(3)
    polygon(3,100.0)
    turtle.end_fill()

def nonagon():
    '''() -> NoneType
    Draws a nonagon.
    '''
    turtle.penup()
    turtle.color('cyan')
    turtle.goto(5,190)
    turtle.pendown()
    
    turtle.right(120)
    polygon(9,20.0)

def background():
    '''() -> NoneType
    Draws a circle to represent background.
    '''
    turtle.penup()
    turtle.goto(0,-300)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor('gold1')
    turtle.circle(300)
    turtle.end_fill()
        
def my_artwork():
    '''() -> NoneType
    Change the turtle settings and calls the other
    functions to draw the entire artwork.
    '''
    turtle.speed("fastest")
    turtle.pensize(3)
    background()
    eyes(-150, 50)
    eyes(150, 50)
    nose()
    face(-300, -10)
    face(200, -10)
    lips_and_mouth()
    tongue()
    firstname()
    triangle()
    nonagon()
