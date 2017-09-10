from snake import *
from food import *
from tkinter import *
import tkinter.messagebox
import math

import utility
class SnakeGame:
    """
     Snake Game class, implement the main game logic
    """
    def __init__(self, snakeColor):
        """
        draw the UI, run the game
        :param snakeColor:
        :return:
        """
        ps = 500
        self.size = 50

        master = Tk()
        master.wm_title( "Snake Game")
        self.master = master
        self.window = Canvas(master, width=ps, height=ps)
        self.window.pack()

        self.cell_size = 10
        self.start = 100
        self.size = 30

        self.snakeColor = snakeColor

        self.drawWall()

        self.master.focus_set()
        self.master.bind("<Key>", self.keyListener)

        self.master.bind("<Up>", self.upKey)
        self.master.bind("<Left>", self.leftKey)
        self.master.bind("<Down>", self.downKey)
        self.master.bind("<Right>", self.rightKey)

        self.food = Food((5,5), self.window, self.cell_size, self.start)

        self.snake = Snake(10,10,4,self.window,self.cell_size, snakeColor, self.size, self.food,self.start)

        self.score = 0
        self.di = 'up'
        self.paused = False

        self.interval = 1000
        self.master.after(self.interval,self.up_dating_move_timer)
        mainloop()

    def upKey(self,event):

        self.di = 'up'

    def leftKey(self,event):

        self.di = 'left'

    def downKey(self,event):

        self.di = 'down'

    def rightKey(self,event):

        self.di = 'right'


    def resetGame(self):
        """
        reset the game board, called when user wants to play again
        :return:
        """
        self.score = 0
        self.snake.clear()
        self.food.clear()
        self.food = Food((5,5), self.window, self.cell_size, self.start)
        self.snake = Snake(10,10,4,self.window,self.cell_size, self.snakeColor, self.size, self.food,self.start)

        self.di = 'up'
        self.paused = False

        self.interval = 1000

    def keyListener(self, event):
        """
        respond to user's key press:  direction arrow key and space key
        :param event:
        :return:
        """

        if event.char == '\uf700' or event.char == 'w':
            self.di = 'up'
        elif event.char == '\uf701' or event.char == 's':
            self.di = 'down'
        elif event.char == '\uf702' or event.char == 'a':
            self.di = 'left'
        elif event.char == '\uf703' or event.char == 'd':
            self.di = 'right'
        elif event.char == ' ':
            """ press space bar, pause the game """
            self.paused = not self.paused

    def drawWall(self):
        """
        draw the wall
        :return:
        """
        for j in [-1, self.size]:
            for i in range(-1, self.size+1):
                utility.drawOne(self.window, self.start, self.cell_size, 'black', [i,j])

        for i in [-1, self.size]:
            for j in range(-1, self.size+1):
                utility.drawOne(self.window, self.start, self.cell_size, 'black', [i,j])

    def up_dating_move_timer(self):
        """
        move the snake
        :return:
        """
        if not self.paused:

            ans = self.snake.moveDi(self.di)
            if ans == 'food':
                self.interval = int(math.ceil(self.interval * 0.7))
                self.score += 1

            elif ans == 'lose':
                replay = tkinter.messagebox.askquestion('Game Over','You scored %d points, do you want to play again?' % self.score)
                if replay == 'no':
                    exit(0)
                else:
                    self.resetGame()

        self.master.after(self.interval,self.up_dating_move_timer)


if __name__ == '__main__':
    SnakeGame('green')



