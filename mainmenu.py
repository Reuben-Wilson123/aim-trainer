#import librarys
import tkinter as tk 
import sys

#create functions
def change(scene):
    global menu
    menu.withdraw()
    if scene == "play":
        import trainer
        trainer.start()
    elif scene == "tutorial":
        import tutorial
        tutorial.tutorial()
    elif scene == "leaderboard":
        import scoreboard
        scoreboard.leaderboard()
    else:
        sys.exit()


try:
    menu = tk.Tk()

    menu.title("Main Menu")
    menu.geometry("500x500")

    menu.config(bg = "#e02b4d")

    title = tk.Label(menu, text = "Aim Trainer",font = ("Arial",30,"bold","underline"),bg = "#e02b4d",fg = "white")
    title.place(x=175,y=50)

    btnplay = tk.Button(menu,text = "Play",font  = ("Arial",20),bg = "#e02b4d",fg = "White",command = lambda: change("play"))
    btnplay.place(x=50,y=150)

    btntutorial = tk.Button(menu,text = "Tutorial",font = ("Arial",20),bg = "#e02b4d",fg = "White",command = lambda: change("tutorial"))
    btntutorial.place(x=50,y=250)

    btnscore = tk.Button(menu, text = "Leaderboard",font = ("Arial",20), bg = "#e02b4d", fg = "White",command = lambda: change("leaderboard"))
    btnscore.place(x=50,y=350)

    btnQuit = tk.Button(menu, text = "Quit",font = ("Arial",20),bg = "#e02b4d",fg = "White", command = lambda: change("END"))
    btnQuit.place(x=50,y=450)

    image1 = tk.PhotoImage(file = "aimtrainerimg1.png")
    lbl1 = tk.Label(menu, image = image1)
    lbl1.place(x=25,y=15)
    menu.mainloop()
except:
    pass

def Mmenu():
    global menu

    try:
        menu.deiconify()
        #menu.mainloop()
    except:
        pass
