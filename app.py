import random
import itertools
from termcolor import colored

suits = ['Hearts', 'Clubs', 'Spades', 'Diamonds']
cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


def valid_input():
    options = ['DRAW', 'EXIT']
    while True:
        value = input('[Gamebot] Answer %s: ' % options).upper()
        if value not in options:
            print('[Gamebot] Invalid Answer: %s (Accepted Answers: %s)' % (value, options))
        elif value == 'EXIT':
            print('Exiting...\n')
            return None
        else:
            return value


def draw(deck):
    computer_random_card = random.choice(deck)
    deck.remove(computer_random_card)
    user_random_card = random.choice(deck)
    deck.remove(user_random_card)
    print('[Gamebot] You Got: %s' % colored(user_random_card, 'green'))
    print('[Gamebot] Computer Got: %s' % colored(computer_random_card, 'red'))
    print('[Gamebot] Cards Remaining: %d' % len(deck))
    computer_random_card_value = cards[computer_random_card.split(' ')[0]]
    user_random_card = cards[user_random_card.split(' ')[0]]
    status = None
    if computer_random_card_value > user_random_card:
        print('[Gamebot] You Lost!')
        status = -1
    elif computer_random_card_value < user_random_card:
        print('[Gamebot] You Won!')
        status = 1
    else:
        print('[Gamebot] Tie')
        status = 0
    return [status, deck]


deck = list(' '.join(card) for card in itertools.product(list(cards.keys()), suits))
score = 0
while deck:
    value = valid_input()
    if value is None:
        break
    status, deck = draw(deck)
    score += status
    print('[Gamebot] Your Score: %d\n' % score)
print('[Gamebot] GAME OVER! Your Score: %d' % score)
