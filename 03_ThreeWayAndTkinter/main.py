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
    rowCount, columnCount = self.playgroundSize

    playgroundAreaSize = rowCount * columnCount
    playgroundIter = iter(sample(range(1, playgroundAreaSize), playgroundAreaSize - 1))

    for rowIndex in range(1, rowCount + 1):
      isLastRow = rowIndex == rowCount
      for columnIndex in range(columnCount - int(isLastRow)):
        i = next(playgroundIter)
        btnName = f'btn_Play{i}'
        def clickHandler(number=i): 
          self.play(number)

        setattr(self, btnName, tk.Button(self, text=i, command=clickHandler))
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


app = Application()
app.master.title('Boss Puzzle')
app.mainloop()
