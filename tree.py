'''
Created on Jul 10, 2018

@author: yiyedang
'''
import turtle
import random

def tree(branchLen,t, pen):
    if branchLen > 20:
        t.pensize(pen)
        pen = pen - 1
        t.color("brown")
        sub = random.randrange(10,15)
        angle = random.randrange(10,45)
        t.forward(branchLen)
        t.right(angle)
        tree(branchLen-sub,t, pen)
        t.left(angle*2)
        tree(branchLen-sub,t, pen)
        t.right(angle)
        t.up()
        t.backward(branchLen)
        t.down()
    elif (branchLen > 5) and (branchLen < 20):
        t.pensize(pen)
        t.color("darkgreen")
        pen = pen - 1
        t.forward(branchLen)
        t.up()
        t.backward(branchLen)
        t.down()

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.speed(10)
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    t.color("brown")
    tree(100, t, 8)
    myWin.exitonclick()

main()
