'''
Created on Jul 9, 2018

@author: yiyedang
'''
import turtle
import random

def draw_tree(branchLen, t):
    if branchLen < 10:
        return
    elif branchLen > 10 and branchLen < 12:
        t.color("darkgreen")
        t.forward(branchLen)
        t.left(30)
        draw_tree(3 * branchLen / 4, t)
        t.right(60)
        draw_tree(3 * branchLen / 4, t)
        t.left(30)
        t.up()
        t.backward(branchLen)
        t.down()
    else:
        t.color("brown")
        t.forward(branchLen)
        t.left(30)
        draw_tree(3 * branchLen / 4, t)
        t.right(60)
        draw_tree(3 * branchLen / 4, t)
        t.left(30)
        t.up()
        t.backward(branchLen)
        t.down()
        
t = turtle.Turtle()
wn = turtle.Screen()
t.speed(10)
t.left(90)
t.backward(100)
draw_tree(100, t)

wn.exitonclick()
