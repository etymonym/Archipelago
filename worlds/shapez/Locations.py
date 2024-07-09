from enum import Enum

from typing import Dict, List

from BaseClasses import Region, Entrance, Location



class ShapezLocationType(Enum):
    Level = 0
    UpgradeTier = 1

class ShapezLocation(Location):
    game = "Shapez"
    location_type: ShapezLocationType
    stage_num: int

    def __init__(location_t: ShapezLocationType, stage_n: int):
        self.location_type = location_t
        self.stage_num = stage_n
        
    



