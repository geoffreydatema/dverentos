from data.engine_constants import DType

class Player():
    def __init__(self, game_manager):
        self.game_manager = game_manager
        
        self.vitality = [0, 0, 0, 0]

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
                "vitality": self.vitality
            }
        
        elif data_type == DType.STR:
            return {
                "vitality": (str(self.vitality[0]), str(self.vitality[1]), str(self.vitality[2]), str(self.vitality[3]))
            }