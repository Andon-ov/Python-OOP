from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if any([x for x in self.pokemons if x.name == pokemon.name]):
            return "This pokemon is already caught"

        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        for pokemon in self.pokemons:
            if pokemon.name == pokemon_name:
                self.pokemons.remove(pokemon)
                return f"You have released {pokemon_name}"

        return "Pokemon is not caught"

    def trainer_data(self):
        data = f"Pokemon Trainer {self.name}\n"
        data += f"Pokemon count {len(self.pokemons)}\n"
        for pokemon in self.pokemons:
            data += f"- {pokemon.pokemon_details()}\n"
        return data

