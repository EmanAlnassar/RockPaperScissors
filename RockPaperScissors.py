#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def move(self):
        move = random.choice(moves)
        return move

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):
    def __init__(self):
        self.name = input("PlEASE TYPE YOUR NAME TO START THE GAME?\n")
        self.points = 0

    def move(self):
        move = input("Type your move (Rock, Paper, Scissors)?\n").lower()
        while move not in moves:
            print("invalid input! \n")
            return self.move()
        else:
            return move

    def learn(self, my_move, their_move):
        pass


class ReflectPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.their_move = random.choice(moves)

    def move(self):
        return self.their_move

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class CyclePlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.index = 0

    def move(self):
        if self.index >= len(moves):
            self.index -= len(moves)
            return self.move()
        else:
            for move in range(len(moves)):
                move = moves[self.index]
                self.index += 1
                return move

    def learn(self, my_move, their_move):
        pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"{self.p1.name}: {move1}  {self.p2.name}: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2) is True:
            print(f"{self.p1.name} beats {self.p2.name}")
            self.p1.points += 1
        elif beats(move2, move1) is True:
            print(f"{self.p2.name} beats {self.p1.name}")
            self.p2.points += 1
        elif move1 == move2:
            print("It is a tie")
        print(f"{self.p1.name}: {self.p1.points} points "
              f"{self.p2.name}: {self.p2.points} points\n")
        print("------------------------\n")

    def playing_again(self):
        playing_again = input("Would you like to play over?"
                              "(Type: Yes or NO) \n").lower()
        if 'yes' in playing_again:
            return
        elif 'no' in playing_again:
            print("Game over!")
            return exit()
        else:
            self.playing_again()

    def play_game(self):
        print(f"Player 1: {self.p1.name} VS. Player 2: {self.p2.name}\n")
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        if self.p1.points == self.p2.points:
            print("No winner!\n")
        elif self.p1.points > self.p2.points:
            print(f"{self.p1.name} is the WINNER"
                  f"by {self.p1.points - self.p2.points} points\n")
        elif self.p2.points > self.p1.points:
            print(f"{self.p2.name} is the WINNER"
                  f"by {self.p2.points - self.p1.points} points\n")


if __name__ == '__main__':
    game = Game(Player(), Player())
    game.play_game()
