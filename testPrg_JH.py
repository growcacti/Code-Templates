from random import randint
import pygame as pg


class RD:
    @staticmethod
    def ddr():
        pg.init()
        # W is width and H is height constants
        W = 800
        H = 600
        hw = W / 2
        hh = H / 2
        center = (hw, hh)
        size = (W, H)

        def get_random_pos():
            X = randint(0, W - 1)
            Y = randint(0, H - 1)
            return (X, Y)

        def random_color():
            red = randint(0, 255)
            green = randint(0, 255)
            blue = randint(0, 255)
            return (red, green, blue)

        surface = pg.display.set_mode(size)
        pg.display.set_caption("JH Demo")
        white = (255, 255, 255)
        surface.fill(white)

        for count in range(100):
            start = get_random_pos()
            end = get_random_pos()

            color = random_color()
            pg.draw.line(surface, color, start, end)

        dot_radius = 10

        for count in range(100):
            pos = get_random_pos()
            color = random_color()
            radius = randint(5, 50)
            pg.draw.circle(surface, color, pos, radius)

        pg.display.flip()


if __name__ == "__main__":

    RD.ddr()
