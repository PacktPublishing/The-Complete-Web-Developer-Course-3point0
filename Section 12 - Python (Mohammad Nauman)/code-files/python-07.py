#! /usr/bin/python

print('Content-type: text/html')
print('')


class Game:
    def __init__(self):
        self.nums = []

    def startGame():
        print("Game is starting now")

    def addNumber(self, num):
        if self.nums is None:
            self.nums = [num]
        else:
            self.nums.append(num)

    def printNumbers(self):
        print("List of numbers: ", self.nums)


g = Game()
g.printNumbers()
g.addNumber(5)
g.printNumbers()
