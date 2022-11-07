from Renderer.Objects.object import Object
from Renderer.Objects.button import Button
from Renderer.Objects.Components.text import Text

class Tag1(Button):
    def __init__(self, action, x):
        self.tag = ""
        super().__init__("Tag1", Text(self.tag, 30, origin=(0.5, 0.5)), action, position=(x, 525))

    def setTag(self, tag):
        self.tag = tag
        self.getComponent("Text").setText(tag)
        self.getComponent("Collider").setSize(self.getComponent("Text").getSize())