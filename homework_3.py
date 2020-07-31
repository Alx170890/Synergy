import random

class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return "{0} {1}".format(self.suit, self.value)

class Deck(object):
    def __init__(self, card):
        self.card = card

    def get_deck(self):
        cards = []
        suit = ["черве", "пика", "кресте", "бубей"]
        for s in suit:
            for v in range(6, 15):
                if v == 11:
                    v = "валетт"
                if v == 12:
                    v = "дама"
                if v == 13:
                    v = "король"
                if v == 14:
                    v = "туз"
                cards.append(str(self.card(v, s)))
        return cards

class Player(object):
    def __init__(self, name, card):
        self.card = card
        self.name = name

    def __str__(self):
        hand = ', '.join(self.card)
        return "{0} получает: {1}".format(self.name, hand)

def get_hand(card):
    hand = []
    i = 0
    while i < 6:
        i += 1
        index = random.randrange(0, len(card))
        cards = card[index]
        card.pop(index)
        hand.append(cards)
    return hand

def game():
    quantity_players = int(input("Введите количество игроков, не больше шести: "))
    if quantity_players > 6:
        print("Максимальное количество игроков: 6!")
    elif quantity_players:
        deck = Deck(Card)
        card = deck.get_deck()
        random.shuffle(card)
        trump = random.choice(card)
        i = 0
        while i < quantity_players:
            i += 1
            names = ["Alex", "John", "Bob", "Nikolas", "Andrew", "Julia", "Jessy", "Opra", "Vita"]
            player = Player(random.choice(names), get_hand(card))
            print(player)
        print("Козырь: " + trump)
    else:
        print("Нет игроков")
game()















