import random

import utility
class Snake:
    """
    Snake class, implement drawing the snake, moving the snake
    """
    def __init__(self, headx, heady, length, window, cell_size, color, size, food, start):
        """
        :param headx: position of the head
        :param heady:
        :param length: length of snake
        :param window:
        :param cell_size:
        :param color:
        :param size:
        :param food:
        :param start:
        :return:
        """
        self.start = start

        self.window = window
        self.cell_size = cell_size

        self.body = [0]*length
        self.bodyCo = [0]*length
        self.length = length
        self.color = color
        self.size = size
        self.food = food

        for j in range(length):
            self.bodyCo[j] = (headx, heady + j)
            self.body[j] = self.drawOne(self.bodyCo[j])

    def clear(self):

        for x in self.body:
            self.window.delete(x)

    def drawOne(self, p):
        """
        draw one cell
        :param p:
        :return:
        """

        return utility.drawOne(self.window, self.start, self.cell_size, self.color, p)



    def getNewRandomP(self):
        """
        :return: new random position for food
        """
        while True:
            p = (random.randint(0, self.size-1), random.randint(0, self.size-1))

            if p not in self.bodyCo:
                return p

    def move(self,dx, dy):
        """
        move the snake
        :param dx:
        :param dy:
        :return:
        """
        np = (self.bodyCo[0][0]+dx, self.bodyCo[0][1]+dy)

        if np[0] < 0 or np[1] < 0 or np[0] >= self.size or np[1] >= self.size:

            return 'lose'

        if np in self.bodyCo:
            return 'lose'

        nh = self.drawOne(np)
        self.bodyCo = [np] + self.bodyCo
        self.body = [nh] + self.body

        if np == self.food.p:
            self.food.setP(self.getNewRandomP())
            return 'food'
        else:
            # self.body[-1].undraw()
            self.window.delete(self.body[-1])
            del self.body[-1]
            del self.bodyCo[-1]

    def moveDi(self, di):
        """
        move the snake
        :param di: the direction
        :return:
        """
        if di == 'up':
            dx = 0
            dy = -1

        elif di == 'down':
            dx = 0
            dy = 1

        elif di == 'left':
            dx = -1
            dy = 0

        elif di == 'right':
            dx = 1
            dy = 0

        else:

            return

        return self.move(dx, dy)


