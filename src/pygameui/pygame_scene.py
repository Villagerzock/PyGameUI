import pygame

from better_math import Vector2i
import scene_handler


class PyGameUIHandler:

    def __init__(self):
        self.visible = True
        self._children = []
        self.parent = EmptyUIHandler()

    def add_child(self, child):
        self._children.append(child)
        child.parent = self

    text = ""


    def draw(self, surface, offset: Vector2i = Vector2i(0, 0)):
        for child in self._children:
            if child.visible:
                child.draw(surface,Vector2i(self.get_rect().x, self.get_rect().y) + offset)

    def handle_event(self, event):
        for child in self._children:
            if child.visible:
                child.handle_event(event)
    def get_rect(self) -> pygame.Rect:
        return pygame.Rect(0, 0, 0, 0).move(self.parent.get_rect().x, self.parent.get_rect().y)

    def collidepoint(self, x, y):
        for drawable in self._children:
            if not drawable.visible:
                continue
            if drawable.get_rect().collidepoint(x, y):
                return True
            elif drawable.collidepoint(x, y):
                return True
        else:
            return False

class EmptyUIHandler(PyGameUIHandler):
    def __init__(self):
        pass

    def get_rect(self) -> pygame.Rect:
        return pygame.Rect(0, 0, 0, 0)
class PyOverlay(PyGameUIHandler):
    def __init__(self, rect: pygame.Rect, color: tuple[int, int, int] = (0, 0, 0)):
        super().__init__()
        self.rect = rect
        self.color = color

    def draw(self, surface, offset: Vector2i = Vector2i(0, 0)):
        pygame.draw.rect(surface, self.color, self.rect)
        super().draw(surface, offset)
    def get_rect(self) -> pygame.Rect:
        return self.rect.move(self.parent.get_rect().x, self.parent.get_rect().y)


class PyGameScene:
    drawables: list[PyGameUIHandler] = []

    def __init__(self):
        self.update()

    def render(self, screen, events) -> bool:
        for event in events:
            if event.type == pygame.QUIT:
                return False
            for drawable in self.drawables:
                if drawable.visible:
                    drawable.handle_event(event)
        for drawable in self.drawables:
            if drawable.visible:
                if drawable.text == "0":
                    print("Drawing Button")
                drawable.draw(screen)
        if scene_handler.debugging:
            for drawable in self.drawables:
                pygame.draw.rect(screen, pygame.Color("red"), drawable.get_rect(),2)
        return True

    def update(self):
        self.drawables.clear()

    def collidepoint(self, x, y):
        for drawable in self.drawables:
            if not drawable.visible:
                continue
            if drawable.get_rect().collidepoint(x, y):
                return True
            elif drawable.collidepoint(x, y):
                return True
        return False
