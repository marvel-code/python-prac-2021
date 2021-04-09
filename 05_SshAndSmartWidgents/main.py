import tkinter as tk
import inspect

class Application(tk.Frame):
    '''Sample tkinter application class'''

    def __init__(self, master=None, title="<application>", **kwargs):
        '''Create root window with frame, tune weight and resize'''
        super().__init__(master, **kwargs)
        self.master.title(title)
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.grid(sticky="NEWS")
        self.create_widgets()
        for column in range(self.grid_size()[0]):
            self.columnconfigure(column, weight=1)
        for row in range(self.grid_size()[1]):
            self.rowconfigure(row, weight=1)

    def create_widgets(self):
        '''Create all the widgets'''

class App(Application):
    
    def __init__(self, title, **kwargs):
      super().__init__(None, title, **kwargs)
      self.figures = []
      self.createdOval = (None, 0, 0)

    def create_widgets(self):
      self.c = c = tk.Canvas(self, bg="#fefefe", width="600", height="300")
      c.bind("<Button-1>", self.onCanvasClick)
      c.bind("<Motion>", self.onCanvasMousemove)
      c.bind("<ButtonRelease-1>", self.onCanvasMouseup)
      self.t = t = tk.Text(self)
      c.grid()
      t.grid()

    def onCanvasClick(self, e):
      self.createdOval = (self.c.create_oval(e.x, e.y, e.x, e.y), e.x, e.y)
      self.figures.append(self.createdOval)

    def onCanvasMousemove(self, e):
      if self.createdOval[0]:
        id, x0, y0 = self.createdOval
        self.c.coords(id, x0, y0, e.x, e.y)
        
    def onCanvasMouseup(self, e):
      print(e)
      self.createdOval = (None, 0, 0)
      

app = App(title="Sample application")
app.mainloop()
