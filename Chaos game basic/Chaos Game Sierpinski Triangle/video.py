from manim import *
import numpy as np
import random as ran


class SierpinskiTriangle(Scene):
    def construct(self):
        self.wait()

        dot = Dot(color=RED, radius=0.2).move_to((0, 3, 0))
        self.add(dot)
        dot = Dot(color=GREEN, radius=0.2).move_to((-3, -3, 0))
        self.add(dot)
        dot = Dot(color=BLUE, radius=0.2).move_to((3, -3, 0))
        self.add(dot)

        point = (0, 3, 0)
        for i in range(50000):
            r = ran.randrange(3)
            if(r == 0):
                point = ((point[0] + 0) / 2, (point[1] + 3) / 2, 0)
            elif(r == 1):
                point = ((point[0] + -3) / 2, (point[1] + -3) / 2, 0)
            else:
                point = ((point[0] + 3) / 2, (point[1] + -3) / 2, 0)

            dot = Dot(radius=0.01).move_to((point))
            self.add(dot)
            if(i % 200 == 0):
                self.wait(0.1)

        self.wait()