#
# FILENAME: drawings.py | APCSP SmileyBugProject
# DESCRIPTION: Draw on the screen
# CREATED: 2023-03-20 @ 12:16 PM
# COPYRIGHT: Copyright (c) 2023 by Ryan Smith
#

from turtle import Turtle

def draw_face(turtle: Turtle) -> None:
	""" Draw the smiley face. """

	turtle.penup()

	FACE_RADIUS = 300
	EYE_RADIUS = 30
	EYE_POS = 150

	# Move the turtle to the bottom of the circle. Once the circle is drawn,
	# it will have a radius of 300 and be centered on the screen. 
	turtle.goto(turtle.xcor(), turtle.ycor() - FACE_RADIUS)
	turtle.pendown()

	# The face will be a yellow circle with a yellow outline
	turtle.pencolor("yellow")
	turtle.fillcolor("yellow")
	
	# Draw the face
	turtle.begin_fill()
	turtle.circle(FACE_RADIUS)
	turtle.end_fill()

	#
	# Draw the eyes
	#

	turtle.penup()
	turtle.goto(-EYE_POS, EYE_POS - EYE_RADIUS)
	turtle.pendown()

	turtle.pencolor("black")
	turtle.fillcolor("black")
	
	# Left eye
	turtle.begin_fill()
	turtle.circle(EYE_RADIUS)
	turtle.end_fill()

	turtle.penup()
	turtle.goto(EYE_POS, turtle.ycor())
	turtle.pendown()
	
	# Right eye
	turtle.begin_fill()
	turtle.circle(EYE_RADIUS)
	turtle.end_fill()

	turtle.penup()
	turtle.goto(
		start_x := turtle.xcor() + 50,
		start_y := turtle.ycor() - 100
	)
	turtle.pendown()

	# Mouth
	turtle.begin_fill()
	turtle.left(90)
	turtle.circle(200, -180)
	turtle.goto(start_x, start_y)
	turtle.end_fill()

def draw_spider(turtle: Turtle) -> None:
	""" Draw the spider. """

	turtle.penup()

	ORIGIN = turtle.pos()
	BODY_RADIUS = 200
	HEAD_RADIUS = 100
	LEGS = 8
	LEG_LENGTH = 1.5 * BODY_RADIUS

	turtle.pencolor("black")
	turtle.fillcolor("black")
	turtle.goto(turtle.xcor(), turtle.ycor() - BODY_RADIUS)
	turtle.pendown()

	# Draw the body
	turtle.begin_fill()
	turtle.circle(BODY_RADIUS)
	turtle.end_fill()

	turtle.penup()
	turtle.goto(turtle.xcor(), turtle.ycor() + BODY_RADIUS + HEAD_RADIUS)
	turtle.pendown()

	# Draw the head
	turtle.begin_fill()
	turtle.circle(HEAD_RADIUS)
	turtle.end_fill()

	turtle.penup()
	turtle.pensize(3)
	turtle.pencolor("black")

	# Postion the turtle to draw the legs
	turtle.goto(ORIGIN[0] + LEG_LENGTH, ORIGIN[1] - LEG_LENGTH)
	turtle.right(-90)

	# Draw the legs
	for leg_set in range(LEGS // 2):
		# Move the turtle outside of the body and orient it to draw an
		# arc from right to left
		turtle.pendown()

		#
		# Draw an arc, making two legs.
		#
		# For odd-numbered leg sets (1 and 3), draw the circle counter-clockwise.
		# Once the turtle is rotated after drawing, it will be on the opposite side
		# of the spider's body. This means that for even-numbered leg sets (2 and 4),
		# we need to draw the circle clockwise. Therefore, the radius should be negative
		# for sets 2 and 4.
		#
		turtle.circle(-LEG_LENGTH if (leg_set + 1) % 2 == 0 else LEG_LENGTH, 180)
		
		turtle.penup()
		
		# Reorient the turtle and move it forward to draw the next set
		turtle.right(180)
		turtle.forward(50)

