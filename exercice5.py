import random
from dataclasses import dataclass


@dataclass
class Personnage:
    force: int = random.randint(1, 20)
    dexterite: int = random.randint(1, 20)
    constitution: int = random.randint(1, 20)
    intelligence: int = random.randint(1, 20)
    sagesse: int = random.randint(1, 20)
    charisme: int = random.randint(1, 20)
