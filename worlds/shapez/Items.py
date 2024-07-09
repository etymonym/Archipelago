
from BaseClasses import Item, ItemClassification

from .Buildings import BuildingEnum, Building, BuildingBundle, ProgressiveBuilding

class ShapezItemType(Enum):
    Building = 0
    Upgrade = 1

class ShapezItem(Item):
    game = "Shapez"
    item_type: ShapezItemType

    def __init__(location_t: ShapezLocationType, stage_n: int):
        self.location_type = location_t
        self.stage_num = stage_n
        