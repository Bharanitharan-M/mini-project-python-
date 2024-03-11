from tkinter import *
from tkinter import ttk
import sqlite3
import tkinter.messagebox




login  = Tk()
special_ch = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', '/', ':', ';', '"', "'", '<', '>', ',', '.', '?']

con = sqlite3.connect('users_info.db')
curs = con.cursor()
curs.execute("""CREATE TABLE IF NOT EXISTS record(Account_number number, User_name text, Customer_id number, password text, MPIN number,PRIMARY KEY("Account_number","User_name","Customer_id"))""")
con.commit()





login.title("Bank Application")
cursor=["hand2"]
width= login.winfo_screenwidth() 
height= login.winfo_screenheight()
login.geometry("%dx%d" % (width, height))
login.config(bg='light green')

def Login_response():
    acc = name.get()
    mail = email.get()
    uname = na.get()
    passwo = passw.get()
    m = pin.get()
    ch = check.get()
    count = 0

    
    if (len(acc) and len(mail) and len(uname) and len(passwo) and len(m)) == 0:
        msg = "All field should be fill"
        count = 1
    elif ch == 0:
        msg = "Please check the Terms&Conditions"
        count = 1
    elif any(ch.isalpha() for ch in acc):
        msg = "Account number not contain Letter"
        count = 1
    elif not any(ch in special_ch for ch in passwo):
        msg = "Password must contain one special character"
        count = 1
    elif not any(ch.isalnum() for ch in passwo):
        msg = "Password must contain one number"
        count = 1
    elif any(ch.isalpha() for ch in m):
        msg = "MPIN number not contain Letter"
        count = 1
    elif (len(m) > 4):
        msg = "MPIN not more than four"
        count = 1
    elif (len(m) < 3):
        msg = "MPIN not less than four"
        count = 1
    elif (len(passwo) < 6):
        msg = "Pasword not less than 7 character"
        count = 1
    elif (len(passwo) > 13):
        msg = "Pasword not more than 13 character"
        count = 1
    elif (len(uname) > 10):
        msg = "Uname not less than 10 character"
        count = 1
    elif (len(uname) < 6):
        msg = "User name not less than 7 character"
        count = 1
    if count == 1:
      tkinter.messagebox.showerror("Input Error",msg)




    account = 0
    cus = 0
    con = sqlite3.connect('users_data.db')
    cur = con.cursor()
    con.commit()
    for i in cur.execute("SELECT * FROM record WHERE Account_Number = ?",(acc,)):
        run = i[9]
        id1 = i[11]
    con = sqlite3.connect('users_info.db')
    curs = con.cursor()
    con.commit()
    for i in curs.execute("SELECT * FROM record WHERE Account_number = ?",(acc,)):
        account = i[0]
        cus = i[2]



    
    counter = 1
    counters = 1
    ccounter = 0
    if count == 0:
        if (int(run) == int(acc) and int(id1) == int(mail)):
            counter = 0
            ccounter +=1
            
        else:
            msg = "Account is not belong your customer id"
        if counter == 0:
            if (int(account) == int(acc) and int(cus) == int(mail)):
                msg = "Account Already exists"
            else:
                counters = 0
                ccounter += 1
        if counters == 0:
            try:
                con = sqlite3.connect('users_info.db')
                curs = con.cursor()
                curs.execute("INSERT INTO record VALUES (:Account_number , :User_name , :Customer_id , :password , :MPIN)", {
                                'Account_number': int(name.get()),
                                'User_name': na.get(),
                                'Customer_id': int(email.get()),
                                'password': passw.get(),
                                'MPIN': pin.get()
                })
                con.commit()
                ccounter += 1
            except sqlite3.IntegrityError as er:
                msgg = "Account Already Exits!!"
                tkinter.messagebox.showerror('Check The Account number', msgg)
            except Exception as ep:
                tkinter.messagebox.showerror("Database error",ep)
        else:
            tkinter.messagebox.showerror("User Error",msg)
    if ccounter == 3:
        tkinter.messagebox.showinfo("Confirm","Account created Successfully")

                
                
                
                
            













l1 = Label(login,text="Welcome to BM Bank",font=('Times New Roman',30,'bold'),bg = "light green").place(relx=0.39,rely=0.045)





separator = ttk.Separator(login, orient='vertical')
separator.place(relx=0.25, rely=0.15, relwidth=0.5, relheight=0.58)



l2 = Label(login,text="New User",font=('Times New Roman',20,'bold')).place(relx=0.45,rely=0.165)


l3 = Label(login,text="Account Number",font=('Times New Roman',15,'bold')).place(relx=0.33,rely=0.25)
name = Entry(login)
name.place(relx=0.43,rely=0.25,relheight=0.03,relwidth=0.2)




l4 = Label(login,text="Customer Id",font=('Times New Roman',15,'bold')).place(relx=0.33,rely=0.31)
email = Entry(login)
email.place(relx=0.43,rely=0.31,relheight=0.03,relwidth=0.2)



l7 = Label(login,text="User Name",font=('Times New Roman',15,'bold')).place(relx=0.33,rely=0.37)
na = Entry(login)
na.place(relx=0.43,rely=0.37,relheight=0.03,relwidth=0.2)


l8 = Label(login,text="Password",font=('Times New Roman',15,'bold')).place(relx=0.33,rely=0.43)
passw = Entry(login)
passw.place(relx=0.43,rely=0.43,relheight=0.03,relwidth=0.2)


l9 = Label(login,text="Set MPIN",font=('Times New Roman',15,'bold')).place(relx=0.33,rely=0.49)
pin = Entry(login)
pin.place(relx=0.43,rely=0.49,relheight=0.03,relwidth=0.2)


check = IntVar()
l5 = Checkbutton(login,text="I agree the Terms&Condition",font=('Times New Roman',15),variable = check,onvalue = 1 ,offvalue = 0).place(relx=0.33,rely=0.55)


l10 = Button(login,text="Create a Account",cursor=cursor,fg="white",bg="black",font=('Times New Roman',15,'bold'),command = Login_response).place(relx=0.45,rely=0.6)






login.mainloop()
