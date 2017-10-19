# import the graphicsCS151 file so we have access to its functions
from graphicsCS151 import *

# Height and width of window, radius of the ball
# THIS IS ALREADY CODED FOR YOU
HEIGHT = 500
WIDTH = HEIGHT # keep it simple
radius = 20

# 1 - code a function that returns an int between a min value and a max value,
# two parameters of the function; that int is input by the user
# Assume that the user will enter an int (extra credit # 1 for checking if the user does)
# Add a third parameter so that the input question to the user can be
# customized when you call the function



# 2 - Use the function in 1 above to get the starting x and y coordinates
# from the user; make sure that the x coordinate is strictly greater than the y coordinate



# 3 - Create the window; use the make_window function
# Look at its function header in the graphicsCS151 file
# THIS IS ALREADY CODED FOR YOU
win = make_window( "Play Ball!", WIDTH, HEIGHT )

# 4 - Create the ball; use the make_circle function
# Look at its function header in the graphicsCS151 file



# 5 - Color the ball and draw it in the window; use the draw_and_color_circle function
# Look at its function header in the graphicsCS151 file



# 6 - Decide how fast your ball will be moving
# horizontal speed and vertical speed
# speed is essentially a number of pixels that the the ball will move
# at every iteration of the various loops



# 7 - 1st loop: move down and right
# To move the ball, use the move function
# Look at its function header in the graphicsCS151 file
# Do not move the ball too fast; use the sleep function to slow it down
# Look at its function header in the graphicsCS151 file
# At this stage, before actually coding this loop, you can test the move and sleep function


# 8 - move down and left



# 9 - move left and up



# 10 - move right and up



# During the testing stage, if you want to keep the window open at the end,
# write this code:
# point = win.getMouse( )

# Extra credit 1: test if the user input is an int, do not assume that it is (2 points)
# Extra credit 2: Drop the constraint x > y and correctly bounce off the walls 4 times (2 points)



