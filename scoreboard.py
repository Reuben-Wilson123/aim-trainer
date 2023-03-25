import tkinter as tk 

def leaderboard():
    counter = 0
    #lb = tk.Tk()
    #lb.title("Leaderboard")
    #lb.geometry("1000x500")
    file = open("leaderboard.txt","r")
    scorelist = []
    for line in file:
        scorelist.append(line)
    file.close()
    for item in scorelist:
        try:
            item1, item2 = item.split(", ")
            item2 = item2.strip()

            scorelist[counter] = ((counter+1),"Name = ", item1, "Score = ",item2)
        except:
            pass
        counter += 1 
    print(scorelist)
    #lbl1 = tk.Label(lb,text = sb)
    #lb.mainloop()

leaderboard()