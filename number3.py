from tkinter import Tk, Canvas
frame=Tk()
canvas=Canvas(bg='black',height=250,width=300)
coord_rectangle=(100, 100, 200, 200)
coord_text = (150, 170)
coord_line = (100, 190, 200, 190)

canvas.create_rectangle(coord_rectangle,fill='white')
canvas.create_line(coord_line,fill='black')
canvas.create_text(coord_text,text='Henry Chan',fill='black')

canvas.pack()
frame.mainloop()
