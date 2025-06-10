import turtle

draw = turtle.Turtle()
draw.clearscreen()
draw.penup()
draw.home()
draw.pendown()
totalangle = 0
length = float(input())
angle = float(input())
draw.clearscreen()
draw.penup()
draw.home()
draw.pendown()
while True:    #This simulates a Do Loop
    draw.forward(length)
    draw.right(angle)
    totalangle = totalangle + int(angle)
    if totalangle % 360 == 0: break
