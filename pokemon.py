pokemon_map = {
    1 : "Bulbasaur",
    2 : "Pikachu",
    3 : "Charmender"
}

print (pokemon_map[2])
if pokemon_map.get(3) is None:
    print("Pokemon Not Found!")
else : print(pokemon_map[3])