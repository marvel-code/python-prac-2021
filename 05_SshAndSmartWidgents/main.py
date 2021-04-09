import tkinter as tk
import inspect
import re


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
      self.createdOval = {
        'id': None,
        'coords': (0, 0, 0, 0)
      }
      self.figureDragging = {
        'id': None,
        'startCoords': (0, 0, 0, 0),
        'startMousePosition': (0, 0),
      }

    def create_widgets(self):
      self.c = c = tk.Canvas(self, bg="#e5ffff", width="600", height="300")
      c.bind("<Button-1>", self.onCanvasMousedown)
      c.bind("<Motion>", self.onCanvasMousemove)
      c.bind("<ButtonRelease-1>", self.onCanvasMouseup)
      self.t = t = tk.Text(self)
      t.bind("<KeyRelease>", self.onTextKeyup)

      c.grid()
      t.grid()

    # Figure serialization interface

    def synTextWithCanvas(self):
      self.t.delete('1.0', 'end')
      for id in self.c.find_all():
        figureType = self.c.type(id)
        coords = self.c.coords(id)
        options = self.c.itemconfigure(id)

        width, fill, outline = options['width'][-1], options['fill'][-1], options['outline'][-1]
        stringOptions = f'{width} {fill} {outline}'
        
        figureString = f'{figureType} {coords} {stringOptions}'
        self.t.insert("end", figureString + '\n')

    def synCanvasWithText(self):
      for id in self.c.find_all():
        self.c.delete(id)

      text = self.t.get('1.0', 'end')
      for line in text.split('\n'):
        try:
          figureType, coords, width, fill, outline = re.match(r"(.+) \[(.+)\] (.+) (.+) (.+)", line).groups()
          coords = tuple(map(float, coords.split(',')))
          width = float(width)

          getattr(self.c, f'create_{figureType}').__call__(*coords, width=width, fill=fill, outline=outline)
        except Exception as ex:
          pass

    # Figure dragging

    def initFigureDragging(self, id, startMousePosition):
        self.figureDragging['id'] = id
        self.figureDragging['startCoords'] = self.c.coords(id)
        self.figureDragging['startMousePosition'] = startMousePosition

    def dragFigure(self, id, dx, dy):
        x0, y0, x1, y1 = self.figureDragging['startCoords']
        self.c.coords(id, x0 + dx, y0 + dy, x1 + dx, y1 + dy)

    # Oval creation

    def createOval(self, offset):
      id = self.c.create_oval(*offset, *offset,
          width=OVAL_DEFAULT_BORDERWIDTH,
          fill=OVAL_DEFAULT_FILLCOLOR,
          outline=OVAL_DEFAULT_OUTLINECOLOR,
        )
      self.createdOval['id'] = id
      self.createdOval['coords'] = (*offset, 0, 0)
      self.figures.append(self.createdOval)

    # Events

    def onCanvasMousedown(self, e):
      dragFigure = self.c.find_overlapping(e.x, e.y, e.x, e.y)
      if len(dragFigure) > 0:
        id = dragFigure[-1]
        self.initFigureDragging(id, (e.x, e.y))
      else:
        self.createOval((e.x, e.y))

    def onCanvasMousemove(self, e):
      if self.createdOval['id']:
        id = self.createdOval['id']
        x0, y0, _, _ = self.createdOval['coords']
        coords = (x0, y0, e.x, e.y)
        self.createdOval['coords'] = coords
        self.c.coords(id, *coords)
      elif self.figureDragging['id']:
        mx0, my0 = self.figureDragging['startMousePosition']
        dx, dy = (e.x - mx0, e.y - my0)
        id = self.figureDragging['id']
        self.dragFigure(id, dx, dy)
        
    def onCanvasMouseup(self, e):
      self.synTextWithCanvas()

      self.createdOval['id'] = None
      self.figureDragging['id'] = None
    
    def onTextKeyup(self, e):
      self.synCanvasWithText()

app = App(title="Sample application")
app.mainloop()
