from manim import *

class DefaultTemplate(Scene):
    def construct(self):
        ax = Axes(x_range=[-3, 3], y_range=[-3, 3])
        curve = ax.plot(lambda x: x**2, color=BLUE)
        area = ax.get_area(curve, x_range=[-2, 2], color=BLUE, opacity=0.5)
        self.play(Create(curve, run_time=5), Create(ax, run_time=2))
        self.play(FadeIn(area))
        self.wait(1)

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)  

        square = Square()
        square.set_fill(BLUE, opacity=0.5)
        square.flip(RIGHT)  # flip horizontally
        square.rotate(-3 * TAU / 8)  # rotate a certain amount

        self.play(DrawBorderThenFill(square)) 
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  

class Positioning(Scene):
    def construct(self):
        plane = NumberPlane()
        self.add(plane)

        red_dot = Dot(color=RED)
        green_dot = Dot(color=GREEN)
        green_dot.next_to(red_dot, RIGHT + UP)
        red_dot.shift(2 * LEFT)
        self.add(red_dot, green_dot)

        label = Tex("This is a \\LaTeX")
        label.next_to(green_dot, RIGHT + UP)
        self.add(label)

        rtarrow0 = MathTex(r"\xrightarrow{x^6y^8}", font_size=96)
        rtarrow1 = Tex(r"$\xrightarrow{x^6y^8}$", font_size=96)

        self.add(VGroup(rtarrow0, rtarrow1).arrange(DOWN))

        square = Square(color=ORANGE)
        square.shift(LEFT + UP)  
        self.play(FadeIn(square))

        c = Circle(radius=0.5, color=BLUE, fill_opacity=0.5)
        self.add(c)

        for d in [(0, 0, 0), UP, UR, RIGHT, DR, DOWN, DL, LEFT, UL]:
            self.play(c.animate.shift(d))

class Equation(Scene):
    def construct(self):
        eq1 = MathTex(r"\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}", tex_to_color_map={"\\sum": RED})
        eq2 = MathTex(r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots",
        substrings_to_isolate="x")
        eq3 = MathTex(r"H(X)=\sum_i^N\of\begin p_i\ \begin Log〗_2 p_i 〗")
        self.add(eq3)
        self.wait(5)
        eq2.set_color_by_tex("x", YELLOW)
        self.play(Write(eq1))
        self.wait(2)
        self.play(Transform(eq1, eq2), run_time=2)
        self.wait(5)