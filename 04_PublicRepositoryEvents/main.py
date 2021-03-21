import tkinter as tk

class Application(tk.Frame):

  FONT_WIDTH = 19

  def __init__(self, master=None):
    super().__init__(master)
    self.grid()
    self.initLblInputState()
    self.initUI()

  def initLblInputState(self):
    """
    Initiates lblInput state.
    """
    self.label_value = tk.StringVar()
    self.label_value.set('My love text...')

  def initUI(self):
    """
    Initiates user interface.
    """
    self.lblInput = tk.Label(self, textvar=self.label_value, font=('Courier New', '24'), takefocus=1, anchor='w')
    self.cursor = tk.Frame(master=self.lblInput, width=5, borderwidth=2, background="black")
    self.btnQuit = tk.Button(self, text="Quit", command=self.quit)

    self.lblInput.bind('<Button>', self.on_lblInput_Click)
    self.lblInput.bind('<FocusIn>', self.on_lblInput_FocusIn)
    self.lblInput.bind('<FocusOut>', self.on_lblInput_FocusOut)

    self.lblInput.grid(sticky="EW")
    self.btnQuit.grid()
    self.cursor.place(width=1, relheight=1)

  def on_lblInput_Click(self, e):
    """
    Handle click on label.
    """
    if e.num == 1:
      print(e)
      self.setCursorPosition((e.x + self.FONT_WIDTH / 2) // self.FONT_WIDTH)

  def on_lblInput_FocusIn(self, e):
    """
    Focus in label.
    """
    print(e)

  def on_lblInput_FocusOut(self, e):
    """
    Focus out label.
    """
    print(e)

  def setCursorPosition(self, position):
    """
    Sets cursor position in label.
    """
    print('set', position)
    self.cursor.place(width=1, relheight=1, x=position * self.FONT_WIDTH)


app = Application()
app.master.title('Public repository events')
app.mainloop()
