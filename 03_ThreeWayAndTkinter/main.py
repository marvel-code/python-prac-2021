import tkinter as tk
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
    pass

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
