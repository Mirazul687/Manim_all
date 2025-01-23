from manim import *

class Birthday_Wish(Scene):
    def construct(self):
        # Set up the black background
        self.camera.background_color = BLACK
        
        # Define the path that will eventually form into the letters
        curve_path = VMobject()
        curve_path.set_points_smoothly([[-10,-2,0], [-1, 2, 0], [1, -2, 0], [3, 2, 0],[5, -2, 0],[7, 2, 0]])
        curve_path.set_color(PINK)

        # Animate the drawing of the curve
        self.play(Create(curve_path), run_time=4, rate_func=linear)

        # Create a transform into the letter "H"
        h_text = Text("H", font_size=130, color=BLUE)
        self.play(ReplacementTransform(curve_path, h_text), run_time=2)
        
        # Fade out "H" and fade in "Happy"
        ha = Text("Ha", font_size=130, color=BLUE_A)
        self.play(ReplacementTransform(h_text,ha),run_time = 1)

        # Fade out "Happy" and fade in "Happy Birthday"
        hap = Text("Hap", font_size=130, color=BLUE_C)
        self.play(ReplacementTransform(ha,hap), run_time=1)

        happ = Text("Hapy", font_size=130, color=BLUE_E)
        self.play(ReplacementTransform(hap,happ), run_time=1)

        happy = Text("Happy", font_size=130, color=DARK_BLUE)
        self.play(ReplacementTransform(happ,happy), run_time=1)

        happy_b = Text("Happy B", font_size=130, color=PINK)
        self.play(ReplacementTransform(happy,happy_b), run_time=2)

        happpy_bi = Text("Happpy Bi", font_size=130, color=LIGHT_PINK)
        self.play(ReplacementTransform(happy_b,happpy_bi), run_time=1)

        happy_bir = Text("Happy Bir", font_size=130, color=ORANGE)
        self.play(ReplacementTransform(happpy_bi,happy_bir), run_time=1)

        happy_birt = Text("Happy Birt", font_size=130, color=YELLOW_D)
        self.play(ReplacementTransform(happy_bir,happy_birt), run_time=1)

        happy_birth = Text("Happy Birth", font_size=130, color=YELLOW)
        self.play(ReplacementTransform(happy_birt,happy_birth), run_time=1)

        happy_birthd = Text("Happy Birthd", font_size=130, color=GREEN_D)
        self.play(ReplacementTransform(happy_birth,happy_birthd), run_time=1)

        happy_birthda = Text("Happy Birthda", font_size=130, color=GREEN_B)
        self.play(ReplacementTransform(happy_birthd,happy_birthda), run_time=1)

        happy_birthday = Text("Happy Birthday", font_size=130, color=GREEN)
        self.play(ReplacementTransform(happy_birthda,happy_birthday), run_time=1)

        # Keep the "Happy Birthday" on screen for a while
        self.wait(2)





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
        h_text = Text("H", font_size=130, color=PINK)
        self.play(ReplacementTransform(curve_path, h_text), run_time=2)

        # Fade out "H" and fade in "Happy"
        happy_text = Text("Happy", font_size=130, color=BLUE)
        self.play(ReplacementTransform(h_text,happy_text), run_time=2)

        # Fade out "Happy" and fade in "Happy Birthday"
        birthday_text = Text("Happy Birthday", font_size=130, color=GREEN)
        self.play(ReplacementTransform(happy_text,birthday_text), run_time=2)

        # Keep the "Happy Birthday" on screen for a while
        self.wait(2)