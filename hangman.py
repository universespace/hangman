
a=[None,None].append('1')

class Card:
    suits = ['spades',
          'hearts',
           'diamonds',
           'clubs']


    values = [None,None,
            '2','3','4','5','6','7','8','9','10',
            'Jack','Queen','King','Ace']
    
    # values = [None,None]+list(map(str,list(range(2, 11))))+['Jack','Queen','King','Ace']
    # values = [None,None]+[str(x) for x in list(range(2, 11))]+['Jack','Queen','King','Ace']

    def __init__(self,v,s):
        '''suit and value are both int'''
        self.value = v
        self.suit = s

        #print(self)

    def __lt__(self,c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False

        # if self.value == c2.value
            # return self.suit < c2.suit
        # return self.value < c2.value
            
        return False

    def __gt__(self,c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] + ' of ' + self.suits[self.suit]
        return v


#card1 = Card(10,0)
#card2 = Card(10,3)
#print(card1 < card2)
#print([card1,card2])


from random import shuffle

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

#deck = Deck()
#for card in deck.cards:
#    print(card)


class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name



class Game:
    def __init__(self):
        name1 = input('p1 name ')
        name2 = input('p2 name ')
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self,winner):
        w = '{} wins this round'
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = '{} drew {} {} drew {}'
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards=self.deck.cards
        print('beginning War!')
        while len(cards) >= 2:
            m = 'q to quit. Any' + 'key to play:'
            response = input(m)
            if response == 'q':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)
        
        if win == 'It was a tie!':
            print('War is over. '+win)
        else:
            print('War is over. {} wins {} rounds. {} wins'.format(win[0],win[1],win[0]))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return [p1.name,p1.wins]
        if p1.wins < p2.wins:
            return [p2.name,p2.wins]
        return 'It was a tie!'

game = Game()
game.play_game()
