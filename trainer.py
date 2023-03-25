#import librarys
import tkinter as tk
import time as dt
import random as ran



#create variables
score = 0
counter = 0

#create constants
TIMER = 5
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

#function to start the game
def start():
    global new_time ,target,lblscore, start_time, game
    game = tk.Toplevel()
    game.geometry("1920x1080")
    game.config(bg = "#cc0203")
    img1 = tk.PhotoImage(file = "aimtrainertarget.png")
    target = tk.Button(master = game,image = img1,command = click)
    target.place(x=100,y=100)
    lblscore = tk.Label(game,text = "Score = 0",font = FONT,bg = "#cc0203",fg = "White")
    lblscore.place(x=0,y=10)
    new_time = dt.time()
    start_time = dt.time()
    game.mainloop()


#function to bring up the end screen
def end():
    global lbl1,btnYes,btnNo,endscreen
    endscreen = tk.Tk()
    endscreen.title("End Screen")
    endscreen.geometry("500x500")
    endscore = tk.Label(endscreen,text = "Your final score is "+str(score),font = FONT)
    endscore.place(x=50,y=50)
    lbl1 = tk.Label(endscreen,text = "Do you want to upload to leaderboard?",font = FONT)
    lbl1.place(x=25,y=100)
    btnYes = tk.Button(endscreen, text = "Yes",font = FONT,command = leaderboardYes)
    btnYes.place(x=25,y=150)
    btnNo = tk.Button(endscreen,text = "No",font = FONT,command = leaderboardNo)
    btnNo.place(x=125,y=150)
    endscreen.mainloop()

def leaderboardYes():
    global lbl1, btnYes, btnNo, endscreen, back, nameEntry, btnSub, lbl2
    lbl1.place_forget()
    btnYes.place_forget()
    btnNo.place_forget()
    back = tk.Button(endscreen, text = "Changed your mind?",command = lambda:replace("Yes"),font = FONT)
    back.place(x=50,y=200)
    nameEntry = tk.Entry(endscreen,font = FONT)
    nameEntry.place(x = 50, y = 50)
    btnSub = tk.Button(endscreen, text = "Submit", font = FONT, command = submit)
    btnSub.place(x= 50, y =125)
    lbl2 = tk.Label(endscreen, text = "Enter Name", font = FONT)
    lbl2.place(x = 50, y=10)


def leaderboardNo():
    global lbl1, btnYes, btnNo,back,home
    lbl1.place_forget()
    btnYes.place_forget()
    btnNo.place_forget()
    back = tk.Button(endscreen, text = "Changed your mind?",command = lambda:replace("No"),font = FONT)
    back.place(x=50,y=200)
    home = tk.Button(endscreen, text = "MainMenu",command = returnHome,font = FONT)
    home.place(x=50,y=125)


def replace(choice):
    global lbl1, btnYes, btnNo, back,home, nameEntry, btnSub, lbl2
    lbl1.place(x=25,y=100)
    btnYes.place(x=25,y=150)
    btnNo.place(x=125,y=150)
    if choice == "Yes":
        back.place_forget()
        nameEntry.place_forget()
        btnSub.place_forget()
        lbl2.place_forget()
    else:
        back.place_forget()
        home.place_forget()

def returnHome():
    global game,endscreen
    endscreen.destroy()
    game.destroy()
    import mainmenu
    mainmenu.Mmenu()

def submit():
    global name, score
    file = open("leaderboard.txt","a")
    name = nameEntry.get()
    file.write(name)
    file.write(", ")
    file.write(str(score))
    file.write("\n")
    file.close()
    returnHome()
#start()