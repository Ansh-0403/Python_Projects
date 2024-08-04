from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from pandas import *
from csv import *
import random

BACKGROUND_COLOR = "#B1DDC6"

right_ans=0
wrong_ans=0
x=""
#------------------------------------CSV/PANDAS----------------------------------------------

data=read_csv("python/Capstone_Flash_card/words.csv")

french_w=data.FRENCH.to_list()
english_w=data.ENGLISH.to_list()

temp={}

for i in range(len(french_w)-1):
    temp[french_w[i]]=english_w[i]


#---------------------------------------functions------------------------------------------------
def timer():
    # text_w=random.choice(french_w)
    # canvas.itemconfig(canvas_text,text=text_w)
    window.after(3000,show)

def right():
    global right_ans
    right_ans+=1
    change()
   
def change():
    text_w=random.choice(french_w)
    global x
    x=text_w
    canvas.itemconfig(canvas_text,text=text_w)
    timer()


def wrong():
    global wrong_ans
    wrong_ans+=1
    change()

def start_game():
    messagebox.askokcancel(message="You have 3 seconds to think! ")
    time=messagebox.QUESTION
    change()
    print(time)

def show():
    global x
    canvas.itemconfig(canvas_text,text=temp[x])

def dikha():
    global right_ans
    global wrong_ans
    messagebox.askokcancel(title="RESULTS",message=f"Right Answers : {right_ans}\nWrong Answers : {wrong_ans}")

#---------------------------------------UI--------------------------------------------------


window=Tk()
window.title("Flash Card Game")
window.config(padx=50,pady=50)

img=Image.open("python/Capstone_Flash_card/thumbs up.png")
right_img=img.resize((100,100))
right_image = ImageTk.PhotoImage(right_img)
right=Button(image=right_image, highlightthickness=0,height=100,width=100,background="Green",command=right)
right.grid(row=1,column=1)

img2=Image.open("python/Capstone_Flash_card/WhatsApp Image 2023-08-24 at 19.32.29.jpg")
wrong_img=img2.resize((100,100))
wrong_image=ImageTk.PhotoImage(wrong_img)
wrong=Button(image=wrong_image,highlightthickness=0,height=100,width=100,background="Red",command=wrong)
wrong.grid(row=1,column=0)

start=Button(text="START",command=start_game)
start.grid(row=2,column=0)

Dikha=Button(text="SHOW RESULTS",command=dikha)
Dikha.grid(row=2,column=1)


canvas=Canvas(width=800,height=600)
bg_img=PhotoImage(file="python/Capstone_Flash_card/card_back.png")
canvas.create_image(400,300,image=bg_img)
canvas_text=canvas.create_text(400,300,font=("Courier",30,"bold"),text="hello")
canvas.grid(row=0,column=0,columnspan=2)


mainloop()