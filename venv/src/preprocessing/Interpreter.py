import json


class Interpreter:

    @staticmethod
    def find(self, value, file):
        with open(file) as f:
            data = json.load(f)
            return int(data[value])

    @staticmethod
    def find_type(self, pkmn_type):
        self.find(pkmn_type, "../pokedex_data/types.json")
