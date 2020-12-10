from tkinter import *
import random


root = Tk()
root.geometry('300x300')
root.title('OTP Generator')
root.resizable(0,0)

def generate_otp():
    number = random.randint(10000, 99999)
    Label(text=f"{number}",font='bold').grid(row=6,column=2)

Button(text='Generate OTP',command=generate_otp,font='bold',bg='green').grid(row=4,column=2,padx=50,pady=40)

root.mainloop()
