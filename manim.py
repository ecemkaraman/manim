from manim import *

class FunctionIntro(Scene):
    def construct(self):
        code = Code(
            code="""
            def greet(name):
                print(f"Hello, {name}!")
            greet("Ecem")
            """,
            language="Python"
        )
        self.play(Write(code))
        self.wait(2)
