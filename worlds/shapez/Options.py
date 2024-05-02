
from Options import Option, Choice, Range, NamedRange, Toggle, DefaultOnToggle

class Goal(NamedRange):
    """The level that needs to be finished in order for 
    the game to be considered completed.
    """
    display_name = "Goal"
    range_start = 1
    range_end = 1000 
    default = 26

    special_range_names = {
        "blueprint%": 12,
        "freeplay%": 26,
    }


class LevelTotalAndThroughput(NamedRange):
    """Percent chance that a given level has a throughput requirement\
    ( versus a total amount requirement -- each level is one or the other )
    E.g. a value of 30 would mean that each level would have a 70% of having a total requirement\
    and a 30% of a throughput requirement instead. 
    """
    display_name = "Total Amount vs Throughput"
    range_start = -1
    range_end = 100
    default = -1

    special_range_names = {
        "vanilla": -1,
        "only amount": 0,
        "equal": 50,
        "only throughput": 100
    }


class LevelTotal(Range):
    range_start = 1
    range_end = 10**8
    default = 30

class LevelTotalMin(LevelTotal):
    """
    Controls the lowest a Level's total requirement can be.
    """
    display_name = "Total Amount Minimum"
    default = 30

class LevelTotalMax(LevelTotal):
    """
    Controls the highest a Level's total requirement can be.
    """
    display_name = "Total Amount Maximum"
    default = 50000

class LevelTotalRamping(DefaultOnToggle):
    """
    Toggles whether the total amount requirements ramp up.
    E.g. 
    On: If level 5 has a total amount requirement of 500, \
    if any of the levels 1-4 have a total amount requirement it must be <=500 \
    and levels 6+ total amount requirements must be >=500.
    Off: Every level can have any total amount requirement that falls in the range \
    determined by the minimum and the maximum.
    """
    display_name = "Level Total Amount Ramping"


class LevelThroughput(Range):
    range_start = 1
    range_end = 550

class LevelThroughputMin(LevelThroughput):
    """
    Controls the lowest a Level's throughput requirement can be.
    All values are "per second".
    """
    display_name = "Throughput Minimum"
    default = 2

class LevelThroughputMax(Range):
    """
    Controls the highest a Level's throughput requirement can be.
    All values are "per second".
    """
    display_name = "Throughput Maximum"
    default = 16
    
class LevelThroughputRamping(Toggle):
    """
    Toggles whether the throughput requirements ramp up.
    E.g. 
    On: If level 5 has a throughput requirement of 5, \
    if any of the levels 1-4 have a throughput requirement it must be <=5 \
    and levels 6+ throughput requirements must be >=5.
    Off: Every level can have any throughput requirement that falls in the range \
    determined by the minimum and the maximum.
    """
    display_name = "Throughput Ramping"


class RandomizeLevels(Choice):
    """
    What the shape requirements will be for each level.
    Vanilla: Unchanged from base game.
    Shuffle: Allows picking individual shuffles for each aspect of each level's shape requirement.
    Random: Randomly determines what the shape requirement will be for each level.
    """
    display_name = "Level Definitions"
    option_vanilla = 0
    option_shuffle = 1
    option_random = 2


class ShuffleLevelShapes(Toggle):
    """
    Every Shuffled Level will have a base shape requirement \
    ( i.e. before other shuffles take place ) of some other level.
    """
    display_name = "Levels: Shuffle Base Shapes"

class ShuffleChoice(Choice):
    option_none = 0
    option_consistent = 1
    option_per_level = 2

class ShuffleLevelQuadrants(ShuffleChoice):
    """
    None: Levels do not have their shape's quadrants shuffled.
    Consistent: Each quadrant is mapped to the same ( distinct ) quadrant for every level's shape.
    Per Level: Each quadrant is mapped to a distinct quadrant which may change between different levels.
    """
    display_name = "Levels: Shuffle Quadrants"

class ShuffleLevelLayers(ShuffleChoice):
    """
    None: Levels do not have their shape's layers shuffled.
    Consistent: Each layer is mapped to the same ( distinct ) relative* layer for every level's shape.
    Per Level: Each layer is mapped to a distinct relative* layer which may change between different levels.
    * If a shape only has e.g. 2 layers, then whichever layer is mapped to the higher layer is the second layer. \
    In general, shapes will follow the order of the layer mapping within the total layers it has, \
    even if some layers should be "skipped".
    """
    display_name = "Levels: Shuffle Layers"

class ShuffleLevelSubshapes(ShuffleChoice):
    """
    None: Levels do not have their shape's subshapes shuffled.
    Consistent: Each subshape is mapped to the same ( distinct ) subshape for every level's shape.
    Per Level: Each subshape is mapped to a distinct subshape which may change between different levels.
    """
    display_name = "Levels: Shuffle Subshapes"

class ShuffleLevelColors(ShuffleChoice):
    """
    None: Levels do not have their shape's colors shuffled.
    Consistent: Each color* is mapped to the same ( distinct ) color* for every level's shape.
    Per Level: Each color* is mapped to a distinct color* which may change between different levels.
    * "Uncolored" is counted as a color.
    """
    display_name = "Levels: Shuffle Colors"


class RandomChoice(Choice):
    option_vanilla = 0
    option_ramping = 1
    option_random = 2

class RandomLevelTotalQuadrants(RandomChoice):
    """
    Vanilla: Levels have the same total quadrants as in the base game.
    Ramping: Levels have a total number of quadrants of ramping difficulty*.
    Random: Every level can have 1,2,3, or 4 total quadrants.
    * This is not the same as "numerical ramping". Specifically the ramping goes 4 -> 2 -> 1 -> 3. \
    This is because 4 is ( theoretically ) able to be satisfied with no Cutter / Stacker, \
    2 always requires at least a single Cutter pass, 1 always requires at least two Cutter passes, \
    and 3 always requires both a Cutter and a Stacker pass at least.
    """
    display_name = "Levels: Total Quadrants"

class RandomLevelTotalLayers(RandomChoice):
    """
    Vanilla: Levels have the same total layers as in the base game.
    Ramping: Levels have a total number of layers that ramp up.
    Random: Every level can have 1,2,3, or 4 total layers.
    """
    display_name = "Levels: Total Layers"

class RandomLevelTotalSubshapes(RandomChoice):
    """
    Vanilla: Levels have the same total subshapes as in the base game.
    Ramping: Levels have a total number of subshapes that ramp up ( clamped by 4x their total layers ).
    Random: Every level can have subshapes totalling between their total layers and 4x their total layers .
    """
    display_name = "Levels: Total Quadrants"

class RandomLevelTotalColors(RandomChoice):
    """
    Vanilla: Levels have the same total colors* as in the base game.
    Ramping: Levels have a total number of colors* that ramp up.
    Random: Every level can have between 1 and 8 total colors* ( clamped by the total number of subshapes ).
    * "Uncolored" is counted as a color.
    """
    display_name = "Levels: Total Colors"


class RandomizeUpgrades(DefaultOnToggle):
    """
    Whether or not to include upgrade tiers in the item pool.
    """
    display_name = "Randomize Upgrades"

class MaxUpgradeTier(Range):
    """
    How many tiers of each upgrade to include in the item pool.
    Completing upgrade requirements beyond this level will not
    do anything currently.
    """
    display_name = "Max Upgrade Tier"
    range_start = 1
    range_end = 1000
    default = 8


class RandomizeUpgradeTierCost(DefaultOnToggle):
    """
    Whether or not to randomize the cost of each upgrade tier.
    """
    display_name = "Upgrade Tier Cost"

class UpgradeTierShapes(Choice):
    """
    Controls how many distinct shapes are needed for each tier of each upgrade.
    Vanilla: Each tier requires the same shapes as vanilla.
    Vanilla Ramping: Each tier requires the same number of distinct shapes as vanilla.
    Follow Ramping: Each tier requires an increasing number of distinct shapes, maxing out at five; \
    the shapes from previous tiers stay the same in later tiers.
    Random Ramping: The same as Follow Ramping, but the shapes from previous tiers need not stay the same in later tiers.
    Consistent Fixed: Each tier requires a fixed number of distinct shapes determined by the max; \
    each upgrade maintains the same shapes for all tiers.
    Random Fixed: The same as Consistent Fixed, but the shapes from previous tiers need not stay the same in later tiers.
    Completely Random: There can be any number of changing distinct shapes in the range of the minimum and maximum for each tier.
    """
    display_name = "Upgrade Tiers: Shapes in Cost"
    option_vanilla = 0
    option_vanilla_ramping = 1
    option_follow_ramping = 2
    option_random_ramping = 3
    option_consistent_fixed = 4
    option_random_fixed = 5
    option_completely_random = 6

class UpgradeTierShapesMin(Range):
    """
    Controls the minimum number of distinct shapes any upgrade tier's cost may require.
    """
    display_name = "Upgrade Tiers: Minimum Distinct Shapes"
    range_start = 1
    range_end = 5
    default = 1

class UpgradeTierShapesMax(Range):
    """
    Controls the maximum number of distinct shapes any upgrade tier's cost may require.
    """
    display_name = "Upgrade Tiers: Maximum Distinct Shapes"
    range_start = 1
    range_end = 5
    default = 3

class UpgradeTierCost(Range):
    range_start = 1
    range_end = 10**10
    default = 30

class UpgradeTierCostMin(UpgradeTierCost):
    """
    Controls the lowest an upgrade tier's cost can be.
    Important: This amount is for each tier's sum total cost. 
    """
    display_name = "Upgrade Tier Minimum Cost"
    default = 30

class UpgradeTierCostMax(UpgradeTierCost):
    """
    Controls the highest an upgrade tier's cost can be.
    Important: This amount is for each tier's sum total cost. 
    """
    display_name = "Upgrade Tier Maximum Cost"
    default = 50000



class UpgradeTierShapesTotalsRamping(Choice):
    """
    Controls whether or not the total amounts of each distinct shape that are required in a tier's cost ramps up.
    Off: An upgrade tier's cost can have distinct shapes with totals and respective sum totals anywhere in the range of the minimum and maximum.
    Ramping Per Tier: Each tier will have the range that each distinct shape's total must fall inbetween determined by their first and last shape's totals. \
    E.g. An upgrade tier's cost that has three distinct shapes, would obligate the second shape's total to fall somewhere between the first shape's total \
    and the third shape's total. 
    Ramping Per Upgrade: An upgrade's tiers must have their sum total ( the sum of all distinct shape totals ) fall between the previous subsequent tiers' sum totals. \
    E.g. An upgrade's tier 2 must have a sum total >= that upgrade's tier 1 sum total, and <= that upgrade's tier 3 sum total.
    Full Ramping: Both Ramping Per Tier and Per Upgrade.
    """
    display_name = "Upgrade Tiers: Ramping Shape Totals"

    option_off = 0
    option_ramping_per_tier = 1
    option_ramping_per_upgrade = 2
    option_full_ramping = 3

class UpgradeTierRandomChoice(Choice):
    option_vanilla = 0
    option_ramping_per_tier = 1
    option_ramping_per_upgrade = 2
    option_full_ramping = 3
    
class RandomUpgradeTierTotalQuadrants(UpgradeTierRandomChoice):
    """
    Vanilla: Upgrade Tier's shapes have the same total quadrants as in the base game.
    Ramping Per Tier: Each tier will have the range that the difficulty* of each distinct shape's total number of quadrants must fall inbetween \
    determined by their first and last shape's total quadrants. \
    E.g. An upgrade tier's cost that has three distinct shapes, would obligate the second shape's total quadrants difficulty* to fall somewhere between the first shape \
    and the third shape's total quadrant difficulty.
    Ramping Per Upgrade: An upgrade's tiers must have their lowest and highest total quadrant difficulty be >= the previous tiers' lowest and highest total quadrant difficulty. \
    E.g. An upgrade's tier 2 must have a sum total >= that upgrade's tier 1 sum total, and <= that upgrade's tier 3 sum total.
    Full Ramping: Both Ramping Per Tier and Per Upgrade.

    Ramping: Upgrade Tier's shapes have a total number of quadrants of ramping difficulty*.
    Random: Every Upgrade Tier's shape can have 1,2,3, or 4 total quadrants.
    * This is not the same as "numerical ramping". Specifically the ramping goes 4 -> 2 -> 1 -> 3. \
    This is because 4 is ( theoretically ) able to be satisfied with no Cutter / Stacker, \
    2 always requires at least a single Cutter pass, 1 always requires at least two Cutter passes, \
    and 3 always requires both a Cutter and a Stacker pass at least.
    """
    display_name = "Upgrade Tiers: Total Quadrants"

class RandomLevelTotalLayers(UpgradeTierRandomChoice):
    """
    Vanilla: Levels have the same total layers as in the base game.
    Ramping: Levels have a total number of layers that ramp up.
    Random: Every level can have 1,2,3, or 4 total layers.
    """
    display_name = "Upgrade Tiers: Total Layers"

class RandomLevelTotalSubshapes(UpgradeTierRandomChoice):
    """
    Vanilla: Levels have the same total subshapes as in the base game.
    Ramping: Levels have a total number of subshapes that ramp up ( clamped by 4x their total layers ).
    Random: Every level can have subshapes totalling between their total layers and 4x their total layers .
    """
    display_name = "Upgrade Tiers: Total Quadrants"

class RandomLevelTotalColors(UpgradeTierRandomChoice):
    """
    Vanilla: Levels have the same total colors* as in the base game.
    Ramping: Levels have a total number of colors* that ramp up.
    Random: Every level can have between 1 and 8 total colors* ( clamped by the total number of subshapes ).
    * "Uncolored" is counted as a color.
    """
    display_name = "Upgrade Tiers: Total Colors"

