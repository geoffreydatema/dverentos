from data.engine_constants import DType

class Player():
    def __init__(self, game_manager):
        self.game_manager = game_manager
        
        # Player stats
        self.vitality = [4, 3, -1, 6]
        self.constitution = [3, 1, -2, 1]
        self.agility = [8, 3, -1, 2]
        self.dexterity = [8, 35, -3, 2]
        self.perception = [23, 3, -8, 12]
        self.rationality = [12, 32, -21, 34]

        # Player skills
        self.salvaging = [4, 3, -1, 123]
        self.harvesting = [4, 3, -1, 6]
        self.hunting = [4, 3, -1, 6]
        self.mining = [4, 3, -1, 6]
        self.lockpicking = [4, 3, -1, 6]
        self.cryptography = [4, 3, -1, 6]
        self.engineering = [4, 3, -1, 6]
        self.stealth = [4, 3, -1, 6]
        self.alchemy = [4, 3, -1, 6]
        self.weaponcrafting = [4, 3, -1, 6]
        self.toolsmithing = [4, 3, -1, 6]
        self.neuralforging = [4, 3, -1, 456]

        # Player mastery
        self.light_melee = 123
        self.heavy_melee = 23
        self.hand_cannons = 12
        self.big_guns = 12
        self.energy = 12
        self.telekinesis = 456

    def get_vitality(self):
        return self.vitality[3]
    
    def update_vitality(self):
        self.vitality[0] = 4 #! hardcoded for testing
        self.vitality[1] = 3 #! hardcoded for testing
        self.vitality[2] = -1 #! hardcoded for testing        
        self.vitality[3] = self.vitality[0] + self.vitality[1] + self.vitality[2]

    def update_values(self):
        self.update_vitality()
    
    def get_stats(self, data_type):
        if data_type == DType.INT:
            return {
                "vitality": (self.vitality[0], self.vitality[1], self.vitality[2], self.vitality[3]),
                "constitution": (self.constitution[0], self.constitution[1], self.constitution[2], self.constitution[3]),
                "agility": (self.agility[0], self.agility[1], self.agility[2], self.agility[3]),
                "dexterity": (self.dexterity[0], self.dexterity[1], self.dexterity[2], self.dexterity[3]),
                "perception": (self.perception[0], self.perception[1], self.perception[2], self.perception[3]),
                "rationality": (self.rationality[0], self.rationality[1], self.rationality[2], self.rationality[3])
            }
        
        elif data_type == DType.STR:
            return {
                "vitality": (str(self.vitality[0]), str(self.vitality[1]), str(self.vitality[2]), str(self.vitality[3])),
                "constitution": (str(self.constitution[0]), str(self.constitution[1]), str(self.constitution[2]), str(self.constitution[3])),
                "agility": (str(self.agility[0]), str(self.agility[1]), str(self.agility[2]), str(self.agility[3])),
                "dexterity": (str(self.dexterity[0]), str(self.dexterity[1]), str(self.dexterity[2]), str(self.dexterity[3])),
                "perception": (str(self.perception[0]), str(self.perception[1]), str(self.perception[2]), str(self.perception[3])),
                "rationality": (str(self.rationality[0]), str(self.rationality[1]), str(self.rationality[2]), str(self.rationality[3]))
            }
        
    def get_skills(self, data_type):
        if data_type == DType.INT:
            return {
                "salvaging": (self.salvaging[0], self.salvaging[1], self.salvaging[2], self.salvaging[3]),
                "harvesting": (self.harvesting[0], self.harvesting[1], self.harvesting[2], self.harvesting[3]),
                "hunting": (self.hunting[0], self.hunting[1], self.hunting[2], self.hunting[3]),
                "mining": (self.mining[0], self.mining[1], self.mining[2], self.mining[3]),
                "lockpicking": (self.lockpicking[0], self.lockpicking[1], self.lockpicking[2], self.lockpicking[3]),
                "cryptography": (self.cryptography[0], self.cryptography[1], self.cryptography[2], self.cryptography[3]),
                "engineering": (self.engineering[0], self.engineering[1], self.engineering[2], self.engineering[3]),
                "stealth": (self.stealth[0], self.stealth[1], self.stealth[2], self.stealth[3]),
                "alchemy": (self.alchemy[0], self.alchemy[1], self.alchemy[2], self.alchemy[3]),
                "weaponcrafting": (self.weaponcrafting[0], self.weaponcrafting[1], self.weaponcrafting[2], self.weaponcrafting[3]),
                "toolsmithing": (self.toolsmithing[0], self.toolsmithing[1], self.toolsmithing[2], self.toolsmithing[3]),
                "neuralforging": (self.neuralforging[0], self.neuralforging[1], self.neuralforging[2], self.neuralforging[3])
            }
        
        elif data_type == DType.STR:
            return {
                "salvaging": (str(self.salvaging[0]), str(self.salvaging[1]), str(self.salvaging[2]), str(self.salvaging[3])),
                "harvesting": (str(self.harvesting[0]), str(self.harvesting[1]), str(self.harvesting[2]), str(self.harvesting[3])),
                "hunting": (str(self.hunting[0]), str(self.hunting[1]), str(self.hunting[2]), str(self.hunting[3])),
                "mining": (str(self.mining[0]), str(self.mining[1]), str(self.mining[2]), str(self.mining[3])),
                "lockpicking": (str(self.lockpicking[0]), str(self.lockpicking[1]), str(self.lockpicking[2]), str(self.lockpicking[3])),
                "cryptography": (str(self.cryptography[0]), str(self.cryptography[1]), str(self.cryptography[2]), str(self.cryptography[3])),
                "engineering": (str(self.engineering[0]), str(self.engineering[1]), str(self.engineering[2]), str(self.engineering[3])),
                "stealth": (str(self.stealth[0]), str(self.stealth[1]), str(self.stealth[2]), str(self.stealth[3])),
                "alchemy": (str(self.alchemy[0]), str(self.alchemy[1]), str(self.alchemy[2]), str(self.alchemy[3])),
                "weaponcrafting": (str(self.weaponcrafting[0]), str(self.weaponcrafting[1]), str(self.weaponcrafting[2]), str(self.weaponcrafting[3])),
                "toolsmithing": (str(self.toolsmithing[0]), str(self.toolsmithing[1]), str(self.toolsmithing[2]), str(self.toolsmithing[3])),
                "neuralforging": (str(self.neuralforging[0]), str(self.neuralforging[1]), str(self.neuralforging[2]), str(self.neuralforging[3]))
            }

    def get_mastery(self, data_type):
        if data_type == DType.INT:
            return {
                "light melee": self.light_melee,
                "heavy melee": self.heavy_melee,
                "hand cannons": self.hand_cannons,
                "big guns": self.big_guns,
                "energy": self.energy,
                "telekinesis": self.telekinesis
            }
        
        elif data_type == DType.STR:
            return {
                "light melee": str(self.light_melee),
                "heavy melee": str(self.heavy_melee),
                "hand cannons": str(self.hand_cannons),
                "big guns": str(self.big_guns),
                "energy": str(self.energy),
                "telekinesis": str(self.telekinesis)
            }