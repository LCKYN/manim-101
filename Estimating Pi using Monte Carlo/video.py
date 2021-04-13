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

        point_text, point_number = point_label = VGroup(
            Text("point : "),
            DecimalNumber(
                0,
                show_ellipsis=True,
                num_decimal_places=4
            )
        )

        in_text, in_number = in_label = VGroup(
            Text("In a circle : "),
            DecimalNumber(0)
        )

        pi_text, pi_number = pi_label = VGroup(
            Text("PI : "),
            DecimalNumber(0)
        )
        point_label.arrange(RIGHT)
        in_label.arrange(RIGHT)
        pi_label.arrange(RIGHT)

        point_label.move_to((2, -1, 0))
        in_label.move_to((2, 0, 0))
        pi_label.move_to((2, 1, 0))

        self.add(point_label, in_label, pi_label)

        # always(count_number.set_value, self.time())
        # count_number.add_updater(lambda m: m.set_value(ran.random()))
        count_all = 0
        c = 0
        apx_pi = 0
        point_number.add_updater(lambda m: m.set_value(count_all))
        in_number.add_updater(lambda m: m.set_value(c))
        pi_number.add_updater(lambda m: m.set_value(apx_pi))

        ran.seed(1)

        for i in range(200):
            pos = (-6 + ran.random() * 4, -2 + ran.random() * 4, 0)
            if((pos[0] + 4) ** 2 + pos[1] ** 2 < 4):
                d = Dot(color=RED, radius = 0.25)
                c += 1
            else:
                d = Dot(color=GREEN, radius = 0.25)
            d.move_to(pos)
            self.play(Create(d, run_time=0.05))
            count_all = i
            apx_pi = c/(i+1) * 4

        # group = VGroup(*point)
        # group2 = VGroup(*count)
        # group2.next_to(count_text, RIGHT)

        # i = 5
        # # def temp(n):
        # #     global i
        # #     i += 1
        # #     n.set_value(i)

        # self.play(
        #     ShowIncreasingSubsets(group, run_time=20.0),
            # ApplyFunction(temp, count_number)
            #   )
        self.wait(2)
