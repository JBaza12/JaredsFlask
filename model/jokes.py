import random

jokes_data = []
joke_list = [
    "If you give someone a program... you will frustrate them for a day; if you teach them how to program... you will "
    "frustrate them for a lifetime.",
    {"name": "Pikachu", "hp": 35, "level": 15, "type": "Electric"},
    "UNIX is basically a simple operating system... but you have to be a genius to understand the simplicity.",
    "Enter any 11-digit prime number to continue.",
    "If at first you don't succeed; call it version 1.0.",
    "Java programmers are some of the most materialistic people I know, very object-oriented",
    "The oldest computer can be traced back to Adam and Eve. It was an apple but with extremely limited memory. Just "
    "1 byte. And then everything crashed.",
    "Q: Why did Wi-Fi and the computer get married? A: Because they had a connection",
    "Bill Gates teaches a kindergarten class to count to ten. 1, 2, 3, 3.1, 95, 98, ME, 2000, XP, Vista, 7, 8, 10.",
    "Q: What’s a aliens favorite computer key? A: the space bar!",
    "There are 10 types of people in the world: those who understand binary, and those who don’t.",
    "If it wasn't for C, we’d all be programming in BASI and OBOL.",
    "Computers make very fast, very accurate mistakes.",
    "Q: Why is it that programmers always confuse Halloween with Christmas? A: Because 31 OCT = 25 DEC.",
    "Q: How many programmers does it take to change a light bulb? A: None. It’s a hardware problem.",
    "The programmer got stuck in the shower because the instructions on the shampoo bottle said: Lather, Rinse, Repeat.",
    "Q: What is the biggest lie in the entire universe? A: I have read and agree to the Terms and Conditions.",
    'An SQL statement walks into a bar and sees two tables. It approaches, and asks may I join you?'
]

# Initialize jokes
def initJokes():
    # setup jokes into a dictionary with id, joke, if_useful, if_not_useful
    item_id = 0
    for item in joke_list:
        jokes_data.append({"id": item_id, "joke": item, "if_useful": 0, "if_not_useful": 0})
        item_id += 1
    # prime some if_useful responses
    for i in range(10):
        id = getRandomJoke()['id']
        addJokeif_useful(id)
    # prime some if_useful responses
    for i in range(5):
        id = getRandomJoke()['id']
        addJokeif_not_useful(id)
        
# Return all jokes from jokes_data
def getJokes():
    return(jokes_data)

# Joke getter
def getJoke(id):
    return(jokes_data[id])

# Return random joke from jokes_data
def getRandomJoke():
    return(random.choice(jokes_data))

# Liked joke
def favoriteJoke():
    best = 0
    bestID = -1
    for joke in getJokes():
        if joke['if_useful'] > best:
            best = joke['if_useful']
            bestID = joke['id']
    return jokes_data[bestID]
    
# Jeered joke
def jeeredJoke():
    worst = 0
    worstID = -1
    for joke in getJokes():
        if joke['if_not_useful'] > worst:
            worst = joke['if_not_useful']
            worstID = joke['id']
    return jokes_data[worstID]

# Add to if_useful for requested id
def addJokeif_useful(id):
    jokes_data[id]['if_useful'] = jokes_data[id]['if_useful'] + 1
    return jokes_data[id]['if_useful']

# Add to if_not_useful for requested id
def addJokeif_not_useful(id):
    jokes_data[id]['if_not_useful'] = jokes_data[id]['if_not_useful'] + 1
    return jokes_data[id]['if_not_useful']

# Pretty Print joke
def printJoke(joke):
    print(joke['id'], joke['joke'], "\n", "if_useful:", joke['if_useful'], "\n", "if_not_useful:", joke['if_not_useful'], "\n")

# Number of jokes
def countJokes():
    return len(jokes_data)

# Test Joke Model
if __name__ == "__main__": 
    initJokes()  # initialize jokes
    
    # Most likes and most jeered
    best = favoriteJoke()
    print("Most liked", best['if_useful'])
    printJoke(best)
    worst = jeeredJoke()
    print("Most jeered", worst['if_not_useful'])
    printJoke(worst)
    
    # Random joke
    print("Random joke")
    printJoke(getRandomJoke())
    
    # Count of Jokes
    print("Jokes Count: " + str(countJokes()))