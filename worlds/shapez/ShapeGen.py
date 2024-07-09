
from typing import Dict, List
from enum import Enum

import orjson
import pkgutil

from concurrent.futures import ThreadPoolExecutor

from .Options import RandomizeLevels

class ConcreteSubshape(Enum):
    circle = "C"
    rectangle = "R"
    star = "S"
    windmill = "W"

class ConcreteColor(Enum):
    uncolored = "u"

    red = "r"
    green = "g"
    blue = "b"

    yellow = "y"
    purple = "p"
    cyan = "c"

    white = "w"

class Shape:
    code: str = None


    quadrants: int = None
    layers: int = None
    subshapes: int = None
    colors: int = None

class AbstractShape(Shape):



def load_json_data(data_name: str) -> Union[List[str], Dict[str, Any]]:
    return orjson.loads(pkgutil.get_data(__name__, "data/" + data_name + ".json"))

class ShapeGenerator:

    pool = ThreadPoolExecutor(1)

    randomize_type: RandomizeLevels = None

    def __init__(self, randomize: RandomizeLevels):
        self.randomize_type = randomize

        self.vanilla_levels = pool.submit(load_json_data, "levels")
        self.building_rules = pool.submit(load_json_data, "buildings")

    def __del__(self):

        del vanilla_levels
        del building_rules
        del self.pool

    def shuffle(self, shuffle_options: Dict[str, ShuffleChoice]):

        self.shuffle: Dict[str,List[int]] = {}

        if shuffle_options['shuffle_levels']:
            self.shuffle[] = pool.submit(ShapeGenerator.shuffle_levels, self.max_level)
            self.level_shuffle = pool.submit(ShapeGenerator.shuffle_levels, self.max_level)




class ShapeSpecType(Enum):



class ShapeSpec:
