from asyncio import Handle
import random
from unicodedata import name


def win_lose(heads_count, tails_count, name:str):
    if heads_count > tails_count:
        print('{} Won!'.format(name))
    else:
        print('{} Lost!'.format(name))


def toss_coin():
    return bool(random.getrandbits(1))


def greet_user_name():
    print('Who are you?')
    name = input('> ')
    print('Hello, {}!'.format(name))
    return name


def coin_toss_game(rounds:int=3):
    name = greet_user_name()
    print('Tossing a coin...')
    results = []
    for rond in range(1, rounds + 1):
        if toss_coin():
            results.append(True)
            print('Round {}: Heads'.format(rond))
        else:
            results.append(False)
            print('Round {}: Tails'.format(rond))
    heads_count = results.count(True)
    tails_count = results.count(False)
    print('Heads: {}, Tails: {}'.format(heads_count, tails_count))
    win_lose(heads_count, tails_count, name)


if __name__ == '__main__':
    coin_toss_game()