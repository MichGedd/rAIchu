import json
import requests
import re
import lxml.html


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


def create_move_list():
    move_id = 1
    move_dict = {}
    r = lambda s: requests.get(s)

    while r(f"https://pokeapi.co/api/v2/move/{move_id}").status_code == 200:
        try:
            json_response = json.loads(r(f"https://pokeapi.co/api/v2/move/{move_id}").text)
            name = json_response["name"].replace("-", "")
            acc = json_response["accuracy"]
            power = json_response["power"]
            pp = json_response["pp"]
            priority = json_response["priority"]
            type = json_response["type"]["name"]
            damage_type = json_response["damage_class"]["name"]
            id = move_id

            move_dict[name] = {}

            move_dict[name]["power"] = power
            move_dict[name]["accuracy"] = acc
            move_dict[name]["pp"] = pp
            move_dict[name]["priority"] = priority
            move_dict[name]["type"] = type
            move_dict[name]["damage_type"] = damage_type
            move_dict[name]["id"] = id

            print(f"Added {name}")
        except:
            print(f"An error occured")

        move_id += 1

    with open('../pokedex_data/moves.json', "w") as file:
        json.dump(move_dict, file)


def create_item_list():
    item_id = 1
    item_dict = {}
    r = lambda s: requests.get(s)

    for i in range(1, 1006):
        if r(f"https://pokeapi.co/api/v2/item/{i}").status_code == 200:
            try:
                json_response = json.loads(r(f"https://pokeapi.co/api/v2/item/{i}").text)
                name = json_response["name"].replace("-", "")
                item_dict[name] = item_id
                print(f"Added {name}")
            except:
                print(f"An error occured")

            item_id += 1

    with open('../pokedex_data/items.json', "w") as file:
        json.dump(item_dict, file)

def create_pokemon_list():
    pokemon_dict = {}
    r = lambda s: requests.get(s)

    for i in range(1, 898):
        json_response = json.loads(r(f"https://pokeapi.co/api/v2/pokemon/{i}").text)
        name = json_response["name"]
        types = []

        try:
            for i in range(2):
                types.append(json_response["types"][i]["type"]["name"])
        except:
            pass

        pokemon_dict[name] = {}
        pokemon_dict[name]["types"] = types
        pokemon_dict[name]["id"] = i
        print(f"Added {name}")

    with open('../pokedex_data/pokemon.json', "w") as file:
        json.dump(pokemon_dict, file)

if __name__ == "__main__":
    create_pokemon_list()
