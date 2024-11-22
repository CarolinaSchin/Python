import random

moves = ['rock', 'paper', 'scissors']


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RockPlayer(Player):
    def move(self):
        return 'rock'


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    print("Welcome to Rock Paper Scissors!")

    def move(self):
        move = input("Enter your move (rock, paper, scissors): ")
        while move not in moves:
            move = input("Invalid move."
                         "Please enter rock, paper, or scissors: ")
        return move


class ReflectPlayer(Player):
    def __init__(self):
        self.my_move = random.choice(moves)

    def move(self):
        return self.my_move

    def learn(self, my_move, their_move):
        self.my_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.my_move = random.choice(moves)

    def move(self):
        return self.my_move

    def learn(self, my_move, their_move):
        idx = moves.index(my_move)
        idx = (idx+1) % len(moves)
        self.my_move = moves[idx]


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score_p1 = 0
        self.score_p2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            self.score_p1 += 1
            print(f"Player 1 wins this round! "
                  f"Player 1: {self.score_p1}, Player 2: {self.score_p2}")
        elif beats(move2, move1):
            self.score_p2 += 1
            print(f"Player 2 wins this round! "
                  f"Player 1: {self.score_p1}, Player 2: {self.score_p2}")
        else:
            print(f"This round is a tie! "
                  f"Player 1: {self.score_p1}, Player 2: {self.score_p2}")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print(f"Final Score: "
              f"Player 1: {self.score_p1}, Player 2: {self.score_p2}")
        if self.score_p1 > self.score_p2:
            print("Player 1 wins the game!")
        elif self.score_p2 > self.score_p1:
            print("Player 2 wins the game!")
        else:
            print("The game is a tie!")
        print("Game over!")


if __name__ == '__main__':
    # game = Game(RockPlayer(), HumanPlayer())
    # game = Game(RandomPlayer(), RandomPlayer())
    game = Game(HumanPlayer(), RandomPlayer())
    # game = Game(ReflectPlayer(), HumanPlayer())
    # game = Game(CyclePlayer(), HumanPlayer())
    game.play_game()
