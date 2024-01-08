#MP2_OlivarezKarlUlrich

from tkinter import *
from tkinter import messagebox
import random

#=====Level number and coin count=====#
lvl = 1
coins = 100

#=====list for button choices and label outputs=====#
btnList = list()
lblList = list()

#=====Open picList file and append image names to list=====#
f = open("picList.txt")
x = f.readlines()

images = list()
for p in x:
    pic = p.strip().split(';')
    images.append(pic[1])

picNum = 0
answer = 'war' #Correct answer
hintLetters = ['W', 'A', 'R'] #List for hint

#=====Class to go to next level=====#
class changeLevel():
    #=====Function to go to next level=====#
    def change(self):
        global picNum
        global answer
    
        picNum+=1
        if picNum == 50:
            picNum = 0
        img.config(file="Images/"+images[picNum]+".png")
        answer = str(images[picNum])

        del hintLetters[0:]
        for letter in answer:
            hintLetters.append(letter.upper())

        for a in lblList:
            a['text'] = ''

        for b in btnList:
            b['image'] = imgButton
            b['state'] = ACTIVE

        btn1['command'] = lambda:[ClickLetters(0),Check()]
        btn2['command'] = lambda:[ClickLetters(1),Check()]
        btn3['command'] = lambda:[ClickLetters(2),Check()]
        btn4['command'] = lambda:[ClickLetters(3),Check()]
        btn5['command'] = lambda:[ClickLetters(4),Check()]
        btn6['command'] = lambda:[ClickLetters(5),Check()]
        btn7['command'] = lambda:[ClickLetters(6),Check()]
        btn8['command'] = lambda:[ClickLetters(7),Check()]
        btn9['command'] = lambda:[ClickLetters(8),Check()]
        btn10['command'] = lambda:[ClickLetters(9),Check()]
        btn11['command'] = lambda:[ClickLetters(10),Check()]
        btn12['command'] = lambda:[ClickLetters(11),Check()]

        self.changeCoinLvl()
        self.Record()
        LblCount()
        buttonLetters()

    #=====Function to change level and coins=====#
    def changeCoinLvl(self):
        global lvl
        global coins
        
        lvl += 1
        lblLvl.config(text='Level:'+str(lvl))
        coins += 10
        lblCoin.config(text=str(coins))

    def Record(self):
        try:
            record = open("Player_Record.txt","a+")
            if lvl == 1:
                record.write("\n")
                
            records = "Level: "+str(lvl)+";"+"Coins: "+str(coins)+";"+"Picture: "+answer+"\n"
            record.write(records)
            record.close()
        except:
            record = open("Player_Record.txt","w")

#======Child class of changeLevel=====#
class PassLevel(changeLevel):
    #=====Overwirtten function=====#
    def changeCoinLvl(self):
        global lvl
        global coins
        
        lvl += 1
        lblLvl.config(text='Level:'+str(lvl))
        coins -= 10
        lblCoin.config(text=str(coins))
    
#=====Function to check how many labels should appear=====#
def LblCount():
    global answer
    
    ans = answer.strip()
    if len(ans) == 3:
        imgGuess.config(file="Images/3Letters.png")
        lblGuess4.place_forget()
        lblGuess5.place_forget()
        lblGuess6.place_forget()
        lblGuess7.place_forget()
        lblGuess8.place_forget()
        
        if len(lblList) > 3:
            del lblList[4:]
        
        lblGuess1.place(x=149,y=383)
        lblGuess2.place(x=179,y=383)
        lblGuess3.place(x=209,y=383)
        frame.place(x=135,y=368)
            
    elif len(ans) == 4:
        imgGuess.config(file="Images/4Letters.png")
        lblGuess5.place_forget()
        lblGuess6.place_forget()
        lblGuess7.place_forget()
        lblGuess8.place_forget()
        
        if len(lblList) == 3:
            lblList.append(lblGuess4)
        else:
            del lblList[4:]

        lblGuess1.place(x=134,y=383)
        lblGuess2.place(x=164,y=383)
        lblGuess3.place(x=194,y=383)
        lblGuess4.place(x=223,y=383)
        frame.place(x=120,y=368)

    elif len(ans) == 5:
        imgGuess.config(file="Images/5Letters.png")
        lblGuess6.place_forget()
        lblGuess7.place_forget()
        lblGuess8.place_forget()
        if len(lblList) == 3:
            lblList.append(lblGuess4)
            lblList.append(lblGuess5)
        elif len(lblList) == 4:
            lblList.append(lblGuess5)
        else:
            del lblList[5:]

        lblGuess1.place(x=119,y=383)
        lblGuess2.place(x=149,y=383)
        lblGuess3.place(x=179,y=383)
        lblGuess4.place(x=209,y=383)
        lblGuess5.place(x=238,y=383)
        frame.place(x=105,y=368)

    elif len(ans) == 6:
        imgGuess.config(file="Images/6Letters.png")
        lblGuess7.place_forget()
        lblGuess8.place_forget()
        if len(lblList) == 3:
            lblList.append(lblGuess4)
            lblList.append(lblGuess5)
            lblList.append(lblGuess6)
        elif len(lblList) == 4:
            lblList.append(lblGuess5)
            lblList.append(lblGuess6)
        elif len(lblList) == 5:
            lblList.append(lblGuess6)
        else:
            del lblList[6:]

        lblGuess1.place(x=104,y=383)
        lblGuess2.place(x=134,y=383)
        lblGuess3.place(x=164,y=383)
        lblGuess4.place(x=194,y=383)
        lblGuess5.place(x=223,y=383)
        lblGuess6.place(x=253,y=383)
        frame.place(x=90,y=368)

    elif len(ans) == 7:
        imgGuess.config(file="Images/7Letters.png")
        lblGuess8.place_forget()
        if len(lblList) == 3:
            lblList.append(lblGuess4)
            lblList.append(lblGuess5)
            lblList.append(lblGuess6)
            lblList.append(lblGuess7)
        elif len(lblList) == 4:
            lblList.append(lblGuess5)
            lblList.append(lblGuess6)
            lblList.append(lblGuess7)
        elif len(lblList) == 5:
            lblList.append(lblGuess6)
            lblList.append(lblGuess7)
        elif len(lblList) == 6:
            lblList.append(lblGuess7)
        else:
            del lblList[7:]

        lblGuess1.place(x=90,y=381)
        lblGuess2.place(x=121,y=381)
        lblGuess3.place(x=150,y=381)
        lblGuess4.place(x=180,y=381)
        lblGuess5.place(x=210,y=381)
        lblGuess6.place(x=240,y=381)
        lblGuess7.place(x=270,y=381)
        frame.place(x=70,y=368)

    else:
        imgGuess.config(file="Images/8Letters.png")
        if len(lblList) == 3:
            lblList.append(lblGuess4)
            lblList.append(lblGuess5)
            lblList.append(lblGuess6)
            lblList.append(lblGuess7)
            lblList.append(lblGuess8)
        elif len(lblList) == 4:
            lblList.append(lblGuess5)
            lblList.append(lblGuess6)
            lblList.append(lblGuess7)
            lblList.append(lblGuess8)
        elif len(lblList) == 5:
            lblList.append(lblGuess6)
            lblList.append(lblGuess7)
            lblList.append(lblGuess8)
        elif len(lblList) == 6:
            lblList.append(lblGuess7)
            lblList.append(lblGuess8)
        elif len(lblList) == 7:
            lblList.append(lblGuess8)

        lblGuess1.place(x=73,y=383)
        lblGuess2.place(x=103,y=383)
        lblGuess3.place(x=133,y=383)
        lblGuess4.place(x=163,y=383)
        lblGuess5.place(x=193,y=383)
        lblGuess6.place(x=223,y=383)
        lblGuess7.place(x=253,y=383)
        lblGuess8.place(x=283,y=383)
        frame.place(x=58,y=368)
   
#=====Function to randomize letters in buttons=====#
def buttonLetters():
    global answer
    
    btn_Letters = list()
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    ctr = 12-len(answer)
    
    for i in answer:
        btn_Letters.append(i.upper())

    for z in range(ctr):
        randNum = random.randint(0,25)
        btn_Letters.append(letters[randNum])

    random.shuffle(btn_Letters)

    for x in range(12):
        btnList[x]['text'] = btn_Letters[x]

#=====Function to make the letters in button appear in label when clicked=====#
def ClickLetters(args):
    try:
        for i in range(12):
            if args == i:
                for x in range(8):
                    if lblList[x]['text'] == '':
                        lblList[x]['text'] = btnList[i]['text']
                        btnList[i]['command'] = lambda:RemoveLetters(args)
                        btnList[i]['image'] = imgUsed
                        break
                break
    except:
        messagebox.showinfo("Error","Text field full, please remove a letter first.")

#=====Function to clear the letter in label when button is clicked again=====#
def RemoveLetters(args):
    for i in range(8):
        if btnList[args]['text'] == lblList[i]['text']:
            lblList[i]['text'] = ''
            btnList[args]['command'] = lambda:[ClickLetters(args),Check()]
            btnList[args]['image'] = imgButton
            break

#=====Function check if the word formed in the labels are correct=====#
def Check():
    ans = ''
    level = changeLevel()
    for i in lblList:
        ans += i['text']
    if ans.lower() == answer:
        level.change()

#=====Function for hint=====#
def Hint():
    global hintLetters
    global coins

    if messagebox.askyesno('Hint','Spend 2 coins for hint?') == True:
        if coins >= 2:
            while True:
                randLetter = random.randint(0,len(hintLetters)-1)
                if lblList[randLetter]['text'] == '':
                    lblList[randLetter]['text'] = hintLetters[randLetter]
                    break
                else:
                    continue

            for i in range(12):
                if btnList[i]['text'] == hintLetters[randLetter]:
                    btnList[i]['state'] = DISABLED
                    break

            coins -= 2
            lblCoin.config(text=str(coins))
            
            Check()
        else:
            messagebox.showinfo('Error','Not Enough coins')

def Pass():
    if messagebox.askyesno('Pass','Spend 10 coins to pass?') == True:
        if coins >= 10:
            passObj = PassLevel()
            passObj.change()
        else:
            messagebox.showinfo('Error','Not Enough coins')

#=====Initially record to text file====#
rec = changeLevel()
rec.Record()

#=====GUI=====#
root = Tk()
root.title("4 pics 1 word")

#=====Code to make the window appear at center=====#
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

xCoor = int((screen_width/2) - 190)
yCoor = int((screen_height/2) - 260)

root.geometry('380x520+'+str(xCoor)+"+"+str(yCoor))

frame = Frame(root)

#Images
imgHint = PhotoImage(file="Images/Hint.png")
imgPass = PhotoImage(file="Images/Pass.png")
imgButton = PhotoImage(file="Images/Button.png")
imgUsed = PhotoImage(file="Images/btnUsed.png")
imgLetter = PhotoImage(file="Images/LetterBg.png")
imgLvl = PhotoImage(file="Images/Level.png")
imgGuess = PhotoImage(file="Images/3Letters.png")
img = PhotoImage(fil="Images/"+images[0]+".png")

image = Label(image=img) #Label for four images
imageLevel = Label(root, image=imgLvl) #Label for level bg

#Labels for level and coin count
lblLvl = Label(root, text='Level:'+str(lvl), fg='white', image=imgLvl, compound=CENTER, width=70, height=10, font=('arial bold', 15))
lblCoin = Label(root, text=str(coins), fg='white', image=imgLvl, compound=CENTER, width=50, height=15, font=('arial bold', 17))
#Background image for the guess
imageGuess = Label(frame, image=imgGuess)

#Labels for the guess
lblGuess1 = Label(root, text='', fg='white', image=imgLetter, compound=CENTER, width=15, height=15, font=('Arial Black', 13))
lblGuess2 = Label(root, text='', fg='white', image=imgLetter, compound=CENTER, width=15, height=15, font=('Arial Black', 13))
lblGuess3 = Label(root, text='', fg='white', image=imgLetter, compound=CENTER, width=15, height=15, font=('Arial Black', 13))
lblGuess4 = Label(root, text='', fg='white', image=imgLetter, compound=CENTER, width=15, height=15, font=('Arial Black', 13))
lblGuess5 = Label(root, text='', fg='white', image=imgLetter, compound=CENTER, width=15, height=15, font=('Arial Black', 13))
lblGuess6 = Label(root, text='', fg='white', image=imgLetter, compound=CENTER, width=15, height=15, font=('Arial Black', 13))
lblGuess7 = Label(root, text='', fg='white', image=imgLetter, compound=CENTER, width=15, height=15, font=('Arial Black', 13))
lblGuess8 = Label(root, text='', fg='white', image=imgLetter, compound=CENTER, width=15, height=15, font=('Arial Black', 13))

#Append guess labels to lblList
lblList.append(lblGuess1)
lblList.append(lblGuess2)
lblList.append(lblGuess3)

#Buttons for choices
btn1 = Button(root, text='', width=28, height=28, relief=FLAT, image=imgButton, compound=CENTER, font=('Arial Bold',13), command=lambda:[ClickLetters(0),Check()])
btn2 = Button(root, text='', width=28, height=28, relief=FLAT, image=imgButton, compound=CENTER, font=('Arial Bold',13), command=lambda:[ClickLetters(1),Check()])
btn3 = Button(root, text='', width=28, height=28, relief=FLAT, image=imgButton, compound=CENTER, font=('Arial Bold',13), command=lambda:[ClickLetters(2),Check()])
btn4 = Button(root, text='', width=28, height=28, relief=FLAT, image=imgButton, compound=CENTER, font=('Arial Bold',13), command=lambda:[ClickLetters(3),Check()])
btn5 = Button(root, text='', width=28, height=28, relief=FLAT, image=imgButton, compound=CENTER, font=('Arial Bold',13), command=lambda:[ClickLetters(4),Check()])
btn6 = Button(root, text='', width=28, height=28, relief=FLAT, image=imgButton, compound=CENTER, font=('Arial Bold',13), command=lambda:[ClickLetters(5),Check()])
btn7 = Button(root, text='', width=28, height=28, relief=FLAT, image=imgButton, compound=CENTER, font=('Arial Bold',13), command=lambda:[ClickLetters(6),Check()])
btn8 = Button(root, text='', width=28, height=28, relief=FLAT, image=imgButton, compound=CENTER, font=('Arial Bold',13), command=lambda:[ClickLetters(7),Check()])
btn9 = Button(root, text='', width=28, height=28, relief=FLAT, image=imgButton, compound=CENTER, font=('Arial Bold',13), command=lambda:[ClickLetters(8),Check()])
btn10 = Button(root, text='', width=28, height=28, relief=FLAT, image=imgButton, compound=CENTER, font=('Arial Bold',13), command=lambda:[ClickLetters(9),Check()])
btn11 = Button(root, text='', width=28, height=28, relief=FLAT, image=imgButton, compound=CENTER, font=('Arial Bold',13), command=lambda:[ClickLetters(10),Check()])
btn12 = Button(root, text='', width=28, height=28, relief=FLAT, image=imgButton, compound=CENTER, font=('Arial Bold',13), command=lambda:[ClickLetters(11),Check()])

#Append buttons to btnList
btnList.append(btn1)
btnList.append(btn2)
btnList.append(btn3)
btnList.append(btn4)
btnList.append(btn5)
btnList.append(btn6)
btnList.append(btn7)
btnList.append(btn8)
btnList.append(btn9)
btnList.append(btn10)
btnList.append(btn11)
btnList.append(btn12)
buttonLetters() #Initial randomization of letters

#Buttons for pass and hint
btnPass = Button(root, image=imgPass, relief=FLAT, command=Pass)
btnHint = Button(frame, image=imgHint, relief=FLAT, command=Hint) 

lblLvl.place(x=10,y=22)
lblCoin.place(x=300,y=20)

btnPass.place(x=300,y=440)

#Place labels for guesses
lblGuess1.place(x=149,y=383)
lblGuess2.place(x=179,y=383)
lblGuess3.place(x=209,y=383)
lblGuess4.place(x=209,y=383)
lblGuess5.place(x=209,y=383)
lblGuess6.place(x=209,y=383)
lblGuess7.place(x=209,y=383)
lblGuess8.place(x=209,y=383)
LblCount() #Initial count of labels

#Place buttons for choices
btn1.place(x=82,y=430)
btn2.place(x=118,y=430)
btn3.place(x=154,y=430)
btn4.place(x=190,y=430)
btn5.place(x=226,y=430)
btn6.place(x=262,y=430)
btn7.place(x=82,y=466)
btn8.place(x=118,y=466)
btn9.place(x=154,y=466)
btn10.place(x=190,y=466)
btn11.place(x=226,y=466)
btn12.place(x=262,y=466)

imageLevel.pack(pady='8')
image.pack()
btnHint.grid(row=0,column=1)
imageGuess.grid(row=0,column=0)
frame.place(x=135,y=368)

#=====Instruction box=====#
messagebox.showinfo('Instructions','Instructions:\n*Click the letters to make your choice\n*Once the letters has changed color, click again to remove the letter from text field\n*Click hint button to show one correct letter\n*Click pass button to go to next level without answering\n\nClick ok to start')

root.mainloop()
