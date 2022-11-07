from Renderer.Objects.object import Object
from Renderer.Objects.Components.image import Image


class Background(Object):
    def __init__(self, x, y):
        super().__init__("Background", position=(x/2, y/2))
