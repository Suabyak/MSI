from Renderer.scene import Scene
from Renderer.Objects.label import Label
from Scenes.SelectTags.Objects.tag1 import Tag1
from Scenes.SelectTags.Objects.leftBackground import LeftBackground
from Scenes.SelectTags.Objects.rightBackground import RightBackground
from Scenes.SelectTags.Objects.tag2 import Tag2


class SelectTags(Scene):
    def __init__(self, main):
        super().__init__("SelectTags", main)
        x = main.getScreenSize()[0]*0.25
        self.addObject(Label("Question", "", 40, (2*x, 375*0.5), origin=(0.5, 0.5)))
        self.addObject(LeftBackground(x))
        self.addObject(RightBackground(x))
        self.addObject(Tag1(main.removeTag1, x))
        self.addObject(Tag2(main.removeTag2, x*3))
