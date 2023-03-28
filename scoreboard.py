#import librarys
import tkinter as tk 

#function that gets the leaderboard from the text file sorts it and outputs it for the user to see
def leaderboard():
    global lb 
    counter = 0
    lb = tk.Tk()
    lb.title("Leaderboard")
    lb.geometry("750x1000")
    lb.config(bg = "#e02b4d")
    scorelist = []
    board = ""
    items = ""
    output = ""
    try:
        with open("leaderboard.txt") as f:
            for line in f:
                counter += 1
                name, score = line.split(', ')
                score = int(score)
                scorelist.append((name, score))
            scorelist.sort(key=lambda s: s[1])
            for item in scorelist:
                board,items = "",""
                for i in range(len(item)):
                    items += str(item[i])
                    if i == 0:
                        items += " = "
                board = str(counter)
                board +=" - "
                board += items
                board+="\n"
                counter-=1
                output = board + output
    except:
        pass
    lblTitle = tk.Label(lb,text = "Leaderboard",bg = "#e02b4d",fg = "white",font = ("Arial",30))
    lblTitle.place(x=150,y=50)
    lbl1 = tk.Label(lb,text = "", font = ("Arial",20),justify = "left",bg = "#e02b4d",fg = "white")
    lbl1.place(x=150,y=150)
    lbl1.config(text = output)
    home = tk.Button(lb,text = "MainMenu",command = mainMenu,font = ("Arial",15),bg = "#e02b4d",fg = "white")
    home.place(x=50,y=500)
    lb.mainloop()

#function to return to the main menu
def mainMenu():
    global lb 
    lb.destroy()
    import mainmenu
    mainmenu.Mmenu()

