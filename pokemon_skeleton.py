from random import randint


#DO NOT CHANGE THIS!!!
# =============================================================================
is_effective_dictionary = {'bug': {'dark', 'grass', 'psychic'}, 
                           'dark': {'ghost', 'psychic'},
                           'dragon': {'dragon'}, 
                           'electric': {'water', 'flying'}, 
                           'fairy': {'dark', 'dragon', 'fighting'},
                           'fighting': {'dark', 'ice', 'normal', 'rock', 'steel'}, 
                           'fire': {'bug', 'grass', 'ice', 'steel'}, 
                           'flying': {'bug', 'fighting', 'grass'}, 
                           'ghost': {'ghost', 'psychic'}, 
                           'grass': {'water', 'ground', 'rock'}, 
                           'ground': {'electric', 'fire', 'poison', 'rock', 'steel'}, 
                           'ice': {'dragon', 'flying', 'grass', 'ground'}, 
                           'normal': set(), 
                           'poison': {'fairy', 'grass'}, 
                           'psychic': {'fighting', 'poison'}, 
                           'rock': {'bug', 'fire', 'flying', 'ice'},
                           'steel': {'fairy', 'ice', 'rock'},
                           'water': {'fire', 'ground', 'rock'}
                           }

not_effective_dictionary = {'bug': {'fairy', 'flying', 'fighting', 'fire', 'ghost','poison','steel'}, 
                            'dragon': {'steel'}, 
                            'dark': {'dark', 'fairy', 'fighting'},
                            'electric': {'dragon', 'electric', 'grass'},
                            'fairy': {'fire', 'poison', 'steel'},
                            'fighting': {'bug', 'fairy', 'flying', 'poison', 'psychic'}, 
                            'fire': {'dragon', 'fire', 'rock', 'water'}, 
                            'flying': {'electric', 'rock', 'steel'}, 
                            'ghost': {'dark'}, 
                            'grass': {'bug', 'dragon', 'grass', 'fire', 'flying', 'poison', 'steel'}, 
                            'ground': {'bug','grass'}, 
                            'ice': {'fire', 'ice', 'steel', 'water'}, 
                            'normal': {'rock', 'steel'}, 
                            'poison': {'ghost', 'ground', 'poison', 'rock'}, 
                            'psychic': {'psychic', 'steel'}, 
                            'rock': {'fighting', 'ground', 'steel'}, 
                            'steel': {'electric', 'fire', 'steel', 'water'},
                            'water': {'dragon','grass', 'ice'}
                            }

no_effect_dictionary = {'electric': {'ground'}, 
                        'dragon': {'fairy'},
                        'fighting': {'ghost'}, 
                        'ghost': {'normal', 'psychic'}, 
                        'ground': {'flying'}, 
                        'normal': {'ghost'}, 
                        'poison': {'steel'},
                        'psychic': {'dark'}, 
                        
                        'bug': set(), 'dark': set(), 'fairy': set(),'fire': set(), 
                        'flying': set(), 'grass': set(), 'ice': set(), 
                        'rock': set(), 'steel': set(), 'water': set()
                        }

#Dictionaries that determine element advantages and disadvantages
# =============================================================================

class Move(object):
    def __init__(self, name = "", element = "Normal", power = 20, accuracy = 80,
                 attack_type = 2):
        
        self.name = name
        self.element = element
        self.power = power
        
        self.accuracy = accuracy
        self.attack_type = attack_type  #attack_type is 1, 2 or 3 
        # 1 - status moves, 2 - physical attacks, 3 - special attacks
        
    def __str__(self):
        pass

    def __repr__(self):
        pass
    
    def get_name(self):
        pass
    
    def get_element(self):
        pass
    
    def get_power(self):
        pass
    
    def get_accuracy(self):
        pass
    
    def get_attack_type(self):
        pass
        
        
class Pokemon(object):
    def __init__(self, name = "", element1 = "Normal", element2 = "", moves = None,
                 hp = 100, patt = 10, pdef = 10, satt = 10, sdef = 10):
        
        self.name = name
        self.element1 = element1
        self.element2 = element2
        
        self.hp = hp
        self.patt = patt
        self.pdef = pdef
        self.satt = satt
        self.sdef = sdef
        
        self.moves = moves
        
        try:
            if len(moves > 4):
                self.moves = moves[:4]
                
            else:
                self.moves = moves
                
        except TypeError: #For Nonetype
            self.moves = list()
            
    def __str__(self):
        pass

    def __repr__(self):
        pass

    def get_name(self):
        pass
    
    def get_element1(self):
        pass
    
    def get_element2(self):
        pass
    
    def get_hp(self):
        pass
    
    def get_patt(self):
        pass

    def get_pdef(self):
        pass

    def get_satt(self):
        pass

    def get_sdef(self):
        pass
    
    def get_moves(self):
        pass

    def get_number_moves(self):
        pass

            
    def choose(self,index):
        """
        Input:
            self: reference to pokemon object that called this method
            index: an index by which a move from the moves list is chosen
                
        Output:
            The corresponding move object or None
            
        Algorithm:
            Returns the move object corresponding to the index choosen
        """        
        pass

        
    def show_move_elements(self):
        """
        Input:
            self: reference to pokemon object that called this method
                
        Output:
            None
            
        Algorithm:
            Displays the elements of the pokemon's moves
        """  
        pass


    def show_move_power(self):
        """
        Input:
            self: reference to pokemon object that called this method
                
        Output:
            None
            
        Algorithm:
            Displays the power of the pokemon's moves
        """  
        pass


    def show_move_accuracy(self):
        """
        Input:
            self: reference to pokemon object that called this method
                
        Output:
            None
            
        Algorithm:
            Displays the accuracy of the pokemon's moves
        """  
        pass
        
        
    def add_move(self, move):
        """
        Input:
            self: reference to pokemon object that called this method
            move: a move object to be added to the pokemon's list of moves
                
        Output:
            None
            
        Algorithm:
            Adds a move object the list of pokemon's moves if the current number of moves
                the pokemon has is less than four.
        """  
        pass
            
        
    def attack(self, move, opponent):
        """
        Input:
            self: reference to pokemon object that called this method
            move: the move object that will be doing damage to the opponent
            opponent: reference to the opposing pokemon
                
        Output:
            None
            
        Algorithm:
            Calculates how much damage the opponent will receive and subtracts that
                from the opponent's hp
        """  
        pass
    
     
    def subtract_hp(self,damage):
        """
        Input:
            self: reference to pokemon object that called this method
            damage: the amount of hp this pokemon object is going to lose
                
        Output:
            None
            
        Algorithm:
            Subtracts the damage from this pokemon's hhp
        """  
        pass