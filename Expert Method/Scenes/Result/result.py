from Renderer.scene import Scene
from Renderer.Objects.label import Label
from Scenes.Result.Objects.background import Background
from Scenes.Result.Objects.title import Title

class Result(Scene):
    def __init__(self, main):
        super().__init__("Result", main)
        x, y = main.getScreenSize()
        self.addObject(Background(x, y))
        self.addObject(Title(main.getScreenSize()[0]/2))
