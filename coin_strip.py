import random

class CoinStrip:

    def __init__(self, num_coins=4):
        self.num_coins = num_coins
        self.strip = []

    def make(self):
        self.strip = [0] * (self.num_coins * random.randrange(2, 7))

    def fill(self):
        fill_list = set()
        while len(fill_list) < self.num_coins:
            fill_list.add(random.randrange(0, len(self.strip)))
        for idx in fill_list:
            self.strip[idx] = 1

    def move_coin(self, coin, spaces):
        coin_idx = self._get_coin_idx(coin)
        new_coin_idx = coin_idx - spaces
        move = self._is_valid_move()
        self.strip[coin_idx] = 0
        self.strip[new_coin_idx] = 1

    def _get_coin_idx(self, coin):
        count = 0
        for idx in range(len(self.strip)):
            if self.strip[idx] == 1:
                count += 1
            if count == coin:
                return idx

    def _is_valid_move():
        pass

    def is_finished(self):
        for coin in self.strip[:self.num_coins]:
            if coin == 0:
                return False
        return True

    def to_s(self):
        count = 1
        strip_str = ""
        for i in self.strip:
            if i == 0:
                strip_str += " "
            else:
                strip_str += f"{count}"
                count += 1
            strip_str += "|"
        return strip_str[:-1]

    def show(self):
        board = self.to_s()
        space = "      "
        print()
        print(space, "*" * (len(board)+2))
        print(space, f"*{board}*")
        print(space, "*" * (len(board)+2), "\n")
