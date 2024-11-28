print("Pham Viet Quan Mssv 235752021610022")
import turtle
window = turtle.Screen()
window.title("Vẽ hình vuông với turtle")
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("blue")
pen.speed(3)
for _ in range(4):
    pen.forward(100)
    pen.left(90)
pen.hideturtle()
window.mainloop()
