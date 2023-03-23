#import librarys
import tkinter as tk 

#import modules
#import trainer



#create functions
def play():
    global menu
    menu.withdraw()
    import trainer
    trainer.start()

try:
    menu = tk.Tk()

    menu.title("Main Menu")
    menu.geometry("500x500")

    menu.config(bg = "#e02b4d")

    title = tk.Label(menu, text = "Aim Trainer",font = ("Arial",30,"bold","underline"),bg = "#e02b4d",fg = "white")
    title.place(x=175,y=100)

    btnplay = tk.Button(menu,text = "Play",font  = ("Arial",20),bg = "#e02b4d",fg = "White",command = play)
    btnplay.place(x=50,y=200)
    btntutorial = tk.Button(menu,text = "Tutorial",font = ("Arial",20),bg = "#e02b4d",fg = "White")
    btntutorial.place(x=50,y=300)

    btnscore = tk.Button(menu, text = "Leaderboard",font = ("Arial",20), bg = "#e02b4d", fg = "White")
    btnscore.place(x=50,y=400)

    image1 = tk.PhotoImage(file = "aimtrainerimg1.png")
    lbl1 = tk.Label(menu, image = image1)
    lbl1.place(x=25,y=50)
    menu.mainloop()
except:
    pass

def Mmenu():
    global menu

    try:
        menu.deiconify()
        menu.mainloop()
    except:
        pass
