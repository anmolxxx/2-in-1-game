from tkinter import *
from tic_tac_toe import *
from dots import *

root = Tk()
root.geometry("1200x710")
root.title('2-in-1-game')

mylabel=Label(root, bg='yellow')
mylabel.place(x=0, y=0 , relheight=1, relwidth=1)

img = PhotoImage(file='game.png')
root.call('wm', 'iconphoto', root._w, img)

l2 = Label(root, text='Welcome \n To 2-in-1 Game',font=("ubuntu",60,"bold"), bg='yellow')
l2.pack()
l3 = Label(root, text='',font=("ubuntu",60,"bold"), bg='yellow')
l3.pack()

g1 = Button(root, text="Tic Tac Toe", font=("Comic Sans MS", 30, "bold"), height=2, width=12, bg="White", command=lambda: xx())
g1.pack(padx=10,pady=10)
g2 = Button(root, text="Connecting Dots", font=("Comic Sans MS", 30, "bold"), height=2, width=12, bg="White", command=lambda: xxx())
g2.pack(padx=10,pady=10)

root.mainloop()