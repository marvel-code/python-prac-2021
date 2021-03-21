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
    self.lblInput = tk.Label(self, textvar=self.label_value, font=('Courier New', '24'), takefocus=1, borderwidth=1)
    self.cursor = tk.Frame(master=self.lblInput, background="black")
    self.btnQuit = tk.Button(self, text="Quit", command=self.quit)

    self.lblInput.bind('<Button-1>', self.on_lblInput_Click)
    self.lblInput.bind('<FocusIn>', self.on_lblInput_FocusIn)
    self.lblInput.bind('<FocusOut>', self.on_lblInput_FocusOut)
    self.lblInput.bind('<KeyPress>', self.on_lblInput_KeyPress)

    self.lblInput.grid(sticky="EW")
    self.btnQuit.grid()
    self.cursor.place(width=1, relheight=1)
    self.setCursorPosition(0)

  def on_lblInput_Click(self, e):
    """
    Handle click on label.
    """
    print(e)
    self.lblInput.focus_set()
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

  def on_lblInput_KeyPress(self, e):
    print(e)
    if e.keysym == 'Right':
      self.setCursorPosition(self.position + 1)
    elif e.keysym == 'Left':
      self.setCursorPosition(self.position - 1)
    elif e.keysym == 'Home':
      self.setCursorPosition(0)
    elif e.keysym == 'End':
      self.setCursorPosition(len(self.label_value.get()))
    elif e.keysym == 'BackSpace':
      p = self.position
      if p > 0:
        s = self.label_value.get()
        self.label_value.set(s[:p - 1] + s[p:])
        self.setCursorPosition(self.position - 1)
    elif e.char:
      p = self.position
      s = self.label_value.get()
      self.label_value.set(s[:p] + e.char + s[p:])
      self.setCursorPosition(self.position + 1)

  def setCursorPosition(self, position):
    """
    Sets cursor position in label.
    """
    print('set', position)

    position = min(position, len(self.label_value.get()))
    position = max(0, position)
    position = int(position)
    self.position = position

    self.cursor.place(width=1, relheight=1, x=position * self.FONT_WIDTH)


app = Application()
app.master.title('Public repository events')
app.mainloop()
