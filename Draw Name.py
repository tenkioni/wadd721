''' Henry Chan Given the following program to draw a simple logo using Canvas widget from tkinter module'''

from tkinter import Tk, Canvas
frame=Tk()
canvas=Canvas(bg='white',height=250,width=300)

canvas.create_rectangle(50, 60, 220, 160, fill='Darkgreen',
                        outline='darkkhaki')

canvas.create_text(100, 100, text='Henry Chan',
                   anchor='nw',font='italic',fill='white')

canvas.create_line(100, 115, 178, 115)
canvas.pack()
frame.mainloop()
