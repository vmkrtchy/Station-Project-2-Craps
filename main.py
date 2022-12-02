from random import randint

class Game:
    def __init__(self):
        self.goal = 0
        self.start()

    def start(self, goal = 0, dice1=randint(1, 6), dice2=randint(1, 6)):
        self.sum = dice1 + dice2
        if self.goal != 0:
            if self.sum == 7:
                print('You lose')
                return
            elif self.sum == self.goal:
                print('You Win')
                return
            else:
                print(f'The sum of dices are: {format(self.sum)}')
        else:
            if self.sum in [7, 11]:
                print('You Won')
                return
            elif self.sum in [2, 3, 12]:
                print('Casino Won')
                return
            elif self.sum in [4, 5, 6, 8, 9, 10]:
                self.goal = self.sum
                print('Your new number is: {}'.format(self.goal))
        self.start(self.goal, dice1=randint(1, 6), dice2=randint(1, 6))

Game()
