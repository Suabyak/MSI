from Renderer.scene import Scene
from Renderer.Objects.label import Label

class Result(Scene):
    def __init__(self, main):
        super().__init__("Result", main)
        self.addObject(Label("Result Label", "", 30, (main.getScreenSize()[0]/2, 50), origin=(0.5, 0)))