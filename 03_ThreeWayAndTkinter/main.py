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
    self.initUI()

  def initSettings(self):
    """
    Init app settings.
    """
    self.playgroundSize = (4, 4)

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
    rowWidth, columnWidth = self.playgroundSize
    playgroundIter = self.makeNewPlaygroundSequence(rowWidth, columnWidth)

    for rowIndex in range(1, rowWidth + 1):
      isLastRow = rowIndex == rowWidth
      for columnIndex in range(columnWidth - int(isLastRow)):
        i = next(playgroundIter)
        btnName = f'btn_Play{i}'
        def playHandler(number=i): 
          self.play(number)

        setattr(self, btnName, tk.Button(self, text=i, command=playHandler))
        getattr(self, btnName).grid(row=rowIndex, column=columnIndex)


  def startNewGame(self):
    """
    Start new game.
    """
    pass

  def play(self, number):
    """
    Play `number`.
    """
    print(number)
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
