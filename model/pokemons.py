import random


#List of pokemon 0001-0100 format might be wrong vscode keeps saying there is a bug
pokemon_data = []
pokemon_list = [
    {
        "name": "Bulbasaur",
        "hp": 9,
        "attack": 7,
        "height": "28",
        "weight_in_lbs": "15.2",
        "abilities": "Overgrow",
        "type": "Grass/Poison",
        "weakness": ["Fire", "Psychic", "Ice", "Flying"]
    },
    {
        "name": "Ivysaur",
        "hp": 13,
        "attack": 8,
        "height": "39",
        "weight_in_lbs": "28.7",
        "abilities": "Overgrow",
        "type": "Grass/Poison",
        "weakness": ["Fire", "Psychic", "Ice", "Flying"]
    },
    {
        "name": "Venusaur",
        "hp": 14,
        "attack": 9,
        "height": "79",
        "weight_in_lbs": "220.5",
        "abilities": "Overgrow",
        "type": "Grass/Poison",
        "weakness": ["Fire", "Psychic", "Ice", "Flying"]
    },
    {
        "name": "Charmander",
        "hp": 7,
        "attack": 8,
        "height": "24",
        "weight_in_lbs": "18.7",
        "abilities": "Blaze",
        "type": "Fire",
        "weakness": ["Water", "Rock", "Ground"]
    },
    {
        "name": "Charmeleon",
        "hp": 10,
        "attack": 9,
        "height": "43",
        "weight_in_lbs": "41.9",
        "abilities": "Blaze",
        "type": "Fire",
        "weakness": ["Water", "Rock", "Ground"]
    }

]

def initPokemons():
    
    #moving pokemon from list to data
    item_id=0
    for item in pokemon_list:
        pokemon_data.append({"id": item_id, "pokemon": item, "upvote": 0, "downvote": 0})
        item_id += 1
    #adding default upvotes (10)
    for i in range(10):
        id = getRandomPokemon()['id']
        addUpVote(id)
    #adding default downvotes (5)
    for i in range(5):
        id = getRandomPokemon()['id']
        addDownVote(id)

#returns all pokemon
def getPokemons():
    return(pokemon_data)

#gets a specific pokemon
def getPokemon(id):
    return(pokemon_data[id])

#gets a random pokemon
def getRandomPokemon():
    return(random.choice(pokemon_data))

#Upvote Pokemon
def bestPokemon():
    best = 0 
    bestID = -1
    for pokemon in getPokemons():
        if pokemon['upvote'] > best:
            best = pokemon['upvote']
            bestID = pokemon['id']
    return pokemon_data[bestID]

#Downvote Pokemon
def worstPokemon():
    worst = 0 
    worstID = -1
    for pokemon in getPokemons():
        if pokemon['downvote'] > worst:
            worst = pokemon['downvote']
            worstID = pokemon['id']
    return pokemon_data[worstID]

#Add Upvote
def addUpVote(id):
    pokemon_data[id]['upvote'] = pokemon_data[id]['upvote'] +1
    return pokemon_data[id]['upvote']

#Add Downvote
def addDownVote(id):
    pokemon_data[id]['downvote'] = pokemon_data[id]['downvote'] +1
    return pokemon_data[id]['downvote']

def printPokemon(pokemon):
    print(pokemon['id'],pokemon['pokemon'],"\n", "upvotes: ", pokemon['upvote'], "\n", "downvote: ", pokemon['downvote'], "\n")

def countPokemons():
    return len(pokemon_data)

if __name__ == "__main__": 
    initPokemons()
    
    best= bestPokemon()
    print("Most Upvoted", best['upvote'])
    printPokemon(best)
    
    worst= worstPokemon()
    print("Most Downvoted", worst['downvote'])
    printPokemon(worst)
    
    print("Random Pokemon")
    printPokemon(getRandomPokemon())
    
    print("Pokemons Count: " + str(countPokemons()))