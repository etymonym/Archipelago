
from Options import Option, Choice, Range, Toggle

class Goal(Range):
    """The level that needs to be finished in order for 
    the game to be considered completed.
    """
    display_name = "Goal"
    range_start = 1
    # So... this needn't be the cap, but gonna leave it here for now
    # Until I'm asked to increase it I guess
    range_end = 100 
    default = 26

class RandomizeLevels(Choice):
    """What the shape / throughput requirements will be for each level.
    Vanilla: Unchanged from base game.
    """
    display_name = "Level Definitions"
    option_vanilla = 0
    option_shuffle = 1
    option_random = 2

class ShuffleLevelShapes(Toggle):

    display_name = "Shuffled Levels: Shapes"

class ShuffleLevelQuadrants(Toggle):

    display_name = "Shuffled Levels: Quadrants"

class ShuffleLevelSubshapes(Toggle):

    display_name = "Shuffled Levels: Subshapes"

class ShuffleLevelColors(Toggle):

    display_name = "Shuffled Levels: Colors"

class ShuffleLevelLayers(Toggle):

    display_name = "Shuffled Levels: Layers"

class RandomLevelShapes(Toggle):

    display_name = "Random Levels: Shapes"

class RandomLevelTotalQuadrants(Choice):

    display_name = "Random Level's Shapes: Total Quadrants"

    option_vanilla = 0
    option_ramping = 1
    option_random = 2

class RandomLevelTotalLayers(Choice):

    display_name = "Random Level's Shapes: Total Layers"

    option_vanilla = 0
    option_ramping = 1
    option_random = 2

class RandomLevelTotalColors(Choice):

    display_name = "Random Level's Shapes: Total Colors"

    option_vanilla = 0
    option_ramping = 1
    option_random = 2

class RandomLevelThroughput(Toggle):

    display_name = "Random Levels: Throughput"


class RandomLevelThroughputMin(Range):
    display_name = "Random Level's Throughput: Minimum"
    range_end = 2000
    default = 5

class RandomLevelThroughputMax(Range):
    display_name = "Random Level's Throughput: Maximum"
    range_end = 2000
    default = 100
    
class RandomLevelThroughputRamping(Toggle):

    display_name = "Random Level's Throughput: Ramping"


class RandomizeUpgrades(Toggle):
    """Whether or not to include upgrades in the item pool."""
    display_name = "Randomize Upgrades"

class MaxUpgradeTier(Range):
    """How many tiers of each upgrade to include in the item pool.
    ( Completing upgrade requirements beyond this level will not
    do anything currently )
    """
    display_name = "Max Upgrade Tier"
    range_start = 1
    range_end = 1000
    default = 8

class Randomizer