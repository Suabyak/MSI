from Renderer.Objects.object import Object
from Renderer.Objects.Components.rect import Rect


class RightBackground(Object):
    def __init__(self, x):
        super().__init__("RightBackground", (x*3, 525))
        self.addComponent(
            Rect((x*2, 300), (0, 0, 255), (0.5, 0.5)))
