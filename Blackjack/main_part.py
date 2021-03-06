import random
from card import Card


class Blackjack:
    def __init__(self, seed):
        self.cards = [Card(i) for i in range(52)]
        random.seed(seed)
        random.shuffle(self.cards)

    def pop(self):
        return self.cards.pop(0)

    def show(self, hide):
        pass  # 後のクエストで作成します


if __name__ == '__main__':
    bj = Blackjack(0)
    print(bj.pop(), bj.pop(), bj.pop(), bj.pop())
