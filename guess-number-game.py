from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
import random


loginForm = Tk()
loginForm.title('guess number game')
loginForm.geometry('400x200')
right = int(loginForm.winfo_screenwidth() / 2 - 400 / 2)
down = int(loginForm.winfo_screenheight() / 2 - 200 / 2)
loginForm.geometry('+{}+{}'.format(right, down))
loginForm.resizable(0,0)
loginForm.iconbitmap('images/login.ico')

#function

def resetForm():
    txtNumber1.set("")

attempt = 0
def plus():
    random_number = random.randint(1, 100)
    global attempt
    attempt += 1

    if attempt > 5:
        msg.showinfo(':(', 'You lose!')
        loginForm.quit()
    else:
        user_guess = int(txtNumber1.get())
        if user_guess < random_number:
            lblexplain.config(text='Choose the larger number')
        elif user_guess > random_number:
            lblexplain.config(text='Choose the smaller number')
        else:
            msg.showinfo(':)', f"congragulation! You guessed {random_number} number in {attempt} tries.")
            loginForm.quit()

lblexplain=Label(loginForm,text='You can only play this game ten times')
lblexplain.grid(row=0,column=1,padx=10,pady=10)

lblNumber1=Label(loginForm,text='Number1:')
lblNumber1.grid(row=1,column=0,padx=10,pady=10)

txtNumber1=IntVar(value="")
entNumber1=Entry(loginForm,width=20,textvariable=txtNumber1)
entNumber1.grid(row=1,column=1,padx=10,pady=10)

btnlogin=ttk.Button(loginForm,text='+',width=10,command=plus)
btnlogin.grid(row=2,column=1,padx=10,pady=10)

loginForm.mainloop()




