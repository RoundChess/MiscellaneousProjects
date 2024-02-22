from tkinter import *

tk = Tk()
tk.title("Calculator")

canvas = Canvas(window, 300, 400)
c.pack()

class Shapes:
	def __init__(self, x, y, width, height, col):
	    self.x = x
	    self.y = y
	    self.width = width
	    self.height = height
		  self.col = col
		
	def drawCircle():
		canvas.create_oval(self.x, self.y, self.width, self.height, self.col)
s = Shape(200, 200, 25, 25, #fffff)
s.drawCircle()
