#from typing import 

class ShapezWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide for installing the Archipelago mod for Shapez.",
        "English",
        "en_setup.md",
        "setup/en",
        ["Etymonym"]
    )]

class Shapez(World):

    game = "Shapez"
    
    web = ShapezWeb()