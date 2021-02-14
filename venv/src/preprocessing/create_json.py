import json
import requests
import re


def create_ability_list():
    r = requests.get("https://bulbapedia.bulbagarden.net/wiki/Ability#List_of_Abilities")
    regex_text = r.text.split('id=\"List_of_Abilities\"')[1].split("In_other_games")[0]
    match = re.findall('(?<=\/wiki\/)\S+(?=_\(Ability\))', regex_text)
    match.append("noability")
    abilities_dict = {}

    num = 1
    for ability in match:
        cleaned = ability.lower()
        cleaned = cleaned.replace("_", "").replace("%27", "")
        abilities_dict[cleaned] = num
        num += 1

    with open('../pokedex_data/abilities.json', "w") as file:
        json.dump(abilities_dict, file)


if __name__ == "__main__":
    create_ability_list()
