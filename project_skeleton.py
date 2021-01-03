import csv
from random import randint
from random import seed
from copy import deepcopy

from pokemon import Pokemon
from pokemon import Move

seed(1) #Set the seed so that the same events always happen


#DO NOT CHANGE THIS!!!
# =============================================================================
element_id_list = [None, "normal", "fighting", "flying", "poison", "ground", "rock", 
                   "bug", "ghost", "steel", "fire", "water", "grass", "electric", 
                   "psychic", "ice", "dragon", "dark", "fairy"]

#Element list to work specifically with the moves.csv file.
#   The element column from the moves.csv files gives the elements as integers.
#   This list returns the actual element when given an index
# =============================================================================
    
def read_file_moves(fp):  
    """
    Input:
        fp: file pointer for moves.csv
            
    Output:
        list of move objects
        
    Algorithm:
        Reads fp line by line and creates move objects. Each object that fills the 
            project criteria is added to the returned move list.
    """


def read_file_pokemon(fp):
    """
    Input:
        fp: file pointer for pokemon.csv
            
    Output:
        list of pokemon objects
        
    Algorithm:
        Reads fp line by line and creates pokemon objects. Each object that fills the 
            project criteria is added to the returned pokemon list.
    """
    pass

def choose_pokemon(choice,pokemon_list):
    """
    Input:
        choice: string 
        pokemon_list: list of available Pokemon objects
            
    Output:
        None
        
    Algorithm:
        Adds moves to the pokemon until the pokemon has four moves.
        First a random move is added, then three moves of the same type are added.
    
    DO NOT change pokemon_list in this function because it is passed by reference
    """
    pass

def add_moves(pokemon,moves_list):
    """
    Input:
        pokemon: Pokemon object
        move_list: list of available Move objects
            
    Output:
        None
        
    Algorithm:
        Adds moves to the pokemon until the pokemon has four moves.
        First a random move is added, then three moves of the same type are added.
        
    DO NOT change moves_list in this function because it is passed by reference
    """
    pass

def main():
        
    usr_inp = input("Would you like to have a pokemon battle?").lower()
    while usr_inp != 'n' and usr_inp != 'q' and usr_inp != 'y':
        usr_inp = input("Invalid option! Please enter a valid choice: Y/y, N/n or Q/q:").lower()
        
    if usr_inp != 'y':
        print("Well that's a shame, goodbye")
        return
    
    else:
        pass
    
if __name__ == "__main__":
    main()