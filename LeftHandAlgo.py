from magame import mappy    # Import the Mappy game
from magame import mazes
import pygame

maze = mazes[1]

frontLeft = [1,0,0,0]
frontUp = [0,1,0,0]
frontRight = [0,0,1,0]
frontDown = [0,0,0,1]

faceDirection = [frontLeft,frontUp,frontRight,frontDown]

def find_edge(position):
	edgeCase = [0,0,0,0]
	for i in range(4):
		if (i == 0 and position[1] == 0):
			edgeCase[i] = 1
		elif (i == 1 and position[0] == 0):
			edgeCase[i] = 1
		elif (i == 2 and position[1] == 9):
			edgeCase[i] = 1
		elif (i == 3 and position[0] == 9):
			edgeCase[i] = 1
		else:
			edgeCase[i] = 0

	return edgeCase

def find_open_space(position):
	space = find_edge(position)
	for i in range(4):
		if (i == 0 and space[i] == 0):
			space[i] = maze[position[0]][position[1]-1]
		elif (i == 1 and space[i] == 0):
			space[i] = maze[position[0]-1][position[1]]
		elif (i == 2 and space[i] == 0):
			space[i] = maze[position[0]][position[1]+1]
		elif (i == 3 and space[i] == 0):
			space[i] = maze[position[0]+1][position[1]]

	return space

def turn_ninety_ccw(direction):
	for i in faceDirection:
		if i == direction:
			rotateCCW = faceDirection[faceDirection.index(i) - 1]

	return rotateCCW

def turn_ninety_cw(direction):
	for i in faceDirection:
		if i == direction:
			if (faceDirection.index(i) + 1 == 4):
				rotateCW = faceDirection[0]
			else:
				rotateCW = faceDirection[faceDirection.index(i) + 1]

	return rotateCW

def check_left_space_open(direction, openSpace):
	# this function checks if the left direction relative to the current direction is empty, if it is empty function returns true
	for i in range(len(direction)):
		if direction[i] == 1:
			if openSpace[i - 1] == 0 or openSpace[i - 1] == -1:
				return True
			else:
				return False

def check_forward_space_open(direction, openSpace):
	for i in range(len(direction)):
		if direction[i] == 1:
			if openSpace[i] == 0 or openSpace[i] == -1:
				return True
			else:
				return False


def maze_move(maze, position , memory):
	if (position == (0,0)):
		memory = frontDown

	openSpace = find_open_space(position)

	moveDown = (1,0)
	moveRight = (0,1)
	moveUp = (-1,0)
	moveLeft = (0,-1)
	static = (0,0)

	#remove loops from this function (having loops confuses the algo). The entire algo needs to be looped.

	# check for left walls, if left wall is open then turn ONCE cccw and then step forward
	if (check_left_space_open(memory, openSpace) == True):
		memory = turn_ninety_ccw(memory)
		# find direction key and movement value associated with it. then move forward
		if memory == frontLeft:
			move = moveLeft
		if memory == frontUp:
			move = moveUp
		if memory == frontRight:
			move = moveRight
		if memory == frontDown:
			move = moveDown

		return move, memory
	else:
		# check for front wall, if front wall is open go forward immidietly
		if (check_forward_space_open(memory, openSpace) == True):
			# find direction key and movement value associated with it
			if memory == frontLeft:
				move = moveLeft
			if memory == frontUp:
				move = moveUp
			if memory == frontRight:
				move = moveRight
			if memory == frontDown:
				move = moveDown

			return move, memory

		else:
			# if there isnt a front wall, then do a rotation clockwise ONCE
			memory = turn_ninety_cw(memory)
			move = static

			return move, memory


mappy.play(maze, maze_move)