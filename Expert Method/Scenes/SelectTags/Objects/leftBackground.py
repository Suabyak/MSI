from Renderer.Objects.object import Object
from Renderer.Objects.Components.rect import Rect

class LeftBackground(Object):
    def __init__(self, x):
        super().__init__("LeftBackground", (x, 525))
        self.addComponent(
            Rect((x*2, 300), (255, 0, 0), (0.5, 0.5)))

