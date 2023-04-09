import pygame as pg
import sys

# The use of the main function is described in Chapter 9.

# Define some colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Function of Stick Figure
def draw_stick_figure(screen, x, y):
    # Head
    pg.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)

    # Legs
    pg.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pg.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)

    # Body
    pg.draw.line(screen, RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)

    # Arms
    pg.draw.line(screen, RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pg.draw.line(screen, RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)


def main():
    """Main function for the game."""
    pg.init()

    # Set the width and height of the screen [width,height]
    size = [1700, 800]
    screen = pg.display.set_mode(size)

    pg.display.set_caption("My Game")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pg.time.Clock()

    # Hide the mouse cursor
    pg.mouse.set_visible(1)

    # -------- Main Program Loop -----------
    while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
                # Close the window and quit.
                pg.quit()
                sys.exit()
                quit()

        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
        pos = pg.mouse.get_rel()
        pos2 = pg.mouse.get_pos()
        x = pos[0] + pos2[0]
        y = pos[1] + pos2[1]

        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(WHITE)

        draw_stick_figure(screen, x, y)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Go ahead and update the screen with what we've drawn.
        pg.display.flip()

        # Limit to 60 frames per second
        clock.tick(60)

        pg.time.delay(10)


if __name__ == "__main__":
    main()
