#!/usr/bin/env python3
import random
import time

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


def print_pause(S):
    print(S)
    time.sleep(1)


def intro():
    print("\n------------------------\n")
    print("ROCK-PAPER-SCISSORS GAME")
    print('\n------------------------\n')
    print_pause("WELCOME TO THE GAME!!\n")
    print_pause("*** You will play against 4 different")
    print_pause("artificial players, and you will play")
    print_pause("with each one a game of 3 rounds ***\n")


class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
        # players points will be summed and return under this variable.

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    # This player takes the random module to play his move.
    def __init__(self, name):
        super().__init__(name)

    def move(self):
        move = random.choice(moves)
        return move

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):
    # The only real player.
    def __init__(self):
        # Taking the user's name to make the game more personalized.
        self.name = input("PlEASE TYPE YOUR NAME TO START THE GAME?\n")
        self.points = 0

    def move(self):
        # He takes his move via an input of the user's keyboard.
        # lower() is a string method which turned all characters to lowercase.
        move = input("Type your move (Rock, Paper, Scissors)?\n").lower()
        # Theis lines check the user input which,
        # it has to be right and spelled correctly.
        # if the user input wrong or incorrect,
        # the user will try again until he writes it correctly.
        while move not in moves:
            print("invalid input! \n")
            return self.move()
        else:
            return move

    def learn(self, my_move, their_move):
        pass


class ReflectPlayer(Player):
    # This player learn the other player moves,
    # Then he returned it as his move.
    def __init__(self, name):
        # This lines to call the __init__ in the parent class.
        super().__init__(name)
        # For the first move, he will play randomly,
        # until he learn his opponents move.
        self.their_move = random.choice(moves)

    def move(self):
        # This function to return the other player move.
        return self.their_move

    def learn(self, my_move, their_move):
        # This function teach the player his opponents move.
        self.my_move = my_move
        self.their_move = their_move


class CyclePlayer(Player):
    # This player takes his move by cycling over the game moves.
    def __init__(self, name):
        # This lines to call the __init__ in the parent class.
        super().__init__(name)
        # An index variable to help us looping over the moves list.
        self.index = 0

    def move(self):
        # These lines make sure that the index value
        # stays within the length of the moves list.
        # So every time it reaches the moves list length, it will reset to 0.
        if self.index >= len(moves):
            self.index -= len(moves)
            return self.move()
        # Here the code that loops over the moves list by an index,
        # and increases it every time to move to the next string in the list.
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
        # This code takes the players moves and adds points to the right move.
        # Also, it's print who beats who.
        if beats(move1, move2) is True:
            print(f"{self.p1.name} beats {self.p2.name}")
            self.p1.points += 1
        elif beats(move2, move1) is True:
            print(f"{self.p2.name} beats {self.p1.name}")
            self.p2.points += 1
        elif move1 == move2:
            print("It is a tie")
        # This line prints the points of the players.
        print(f"{self.p1.name}: {self.p1.points} points "
              f"{self.p2.name}: {self.p2.points} points\n")
        print("------------------------\n")

    def playing_again(self):
        # This function take the user input to play again or to exit the game.
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
        # The code below compares the players points to determinate the winner,
        # and how many distinct points the winner has.
        if self.p1.points == self.p2.points:
            print("No winner!\n")
        elif self.p1.points > self.p2.points:
            print(f"{self.p1.name} is the WINNER"
                  f"by {self.p1.points - self.p2.points} points\n")
        elif self.p2.points > self.p1.points:
            print(f"{self.p2.name} is the WINNER"
                  f"by {self.p2.points - self.p1.points} points\n")


if __name__ == '__main__':

    computer_players = [Player('MonoMove'), RandomPlayer('CasualCommander'),
                        ReflectPlayer('CopyCat'), CyclePlayer('OverOrbit')]

    intro()
    User = HumanPlayer()
    while True:
        for player in computer_players:
            User.points = 0
            game = Game(User, player)
            game.play_game()
        game.playing_again()
