from manim import *
import numpy as np
import random as ran


class MonteCarlo(Scene):
    def construct(self):
        code = Code("temp.py")
        self.play(Write(code), run_time=1.3)
        self.wait()
        line = self.get_remark_rectangle(code, 1)
        self.add(line)
        self.wait()