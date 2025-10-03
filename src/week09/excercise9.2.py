import os
import random
import pickle
from typing import List
from dataclasses import dataclass, field
@dataclass
class Player:
    number: int
    score: int = field(default_factory=lambda: random.randint(0, 10))

    def __str__(self):
        return f"Player_{self.number} score: {self.score}"

class Game:
    def __init__(self):
        self.players: List[Player] = []
        self.file_name = "game.data"

    def play(self):
        self.players = [Player(i + 1) for i in range(10)]
        print("Game played. Players initialized.")

    def save(self):
        mode = 'ab' if os.path.exists(self.file_name) else 'wb'
        with open(self.file_name, mode) as file:
            pickle.dump(self.players, file)
        print(f"Players saved to {self.file_name}.")

    def show(self):
        if not os.path.exists(self.file_name):
            print("No game data found.")
            return
        with open(self.file_name, 'rb') as file:
            try:
                while True:
                    players = pickle.load(file)
                    for player in players:
                        print(player)
            except EOFError:
                pass

    def clear(self):
        if os.path.exists(self.file_name):
            os.remove(self.file_name)
            print(f"{self.file_name} cleared.")
        else:
            print("No game data to clear.")

    def menu(self):
        while True:
            choice = input("(p)lay, (s)ave, (v)iew, (c)lear, e(x)it: ").strip().lower()
            if choice == 'p':
                self.play()
            elif choice == 's':
                self.save()
            elif choice == 'v':
                self.show()
            elif choice == 'c':
                self.clear()
            elif choice == 'x':
                print("Exiting the game.")
                break
            else:
                print("Invalid choice. Please try again.")
    def main(self):
        self.menu()


if __name__ == "__main__":
    game = Game()
    game.main()