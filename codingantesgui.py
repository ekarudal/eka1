from tkinter import *
root = Tk()
frame = Frame(root)
frame.pack()
bottomframe = Frame(root)
bottomframe.pack(side = BOTTOM)
#Green Color for Hadir
greenbutton = Button(frame, text ='Lampu Merah', fg = 'red')
greenbutton.pack( side = LEFT) 
#Red Color for Tidak Hadir
redbutton = Button(frame, text = 'Lampu Kuning', fg = 'yellow')
redbutton.pack( side = LEFT)
#Blue Color for Telat
bluebutton = Button(frame, text = 'Lampu Hijau', fg = 'green')
bluebutton.pack( side = LEFT)
root.mainloop()
