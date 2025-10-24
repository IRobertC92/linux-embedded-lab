import sys
import types

# Headless mock Turtle class with all used methods
class MockTurtle:
    def __init__(self, *args, **kwargs):
        self._x = 0
        self._y = 0

    def shape(self, *args, **kwargs): pass
    def penup(self): pass
    def goto(self, x, y=None):
        if y is None and isinstance(x, (tuple, list)):
            x, y = x
        self._x, self._y = x, y
    def forward(self, dist):
        self._y += dist  # assume heading 90 for simplicity
    def setheading(self, deg): pass
    def shapesize(self, stretch_wid=1, stretch_len=1): pass
    def color(self, *args): pass
    def distance(self, other): return 100
    def hideturtle(self): pass
    def write(self, *args, **kwargs): pass
    def clear(self): pass
    def xcor(self): return self._x
    def ycor(self): return self._y
    def sety(self, y): self._y = y

# Headless mock Screen class
class MockScreen:
    def setup(self, **kwargs): pass
    def tracer(self, x): pass
    def title(self, t): pass
    def listen(self): pass
    def onkey(self, func, key): pass
    def update(self): pass
    def exitonclick(self): pass

# Replace turtle module with mocks
mock_turtle_module = types.ModuleType("turtle")
mock_turtle_module.Turtle = MockTurtle
mock_turtle_module.Screen = MockScreen
sys.modules["turtle"] = mock_turtle_module

# Mock pygame for headless sound tests
mock_pygame = types.ModuleType("pygame")
mock_pygame.mixer = types.SimpleNamespace(
    init=lambda: None,
    Sound=lambda filename: types.SimpleNamespace(
        play=lambda loops=0: None
    )
)
sys.modules["pygame"] = mock_pygame