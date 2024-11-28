import turtle
window = turtle.Screen()
window.title("Hình ảnh đồ họa - Hình tròn lồng nhau")
window.bgcolor("white")
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)
colors = ["red", "blue", "green", "orange", "purple"]
def draw_circle_pattern(radius, step, repeat):
    for i in range(repeat):
        pen.color(colors[i % len(colors)])
        pen.circle(radius)
        pen.right(step)
draw_circle_pattern(radius=100, step=30, repeat=12)
pen.hideturtle()
window.mainloop()
