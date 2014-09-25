import  pygame
import Agent
from time import sleep

BOARDSIZE = 1024

def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surface_sz = BOARDSIZE   # Desired physical surface size, in pixels.

    # Create surface of (width, height), and its window.
    main_surface = pygame.display.set_mode((surface_sz, surface_sz))
    ndim = 2 # number of dimensions
    # Create a bunch of agents
    al = []
    for i in range(0,1090):
        al.append(Agent.Agent(ndim, i))

    Agent.Agent.place([BOARDSIZE, BOARDSIZE])
    
    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break    #   ... leave game loop

        # Update your game objects and data structures here...

        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        #main_surface.fill((0,0,0))
        for i in al:
            try:
                z = i.loc()[0] + i.loc()[1]
            except TypeError:
                print("Invalid agent coordinates", i.loc())
            main_surface.set_at(i.loc(), (255,0,0))

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        # clear the agents for their next move
        for i in al:
            main_surface.set_at(i.loc(), (0,0,0))
        #sleep(.1)

        Agent.Agent.move(BOARDSIZE)

    pygame.quit()     # Once we leave the loop, close the window.

main()


