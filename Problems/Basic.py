from random import random, randint


class Game:

    def __init__(self, size):

        self.size = size
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]
        self.snake_row = randint(0, size - 1)
        self.snake_col = randint(0, size - 1)
        self.grid[self.snake_row][self.snake_col] = 'X'

        while True:
            self.apple_row = randint(0, size - 1)
            self.apple_col = randint(0, size - 1)

            if self.apple_row != self.snake_row and self.apple_col == self.snake_col:
                break

        self.grid[self.apple_row][self.apple_col] = 'A'

    def print_board(self):
        for row in self.grid:
            line = "|"
            for cell in row:
                line += f"{cell} |"
            print(line)

    def status(self):
        if self.snake_row == self.apple_row and self.snake_col == self.apple_col:
            print("You win!")
            return False

        return True


    def move_snake(self, direction):
        self.grid[self.snake_row][self.snake_col] = ""
        if direction == 'up':
            self.snake_row = self.snake_row - 1
        #why do I need elif instead of just a series of ifs
        if direction == 'down':
            self.snake_row = self.snake_row+1

        if direction == 'left':
            self.snake_col = self.snake_col-1

        if direction == 'right':
            self.snake_col = self.snake_col+1

        self.grid[self.snake_row][self.snake_col] = 'X'



game = Game(4)

#I now need a way to take keyboard input as direction
#Also to keep the board displayed while we press the keys i.e. real time update
#For now ig the behavior I want is I keep typing up/down/whatever and each time board printed
#Also a mechanism to break out of the loop when apple and snake coordinates match
#Maybe loop breaks when

while game.status():
    game.print_board()
    print("Enter direction:")
    direction = input()
    if direction.lower() == "quit":
        break
    game.move_snake(direction)
    game.print_board()
    print()

