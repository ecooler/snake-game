
import utility
class Food:
    """
    Food class, food drawing
    """
    def __init__(self, p, window, cell_size, start):
        self.p = p
        self.start = start
        self.window = window
        self.color = 'yellow'
        self.cell_size = cell_size
        self.img = self.drawOne(self.p)

    def drawOne(self, p):
        """
        draw one cell
        :param p:
        :return:
        """

        return utility.drawOne(self.window, self.start, self.cell_size, self.color, p)


    def clear(self):
        """
        clear the food
        :return:
        """
        # self.img.undraw()
        self.window.delete(self.img)


    def setP(self, np):
        """
        set a new position
        :param np:
        :return:
        """
        self.clear()

        self.p = np
        self.img = self.drawOne(self.p)
