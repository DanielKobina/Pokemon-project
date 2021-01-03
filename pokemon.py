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
        ret_str = str(self.name)
        return ret_str

    def __repr__(self):
        return self.__str__()
    
    def get_name(self):
        return self.name
    
    def get_element(self):
        return self.element
    
    def get_power(self):
        return self.power
    
    def get_accuracy(self):
        return self.accuracy
    
    def get_attack_type(self):
        return self.attack_type
        
        
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
        ret_str = "{:<15s} {:<15d} {:<15d} {:<15d} {:<15d} {:<15d}\n".format(
                self.name,self.hp,self.patt,self.pdef,self.satt,self.sdef)
        
        ret_str += "{:<15s} {:<15s}\n".format(self.element1,self.element2)
        
        if len(self.moves) == 4:
            mv1 = str(self.moves[0])
            mv2 = str(self.moves[1])
            mv3 = str(self.moves[2])
            mv4 = str(self.moves[3])
            ret_str += "{:<15} {:<15} {:<15} {:<15}".format(mv1,mv2,mv3,mv4)
       
        else:
            for idx,move in enumerate(self.moves):
                ret_str = ret_str + str(move)
                if idx != len(self.moves)-1:
                    ret_str += 15 * ' '
        
        return ret_str

    def __repr__(self):
        return self.__str__()


    def get_name(self):
        return self.name
    
    def get_element1(self):
        return self.element1
    
    def get_element2(self):
        return self.element2
    
    def get_hp(self):
        return self.hp
    
    def get_patt(self):
        return self.patt

    def get_pdef(self):
        return self.pdef

    def get_satt(self):
        return self.satt

    def get_sdef(self):
        return self.sdef
    
    def get_moves(self):
        return self.moves

    def get_number_moves(self):
        return len(self.moves)

            
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
        try:
            return self.moves[index]
        
        except IndexError:
            return None
        
        
    def show_move_elements(self):
        """
        Input:
            self: reference to pokemon object that called this method
                
        Output:
            None
            
        Algorithm:
            Displays the elements of the pokemon's moves
        """  
        ret_str = ""
        if len(self.moves) == 4:
            mv1 = self.moves[0].get_element()
            mv2 = self.moves[1].get_element()
            mv3 = self.moves[2].get_element()
            mv4 = self.moves[3].get_element()
            ret_str += "{:<15} {:<15} {:<15} {:<15}".format(mv1,mv2,mv3,mv4)
       
        else:
            for idx,move in enumerate(self.moves):
                ret_str = ret_str + move.get_element()
                if idx != len(self.moves)-1:
                    ret_str += 15 * ' '  
                    
        print(ret_str)


    def show_move_power(self):
        """
        Input:
            self: reference to pokemon object that called this method
                
        Output:
            None
            
        Algorithm:
            Displays the power of the pokemon's moves
        """  
        ret_str = ""
        if len(self.moves) == 4:
            mv1 = self.moves[0].get_power()
            mv2 = self.moves[1].get_power()
            mv3 = self.moves[2].get_power()
            mv4 = self.moves[3].get_power()
            ret_str += "{:<15} {:<15} {:<15} {:<15}".format(mv1,mv2,mv3,mv4)
       
        else:
            for idx,move in enumerate(self.moves):
                ret_str = ret_str + move.get_power()
                if idx != len(self.moves)-1:
                    ret_str += 15 * ' '  
                    
        print(ret_str)


    def show_move_accuracy(self):
        """
        Input:
            self: reference to pokemon object that called this method
                
        Output:
            None
            
        Algorithm:
            Displays the accuracy of the pokemon's moves
        """  
        ret_str = ""
        if len(self.moves) == 4:
            mv1 = self.moves[0].get_accuracy()
            mv2 = self.moves[1].get_accuracy()
            mv3 = self.moves[2].get_accuracy()
            mv4 = self.moves[3].get_accuracy()
            ret_str += "{:<15} {:<15} {:<15} {:<15}".format(mv1,mv2,mv3,mv4)
       
        else:
            for idx,move in enumerate(self.moves):
                ret_str = ret_str + move.get_accuracy()
                if idx != len(self.moves)-1:
                    ret_str += 15 * ' '  
                    
        print(ret_str)  
        
        
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
        
        if len(self.moves) < 4:
            if type(move) == Move:
                self.moves.append(move)
                
            else:
                print("Invalid type!")
                
        else:
            print("This pokemon already has 4 moves.")
            
        
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
        
        damage = move.get_power()
        
        #If physical attack
        if move.get_attack_type() == '2':
            A = self.patt
            D = opponent.pdef
            
        #If special attack
        elif move.get_attack_type() == '3':
            A = self.satt
            D = opponent.sdef
            
        else:
            print("Invalid attack_type, turn skipped")
            return

        #Damage calculator
        damage = damage * (A/D) * 20
        damage = (damage / 50.0) + 2
        
        
        #Accuracy 
        acc_val = randint(1,100)
        if acc_val > move.get_accuracy():
            print("Move missed!")
            return #No need for further calculations
        
        
        modifier = 1.0
        
        se = 0
        ne = 0
        
        if opponent.get_element1() in is_effective_dictionary[move.get_element()]:
            #print("It's super effective!!!!")
            modifier = modifier * 2
            se += 1
            
        elif opponent.get_element1() in not_effective_dictionary[move.get_element()]:
            #print("Not very effective...")
            modifier = modifier * 0.5
            ne += 1
        
        elif opponent.get_element1()  in no_effect_dictionary[move.get_element()]:
            print("No effect!")            
            return #No need for further calculations
            
            
        if opponent.get_element2() in is_effective_dictionary[move.get_element()]:
            #print("It's super effective!!!!")
            modifier = modifier * 2
            se += 1
            
        elif opponent.get_element2() in not_effective_dictionary[move.get_element()]:
            #print("Not very effective...")
            modifier = modifier * 0.5
            ne += 1
        
        elif opponent.get_element2() in no_effect_dictionary[move.get_element()]:
            print("No effect!")            
            return #No need for further calculations
        
        #Determine printing message
        if se > ne:
            print("It's super effective!!!!")
            
        elif se < ne:
            print("Not very effective...")

        
        #Same-type attack bonus (STAB)
        if move.get_element() == self.element1 or move.get_element() == self.element2:
            modifier = modifier * 1.5
        
        damage = int(damage * modifier)
        opponent.subtract_hp(damage)
    
     
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
        
        #Hp should never become negative
        self.hp = max(self.hp - damage,0)