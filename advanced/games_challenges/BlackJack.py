import random

suits = ['Club', 'Heart', 'Diamond', 'Spade']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 
'Ten', 'Jack', 'Queen', 'King', 'Ace']
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6,
'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 
'Queen':10, 'King':10, 'Ace':11}

deck_order = []
game_number = 1
playing = True
card_table = []



class Deck:
    
    def __init__(self,sumPlayer = 0,sumDealer = 0):
       self.sumPlayer = sumPlayer
       self.sumDealer = sumDealer
  
    def make_deck(self):
        for suit in suits:
            for rank in ranks:
                made_card = rank + ' of ' + suit
                deck_order.append(made_card)
        random.shuffle(deck_order)
    
    def take_card(self):
        for table in range(6):
            card_table.append(deck_order.pop())
    
    def decision(self):
        return bool(input('Type anything to HIT or leave empty to STAY?\t'))
    
    def check_winner(self):
        if self.sumPlayer == self.sumDealer:
            print('\n\nTIE\n\n')
            
        elif self.sumPlayer > self.sumDealer or self.sumDealer >21:
            print('\n\n\n\nPLAYER WINS\n\n')
            return 2

        elif self.sumPlayer < self.sumDealer or self.sumPlayer >21:
            print('\n\nDEALER WINS\n\n')
            return 0   

    def play_again(self):
        return bool(input('Type anything to CONTINUE or ENTER to QUIT\t'))

class Dealer(Deck):
    
    def __init__(self,card_one,card_two,card_three=0):
        self.card_one = card_one
        self.card_two = card_two
        self.card_three = card_three
    
    def hand(self):
        if self.card_three != 0:
            print(f'\n=== Dealer ===\nCard 01:\t{self.card_one}\nCard 02:\txXxXxXxXxXxXx\nCard 03:\txXxXxXxXxXxXx\n\n\n')
        else:
            print(f'\n=== Dealer ===\nCard 01:\t{self.card_one}\nCard 02:\txXxXxXxXxXxXx\n\n\n')

    def check_points(self):
        sum_rank = 0
        value_hand = []

        if self.card_three != 0:
            for value in range(3):   ### How many card is table ##     
                card_rank = card_table[value].split()
                value_hand.append(values[card_rank[0]])
                sum_rank += value_hand[value]
            return sum_rank

        else:
            for value in range(2):   ### How many card is table ###     
                card_rank = card_table[value].split()
                value_hand.append(values[card_rank[0]])
                sum_rank += value_hand[value]
            return sum_rank 
        return sum_rank  
    
    def decision(self):
        if self.check_points() <=21:
            self.add_card()
        else:
            pass

    def add_card(self):
        self.card_three = card_table[2]

class Player(Deck):
    
    def __init__(self,card_one,card_two,card_three=0):
        self.card_one = card_one
        self.card_two = card_two
        self.card_three = card_three
    
    def hand(self):
        if self.card_three != 0:
            print(f'\n=== Player ===\nCard 03:\t{self.card_three}\n')
        else:
            print(f'=== Player ===\nCard 01:\t{self.card_one}\nCard 02:\t{self.card_two}\n')
    
    def check_points(self):
        sum_rank = 0
        value_hand = []

        if self.card_three != 0:
            for value in range(3,6):   ### How many card is table ##     
                card_rank = card_table[value].split()
                value_hand.append(values[card_rank[0]])
                sum_rank += value_hand[value-3]
            print(f'-------\n{card_table[5]} = {value_hand[2]}')
            print('Total sum is {}\n'.format(sum_rank))
            return sum_rank
        else:
            for value in range(3,5):   ### How many card is table ##     
                card_rank = card_table[value].split()
                value_hand.append(values[card_rank[0]])
                sum_rank += value_hand[value-3]
                print(f'{card_table[value]} = {value_hand[value-3]}')
            print('Total sum is {}'.format(sum_rank))
            return sum_rank
        return sum_rank

    def add_card(self):
        self.card_three = card_table[5]

class Account(Deck):
        
    def __init__(self):
        print('Account Created')
        self.wallet = 0
        self.bet = 0
    def create_account(self):
        self.wallet += int(input('How much to deposit?\t'))

    def place_bet(self):
        self.bet = int(input('BET VALUE?\t'))
        if self.bet > self.wallet:
            print('Funds Insufficient')
        else:
           self.wallet -= self.bet
        print(f" ======== bet = ${self.bet}") 

    def winner_money(self, result):
        if result == 2:
            print(f'WALLET BEFORE: {self.wallet}')
            self.wallet += self.bet * 2
            print(f'WALLET AFTER: {self.wallet}')
        else:
            pass
    

# First Step
human_account = Account()
human_account.create_account()

while playing:
    #Create a game object
    game = Deck()

    # make deck and distribute cards
    game.make_deck()
    game.take_card()

    # Dealer Hand
    computer = Dealer(card_table[0],card_table[1])
    computer.hand()

    # Human Hand and points
    human = Player(card_table[3],card_table[4])
    human.hand()
    human.check_points()

    # Decision 
    human_account.place_bet()

    if game.decision(): # return boolean
        human.add_card()
        human.check_points()

    # Dealer decision based on value < 21
    computer.decision()

    # Check winner
    game = Deck(human.check_points(),computer.check_points())
    result = game.check_winner()
    human_account.winner_money(result)
    playing = game.play_again()
    
    #Clear object and list 
    del game
    del computer
    del human
    card_table.clear()

    
