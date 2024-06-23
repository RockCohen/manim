from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle), subcaption_duration=2)  # show the circle on screen
        self.next_section("Create Circle", skip_animations=False)
        quat = Square()
        quat.set_fill(YELLOW, opacity=8)
        self.play(Create(quat))
