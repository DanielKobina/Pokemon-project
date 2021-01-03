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
    reader = csv.reader(fp) #Attaches reader to the file pointer
    next(reader,None) #Skip first line
    
    move_list = list()

    for line_list in reader:
        gen = line_list[2]
        if gen != '1':
            break
                
        attack_type = line_list[9] #2 phy, #3 spe, #1 status effect
        if attack_type == '1':
            continue
        
        ele_idx = int(line_list[3])
        element = element_id_list[ele_idx]     
        

        name = line_list[1].lower()

        #Power and accuracy sections
        power = line_list[4]
        if power == '':
            continue
        else:
            power = int(power)
            
        
        accuracy = line_list[6]
        if accuracy == '':
            continue
        else:
            accuracy = int(accuracy)
            
        move = Move(name,element,power,accuracy,attack_type)
        move_list.append(move)
        
    return move_list

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
    reader = csv.reader(fp) #Attaches reader to the file pointer
    next(reader,None) #Skip first line
    
    pokemon_list = list()
    ID_set = set() #In the file we only include the first instance of the pokemon
    # Not the second or third if they have one.
    
    for line_list in reader:
        gen = line_list[11]
        
        if gen != '1':
            break
        
        ID = int(line_list[0])
        if ID not in ID_set:
            ID_set.add(ID)
            
        else:
            continue
        
        name = line_list[1].lower()                
        element1 = line_list[2].lower()
        element2 = line_list[3].lower()
        
        #Have to be integer values
        hp = int(line_list[5])
        patt = int(line_list[6])
        pdef = int(line_list[7])
        satt = int(line_list[8])
        sdef = int(line_list[9])
        
        pokemon = Pokemon(name,element1,element2,None,
                          hp,patt,pdef,satt,sdef)
        
        pokemon_list.append(pokemon)
        
    return pokemon_list

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
    
    if choice.isdigit():
        try:
            #Has to be a deepcopy or else the pokemon returned is a reference
            return deepcopy(pokemon_list[int(choice)-1])
        
        except IndexError:
            return None
        
    for pokemon in pokemon_list:
        if choice == pokemon.get_name():
            
            #Has to be a deepcopy or else the pokemon returned is a reference
            return deepcopy(pokemon)
        
    return None
    

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
    element1 = pokemon.get_element1()
    element2 = pokemon.get_element2()

    #1 random move and 3 of the pokemon's type    
    val = randint(0,len(moves_list)-1)
    move = moves_list[val]
    pokemon.add_move(move)  
      
    while (pokemon.get_number_moves() < 4):
        val = randint(0,len(moves_list)-1)
        move = moves_list[val]
        if move.get_element() == element1 or move.get_element() == element2:
            if move not in pokemon.get_moves():
                pokemon.add_move(move)
    
    return None
    
def main():
        
    usr_inp = input("Would you like to have a pokemon battle?").lower()
    while usr_inp != 'n' and usr_inp != 'q' and usr_inp != 'y':
        usr_inp = input("Invalid option! Please enter a valid choice: Y/y, N/n or Q/q:").lower()
        
    if usr_inp != 'y':
        print("Well that's a shame, goodbye")
        return
    
    else:
        # From armgilles https://gist.github.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6
        mv_file = open("moves.csv")    
        move_list = read_file_moves(mv_file)
        
        # From https://github.com/veekun/pokedex/tree/master/pokedex/data/csv
        pk_file = open("pokemon.csv")
        pokemon_list = read_file_pokemon(pk_file)    
        
        #Loop for new battle
        while usr_inp != 'n' and usr_inp != 'q':
            #Phase 1 selected pokemon
            p1_inp = input("Player 1, choose a pokemon by name or index:").lower()
            p1_pk = choose_pokemon(p1_inp,pokemon_list)
            
            while p1_pk == None:
                p1_inp = input("Invalid option, choose a pokemon by name or index:").lower()
                p1_pk = choose_pokemon(p1_inp,pokemon_list)     


            p2_inp = input("Player 2, choose a pokemon by name or index:").lower()
            p2_pk = choose_pokemon(p2_inp,pokemon_list)
            
            while p2_pk == None:
                p2_inp = input("Invalid option, choose a pokemon by name or index:").lower()
                p2_pk = choose_pokemon(p2_inp,pokemon_list)   

            print()
            print("{:<15s} {:<15s} {:<15s} {:<15s} {:<15s} {:<15s}\n".format(
                    "name","hp","patt","pdef","satt","sdef"))
            print(p1_pk)
            print(p2_pk)     
            print()

            #Phase 2 select moves
            #Random, too many factors for what each pokemon can do
            add_moves(p1_pk,move_list)
            add_moves(p2_pk,move_list)
                      
            
            #Loop for new round in same battle
            while True:

                #Phase 3 battle
                #P1 turn
                print("Player 1's turn")
                print(p1_pk)
                p1_inp = input("Select an attack inbetween {} and {}:".format(1,p1_pk.get_number_moves()))
                while True:
                    if p1_inp.isdigit():
                        p1_inp = int(p1_inp)
                        if 1 <= p1_inp <= p1_pk.get_number_moves():
                            break
                        
                        else:
                            print("number out of index range")
                            p1_inp = input("Select an attack inbetween {} and {}:".format(1,p1_pk.get_number_moves()))
    
                    else:
                        if p1_inp.lower() == 'q':
                            break
                        
                        elif p1_inp.lower() == "show ele":
                            p1_pk.show_move_elements()

                        elif p1_inp.lower() == "show pow":
                            p1_pk.show_move_power()
                            
                        elif p1_inp.lower() == "show acc":
                            p1_pk.show_move_accuracy()
                            
                        else:
                            print("Invalid input")
                        p1_inp = input("Select an attack inbetween {} and {}:".format(1,p1_pk.get_number_moves()))

                if type(p1_inp) == str:
                    if p1_inp.lower() == 'q':
                        print("Player 1 quits, Player 2 has won the pokemon battle!")

                        break    
                mv = p1_pk.get_moves()[p1_inp-1]
                
                print("selected move:",mv.get_name())
                print()
                print("{} hp before:{}".format(p2_pk.get_name(),p2_pk.get_hp()))
                p1_pk.attack(mv,p2_pk)
                print("{} hp after:{}".format(p2_pk.get_name(),p2_pk.get_hp()))
                print()
                
                if p2_pk.get_hp() <= 0:
                    print("Player 2's pokmeon fainted, Player 1 has won the pokemon battle!")
                    break                        
                    
                    
                #P2 turn
                print("Player 2's turn")
                print(p2_pk)
                p2_inp = input("Select an attack inbetween {} and {}:".format(1,p1_pk.get_number_moves()))
                while True:
                    if p2_inp.isdigit():
                        p2_inp = int(p2_inp)
                        if 1 <= p2_inp <= p2_pk.get_number_moves():
                            break
                        
                        else:
                            print("number out of index range")
                            p2_inp = input("Select an attack inbetween {} and {}:".format(1,p2_pk.get_number_moves()))
    
                    else:
                        if p2_inp.lower() == 'q':
                            break
                        
                        elif p2_inp.lower() == "show ele":
                            p2_pk.show_move_elements()

                        elif p2_inp.lower() == "show pow":
                            p2_pk.show_move_power()
                            
                        elif p2_inp.lower() == "show acc":
                            p2_pk.show_move_accuracy()
                        
                        else:
                            print("Invalid input")
                            
                        p2_inp = input("Select an attack inbetween {} and {}:".format(1,p2_pk.get_number_moves()))
    
                if type(p2_inp) == str:    
                    if p2_inp.lower() == 'q':
                        print("Player 2 quits, Player 1 has won the pokemon battle!")
                        break
                
                mv = p2_pk.get_moves()[p2_inp-1]            
                
                print("selected move:",mv.get_name())
                print()
                print("{} hp before:{}".format(p1_pk.get_name(),p1_pk.get_hp()))
                p2_pk.attack(mv,p1_pk)
                print("{} hp before:{}".format(p1_pk.get_name(),p1_pk.get_hp()))
                print()
                
                if p1_pk.get_hp() <= 0:
                    print("Player 1's pokmeon fainted, Player 2 has won the pokemon battle!")
                    break           
                
                    
                #Phase 4 post-round(remaining hp)
                print("P1 hp after:", p1_pk.get_hp())
                print("P2 hp after:", p2_pk.get_hp())
                print()
        
            
            usr_inp = input("Battle over, would you like to have another?").lower()    
            while usr_inp != 'n' and usr_inp != 'q' and usr_inp != 'y':        
                usr_inp = input("Invalid option! Please enter a valid choice:").lower()
     
if __name__ == "__main__":
    main()