# powered by pygame tm
import pygame
#player.py holds player class and functions

from player import *


# constants holds all the  ... constants
from constants import *
#asteroids stuff
from asteroid import *
# making asteroids and how
from asteroidfield import *

#still not 100% sure why we run the program in a function... 
def main():

# set up pygame defaults
    pygame.init()

# let user know things are happening, and resolution set
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
# set up groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
#pygame magic to make a playing window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# deffo did this wrong, but just in case there is a need to kill the game, update this variable with a key press
    game = "on"

# tick tick etc
    clock = pygame.time.Clock() 

# to get the frame rate relate to the other defined speeds in game, stopping things going to fast 
    dt = 0
    

# Create the player (triangle but really a circle) ship
    player = Player((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2),PLAYER_RADIUS)

#set the field in place
    asteroid_field = AsteroidField()

# litteral gameplay loop
    while game == "on":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
# paint it all black
        screen.fill(000)
    #do the space ship and rock things like flying n stuff
        updatable.update(dt)
    #and show that on the screen
        for thing in drawable:
            thing.draw(screen)
    # frame happens
        pygame.display.flip()
    # frame rate limit and adjustment for ms for ratios in other places
        dt = clock.tick(60) /1000
        



# only run if actually run as main.py
if __name__ == "__main__":
    main()

