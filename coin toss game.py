import random
def toss_coin():
    return bool(random.getrandbits(1))


def coin_toss_game(rounds:int=3):
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
    

if __name__ == '__main__':
    coin_toss_game()