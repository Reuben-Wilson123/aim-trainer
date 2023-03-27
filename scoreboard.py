import tkinter as tk 

def leaderboard():
    counter = 1
    lb = tk.Tk()
    lb.title("Leaderboard")
    lb.geometry("1000x500")
    file = open("leaderboard.txt","r")
    scorelist = []
    board = ""
    items = ""
    output = ""
    try:
        with open("leaderboard.txt") as f:
            for line in f:
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
                counter+=1
                output +=board
    except:
        pass
    lbl1 = tk.Label(lb,text = output, font = ("Arial",20),justify = "left")
    lbl1.place(x=100,y=100)
    lb.mainloop()

leaderboard()