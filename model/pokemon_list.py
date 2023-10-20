import random

#List of pokemon 0001-0100 format might be wrong vscode keeps saying there is a bug

poke_list = [
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
    },
    {
        "name": "Charizard",
        "hp": 12,
        "attack": 10,
        "height": "67",
        "weight_in_lbs": "199.5",
        "abilities": "Blaze",
        "type": "Fire/Flying",
        "weakness": ["Water", "Rock", "Electric"]
    },
    {
        "name": "Squirtle",
        "hp": 8,
        "attack": 7,
        "height": "20",
        "weight_in_lbs": "19.8",
        "abilities": "Torrent",
        "type": "Water",
        "weakness": ["Grass", "Electric"]
    },
    {
        "name": "Wartortle",
        "hp": 11,
        "attack": 8,
        "height": "39",
        "weight_in_lbs": "49.6",
        "abilities": "Torrent",
        "type": "Water",
        "weakness": ["Grass", "Electric"]
    },
    {
        "name": "Blastoise",
        "hp": 13,
        "attack": 9,
        "height": "63",
        "weight_in_lbs": "188.5",
        "abilities": "Torrent",
        "type": "Water",
        "weakness": ["Grass", "Electric"]
    },
    {
        "name": "Caterpie",
        "hp": 6,
        "attack": 3,
        "height": "12",
        "weight_in_lbs": "6.4",
        "abilities": "Shield Dust",
        "type": "Bug",
        "weakness": ["Fire", "Flying", "Rock"]
    },
    {
        "name": "Metapod",
        "hp": 7,
        "attack": 4,
        "height": "28",
        "weight_in_lbs": "21.8",
        "abilities": "Shed Skin",
        "type": "Bug",
        "weakness": ["Fire", "Flying", "Rock"]
    },
    {
        "name": "Butterfree",
        "hp": 10,
        "attack": 9,
        "height": "43",
        "weight_in_lbs": "70.5",
        "abilities": "Compound Eyes",
        "type": "Bug/Flying",
        "weakness": ["Electric", "Ice", "Rock"]
    },
    {
        "name": "Weedle",
        "hp": 6,
        "attack": 5,
        "height": "12",
        "weight_in_lbs": "7.1",
        "abilities": "Shield Dust",
        "type": "Bug/Poison",
        "weakness": ["Fire", "Flying", "Psychic", "Rock"]
    },
    {
        "name": "Kakuna",
        "hp": 7,
        "attack": 5,
        "height": "24",
        "weight_in_lbs": "22",
        "abilities": "Shed Skin",
        "type": "Bug/Poison",
        "weakness": ["Fire", "Flying", "Psychic", "Rock"]
    },
    {
        "name": "Beedrill",
        "hp": 9,
        "attack": 8,
        "height": "47",
        "weight_in_lbs": "65",
        "abilities": "Swarm",
        "type": "Bug/Poison",
        "weakness": ["Fire", "Flying", "Psychic", "Rock"]
    },
    {
        "name": "Pidgey",
        "hp": 8,
        "attack": 6,
        "height": "12",
        "weight_in_lbs": "4",
        "abilities": "Keen Eye",
        "type": "Normal/Flying",
        "weakness": ["Electric", "Ice", "Rock"]
    },
    {
        "name": "Pidgeotto",
        "hp": 10,
        "attack": 8,
        "height": "39",
        "weight_in_lbs": "66.1",
        "abilities": "Keen Eye",
        "type": "Normal/Flying",
        "weakness": ["Electric", "Ice", "Rock"]
    },
    {
        "name": "Pidgeot",
        "hp": 12,
        "attack": 9,
        "height": "87",
        "weight_in_lbs": "87.1",
        "abilities": "Keen Eye",
        "type": "Normal/Flying",
        "weakness": ["Electric", "Ice", "Rock"]
    },
    {
        "name": "Rattata",
        "hp": 6,
        "attack": 7,
        "height": "12",
        "weight_in_lbs": "7.7",
        "abilities": "Run Away",
        "type": "Normal",
        "weakness": ["Fighting"]
    },
    {
        "name": "Raticate",
        "hp": 9,
        "attack": 8,
        "height": "28",
        "weight_in_lbs": "40.8",
        "abilities": "Run Away",
        "type": "Normal",
        "weakness": ["Fighting"]
    },
    {
        "name": "Spearow",
        "hp": 7,
        "attack": 8,
        "height": "12",
        "weight_in_lbs": "4.4",
        "abilities": "Keen Eye",
        "type": "Normal/Flying",
        "weakness": ["Electric", "Ice", "Rock"]
    },
    {
        "name": "Fearow",
        "hp": 9,
        "attack": 9,
        "height": "47",
        "weight_in_lbs": "83.8",
        "abilities": "Keen Eye",
        "type": "Normal/Flying",
        "weakness": ["Electric", "Ice", "Rock"]
    },
    {
        "name": "Ekans",
        "hp": 8,
        "attack": 7,
        "height": "79",
        "weight_in_lbs": "15.2",
        "abilities": "Intimidate",
        "type": "Poison",
        "weakness": ["Ground", "Psychic"]
    },
    {
        "name": "Arbok",
        "hp": 11,
        "attack": 8,
        "height": "118",
        "weight_in_lbs": "143.3",
        "abilities": "Intimidate",
        "type": "Poison",
        "weakness": ["Ground", "Psychic"]
    },
    {
        "name": "Pikachu",
        "hp": 8,
        "attack": 9,
        "height": "16",
        "weight_in_lbs": "13.2",
        "abilities": "Static",
        "type": "Electric",
        "weakness": ["Ground"]
    },
    {
        "name": "Raichu",
        "hp": 9,
        "attack": 10,
        "height": "31",
        "weight_in_lbs": "66.1",
        "abilities": "Static",
        "type": "Electric",
        "weakness": ["Ground"]
    },
    {
        "name": "Sandshrew",
        "hp": 9,
        "attack": 8,
        "height": "24",
        "weight_in_lbs": "26.5",
        "abilities": "Sand Veil",
        "type": "Ground",
        "weakness": ["Water", "Grass", "Ice"]
    },
    {
        "name": "Sandslash",
        "hp": 11,
        "attack": 9,
        "height": "39",
        "weight_in_lbs": "55.1",
        "abilities": "Sand Veil",
        "type": "Ground",
        "weakness": ["Water", "Grass", "Ice"]
    },
    {
        "name": "Nidoran♀",
        "hp": 9,
        "attack": 7,
        "height": "20",
        "weight_in_lbs": "15.4",
        "abilities": "Poison Point",
        "type": "Poison",
        "weakness": ["Ground", "Psychic"]
    },
    {
        "name": "Nidorina",
        "hp": 11,
        "attack": 8,
        "height": "35",
        "weight_in_lbs": "44.1",
        "abilities": "Poison Point",
        "type": "Poison",
        "weakness": ["Ground", "Psychic"]
    },
    {
        "name": "Nidoqueen",
        "hp": 13,
        "attack": 9,
        "height": "51",
        "weight_in_lbs": "132.3",
        "abilities": "Poison Point",
        "type": "Poison/Ground",
        "weakness": ["Ground", "Psychic", "Water", "Ice", "Grass"]
    },
    {
        "name": "Nidoran♂",
        "hp": 9,
        "attack": 9,
        "height": "20",
        "weight_in_lbs": "19.8",
        "abilities": "Poison Point",
        "type": "Poison",
        "weakness": ["Ground", "Psychic"]
    },
    {
        "name": "Nidorino",
        "hp": 11,
        "attack": 10,
        "height": "35",
        "weight_in_lbs": "43.7",
        "abilities": "Poison Point",
        "type": "Poison",
        "weakness": ["Ground", "Psychic"]
    },
    {
        "name": "Nidoking",
        "hp": 13,
        "attack": 11,
        "height": "55",
        "weight_in_lbs": "137",
        "abilities": "Poison Point",
        "type": "Poison/Ground",
        "weakness": ["Ground", "Psychic", "Water", "Ice", "Grass"]
    },
    {
        "name": "Clefairy",
        "hp": 12,
        "attack": 6,
        "height": "24",
        "weight_in_lbs": "16.5",
        "abilities": "Cute Charm",
        "type": "Fairy",
        "weakness": ["Steel", "Poison"]
    },
    {
        "name": "Clefable",
        "hp": 13,
        "attack": 7,
        "height": "51",
        "weight_in_lbs": "88.2",
        "abilities": "Cute Charm",
        "type": "Fairy",
        "weakness": ["Steel", "Poison"]
    },
    {
        "name": "Vulpix",
        "hp": 7,
        "attack": 6,
        "height": "24",
        "weight_in_lbs": "21.8",
        "abilities": "Flash Fire",
        "type": "Fire",
        "weakness": ["Water", "Rock", "Ground"]
    },
    {
        "name": "Ninetales",
        "hp": 9,
        "attack": 8,
        "height": "47",
        "weight_in_lbs": "43.9",
        "abilities": "Flash Fire",
        "type": "Fire",
        "weakness": ["Water", "Rock", "Ground"]
    },
    {
        "name": "Jigglypuff",
        "hp": 12,
        "attack": 3,
        "height": "12",
        "weight_in_lbs": "12.1",
        "abilities": "Cute Charm",
        "type": "Normal/Fairy",
        "weakness": ["Steel", "Poison"]
    },
    {
        "name": "Wigglytuff",
        "hp": 14,
        "attack": 5,
        "height": "39",
        "weight_in_lbs": "26.5",
        "abilities": "Cute Charm",
        "type": "Normal/Fairy",
        "weakness": ["Steel", "Poison"]
    },
    {
        "name": "Zubat",
        "hp": 6,
        "attack": 7,
        "height": "31",
        "weight_in_lbs": "16.5",
        "abilities": "Inner Focus",
        "type": "Poison/Flying",
        "weakness": ["Electric", "Ice", "Psychic", "Rock"]
    },
    {
        "name": "Golbat",
        "hp": 9,
        "attack": 8,
        "height": "63",
        "weight_in_lbs": "121.3",
        "abilities": "Inner Focus",
        "type": "Poison/Flying",
        "weakness": ["Electric", "Ice", "Psychic", "Rock"]
    },
    {
        "name": "Oddish",
        "hp": 7,
        "attack": 6,
        "height": "20",
        "weight_in_lbs": "11.9",
        "abilities": "Chlorophyll",
        "type": "Grass/Poison",
        "weakness": ["Fire", "Psychic", "Ice", "Flying"]
    },
    {
        "name": "Gloom",
        "hp": 8,
        "attack": 7,
        "height": "31",
        "weight_in_lbs": "19",
        "abilities": "Chlorophyll",
        "type": "Grass/Poison",
        "weakness": ["Fire", "Psychic", "Ice", "Flying"]
    },
    {
        "name": "Vileplume",
        "hp": 10,
        "attack": 8,
        "height": "47",
        "weight_in_lbs": "41",
        "abilities": "Chlorophyll",
        "type": "Grass/Poison",
        "weakness": ["Fire", "Psychic", "Ice", "Flying"]
    },
    {
        "name": "Paras",
        "hp": 8,
        "attack": 6,
        "height": "12",
        "weight_in_lbs": "11.9",
        "abilities": "Effect Spore",
        "type": "Bug/Grass",
        "weakness": ["Fire", "Flying", "Rock", "Ice"]
    },
    {
        "name": "Parasect",
        "hp": 9,
        "attack": 7,
        "height": "39",
        "weight_in_lbs": "65",
        "abilities": "Effect Spore",
        "type": "Bug/Grass",
        "weakness": ["Fire", "Flying", "Rock", "Ice"]
    },
    {
        "name": "Venonat",
        "hp": 7,
        "attack": 6,
        "height": "39",
        "weight_in_lbs": "66.1",
        "abilities": "Compound Eyes",
        "type": "Bug/Poison",
        "weakness": ["Fire", "Flying", "Psychic", "Rock"]
    },
    {
        "name": "Venomoth",
        "hp": 10,
        "attack": 8,
        "height": "51",
        "weight_in_lbs": "27.6",
        "abilities": "Shield Dust",
        "type": "Bug/Poison",
        "weakness": ["Fire", "Flying", "Psychic", "Rock"]
    }
    {
        "name": "Diglett",
        "hp": 7,
        "attack": 10,
        "height": "8",
        "weight_in_lbs": "1.8",
        "abilities": "Sand Veil",
        "type": "Ground",
        "weakness": ["Water", "Ice", "Grass"]
    },
    {
        "name": "Dugtrio",
        "hp": 10,
        "attack": 12,
        "height": "28",
        "weight_in_lbs": "73.4",
        "abilities": "Sand Veil",
        "type": "Ground",
        "weakness": ["Water", "Ice", "Grass"]
    },
    {
        "name": "Meowth",
        "hp": 8,
        "attack": 7,
        "height": "16",
        "weight_in_lbs": "9.3",
        "abilities": "Pickup",
        "type": "Normal",
        "weakness": ["Fighting"]
    },
    {
        "name": "Persian",
        "hp": 10,
        "attack": 8,
        "height": "43",
        "weight_in_lbs": "70.5",
        "abilities": "Limber",
        "type": "Normal",
        "weakness": ["Fighting"]
    },
    {
        "name": "Psyduck",
        "hp": 9,
        "attack": 6,
        "height": "28",
        "weight_in_lbs": "43.2",
        "abilities": "Damp",
        "type": "Water",
        "weakness": ["Electric", "Grass"]
    },
    {
        "name": "Golduck",
        "hp": 13,
        "attack": 9,
        "height": "67",
        "weight_in_lbs": "168.9",
        "abilities": "Damp",
        "type": "Water",
        "weakness": ["Electric", "Grass"]
    },
    {
        "name": "Mankey",
        "hp": 7,
        "attack": 10,
        "height": "20",
        "weight_in_lbs": "61.7",
        "abilities": "Vital Spirit",
        "type": "Fighting",
        "weakness": ["Flying", "Psychic"]
    },
    {
        "name": "Primeape",
        "hp": 10,
        "attack": 12,
        "height": "39",
        "weight_in_lbs": "70.5",
        "abilities": "Vital Spirit",
        "type": "Fighting",
        "weakness": ["Flying", "Psychic"]
    },
    {
        "name": "Growlithe",
        "hp": 10,
        "attack": 8,
        "height": "28",
        "weight_in_lbs": "41.9",
        "abilities": "Intimidate",
        "type": "Fire",
        "weakness": ["Water", "Rock", "Ground"]
    },
    {
        "name": "Arcanine",
        "hp": 13,
        "attack": 10,
        "height": "75",
        "weight_in_lbs": "341.7",
        "abilities": "Intimidate",
        "type": "Fire",
        "weakness": ["Water", "Rock", "Ground"]
    },
    {
        "name": "Poliwag",
        "hp": 8,
        "attack": 7,
        "height": "24",
        "weight_in_lbs": "27.3",
        "abilities": "Water Absorb",
        "type": "Water",
        "weakness": ["Electric", "Grass"]
    },
    {
        "name": "Poliwhirl",
        "hp": 10,
        "attack": 8,
        "height": "39",
        "weight_in_lbs": "44.1",
        "abilities": "Water Absorb",
        "type": "Water",
        "weakness": ["Electric", "Grass"]
    },
    {
        "name": "Poliwrath",
        "hp": 12,
        "attack": 10,
        "height": "51",
        "weight_in_lbs": "119",
        "abilities": "Water Absorb",
        "type": "Water/Fighting",
        "weakness": ["Electric", "Grass", "Psychic", "Fairy"]
    },
    {
        "name": "Abra",
        "hp": 6,
        "attack": 4,
        "height": "39",
        "weight_in_lbs": "43",
        "abilities": "Synchronize",
        "type": "Psychic",
        "weakness": ["Bug", "Ghost", "Dark"]
    },
    {
        "name": "Kadabra",
        "hp": 9,
        "attack": 7,
        "height": "51",
        "weight_in_lbs": "124.6",
        "abilities": "Synchronize",
        "type": "Psychic",
        "weakness": ["Bug", "Ghost", "Dark"]
    },
    {
        "name": "Alakazam",
        "hp": 11,
        "attack": 9,
        "height": "51",
        "weight_in_lbs": "105.8",
        "abilities": "Synchronize",
        "type": "Psychic",
        "weakness": ["Bug", "Ghost", "Dark"]
    },
    {
        "name": "Machop",
        "hp": 9,
        "attack": 8,
        "height": "39",
        "weight_in_lbs": "43",
        "abilities": "Guts",
        "type": "Fighting",
        "weakness": ["Flying", "Psychic"]
    },
    {
        "name": "Machoke",
        "hp": 12,
        "attack": 10,
        "height": "51",
        "weight_in_lbs": "155.4",
        "abilities": "Guts",
        "type": "Fighting",
        "weakness": ["Flying", "Psychic"]
    },
    {
        "name": "Machamp",
        "hp": 13,
        "attack": 11,
        "height": "63",
        "weight_in_lbs": "286.6",
        "abilities": "Guts",
        "type": "Fighting",
        "weakness": ["Flying", "Psychic"]
    },
    {
        "name": "Bellsprout",
        "hp": 7,
        "attack": 9,
        "height": "31",
        "weight_in_lbs": "8.8",
        "abilities": "Chlorophyll",
        "type": "Grass/Poison",
        "weakness": ["Fire", "Psychic", "Ice", "Flying"]
    },
    {
        "name": "Weepinbell",
        "hp": 10,
        "attack": 9,
        "height": "39",
        "weight_in_lbs": "14.1",
        "abilities": "Chlorophyll",
        "type": "Grass/Poison",
        "weakness": ["Fire", "Psychic", "Ice", "Flying"]
    },
    {
        "name": "Victreebel",
        "hp": 12,
        "attack": 11,
        "height": "67",
        "weight_in_lbs": "34.2",
        "abilities": "Chlorophyll",
        "type": "Grass/Poison",
        "weakness": ["Fire", "Psychic", "Ice", "Flying"]
    },
    {
        "name": "Tentacool",
        "hp": 11,
        "attack": 5,
        "height": "31",
        "weight_in_lbs": "100.3",
        "abilities": "Clear Body",
        "type": "Water/Poison",
        "weakness": ["Electric", "Psychic", "Ground"]
    },
    {
        "name": "Tentacruel",
        "hp": 13,
        "attack": 8,
        "height": "63",
        "weight_in_lbs": "121.3",
        "abilities": "Clear Body",
        "type": "Water/Poison",
        "weakness": ["Electric", "Psychic", "Ground"]
    },
    {
        "name": "Geodude",
        "hp": 8,
        "attack": 9,
        "height": "16",
        "weight_in_lbs": "44.1",
        "abilities": "Rock Head",
        "type": "Rock/Ground",
        "weakness": ["Water", "Grass", "Ice", "Fighting", "Ground", "Steel"]
    },
    {
        "name": "Graveler",
        "hp": 10,
        "attack": 11,
        "height": "39",
        "weight_in_lbs": "231.5",
        "abilities": "Rock Head",
        "type": "Rock/Ground",
        "weakness": ["Water", "Grass", "Ice", "Fighting", "Ground", "Steel"]
    },
    {
        "name": "Golem",
        "hp": 12,
        "attack": 12,
        "height": "51",
        "weight_in_lbs": "661.4",
        "abilities": "Rock Head",
        "type": "Rock/Ground",
        "weakness": ["Water", "Grass", "Ice", "Fighting", "Ground", "Steel"]
    },
    {
        "name": "Ponyta",
        "hp": 9,
        "attack": 9,
        "height": "39",
        "weight_in_lbs": "66.1",
        "abilities": "Run Away",
        "type": "Fire",
        "weakness": ["Water", "Rock", "Ground"]
    },
    {
        "name": "Rapidash",
        "hp": 12,
        "attack": 10,
        "height": "67",
        "weight_in_lbs": "209.4",
        "abilities": "Run Away",
        "type": "Fire",
        "weakness": ["Water", "Rock", "Ground"]
    },
    {
        "name": "Slowpoke",
        "hp": 10,
        "attack": 6,
        "height": "47",
        "weight_in_lbs": "79.4",
        "abilities": "Oblivious",
        "type": "Water/Psychic",
        "weakness": ["Electric", "Grass", "Bug", "Ghost", "Dark"]
    },
    {
        "name": "Slowbro",
        "hp": 13,
        "attack": 8,
        "height": "79",
        "weight_in_lbs": "173.1",
        "abilities": "Oblivious",
        "type": "Water/Psychic",
        "weakness": ["Electric", "Grass", "Bug", "Ghost", "Dark"]
    },
    {
        "name": "Magnemite",
        "hp": 8,
        "attack": 6,
        "height": "12",
        "weight_in_lbs": "13.2",
        "abilities": "Magnet Pull",
        "type": "Electric/Steel",
        "weakness": ["Ground", "Fire"]
    },
    {
        "name": "Magneton",
        "hp": 10,
        "attack": 9,
        "height": "39",
        "weight_in_lbs": "132.3",
        "abilities": "Magnet Pull",
        "type": "Electric/Steel",
        "weakness": ["Ground", "Fire"]
    },
    {
        "name": "Farfetch'd",
        "hp": 9,
        "attack": 7,
        "height": "31",
        "weight_in_lbs": "33.1",
        "abilities": "Keen Eye",
        "type": "Normal/Flying",
        "weakness": ["Electric", "Ice", "Rock"]
    },
    {
        "name": "Doduo",
        "hp": 8,
        "attack": 9,
        "height": "55",
        "weight_in_lbs": "86.4",
        "abilities": "Run Away",
        "type": "Normal/Flying",
        "weakness": ["Electric", "Ice", "Rock"]
    },
    {
        "name": "Dodrio",
        "hp": 10,
        "attack": 10,
        "height": "71",
        "weight_in_lbs": "187.8",
        "abilities": "Run Away",
        "type": "Normal/Flying",
        "weakness": ["Electric", "Ice", "Rock"]
    },
    {
        "name": "Seel",
        "hp": 9,
        "attack": 6,
        "height": "43",
        "weight_in_lbs": "198.4",
        "abilities": "Thick Fat",
        "type": "Water",
        "weakness": ["Electric", "Grass"]
    },
     {
        "name": "Dewgong",
        "hp": 9,
        "attack": 7,
        "height": "67",
        "weight_in_lbs": "264.6",
        "abilities": "Thick Fat",
        "type": "Water/Ice",
        "weakness": ["Electric", "Fighting", "Grass", "Rock"]
    },
    {
        "name": "Grimer",
        "hp": 10,
        "attack": 7,
        "height": "31",
        "weight_in_lbs": "66.1",
        "abilities": "Stench",
        "type": "Poison",
        "weakness": ["Ground", "Psychic"]
    },
    {
        "name": "Muk",
        "hp": 12,
        "attack": 9,
        "height": "47",
        "weight_in_lbs": "66.1",
        "abilities": "Stench",
        "type": "Poison",
        "weakness": ["Ground", "Psychic"]
    },
    {
        "name": "Shellder",
        "hp": 7,
        "attack": 6,
        "height": "24",
        "weight_in_lbs": "8.8",
        "abilities": "Shell Armor",
        "type": "Water",
        "weakness": ["Electric", "Fighting", "Grass"]
    },
    {
        "name": "Cloyster",
        "hp": 9,
        "attack": 8,
        "height": "51",
        "weight_in_lbs": "292.1",
        "abilities": "Shell Armor",
        "type": "Water/Ice",
        "weakness": ["Electric", "Fighting", "Grass", "Rock"]
    },
    {
        "name": "Gastly",
        "hp": 6,
        "attack": 6,
        "height": "51",
        "weight_in_lbs": "0.2",
        "abilities": "Levitate",
        "type": "Ghost/Poison",
        "weakness": ["Dark", "Ghost", "Ground", "Psychic"]
    },
    {
        "name": "Haunter",
        "hp": 9,
        "attack": 8,
        "height": "63",
        "weight_in_lbs": "0.2",
        "abilities": "Levitate",
        "type": "Ghost/Poison",
        "weakness": ["Dark", "Ghost", "Ground", "Psychic"]
    },
    {
        "name": "Gengar",
        "hp": 12,
        "attack": 9,
        "height": "63",
        "weight_in_lbs": "89.3",
        "abilities": "Cursed Body",
        "type": "Ghost/Poison",
        "weakness": ["Dark", "Ghost", "Ground", "Psychic"]
    },
    {
        "name": "Onix",
        "hp": 13,
        "attack": 10,
        "height": "394",
        "weight_in_lbs": "463",
        "abilities": "Rock Head",
        "type": "Rock/Ground",
        "weakness": ["Fighting", "Grass", "Ground", "Ice", "Steel", "Water"]
    },
    {
        "name": "Drowzee",
        "hp": 8,
        "attack": 6,
        "height": "39",
        "weight_in_lbs": "71.4",
        "abilities": "Insomnia",
        "type": "Psychic",
        "weakness": ["Bug", "Dark", "Ghost"]
    },
    {
        "name": "Hypno",
        "hp": 11,
        "attack": 8,
        "height": "63",
        "weight_in_lbs": "166.7",
        "abilities": "Insomnia",
        "type": "Psychic",
        "weakness": ["Bug", "Dark", "Ghost"]
    },
    {
        "name": "Krabby",
        "hp": 9,
        "attack": 8,
        "height": "16",
        "weight_in_lbs": "14.3",
        "abilities": "Hyper Cutter",
        "type": "Water",
        "weakness": ["Electric", "Grass"]
    },
    {
        "name": "Kingler",
        "hp": 11,
        "attack": 10,
        "height": "55",
        "weight_in_lbs": "132.3",
        "abilities": "Hyper Cutter",
        "type": "Water",
        "weakness": ["Electric", "Grass"]
    },
    {
        "name": "Voltorb",
        "hp": 8,
        "attack": 7,
        "height": "12",
        "weight_in_lbs": "22.9",
        "abilities": "Soundproof",
        "type": "Electric",
        "weakness": ["Ground"]
    },
]