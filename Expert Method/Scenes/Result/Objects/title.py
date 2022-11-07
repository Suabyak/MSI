from Renderer.Objects.Components.rect import Rect
from Renderer.Objects.Components.text import Text
from Renderer.Objects.object import Object


class Title(Object):
    def __init__(self, x):
        super().__init__("Result Label", (x, 30))
        self.addComponent(Rect((0, 0), (0, 0, 0), (0.5, 0.5)))
        self.addComponent(Text("", 30, origin=(0.5, 0.5)))

    def setText(self, text):
        self.getComponent("Text").setText(text)
        text_size = self.getComponent("Text").getSize()
        self.getComponent("Rect").setSize((text_size[0]+10, text_size[1]+10))