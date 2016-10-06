# Visualize recursion by using the turtle module to recursively draw a spiral

import turtle

my_turtle = turtle.Turtle()
my_win = turtle.Screen()

def draw_spiral(my_turtle, line_len):
	if line_len > 0:
		my_turtle.forward(line_len)
		my_turtle.right(90)
		draw_spiral(my_turtle, line_len - 5)

draw_spiral(my_turtle, 100)
my_win.exitonclick()