import random

class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color
    def __str__(self):
        return f'|{self.value} {self.color}|'

card_0_r = Card(0, 'red')
card_1_r = Card(1, 'red')
card_2_r = Card(2, 'red')
card_3_r = Card(3, 'red')
card_4_r = Card(4, 'red')
card_5_r = Card(5, 'red')
card_6_r = Card(6, 'red')
card_7_r = Card(7, 'red')
card_8_r = Card(8, 'red')
card_9_r = Card(9, 'red')

card_0_g = Card(0, 'green')
card_1_g = Card(1, 'green')
card_2_g = Card(2, 'green')
card_3_g = Card(3, 'green')
card_4_g = Card(4, 'green')
card_5_g = Card(5, 'green')
card_6_g = Card(6, 'green')
card_7_g = Card(7, 'green')
card_8_g = Card(8, 'green')
card_9_g = Card(9, 'green')

card_0_y = Card(0, 'yellow')
card_1_y = Card(1, 'yellow')
card_2_y = Card(2, 'yellow')
card_3_y = Card(3, 'yellow')
card_4_y = Card(4, 'yellow')
card_5_y = Card(5, 'yellow')
card_6_y = Card(6, 'yellow')
card_7_y = Card(7, 'yellow')
card_8_y = Card(8, 'yellow')
card_9_y = Card(9, 'yellow')

card_0_b = Card(0, 'blue')
card_1_b = Card(1, 'blue')
card_2_b = Card(2, 'blue')
card_3_b = Card(3, 'blue')
card_4_b = Card(4, 'blue')
card_5_b = Card(5, 'blue')
card_6_b = Card(6, 'blue')
card_7_b = Card(7, 'blue')
card_8_b = Card(8, 'blue')
card_9_b = Card(9, 'blue')

cards = [card_0_r,
        card_2_r,
        card_1_r,
        card_3_r,
        card_4_r,
        card_5_r,
        card_6_r,
        card_7_r,
        card_8_r,
        card_9_r,

        card_0_g, 
        card_1_g, 
        card_2_g, 
        card_3_g, 
        card_4_g, 
        card_5_g, 
        card_6_g, 
        card_7_g, 
        card_8_g, 
        card_9_g, 

        card_0_y,
        card_1_y,
        card_2_y,
        card_3_y,
        card_4_y,
        card_5_y,
        card_6_y,
        card_7_y,
        card_8_y,
        card_9_y,

        card_0_b,
        card_1_b,
        card_2_b,
        card_3_b,
        card_4_b,
        card_5_b,
        card_6_b,
        card_7_b,
        card_8_b,
        card_9_b,
        ]

def showing_cards(cards, owner):
    string = ''
    for i in range(len(cards)):
        string = string + f'|{cards[i].value} {cards[i].color}|'
    print(f'{owner} - {string}')

def create_deck(cards):
    deck = []
    for i in range(7):
        card_deck = random.choice(cards)
        deck.append(card_deck)
        cards.remove(card_deck)
    return deck



player_cards = create_deck(cards)
bot_cards = create_deck(cards)

showing_cards(player_cards, 'I')
showing_cards(bot_cards, 'Bot')

current_card = random.choice(cards)
cards.remove(current_card)
print(current_card)


def player_step(current_card):
    print('Choose a card')
    chosen_number = int(input())
    while  chosen_number != 0 and player_cards[chosen_number - 1].value != current_card.value and player_cards[chosen_number - 1].color != current_card.color:
        print('Wrong card, please choose different one.')
        chosen_number = int(input())
    if chosen_number == 0: #Берем карту
        adding_card = random.choice(cards)
        cards.remove(adding_card)
        print('You took:')
        print(adding_card)
        if adding_card.value == current_card.value or adding_card.color == current_card.color:
            current_card = adding_card
            
        else:
            player_cards.append(adding_card)
            return current_card #Пропуск хода

    else:
        current_card = player_cards[chosen_number - 1]
        player_cards.remove(current_card)
    return current_card


def bot_step(current_card):
    for i in range (len(bot_cards)):
        if bot_cards[i].value == current_card.value or bot_cards[i].color == current_card.color:
            current_card = bot_cards[i]
            bot_cards.remove(bot_cards[i])
            return current_card
        
    adding_card = random.choice(cards)
    cards.remove(adding_card)
    print('Bot took')
    print(adding_card)
    if adding_card.value == current_card.value or adding_card.color == current_card.color:
        return adding_card

    else:
        bot_cards.append(adding_card)
        return current_card #Пропуск хода


            

#Ход игрока
current_card = player_step(current_card)
print('Playing card')    
print(current_card)
showing_cards(player_cards, 'I')


#ход бота
current_card = bot_step(current_card)
print('Playing card')    
print(current_card)
showing_cards(bot_cards, 'Bot')

