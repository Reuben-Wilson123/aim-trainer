import tkinter as tk 

def tutorial():
    global tutorialW
    tutorialW = tk.Tk()
    tutorialW.title("Tutorial")
    tutorialW.geometry("1000x500")
    text1 = tk.Label(tutorialW, text = "The aim of this program is to improve your aim in videogames. \n\nWhen you press play a new window will appear in this window there will be a target. \nYou need to click that target as fast as you can. \nThe faster you click it the more points you will get. \nDepending on the mode you select you will have a different ammount of time. \nThe standard mode you will have 20 secconds to get as many points as you can. \n\n\nOnce the time is over you will be asked whether you want to upload your score onto the leaderboard\n where you can see how you compare to the rest of the people who use this. ",font = ("Arial","15"))
    text1.place(x=50,y=50)
    menu = tk.Button(tutorialW, text = "MainMenu",command = back,font = ("Arial","20"))
    menu.place(x= 100, y = 450)
    tutorialW.mainloop()


def back():
    global tutorialW
    tutorialW.destroy()
    import mainmenu
    mainmenu.Mmenu()
#tutorial()