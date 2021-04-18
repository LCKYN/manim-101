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

        self.wait()

        allDot = set()
        allDot.add((0, 3, 0))
        allDot.add((-3, -3, 0))
        allDot.add((3, -3, 0))

        r = 0.01

        for i in allDot :
            dot = Dot(radius=r).move_to((i))
            self.add(dot)
        self.wait()


        for i in range(10):
            tempset = set()

            print(i, len(allDot))

            for d in allDot:
                
                meanpoint1 = ((d[0] + 0)/2, (d[1] + 3)/2, 0)
                meanpoint2 = ((d[0] - 3)/2, (d[1] - 3)/2, 0)
                meanpoint3 = ((d[0] + 3)/2, (d[1] - 3)/2, 0)

                tempset.add(meanpoint1)
                tempset.add(meanpoint2)
                tempset.add(meanpoint3)

            for m in tempset:
                allDot.add(m)
                dot = Dot(radius=r).move_to((m))
                self.add(dot)


            self.wait()

        self.wait()
