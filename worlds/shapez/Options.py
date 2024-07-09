
from Options import Option, Choice, Range, NamedRange, Toggle, DefaultOnToggle

class Goal(NamedRange):
    """
    The level that needs to be finished in order for the game to be considered completed.
    """
    display_name = "Goal"
    range_start = 1
    range_end = 1000 
    default = 26

    special_range_names = {
        "blueprint%": 12,
        "reward%": 26,
    }

class GoalLevelRewardDifference(Choice):
    """
    How to deal with any difference in the Goal Level and number of Rewards ( currently 26 + 4x max upgrade tier).
    Starting Rewards: This setting will only assign random rewards to levels up to the goal level \
    and will give the remaining rewards to the player to start with.
    Post Game: This setting simply assigns one reward to one level, meaning that if the chosen goal level \
    is below the number of rewards then remaining items that are randomized into levels greater than the goal level, \
    checking ( or releasing ) those levels may be required for other games' to complete their goals -- \
    of course, if the multiworld is set to "release on goal" then these levels will automatically release on goal.
    Reward Bundling: This setting bundles rewards so that individual checks will send multiple rewards at once; \
    this means there will be a number of checks exactly equal to the goal level + 4x max upgrade tier \
    ( if upgrade tiers are included in the item pool ).
    """
    display_name = "Goal Level vs Reward Total"
    option_starting_rewards = 0
    option_post_game = 1
    option_reward_bundling = 2

class BlueprintCostMultiplier(NamedRange):
    """
    What the multiplier on the cost ( in blueprints ) for paste operations should be.
    """
    range_start = 0
    range_end = 10
    default = 1

    special_range_names = {
        "free": 0,
        "vanilla": 1
    }


class RandomizeBlueprintShape(Choice):
    """
    If the Blueprint shape should be randomized and if so, how to randomize the shape.
    Vanilla: The blueprint shape is not randomized.
    Shuffled: The vanilla blueprint's layers, quadrants, and colors are shuffled.
    Analogous: A shape with the same "complexity" as the blueprint will be generated to replace the blueprint shape. \
    E.g. RgRgRgCg:RwRwRwRw, RyCyCyCy:CcCcCcCc, CrCrRrCr:RwRwRwRw, RpCpRpRp:RyRyRyRy
    Random: A totally random shape is chosen as the blueprint shape.
    """
    option_vanilla = 0
    option_shuffled = 1
    option_analogous = 2
    option_random = 3

class StartWithBluePrints(DefaultOnToggle):
    """
    Whether or not to start with the ability to Copy/Paste parts of your factory.
    This setting does not effect the cost of Copy/Pasting ( i.e. if the cost multiplier is not 0, you must still pay \
    even with this setting on )
    """
    display_name = "Start with Blueprints"



class ProgressiveBalancers(DefaultOnToggle):
    """
    Whether or not to merge Balancers, Mergers, and Splitters into "Progressive Balancers" \
    so that each is awarded in order.
    """
    display_name = "Progressive Balancers"

class ProgressiveTunnels(DefaultOnToggle):
    """
    Whether or not to merge the two Tunnel tiers into "Progressive Tunnels" \
    so that each is awarded in order.
    """
    display_name = "Progressive Tunnels"

class ProgressiveExtractors(DefaultOnToggle):
    """
    Whether or not to merge Extractors and Chained Extractors into "Progressive Extractors" \
    so that each is awarded in order.
    """
    display_name = "Progressive Extractors"

class ProgressiveCutters(DefaultOnToggle):
    """
    Whether or not to merge Cutters and Quad Cutters into "Progressive Cutters" \
    so that each is awarded in order.
    """
    display_name = "Progressive Cutters"

class ProgressiveRotators(Toggle):
    """
    Whether or not to merge Rotator (CW), Rotator (CCW), and Rotator (180°) into "Progressive Rotators" \
    so that each is awarded in order.
    """
    display_name = "Progressive Rotators"

class ProgressivePainters(DefaultOnToggle):
    """
    Whether or not to merge Painters, Double Painters, and Quad Painters into "Progressive Painters" \
    so that each is awarded in order.
    """
    display_name = "Progressive Painters"

class ProgressiveWires(DefaultOnToggle):
    """
    Whether or not to merge Wires, Constant Signal, Display, Logic Gates, and Virtual Processing into "Progressive Wires" \
    so that each is awarded in order.
    """
    display_name = "Progressive Wires"

class LevelTotalAndThroughput(NamedRange):
    """
    Percent chance that a given level has a throughput requirement \
    ( versus a total amount requirement -- each level is one or the other )
    E.g. a value of 30 would mean that each level would have a 70% of having a total requirement \
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
    Random: Each upgrade tier's distinct shapes can have any total as long as the tier's sum total is in the range of the minimum and maximum.
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
    
class UpgradeTierTotalQuadrants(UpgradeTierRandomChoice):
    """
    Vanilla: Upgrade Tier's shapes have the same total quadrants as in the base game.
    Ramping Per Tier: Each tier will have the range that the TQD of each distinct shape must fall between \
    determined by their first and last shape's TQD. \
    E.g. An upgrade tier's cost that has three distinct shapes, would obligate the second shape's total quadrants difficulty* (TQD) \
    to fall somewhere between the first shape and the third shape's TQD.
    Ramping Per Upgrade: An upgrade's tiers must have their lowest and highest TQD be >= the previous tiers' lowest and highest TQD respectively,\
    and they must also be <= the next tier's lowest and highest TQD, respectively. \
    E.g. An upgrade's tier 2 must have its lowest TQD >= that upgrade's TQD for tier 1, and <= that upgrade's tier 3 TQD.
    Full Ramping: Both Ramping Per Tier and Per Upgrade.
    Random: Each tier's shapes can have 1, 2, 3, or 4 quadrants.

    * Total Quadrant Difficulty (TQD) ramping is not the same as "numerical ramping". Specifically the ramping goes 4 -> 2 -> 1 -> 3. \
    This is because 4 is ( theoretically ) able to be satisfied with no Cutter / Stacker, \
    2 always requires at least a single Cutter pass, 1 always requires at least two Cutter passes, \
    and 3 always requires both a Cutter and a Stacker pass at least.
    """
    display_name = "Upgrade Tiers: Total Quadrants"

class UpgradeTierTotalLayers(UpgradeTierRandomChoice):
    """
    Vanilla: Upgrade Tier's shapes have the same total layers as in the base game.
    Ramping Per Tier: Each tier will have the range that the total layers of each distinct shape must fall between \
    determined by their first and last shape's total layers. \
    E.g. An upgrade tier's cost that has three distinct shapes, would obligate the second shape's total layers to fall somewhere between the first shape \
    and the third shape's total layers.
    Ramping Per Upgrade: An upgrade's tiers must have their lowest and highest total layers be >= the previous tiers' lowest and highest total layers respectively,\
    and they must also be <= the next tier's lowest and highest total layers, respectively. \
    E.g. An upgrade's tier 2 must have its lowest and highest total layers >= that upgrade's lowest and highest total layers for tier 1 respectively, \
    and <= that upgrade's tier 3 lowest and highest total layers respectively.
    Full Ramping: Both Ramping Per Tier and Per Upgrade.
    Random: Every level can have 1,2,3, or 4 total layers.
    """
    display_name = "Upgrade Tiers: Total Layers"

class UpgradeTierTotalSubshapes(UpgradeTierRandomChoice):
    """
    Vanilla: Upgrade Tier's shapes have the same total subshapes as in the base game.
    Ramping Per Tier: Each tier will have the range that the total subshapes of each distinct shape must fall between \
    determined by their first and last shape's total subshapes. \
    E.g. An upgrade tier's cost that has three distinct shapes, would obligate the second shape's total subshapes to fall somewhere between the first shape \
    and the third shape's total subshapes.
    Ramping Per Upgrade: An upgrade's tiers must have their lowest and highest total subshapes be >= the previous tiers' lowest and highest total subshapes respectively,\
    and they must also be <= the next tier's lowest and highest total subshapes, respectively. \
    E.g. An upgrade's tier 2 must have its lowest and highest total subshapes >= that upgrade's lowest and highest total subshapes for tier 1 respectively, \
    and <= that upgrade's tier 3 lowest and highest total subshapes respectively.
    Full Ramping: Both Ramping Per Tier and Per Upgrade.
    Random: Every level can have subshapes totalling between their total layers and 4x their total layers.

    All subshape amounts are clamped by a shape's total layers.
    """
    display_name = "Upgrade Tiers: Total Quadrants"

class UpgradeTierTotalColors(UpgradeTierRandomChoice):
    """
    Vanilla: Upgrade Tier's shapes have the same total colors as in the base game.
    Ramping Per Tier: Each tier will have the range that the total colors* of each distinct shape must fall between \
    determined by their first and last shape's total colors*. \
    E.g. An upgrade tier's cost that has three distinct shapes, would obligate the second shape's total colors to fall somewhere between the first shape \
    and the third shape's total colors*.
    Ramping Per Upgrade: An upgrade's tiers must have their lowest and highest total colors* be >= the previous tiers' lowest and highest total colors* respectively,\
    and they must also be <= the next tier's lowest and highest total colors*, respectively. \
    E.g. An upgrade's tier 2 must have its lowest and highest total colors* >= that upgrade's lowest and highest total colors* for tier 1 respectively, \
    and <= that upgrade's tier 3 lowest and highest total subshapes respectively.
    Full Ramping: Both Ramping Per Tier and Per Upgrade.
    Random: Every level can have between 1 and 8 total colors*.

    All color amounts are clamped by a shape's total subshapes.
    * "Uncolored" is counted as a color.
    """
    display_name = "Upgrade Tiers: Total Colors"


shapez_options: typing.Dict[str, type(Option)] = {
    "goal": Goal,
    "blueprint_cost_multiplier": BlueprintCostMultiplier,
    "randomize_blueprint_shape": RandomizeBlueprintShape,
    "start_with_blueprints": StartWithBluePrints,
    "goal_level_reward_difference": GoalLevelRewardDifference,
    "progressive_balancers": ProgressiveBalancers,
    "progressive_tunnels": ProgressiveTunnels,
    "progressive_extractors": ProgressiveExtractors,
    "progressive_cutters": ProgressiveCutters,
    "progressive_rotators": ProgressiveRotators,
    "progressive_painters": ProgressivePainters,
    "progressive_wires": ProgressiveWires,
    "level_total_and_throughput": LevelTotalAndThroughput,
    "level_total": LevelTotal,
    "level_total_min": LevelTotalMin,
    "level_total_max": LevelTotalMax,
    "level_total_ramping": LevelTotalRamping,
    "level_throughput": LevelThroughput,
    "level_throughput_min": LevelThroughputMin,
    "level_throughput_max": LevelThroughputMax,
    "level_throughput_ramping": LevelThroughputRamping,
    "randomize_levels": RandomizeLevels,
    "shuffle_level_shapes": ShuffleLevelShapes,
    "shuffle_level_quadrants": ShuffleLevelQuadrants,
    "shuffle_level_layers": ShuffleLevelLayers,
    "shuffle_level_subshapes": ShuffleLevelSubshapes,
    "shuffle_level_colors": ShuffleLevelColors,
    "random_level_total_quadrants": RandomLevelTotalQuadrants,
    "random_level_total_layers": RandomLevelTotalLayers,
    "random_level_total_subshapes": RandomLevelTotalSubshapes,
    "random_level_total_colors": RandomLevelTotalColors,
    "randomize_upgrades": RandomizeUpgrades,
    "max_upgrade_tier": MaxUpgradeTier,
    "randomize_upgrade_tier_cost": RandomizeUpgradeTierCost,
    "upgrade_tier_shapes": UpgradeTierShapes,
    "upgrade_tier_shapes_min": UpgradeTierShapesMin,
    "upgrade_tier_shapes_max": UpgradeTierShapesMax,
    "upgrade_tier_cost": UpgradeTierCost,
    "upgrade_tier_cost_min": UpgradeTierCostMin,
    "upgrade_tier_cost_max": UpgradeTierCostMax,
    "upgrade_tier_shapes_totals_ramping": UpgradeTierShapesTotalsRamping,
    "upgrade_tier_total_quadrants": UpgradeTierTotalQuadrants,
    "upgrade_tier_total_layers": UpgradeTierTotalLayers,
    "upgrade_tier_total_subshapes": UpgradeTierTotalSubshapes,
    "upgrade_tier_total_colors": UpgradeTierTotalColors
    # TODO: Traps
    ## Level Total / Throughput Increase
    ## Upgrade Tier Cost Shape Reset
    ## Chunk Emptying Bomb
    # TODO: EnergyLink
    # TODO: StartInventoryPool
}