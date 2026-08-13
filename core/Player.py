from data.engine_constants import DType

class Player():
    def __init__(self, game_manager):
        self.game_manager = game_manager
        
        # Player stats
        self.vitality = [0, 0, 0, 0]
        self.constitution = [0, 0, 0, 0]
        self.strength = [0, 0, 0, 0]
        self.agility = [0, 0, 0, 0]
        self.dexterity = [0, 0, 0, 0]
        self.perception = [0, 0, 0, 0]
        self.intelligence = [0, 0, 0, 0]
        self.rationality = [0, 0, 0, 0]

        # Player skills
        self.navigation = [0, 0, 0, 0]
        self.stealth = [0, 0, 0, 0]
        self.combat = [0, 0, 0, 0]
        self.hunting = [0, 0, 0, 0]
        self.recovery = [0, 0, 0, 0]
        self.salvaging = [0, 0, 0, 0]
        self.resources = [0, 0, 0, 0]
        self.alchemy = [0, 0, 0, 0]
        self.bartering = [0, 0, 0, 0]
        self.lockpicking = [0, 0, 0, 0]
        self.cryptography = [0, 0, 0, 0]
        self.engineering = [0, 0, 0, 0]
        self.gunsmithing = [0, 0, 0, 0]
        self.bladecasting = [0, 0, 0, 0]
        self.neuralforging = [0, 0, 0, 0]
        self.armorcrafting = [0, 0, 0, 0]

        # Player mastery
        self.carbines = [0, 0]
        self.subcarbines = [0, 0]
        self.lancers = [0, 0]
        self.suppressors = [0, 0]
        self.handcanons = [0, 0]
        self.breachers = [0, 0]
        self.launchers = [0, 0]
        self.greatswords = [0, 0]
        self.knives = [0, 0]

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
                "strength": (self.strength[0], self.strength[1], self.strength[2], self.strength[3]),
                "agility": (self.agility[0], self.agility[1], self.agility[2], self.agility[3]),
                "dexterity": (self.dexterity[0], self.dexterity[1], self.dexterity[2], self.dexterity[3]),
                "perception": (self.perception[0], self.perception[1], self.perception[2], self.perception[3]),
                "intelligence": (self.intelligence[0], self.intelligence[1], self.intelligence[2], self.intelligence[3]),
                "rationality": (self.rationality[0], self.rationality[1], self.rationality[2], self.rationality[3])
            }
        
        elif data_type == DType.STR:
            return {
                "vitality": (str(self.vitality[0]), str(self.vitality[1]), str(self.vitality[2]), str(self.vitality[3])),
                "constitution": (str(self.constitution[0]), str(self.constitution[1]), str(self.constitution[2]), str(self.constitution[3])),
                "strength": (str(self.strength[0]), str(self.strength[1]), str(self.strength[2]), str(self.strength[3])),
                "agility": (str(self.agility[0]), str(self.agility[1]), str(self.agility[2]), str(self.agility[3])),
                "dexterity": (str(self.dexterity[0]), str(self.dexterity[1]), str(self.dexterity[2]), str(self.dexterity[3])),
                "perception": (str(self.perception[0]), str(self.perception[1]), str(self.perception[2]), str(self.perception[3])),
                "intelligence": (str(self.intelligence[0]), str(self.intelligence[1]), str(self.intelligence[2]), str(self.intelligence[3])),
                "rationality": (str(self.rationality[0]), str(self.rationality[1]), str(self.rationality[2]), str(self.rationality[3]))
            }
        
    def get_skills(self, data_type):
        if data_type == DType.INT:
            return {
                "navigation": (self.navigation[0], self.navigation[1], self.navigation[2], self.navigation[3]),
                "stealth": (self.stealth[0], self.stealth[1], self.stealth[2], self.stealth[3]),
                "combat": (self.combat[0], self.combat[1], self.combat[2], self.combat[3]),
                "hunting": (self.hunting[0], self.hunting[1], self.hunting[2], self.hunting[3]),
                "recovery": (self.recovery[0], self.recovery[1], self.recovery[2], self.recovery[3]),
                "salvaging": (self.salvaging[0], self.salvaging[1], self.salvaging[2], self.salvaging[3]),
                "resources": (self.resources[0], self.resources[1], self.resources[2], self.resources[3]),
                "alchemy": (self.alchemy[0], self.alchemy[1], self.alchemy[2], self.alchemy[3]),
                "bartering": (self.bartering[0], self.bartering[1], self.bartering[2], self.bartering[3]),
                "lockpicking": (self.lockpicking[0], self.lockpicking[1], self.lockpicking[2], self.lockpicking[3]),
                "cryptography": (self.cryptography[0], self.cryptography[1], self.cryptography[2], self.cryptography[3]),
                "engineering": (self.engineering[0], self.engineering[1], self.engineering[2], self.engineering[3]),
                "gunsmithing": (self.gunsmithing[0], self.gunsmithing[1], self.gunsmithing[2], self.gunsmithing[3]),
                "bladecasting": (self.bladecasting[0], self.bladecasting[1], self.bladecasting[2], self.bladecasting[3]),
                "neuralforging": (self.neuralforging[0], self.neuralforging[1], self.neuralforging[2], self.neuralforging[3]),
                "armorcrafting": (self.armorcrafting[0], self.armorcrafting[1], self.armorcrafting[2], self.armorcrafting[3])
            }
        
        elif data_type == DType.STR:
            return {
                "navigation": (str(self.navigation[0]), str(self.navigation[1]), str(self.navigation[2]), str(self.navigation[3])),
                "stealth": (str(self.stealth[0]), str(self.stealth[1]), str(self.stealth[2]), str(self.stealth[3])),
                "combat": (str(self.combat[0]), str(self.combat[1]), str(self.combat[2]), str(self.combat[3])),
                "hunting": (str(self.hunting[0]), str(self.hunting[1]), str(self.hunting[2]), str(self.hunting[3])),
                "recovery": (str(self.recovery[0]), str(self.recovery[1]), str(self.recovery[2]), str(self.recovery[3])),
                "salvaging": (str(self.salvaging[0]), str(self.salvaging[1]), str(self.salvaging[2]), str(self.salvaging[3])),
                "resources": (str(self.resources[0]), str(self.resources[1]), str(self.resources[2]), str(self.resources[3])),
                "alchemy": (str(self.alchemy[0]), str(self.alchemy[1]), str(self.alchemy[2]), str(self.alchemy[3])),
                "bartering": (str(self.bartering[0]), str(self.bartering[1]), str(self.bartering[2]), str(self.bartering[3])),
                "lockpicking": (str(self.lockpicking[0]), str(self.lockpicking[1]), str(self.lockpicking[2]), str(self.lockpicking[3])),
                "cryptography": (str(self.cryptography[0]), str(self.cryptography[1]), str(self.cryptography[2]), str(self.cryptography[3])),
                "engineering": (str(self.engineering[0]), str(self.engineering[1]), str(self.engineering[2]), str(self.engineering[3])),
                "gunsmithing": (str(self.gunsmithing[0]), str(self.gunsmithing[1]), str(self.gunsmithing[2]), str(self.gunsmithing[3])),
                "bladecasting": (str(self.bladecasting[0]), str(self.bladecasting[1]), str(self.bladecasting[2]), str(self.bladecasting[3])),
                "neuralforging": (str(self.neuralforging[0]), str(self.neuralforging[1]), str(self.neuralforging[2]), str(self.neuralforging[3])),
                "armorcrafting": (str(self.armorcrafting[0]), str(self.armorcrafting[1]), str(self.armorcrafting[2]), str(self.armorcrafting[3]))
            }

    def get_mastery(self, data_type):
        # ["carbines", "subcarbines", "lancers", "suppressors", "handcanons", "breachers", "launchers", "greatswords", "knives"]

        if data_type == DType.INT:
            return {
                "carbines": (self.carbines[0], self.carbines[1]),
                "subcarbines": (self.subcarbines[0], self.subcarbines[1]),
                "lancers": (self.lancers[0], self.lancers[1]),
                "suppressors": (self.suppressors[0], self.suppressors[1]),
                "handcanons": (self.handcanons[0], self.handcanons[1]),
                "breachers": (self.breachers[0], self.breachers[1]),
                "launchers": (self.launchers[0], self.launchers[1]),
                "greatswords": (self.greatswords[0], self.greatswords[1]),
                "knives": (self.knives[0], self.knives[1])
            }
        
        elif data_type == DType.STR:
            return {
                "carbines": (str(self.carbines[0]), str(self.carbines[1])),
                "subcarbines": (str(self.subcarbines[0]), str(self.subcarbines[1])),
                "lancers": (str(self.lancers[0]), str(self.lancers[1])),
                "suppressors": (str(self.suppressors[0]), str(self.suppressors[1])),
                "handcanons": (str(self.handcanons[0]), str(self.handcanons[1])),
                "breachers": (str(self.breachers[0]), str(self.breachers[1])),
                "launchers": (str(self.launchers[0]), str(self.launchers[1])),
                "greatswords": (str(self.greatswords[0]), str(self.greatswords[1])),
                "knives": (str(self.knives[0]), str(self.knives[1]))
            }
