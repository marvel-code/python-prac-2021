import tkinter as tk
import inspect


OVAL_DEFAULT_FILLCOLOR = 'green'
OVAL_DEFAULT_BORDERWIDTH = 2
OVAL_DEFAULT_OUTLINECOLOR = 'red'


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
      self.createdOval = (None, 0, 0) # id, x0, y0
      self.figureDragging = {
        'id': None,
        'startCoords': (0, 0, 0, 0),
        'startMousePosition': (0, 0),
      }
      #(None, 0, 0, 0, 0) # id, offsetX0, offsetY0, x0, y0

    def create_widgets(self):
      self.c = c = tk.Canvas(self, bg="#e5ffff", width="600", height="300")
      c.bind("<Button-1>", self.onCanvasClick)
      c.bind("<Motion>", self.onCanvasMousemove)
      c.bind("<ButtonRelease-1>", self.onCanvasMouseup)
      self.t = t = tk.Text(self)
      c.grid()
      t.grid()

    def onCanvasClick(self, e):
      dragFigure = self.c.find_overlapping(e.x, e.y, e.x, e.y)
      if len(dragFigure) > 0:
        id = dragFigure[-1]
        self.figureDragging['id'] = id
        self.figureDragging['startCoords'] = self.c.coords(id)
        self.figureDragging['startMousePosition'] = (e.x, e.y)
      else:
        id = self.c.create_oval(e.x, e.y, e.x, e.y,
            width=OVAL_DEFAULT_BORDERWIDTH,
            fill=OVAL_DEFAULT_FILLCOLOR,
            outline=OVAL_DEFAULT_OUTLINECOLOR,
          )
        self.createdOval = (id, e.x, e.y)
        self.figures.append(self.createdOval)

    def onCanvasMousemove(self, e):
      if self.createdOval[0]:
        id, x0, y0 = self.createdOval
        self.c.coords(id, x0, y0, e.x, e.y)
      elif self.figureDragging['id']:
        mx0, my0 = self.figureDragging['startMousePosition']
        dx, dy = (e.x - mx0, e.y - my0)
        id = self.figureDragging['id']
        x0, y0, x1, y1 = self.figureDragging['startCoords']
        self.c.coords(id, x0 + dx, y0 + dy, x1 + dx, y1 + dy)
        
    def onCanvasMouseup(self, e):
      self.createdOval = (None, 0, 0)
      self.figureDragging['id'] = None
      

app = App(title="Sample application")
app.mainloop()
