from Renderer.scene import Scene
from Renderer.Objects.label import Label
from Renderer.Objects.Components.rect import Rect
from Scenes.Result.Objects.background import Background

class Result(Scene):
    def __init__(self, main):
        super().__init__("Result", main)
        x, y = main.getScreenSize()
        self.addObject(Background(x, y))
        self.addObject(Label("Result Label", "", 30,
                             (main.getScreenSize()[0]/2, 50), origin=(0.5, 0)))
