import tkinter as tk
from tkinter import messagebox
from random import sample


class Application(tk.Frame):

  def __init__(self, master=None):
    """
    Init app.
    """
    super().__init__(master)
    self.grid()
    self.initSettings()
    self.initPlayState()
    self.initUI()

  def initSettings(self):
    """
    Init app settings.
    """
    self.playgroundSize = (4, 4)

  def initPlayState(self):
    """
    Init play state
    """
    width, height = self.playgroundSize
    self.emptyCell = (width - 1, height - 1)

  def initUI(self):
    """
    Init user interface.
    """
    self.initMenu()
    self.initPlayground()

  def initMenu(self):
    """
    Init user menu.
    """
    self.btn_New = tk.Button(self, text='New', command=self.startNewGame)
    self.btn_Exit = tk.Button(self, text='Exit', command=self.quit)

    columnSpan = self.playgroundSize[1] // 2
    self.btn_New.grid(row=0, column=0, columnspan=columnSpan)
    self.btn_Exit.grid(row=0, column=columnSpan, columnspan=columnSpan)

  def initPlayground(self):
    """
    Init playground.
    """
    playgroundAreaSize = self.playgroundSize[0] * self.playgroundSize[1]
    for i in range(1, playgroundAreaSize):
      btnName = f'btn_Play{i}'
      def playHandler(number=i): 
        self.play(number)

      setattr(self, btnName, tk.Button(self, text=i, command=playHandler))

    self.startNewGame()

  def startNewGame(self):
    """
    Start new game.
    """
    print('New game')

    self.emptyCell = (self.playgroundSize[0] - 1, self.playgroundSize[1] - 1)
    playgroundIter = self.makeNewPlaygroundSequence(*self.playgroundSize)
    j = -1
    missCount = 0
    for i in playgroundIter:
      j += 1
      rowIndex = 1 + j // self.playgroundSize[0]
      columnIndex = j % self.playgroundSize[1]
      btn = getattr(self, f'btn_Play{i}')
      btn.grid(row=rowIndex, column=columnIndex, sticky=tk.N+tk.E+tk.S+tk.W)
      
      okRowIndex = 1 + i // self.playgroundSize[0]
      okColumnIndex = i % self.playgroundSize[1]
      missCount += int(rowIndex != okRowIndex or columnIndex != okColumnIndex)

    if missCount == 0:
      self.startNewGame()
    
  def play(self, number):
    """
    Play `number`.
    """
    print(f'Play {number}')

    btn = getattr(self, f'btn_Play{number}')
    btnGridInfo = btn.grid_info()
    row, column = btnGridInfo['row'], btnGridInfo['column']

    if self.isNearEmptyCell(row, column):
      btn.grid(row=1+self.emptyCell[0], column=self.emptyCell[1])
      self.emptyCell = (row - 1, column)

    self.tryToWin()

  def tryToWin(self):
    win = True

    for i in range(self.playgroundSize[0] * self.playgroundSize[1] - 1):
        irow = 1 + i // self.playgroundSize[0]
        icolumn = i % self.playgroundSize[1]

        btnGridInfo = getattr(self, f'btn_Play{1 + i}').grid_info()
        row, column = btnGridInfo['row'], btnGridInfo['column']

        if row != irow or column != icolumn:
          win = False

    if win:
      messagebox.showinfo(message='You win!')


  def isNearEmptyCell(self, row, column):
    """
    Is button near emptiness.
    """
    return abs(self.emptyCell[0] + 1 - row) + abs(self.emptyCell[1] - column) <= 1

  def makeNewPlaygroundSequence(self, width, height):
    """
    Make new play sequence for `width*height` playground.
    """
    playgroundAreaSize = width * height
    playgroundIter = iter(sample(range(1, playgroundAreaSize), playgroundAreaSize - 1))

    return playgroundIter


app = Application()
app.master.title('Boss Puzzle')
app.mainloop()
