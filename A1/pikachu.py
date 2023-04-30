import turtle as t

def eye(position1,position2,size,radius):
    '''() -> NoneType
Draw 2 circles

'''
    t.penup()
    t.goto(position1,position2)
    t.pendown()
    t.begin_fill()
    t.fillcolor('grey4')
    t.circle(size)
    t.end_fill()
    t.penup()
    t.goto(position1+15,position2+40)
    t.pendown()
    t.begin_fill()
    t.fillcolor('azure')
    t.circle(size*0.45)
    t.end_fill()

def nose():
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.begin_fill()
    t.fillcolor('grey18')
    t.left(45)
    t.fd(25)
    t.left(90)
    t.circle(25,90)
    t.left(90)
    t.fd(25)
    t.end_fill()

def face(star,position1,position2):
    t.pencolor('brown1')
    t.penup()
    t.goto(position1,position2)
    t.degrees(90)
    t.pendown()
    t.begin_fill()
    t.fillcolor('brown2')
    i=1
    while i<=star:
        t.fd(100)
        t.right(144)
        i+=1
    t.end_fill()
    

def mouse():
    t.pencolor('grey13')
    t.pensize(3)
    t.penup()
    t.goto(0,-20)
    t.pendown()
    t.begin_fill()
    t.fillcolor('firebrick3')
    t.left(60)
    t.fd(90)
    t.circle(-30,15)
    t.penup()
    t.circle(-30,-15)
    t.bk(90)
    t.pendown()
    t.right(53)
    t.fd(90)
    t.circle(30,15)
    t.penup()
    t.circle(30,-15)
    t.right(-65)
    t.fd(180)
    a=1
    for i in range(11):
        a+=0.5
        t.right(3)
        t.fd(a)
    t.fd(160)
    t.end_fill()
    
def tounge():
    t.penup()
    t.pencolor('firebrick4')
    t.bk(70)
    t.pendown()
    t.begin_fill()
    t.fillcolor('firebrick2')
    a=3
    for i in range(20):
        a+=0.47
        t.right(2.1)
        t.fd(a)
    t.fd(2)
    t.right(15)
    t.fd(110)
    a=1
    for i in range(11):
        a+=0.5
        t.right(3)
        t.fd(a)
    t.fd(95)
    t.end_fill()

def firstname():
    t.penup()
    t.pencolor('hotpink')
    t.goto(-30,205)
    t.right(9)
    t.pendown()
    t.fd(100)
    t.right(37)
    t.fd(100)
    t.bk(50)
    t.right(26)
    t.fd(25)
    t.hideturtle()

def square():
    t.penup()
    t.pencolor('orange')
    t.goto(45,190)
    t.pendown()
    t.begin_fill()
    t.fillcolor('orange')
    t.right(0.75)
    i=0
    while i<=3:
        t.fd(100)
        t.left(300)
        i+=1
    t.end_fill()
    t.penup()
    t.pencolor('cyan')
    t.goto(5,190)
    t.pendown()
    t.rt(30)
    i=0
    while i<10:
        t.fd(20)
        t.left(100)
        i+=1
        
def my_artwork():
    t.speed("fastest")
    t.penup()
    t.goto(0,-300)
    t.pendown()
    t.begin_fill()
    t.fillcolor('gold1')
    t.circle(300)
    t.end_fill()
    #t.screensize(bg='gold1')
    eye(-150,50,45,10)
    eye(150,50,45,10)
    nose()
    face(5,-300,-10)
    face(5,200,-10)
    mouse()
    tounge()
    firstname()
    square()
    t.done()

