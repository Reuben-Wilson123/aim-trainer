#import librarys
import tkinter as tk
import time as dt
import random as ran

score = 0
counter = 0

TIMER = 10
FONT = "Arial",20
#generate random x and y values 
def ranx():
    return ran.randint(100,1780)

def rany():
    return ran.randint(100,940)




#function for when the button is clicked 
def click():
    global old_time, new_time, target, score, lblscore, counter
    if dt.time() - start_time <= TIMER:
        counter += 1
        old_time = new_time
        new_time = dt.time()
        delta = new_time-old_time
        score += round((100/delta))
        outputScore = "Score = "+ str(score)
        lblscore.config(text = outputScore)
        x= ranx()
        y = rany()
        target.place(x=x,y=y)
    else:
        end()


def start():
    global new_time ,target,lblscore, start_time
    game = tk.Tk()
    game.geometry("1920x1080")
    game.config(bg = "#cc0203")
    img1 = tk.PhotoImage(file = "aimtrainertarget.png")
    target = tk.Button(game,image = img1,command = click)
    target.place(x=100,y=100)
    lblscore = tk.Label(game,text = "Score = 0",font = FONT,bg = "#cc0203",fg = "White")
    lblscore.place(x=0,y=10)
    new_time = dt.time()
    start_time = dt.time()
    game.mainloop()



def end():
    endscreen = tk.Tk()
    endscore = tk.Label(endscreen,text = "Your final score is "+str(score),font = ("Arial",20))
    endscore.place(x=50,y=20)
    lbl1 = tk.Label(endscreen,text = "Do you want to upload to leaderboard?",font = ("Arial",15))
    btnYes = tk.Button(text = "Yes",font = ("Arial"))
    endscreen.mainloop()




start()