def square(length, angle):
    for i in range(angle):
        t.forward(length)
        t.left(360/angle)

import turtle
t=turtle.Turtle()
t.shape("turtle")

length=int(input("변의 길이를 입력하세요:"))
angle=int(input("각의 개수를 입력하세요:"))
square(length, angle)
length=int(input("변의 길이를 입력하세요:"))
angle=int(input("각의 개수를 입력하세요:"))
square(length, angle)
length=int(input("변의 길이를 입력하세요:"))
angle=int(input("각의 개수를 입력하세요:"))
square(length, angle)
