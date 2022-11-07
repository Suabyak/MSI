from Renderer.scene import Scene
from Renderer.Objects.label import Label
from Scenes.SelectTags.Objects.tag1 import Tag1
from Scenes.SelectTags.Objects.tag2 import Tag2


class SelectTags(Scene):
    def __init__(self, main):
        super().__init__("SelectTags", main)

        self.addObject(Label("Question", "", 24, (main.getScreenSize()[0]/2, 100), origin=(0.5, 0)))
        self.addObject(Tag1(main.removeTag1))
        self.addObject(Tag2(main.removeTag2))
