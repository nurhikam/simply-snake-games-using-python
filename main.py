import pygame
import time
import random

# set the snake speed
snake_speed = 12

# set size of the wall 
window_x = 960
window_y = 540

# initialise color will use
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
blue = pygame.Color(0, 0, 255)
yellow = pygame.Color(196, 195, 0)

# initialising pygame method
pygame.init()

# Initialise game window
pygame.display.set_caption('Snake Games')
game_window = pygame.display.set_mode((window_x, window_y))
 
# FPS (frames per second) controller
fps = pygame.time.Clock()

# defining snake default position
snake_position = [150, 100]

# defining first 4 blocks of snake
# body
snake_body = [ [100, 50],
				[90, 50],
				[80, 50],
				[70, 50]]
# fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10,
			    random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True

# set default snake direction
# towards right
direction = 'RIGHT'
change_to = direction

# initialise default score
score = 0

# display score function
def show_score(choice, color, font, size):

  # create font object named score_font
	score_font = pygame.font.SysFont(font, size)
	
	# create the display surface object named score_surface
	score_surface = score_font.render('Score : ' + str(score), True, color)
	
	# create a rectangular object for the text surface object
	score_box = score_surface.get_rect()
	
	# displaying the text
	game_window.blit(score_surface, score_box)
 
# game over function
def game_over():

	# creating font object my_font
	my_font = pygame.font.SysFont('times new normal', 50)
	
	# creating a text surface on which text will be drawn
	game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
	
	# create a rectangular object for the text surface object
	game_over_box = game_over_surface.get_rect()
	
	# setting position of the text
	game_over_box.midtop = (window_x/2, window_y/4)
	
	# blit will draw the text on screen
	game_window.blit(game_over_surface, game_over_box)
	pygame.display.flip()
	
	# after 2 seconds we will quit the program
	time.sleep(2)
	
	# deactivating pygame library
	pygame.quit()
	
	# quit the program
	quit()

# Main Function
while True:

	# handling key events
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				change_to = 'UP'
			if event.key == pygame.K_DOWN:
				change_to = 'DOWN'
			if event.key == pygame.K_LEFT:
				change_to = 'LEFT'
			if event.key == pygame.K_RIGHT:
				change_to = 'RIGHT'

	# If two keys pressed simultaneously the snake will not to move into two directions simultaneously
	if change_to == 'UP' and direction != 'DOWN':
		direction = 'UP'
	if change_to == 'DOWN' and direction != 'UP':
		direction = 'DOWN'
	if change_to == 'LEFT' and direction != 'RIGHT':
		direction = 'LEFT'
	if change_to == 'RIGHT' and direction != 'LEFT':
		direction = 'RIGHT'

	# Moving the snake
	if direction == 'UP':
		snake_position[1] -= 10
	if direction == 'DOWN':
		snake_position[1] += 10
	if direction == 'LEFT':
		snake_position[0] -= 10
	if direction == 'RIGHT':
		snake_position[0] += 10

	# Snake body growing mechanism
	# if fruits and snakes collide then scores will be incremented by 10
	snake_body.insert(0, list(snake_position))
	if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
		score += 100
		fruit_spawn = False
	else:
		snake_body.pop()
		
	if not fruit_spawn:
		fruit_position = [random.randrange(1, (window_x//10)) * 10,
						random.randrange(1, (window_y//10)) * 10]
		
	fruit_spawn = True
	game_window.fill(black)
	
	for pos in snake_body:
		pygame.draw.rect(game_window, yellow, pygame.Rect(
		pos[0], pos[1], 10, 10))
		
	pygame.draw.rect(game_window, white, pygame.Rect(
	fruit_position[0], fruit_position[1], 10, 10))

	# Game Over conditions
	if snake_position[0] < 0 or snake_position[0] > window_x-10:
		game_over()
	if snake_position[1] < 0 or snake_position[1] > window_y-10:
		game_over()
	
	# Touching the snake body
	for block in snake_body[1:]:
		if snake_position[0] == block[0] and snake_position[1] == block[1]:
			game_over()
	
	# displaying score countinuously
	show_score(1, white, 'times new normal', 20)
	
	# Refresh game screen
	pygame.display.update()

	# Frame Per Second /Refresh Rate
	fps.tick(snake_speed)

