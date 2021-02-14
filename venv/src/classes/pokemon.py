import tensorflow

class Pokemon:
    def __init__(self, name, number, pkmn_type):
        self.name = name
        self.number = number
        self.pkmn_type = pkmn_type
        self.ability = None
        self.move_list = []
        self.hp_percentage = 1

    def add_move(self):
        pass