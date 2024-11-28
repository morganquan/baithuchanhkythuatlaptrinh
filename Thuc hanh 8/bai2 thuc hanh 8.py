import turtle
window = turtle.Screen()
window.title("Vẽ bông hoa với turtle")
window.bgcolor("white")
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("red")
pen.speed(5)
def draw_petal():
    for _ in range(2):
        pen.circle(50, 60)
        pen.left(120)
for _ in range(6):
    draw_petal()
    pen.right(60)
pen.penup()
pen.goto(0, -30)
pen.pendown()
pen.color("yellow")
pen.begin_fill()
pen.circle(30)
pen.end_fill()
pen.hideturtle()
window.mainloop() 
