from manim import *
import numpy as np
import random as ran

def lerp(v, d):
    return v[0] * (1 - d) + v[1] * d
class SierpinskiTriangle(Scene):


    def construct(self):
        self.wait()

        initpoint = [(-3, -3, 0),
                     (-3,  0, 0),
                     (-3,  3, 0),
                     (0, -3, 0),
                     (0,  3, 0),
                     (3, -3, 0),
                     (3,  0, 0),
                     (3,  3, 0)]

        allDot = set()

        c = [BLUE, TEAL, GREEN, YELLOW, GOLD, RED, MAROON, PURPLE]
        for i in range(len(initpoint)):
            allDot.add(initpoint[i])

            dot = Dot(color=c[i], radius=0.2).move_to(initpoint[i])
            self.add(dot)
        self.wait()

        r = 0.02

        ratio = 2/3

        for i in allDot:
            dot = Dot(radius=r).move_to((i))
            self.add(dot)
        self.wait()

        for i in range(5):
            tempset = set()

            print(i, len(allDot))

            for d in allDot:
                for j in range(len(initpoint)):
                    meanpoint = (lerp([d[0], initpoint[j][0]], ratio), lerp([d[1], initpoint[j][1]], ratio), 0)
                    tempset.add(meanpoint)

            for count, m in enumerate(tempset):
                print(count, " : ", len(tempset), end="\r")
                allDot.add(m)
                dot = Dot(radius=r).move_to((m))
                self.add(dot)

            self.wait()

        self.wait()
