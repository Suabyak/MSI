from Renderer.Objects.Components.rect import Rect
from Renderer.Objects.Components.image import Image
import pygame
from Utils.eventOperator import EventOperator
from Renderer.renderer import Renderer
from Renderer.Objects.object import Object
from Renderer.Objects.Components.animation import Animation
from Renderer.Objects.Components.animationSequence import AnimationSequence
from log import Log
from os import listdir, system
from random import randint
import traceback
# from Utils.mixer import Mixer
# from Scenes.MainMenu.mainMenu import MainMenu
# from Scenes.Game.game import Game
from Scenes.SelectTags.selectTags import SelectTags
from Scenes.Result.result import Result


class Main:
    def __init__(self):
        pygame.init()  # Inicjalizacja pygame
        self.__TITLE = "Metoda Ekspercka"
        self.__SCREEN_SIZE = (1200, 675)
        Log.executionLog(f"\n{'-'*50}")
        Log.executionLog(f"{self.__TITLE} started.")

        self.__eventOperator = EventOperator(self)
        self.__renderer = Renderer(self.__SCREEN_SIZE)
        # self.__mixer = Mixer()
        pygame.display.set_caption(self.__TITLE)
        self.__scenes = self.loadScenes()
        self.__activeScene = None
        self.__running = True
        self.__keysDown = dict()
        self.__tags = self.__readTags()
        self.__games = self.__readGames()

        self.setActiveScene("SelectTags")
        self.selectQuestion()
        self.__gameLoop()

    def __gameLoop(self):
        """Pętla która będzie się wykonywała cały czas dopóki użytkownik
        nie zechce wyjść z aplikacji, obsługuje ona renderowanie i eventy."""
        while self.__running:
            self.__eventOperator.operateEvents()
            if self.__activeScene == "Game":
                self.tickGame()
            self.__renderer.render(self.getActiveScene())
            self.tickAnimations(self.getActiveScene())

    def loadScenes(self):
        scenes = dict()

        # scenes["MainMenu"] = MainMenu(self)
        # scenes["Game"] = Game(self)
        scenes["SelectTags"] = SelectTags(self)
        scenes["Result"] = Result(self)

        return scenes

    def setActiveScene(self, scene):
        self.__activeScene = scene
        Log.executionLog(f"Scene set to \"{scene}\".")

    def getActiveScene(self):
        return self.__scenes[self.__activeScene]

    def getScreenSize(self):
        return self.__SCREEN_SIZE

    def isKeyDown(self, key):
        if key not in self.__keysDown.keys():
            return False
        return True

    def mouseClick(self, event):
        # pętla od tyłu (jak michael jackson i jego moonwalk)
        for obj in reversed(self.getActiveScene().getObjects()):
            if not obj.hasComponent("Collider") or not obj.isActive():
                continue
            collider = obj.getComponent("Collider")
            if collider.isOver(obj.getComponent(
                    "Transform").getPosition(), event.dict["pos"]):
                obj.getComponent("Event").run("Click", event)
                return
        if self.__activeScene == "Game":
            Object.get("WaterCannon").fire()

    def keyDown(self, event):
        self.__keysDown[event.dict["key"]] = 1
        if event.dict["key"] == pygame.constants.K_SPACE:
            Object.get("Truck").setHandleBrake(1)

    def keyUp(self, event):
        self.__keysDown.pop(event.dict["key"])
        if event.dict["key"] == pygame.constants.K_SPACE:
            Object.get("Truck").setHandleBrake(0)

    def tickAnimations(self, scene):
        for obj in scene.getObjects():
            for component in obj.getComponents().values():
                if ((issubclass(component.__class__, Animation) and component.isActive())
                        or (isinstance(component, AnimationSequence) and component.isRunning())):
                    component.tick()

    def tickGame(self):
        truck = Object.get("Truck")
        rotSpeed = -int(self.isKeyDown(pygame.constants.K_a))
        rotSpeed += int(self.isKeyDown(pygame.constants.K_d))
        truck.rotate(rotSpeed*8.5)

        acceleration = 3 * \
            int(self.isKeyDown(pygame.constants.K_w))
        acceleration -= int(self.isKeyDown(pygame.constants.K_s))
        truck.accelerate(acceleration*4.2)

        truck.move()
        firePointer = Object.get("FirePointer")
        fire = Object.get("Fire")
        if fire.isActive() and not firePointer.isActive():
            truckPosition = truck.getComponent("Transform").getPosition()
            x, y = fire.getComponent("Transform").getPosition()
            x = truckPosition[0] - x
            y = truckPosition[1] - y
            if abs(x) > self.__SCREEN_SIZE[0]/2 or abs(y) > self.__SCREEN_SIZE[1]/2:
                firePointer.setActive(True)
        if firePointer.isActive():
            firePointer.calcRotation()
        fire.tick()
        waterCannon = Object.get("WaterCannon")
        waterCannon.tick(Renderer.getDeltaTime())
        waterCannon.tickWaterBalls()

    def quit(self, event):
        """Zakończenie działania programu."""
        self.__running = False
        Log.executionLog(f"{self.__TITLE} shat down.")

    def playSound(self, event):
        self.__mixer.playSound(self, event)

    def stopSound(self, event):
        self.__mixer.stopSound(self, event)

    def startGame(self):
        Log.executionLog("Game started.")
        self.setActiveScene("Game")
        EventOperator.createEvent(EventOperator.PLAY, {"name": "peaceful"})
        mouseX, mouseY = self.mousePos
        Object.get("WaterCannon").calcRotation(mouseX-self.__SCREEN_SIZE[0]/2,
                                               mouseY-self.__SCREEN_SIZE[1]/2)

    def mouseMotion(self, event):
        self.mousePos = event.dict["pos"]
        if self.__activeScene == "Game":
            mouseX, mouseY = self.mousePos
            Object.get("WaterCannon").calcRotation(mouseX-self.__SCREEN_SIZE[0]/2,
                                                   mouseY-self.__SCREEN_SIZE[1]/2)

    def __readTags(self):
        file = open("Expert Method\\tags.csv")
        file = file.read().split("\n")
        lines = list()
        for line in file:
            lines.append(line.split(";"))
        print(f"Wczytano {len(lines)} tagow")
        return lines

    def __readGames(self):
        file = open("Expert Method\\games.csv")
        file = file.read().split("\n")
        lines = list()
        for line in file:
            lines.append(line.split(";"))
        print(f"Wczytano {len(lines)} gier")
        return lines
    
    def selectQuestion(self):
        if len(self.__games) == 1:
            self.setActiveScene("Result")
            self.getActiveScene().getObject("Result Label").setText(self.__games[0][0])
            self.getActiveScene().getObject("Background").addComponent(Image(self.__games[0][0], (0.5, 0.5)))
            Image.setSize(self.__games[0][0], (1200, 675))
            return
        if len(self.__tags) == 0:
            print(self.__games)
        tag = self.__tags[randint(0, len(self.__tags)-1)]
        self.__tag = tag
        self.getActiveScene().getObject("Question").setText(tag[2])
        self.getActiveScene().getObject("Tag1").setTag(tag[0])
        self.getActiveScene().getObject("Tag2").setTag(tag[1])

    def removeTag1(self, event):
        self.removeTag(self.getActiveScene().getObject("Tag2").tag)
        self.selectQuestion()

    def removeTag2(self, event):
        self.removeTag(self.getActiveScene().getObject("Tag1").tag)
        self.selectQuestion()

    def removeTag(self, tag):
        self.__tags.remove(self.__tag)
        deleted = 0
        for i in range(len(self.__games)):
            i = len(self.__games) + deleted - 1 - i
            game = self.__games[i]
            print(tag, game)
            if tag in game:
                self.__games.pop(i)
                deleted += 1
        print(deleted)

if __name__ == "__main__":
    Main()
