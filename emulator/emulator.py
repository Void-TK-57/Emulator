# import base libs
import pygame

ENGINE = RENDERER = LOGIC = None

# import own classes
from base import Renderable

class Logic:

    def __init__(self):
        global ENGINE
        global RENDERER
        self._engine = ENGINE
        self._renderer = RENDERER

    @property
    def engine(self):
        """Engine of the Renderer."""
        return self._engine


    ############################# Methods #############################

    def processes_event(self, events: list):
        """Method to register a Renderable Object"""
        for event in events:
            if event.type == pygame.QUIT: self.engine.stop()

class Renderer:

    def __init__(self):
        global ENGINE
        global LOGIC
        self._engine = ENGINE
        self._logic = LOGIC
        self._objects = set()
        self._size = self._weight, self._height = 800, 640
        self._screen = pygame.display.set_mode(self._size)

    ############################# Properties #############################

    @property
    def engine(self):
        """Engine of the Renderer."""
        return self._engine

    @property
    def objects(self):
        """Set of Objects to Render."""
        return self._objects

    ############################# Methods #############################

    def register_object(self, obj: Renderable):
        """Method to register a Renderable Object"""
        self._objects.add(obj)

    def register_object(self, obj: Renderable):
        """Method to register a Renderable Object"""
        self._objects.remove(obj)

    def render_objects(self):
        for obj in self._objects: obj._render(self.screen)
        # update display
        pygame.display.flip()

class Engine:

    def __init__(self):
        self._running = False
        self.on_init()

    def on_init(self):
        # init pygame
        pygame.init()
        set_engine(self)
        global RENDERER
        global LOGIC
        if RENDERER is None: set_renderer( Renderer() )
        if LOGIC is None: set_logic( Logic() )
        self._renderer = RENDERER
        self._logic = LOGIC

    def start(self):
        """Start Main Loop of the Engine."""
        self._running = True
        while self._running:
            # process events
            self._logic.processes_event(pygame.event.get())
            # call logic object

            # render values
            self._renderer.render_objects()

    def stop(self):
        self._running = False

def set_engine(eng: Engine):
    global ENGINE
    ENGINE = eng

def set_renderer(rndr: Renderer):
    global RENDERER
    RENDERER = rndr

def set_logic(rndr: Logic):
    global LOGIC
    LOGIC = rndr
