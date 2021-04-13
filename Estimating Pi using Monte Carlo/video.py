from manim import *
import numpy as np
import random as ran


class Grid(Scene):
    def construct(self):

        offset = (-4, 0, 0)
        # for i in range(-7, 8):
        #     self.add(Line((-i, 5, 0), (-i, -5, 0)))
        # for i in range(-4, 5):
        #     self.add(Line((-7, i, 0), (7, i, 0)))

        circle = Circle(radius=2, color=RED)
        circle.move_to(offset)

        square = Rectangle(width=4, height=4)
        square.move_to(offset)

        self.add(circle)
        self.add(square)

        self.wait(1)

        point = []
        for i in range(2000):
            pos = (-6 + ran.random() * 4, -2 + ran.random() * 4, 0)
            if((pos[0] + 4) ** 2 + pos[1] ** 2 < 4):
                d = Dot(color=RED)
            else:
                d = Dot(color=GREEN)
            d.move_to(pos)
            point.append(d)
            # self.play(ShowCreation(d, run_time=0.1))

        group = VGroup(*point)
        self.play(ShowIncreasingSubsets(group, run_time=3.0))
        self.wait(2)
