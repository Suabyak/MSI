from Renderer.Objects.object import Object
from Renderer.Objects.button import Button
from Renderer.Objects.Components.text import Text


class Tag2(Button):
    def __init__(self, action):
        self.tag = ""
        super().__init__("Tag2", Text(self.tag, 14, origin=(
            0.5, 0.5)), action, position=(600, 200))

    def setTag(self, tag):
        self.tag = tag
        self.getComponent("Text").setText(tag)
        self.getComponent("Collider").setSize(
            self.getComponent("Text").getSize())
