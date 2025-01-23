from manim import *

class ManimCELogo(Scene):
    def construct(self):
        ax = Axes(x_range=(-3,3),y_range=(-3,3))
        curve = ax.plot(lambda x: (x+2)*x*(x-2)/2,color = "blue")
        area = ax.get_area(curve,x_range=(-2,2),color="green")
        self.play(Create(ax,run_time=1),Create(curve,run_time=3))        
        self.play(FadeIn(area))
        self.wait(2)

class SquareToTriangle(Scene):
    def construct(self):
        red_square = Square(color=GREEN,fill_opacity = 0.5)
        self.play(DrawBorderThenFill(red_square))
        blue_circle = Circle(color=BLUE,fill_opacity = 0.5)
        self.play(ReplacementTransform(red_square,blue_circle,run_time = 2))
        self.play(Indicate(blue_circle))
        self.play(FadeOut(blue_circle),run_time = 2)
        self.wait(2)


class Positioning(Scene):
    def construct(self):
        plane = NumberPlane()
        self.add(plane)

        red_dot = Dot(color=RED)
        blue_dot = Dot(color=BLUE)
        red_dot.next_to(blue_dot,RIGHT + UP)
        self.add(red_dot,blue_dot)

        s = Square(color=ORANGE)
        s.shift(2*UP + 4*RIGHT)
        self.add(s)

        c = Circle(color=PINK)
        c.move_to([-3,-2,0])
        self.add(c)

        c2 = Circle(radius=.5,color=YELLOW,fill_opacity=1)
        c3 = c2.copy().set_color(BLUE)
        c4 = c2.copy().set_color(GREEN)
        c2.align_to(s,UP)
        c3.align_to(s,RIGHT)
        c4.align_to(s,UP + RIGHT)
        self.add(c2,c3,c4)
    

class CriticalPoint(Scene):
    def construct(self):
        c5 = Circle(color=GRAY,fill_opacity=0.8)
        self.add(c5)

        for d in [(0,0,0),UP,DOWN,UL,DL,UR,DR,LEFT,RIGHT]:
            self.add(Cross(scale_factor=0.1).move_to(c5.get_critical_point(d)))
        
        s = Square(color=ORANGE,fill_opacity = 0.5)
        s.move_to([1,0,0],aligned_edge=LEFT)
        self.add(s)


from manim.utils.unit import Percent,Pixels

class usefulunit(Scene):
    def construct(self):
        for d in range(5,51,5):
            self.add(Circle(radius=d*Percent(X_AXIS)))
            self.add(Square(side_length=d*Percent(X_AXIS),color = YELLOW))

        d = Dot()
        d.shift(100*Pixels*RIGHT)
        self.add(d)

import random
class LaggingGroup(Scene):
    def construct(self):
    
        squares = VGroup(*[
            Square(color=ManimColor(random.choice([BLUE, GREEN, YELLOW, 
            RED, PURPLE, ORANGE, TEAL, GOLD, PINK, WHITE])), fill_opacity=0.5)
            for _ in range(20)]).arrange_in_grid(4, 5).scale(0.75)
        
        self.play(AnimationGroup(*[DrawBorderThenFill(s) for s in squares],lag_ratio=0.5))




from manim import *

class BirthdayWish(Scene):
    def construct(self):
        # Set up the black background
        self.camera.background_color = BLACK
        
        # Define the path that will eventually form into the letters
        curve_path = VMobject()
        curve_path.set_points_smoothly([[-3,-2,0], [-1, 2, 0], [1, -2, 0], [3, 2, 0]])
        curve_path.set_color(RED)

        # Animate the drawing of the curve
        self.play(Create(curve_path), run_time=4, rate_func=linear)

        # Create a transform into the letter "H"
        h_text = Text("H", font_size=130, color=GRAY)
        self.play(ReplacementTransform(curve_path, h_text), run_time=2)

        # Fade out "H" and fade in "Happy"
        happy_text = Text("Happy", font_size=130, color=BLUE)
        self.play(ReplacementTransform(h_text,happy_text), run_time=2)

        # Fade out "Happy" and fade in "Happy Birthday"
        birthday_text = Text("Happy Birthday", font_size=130, color=PINK)
        self.play(ReplacementTransform(happy_text,birthday_text), run_time=2)

        # Keep the "Happy Birthday" on screen for a while
        self.wait(2)

        