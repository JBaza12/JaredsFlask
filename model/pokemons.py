import random
import base64
import base64

# Specify the path to your image file
#image_file_path = "/home/ronit/vscode/CSP_BLOG_RT/images/charmander.jpg"

# Function to convert an image to base64
def image_to_base64(image_path):
    try:
        with open(image_path, 'rb') as image_file:
            # Read the binary data of the image
            image_binary = image_file.read()
            
            # Encode the binary data as base64
            base64_data = base64.b64encode(image_binary).decode('utf-8')
            
            return base64_data
    except FileNotFoundError:
        print(f"File '{image_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

# Call the function to get the base64 representation of the image
#base64_image = image_to_base64(image_file_path)
charmander_image=image_to_base64("./images/charmander.jpg")
pikachu_image=image_to_base64("./images/pikachu.jpg")

#List of pokemon 0001-0100 format might be wrong vscode keeps saying there is a bug
pokemon_data = []
#List of Pokemon and their information that will eventually be transferred into the pokemon data list with name
pokemon_list = [
    "Bulbasaur",
    "Ivysaur",
    "Venusaur",
    "Charmander",
    "Charmeleon",
    "Charizard",
    "Squirtle",
    "Wartortle",
    "Blastoise",
    "Caterpie",
    "Metapod",
    "Butterfree"
]

pokemon_info = [
    "Bulbasaur info",
    "Ivysaur  info",
    "Venusaur  info",
    "Charmander  info",
    "Charmeleon  info",
    "Charizard  info",
    "Squirtle  info",
    "Wartortle  info",
    "Blastoise  info",
    "Caterpie  info",
    "Metapod  info",
    "Butterfree  info"
]

image_dict = {
    "Charmander": charmander_image,
    "Pikachu": pikachu_image,
    # Add more mappings for other Pokémon
}

def initPokemons():
    
    item_id = 0
    for item, info in zip(pokemon_list, pokemon_info):
        pokemon_data.append({"id": item_id, "pokemon": item, "info": info, "upvote": 0, "downvote": 0, "image": image_dict.get(item, None)})
        item_id += 1
    #adding default upvotes (10) happens for random pokemon
    for i in range(100000):
        id = getRandomPokemon()['id']
        addUpVote(id)
    #adding default downvotes (5) for random pokemon
    for i in range(50000):
        id = getRandomPokemon()['id']
        addDownVote(id)

#returns all pokemon and their information
def getPokemons():
    return(pokemon_data)

#gets a specific pokemon and returns specific informaiton
def getPokemon(id):
    return(pokemon_data[id])

#gets a random pokemon and returns information
def getRandomPokemon():
    return(random.choice(pokemon_data))

#Upvote Pokemon function
def bestPokemon():
    best = 0 
    bestID = -1
    for pokemon in getPokemons():
        if pokemon['upvote'] > best:
            best = pokemon['upvote']
            bestID = pokemon['id']
    return pokemon_data[bestID]

#Downvote Pokemon function
def worstPokemon():
    worst = 0 
    worstID = -1
    for pokemon in getPokemons():
        if pokemon['downvote'] > worst:
            worst = pokemon['downvote']
            worstID = pokemon['id']
    return pokemon_data[worstID]

#Add Upvote, make it take affect 
def addUpVote(id):
    pokemon_data[id]['upvote'] = pokemon_data[id]['upvote'] +1
    return pokemon_data[id]['upvote']

#Add Downvote, make it take affect
def addDownVote(id):
    pokemon_data[id]['downvote'] = pokemon_data[id]['downvote'] +1
    return pokemon_data[id]['downvote']
#printing out the pokemon
def printPokemon(pokemon):
    print(pokemon['id'],pokemon['pokemon'],"\n", "upvotes: ", pokemon['upvote'], "\n", "downvote: ", pokemon['downvote'], "\n")
#function made to count the number of pokemon
def countPokemons():
    return len(pokemon_data)
# running all the functions and conducting tests of the different functions above and making they run as supposed too.
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