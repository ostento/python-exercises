from swampy.TurtleWorld import *
from math import *
def tree(t, length, n, angle = 30):
	if n==0:
		return
	fd(t, length*n)
	lt(t, angle)
	tree(t, length, n-1, angle)
	rt(t, 2*angle)
	tree(t, length, n-1, angle)
	lt(t, angle)
	bk(t, length*n)

def koch(t, length, n,angle=60):
	if n<3:
		fd(bob, length)
	else:
		l = length/3.0
		print l
		koch(t, l, n-1, angle)
		lt(t, angle)
		koch(t, l, n-1, angle)
		rt(t, angle*2)
		koch(t, l, n-1, angle)
		lt(t, angle)
		koch(t, l, n-1, angle)

def koch_snowflake(t, length, n, angle=60):
	for i in range(3):
		koch(t, length, n, angle)
		rt(t, angle*2)

def torn_square(t,  n, length=1500,angle=85):
	move(bob, 200,200)
	for i in range(4):
		koch(bob, 1500, 7, angle)
		lt(bob, 90)

def move(t, x, y):
	'''precondition: oriented along the x axis'''
	pu(t)
	fd(t, x)
	rt(t, 90)
	fd(t, y)
	lt(t, 90)
	pd(t)


world=TurtleWorld()
bob = Turtle()
bob.delay = .001

'''This was code to make a patterned field with the koch curve'''
#colors=['red','orange','yellow', 'green', 'blue', 'violet']
# for i in range(200):
# 	bob.pen_color = colors[i%6]
# 	print i%10
# 	print bob.pen_color
# 	snowflake(bob, i*10, 4)
# 	lt(bob, i*45)


world.canvas.dump()
wait_for_user()


