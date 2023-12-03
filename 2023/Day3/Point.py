from dataclasses import dataclass

@dataclass(eq=True, frozen=True)
class Point():
    x: int
    y: int