from tkinter import *
from tkinter import ttk
import sqlite3
import tkinter.messagebox



root = Tk()

special_ch = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', '/', ':', ';', '"', "'", '<', '>', ',', '.', '?']

def Login():
    root.destroy()
    import login

root.title("Bank Application")
cursor=["hand2"]
width= root.winfo_screenwidth() 
height= root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
root.config(bg='light green')

def heres():
    global name1
    global email1
    global passw1
    check_counter = 0
    name = name1.get()
    email = email1.get()
    pa = passw1.get()
    if len(name) == 0:
       warn = "Username can't be empty"
    else:
        check_counter += 1
    if len(email) == "":
        warn = "Customer id can't be empty"
    else:
        check_counter += 1
    if (pa) == 0:
        warn = "Password Can't be empty"
    else:
        check_counter +=1
    if not any(ch in special_ch for ch in pa):
        warn = "Password must contain one special character"
    else:
        check_counter +=1
    if not any(ch.isalnum() for ch in pa):
        warn = "Password must contain one number"
    else:
        check_counter +=1
    if (len(pa) < 6):
        warn = "Pasword not less than 7 character"
    else:
        check_counter +=1
    if (len(pa) > 13):
        warn = "Pasword not more than 13 character"
    else:
        check_counter +=1
    if check_counter == 7:
        try:
            con = sqlite3.connect('users_info.db')
            curs = con.cursor()
            
            curs.execute("UPDATE record SET password = ? WHERE Customer_id = ?",(pa,email))
            con.commit()
        except Exception as ep:
            tkinter.messagebox.showerror("Database error",ep)
    else:
        tkinter.messagebox.showerror("Input Error",warn)
    l0 = Button(root,text="Sign-in",command=here,cursor=cursor,fg="white",bg="black",font=('Times New Roman',15,'bold')).place(relx=0.6,rely=0.43)

def forget():
    global name1
    global email1
    global passw1
    separator = ttk.Separator(root, orient='vertical')
    separator.place(relx=0.25, rely=0.15, relwidth=0.5, relheight=0.5)


    l12 = Label(root,text="Password update",font=('Times New Roman',20,'bold')).place(relx=0.43,rely=0.165)
    
    l13 = Label(root,text="User Name",font=('Times New Roman',15,'bold')).place(relx=0.36,rely=0.25)
    name1 = Entry(root)
    name1.place(relx=0.45,rely=0.25,relheight=0.03,relwidth=0.2)




    l15 = Label(root,text="Customer ID",font=('Times New Roman',15,'bold')).place(relx=0.36,rely=0.31)
    email1 = Entry(root)
    email1.place(relx=0.45,rely=0.31,relheight=0.03,relwidth=0.2)



    l17 = Label(root,text="Password",font=('Times New Roman',15,'bold')).place(relx=0.36,rely=0.37)
    passw1 = Entry(root)
    passw1.place(relx=0.45,rely=0.37,relheight=0.03,relwidth=0.2)




   


    l7 = Button(root,text="Confirm",command=heres,cursor=cursor,fg="white",bg="black",font=('Times New Roman',15,'bold')).place(relx=0.36,rely=0.43)


def Login_response():
    global name
    global passw
    global email
    global check
    uname = name.get()
    upwd = passw.get()
    id1 = email.get()
    username = ""
    password = ""
    try:
        
        con = sqlite3.connect('users_info.db')
        c = con.cursor()
        for row in c.execute("Select * from record WHERE Customer_id = ?",(id1,)):
            username = row[1]
            password = row[3]
            
        
    except Exception as ep:
        tkinter.messagebox.showerror('', ep)

    
    check_counter=0
    page = 0
    cname = "BMBank"
    cpwd = "BMBank@"
    
    
    if len(uname) == 0:
       warn = "Username can't be empty"
    else:
        check_counter += 1
    if upwd == "":
        warn = "Password can't be empty"
    else:
        check_counter += 1
    if check.get() == 0:
        warn = "Please check the Terms and Conditions"
    else:
        check_counter +=1
    if len(id1) == 0:
       warn = "Customer id can't be empty"
    else:
        check_counter += 1

        
    if check_counter == 4:
        if (uname == username and upwd == password):
            tkinter.messagebox.showinfo('Login Status', 'Logged in Successfully!')
            page = 1
        elif (uname == cname and upwd == cpwd):
            tkinter.messagebox.showinfo('Login Status', 'Logged in Successfully!')
            page = 2
        
        else:
            tkinter.messagebox.showerror('Login Status', 'invalid username or password')
    else:
        tkinter.messagebox.showerror('', warn)

    if page == 1:
        root.destroy()
        import main
    elif page == 2:
        root.destroy()
        import verfication
        


        

l1 = Label(root,text="Welcome to BM Bank",font=('Times New Roman',30,'bold'),bg = "light green").place(relx=0.39,rely=0.045)




def here():
    global name
    global passw
    global email
    global check
    separator = ttk.Separator(root, orient='vertical')
    separator.place(relx=0.25, rely=0.15, relwidth=0.5, relheight=0.5)



    l2 = Label(root,text="Sign-In",font=('Times New Roman',20,'bold')).place(relx=0.5,rely=0.165)


    l3 = Label(root,text="User Name",font=('Times New Roman',15,'bold')).place(relx=0.36,rely=0.25)
    name = Entry(root)
    name.place(relx=0.45,rely=0.25,relheight=0.03,relwidth=0.2)




    l5 = Label(root,text="Customer ID",font=('Times New Roman',15,'bold')).place(relx=0.36,rely=0.31)
    email = Entry(root)
    email.place(relx=0.45,rely=0.31,relheight=0.03,relwidth=0.2)



    l7 = Label(root,text="Password",font=('Times New Roman',15,'bold')).place(relx=0.36,rely=0.37)
    passw = Entry(root)
    passw.place(relx=0.45,rely=0.37,relheight=0.03,relwidth=0.2)


    check = IntVar()
    l5 = Checkbutton(root,text="I agree the Terms&Condition",font=('Times New Roman',15),variable = check,onvalue = 1 ,offvalue = 0).place(relx=0.36,rely=0.43)




    l5 = Button(root,text="SignIn",cursor=cursor,fg="white",bg="black",font=('Times New Roman',15,'bold'),command = Login_response).place(relx=0.36,rely=0.48)
    l7 = Button(root,text="Forget Password",cursor=cursor,fg="white",bg="black",font=('Times New Roman',15,'bold'),command = forget).place(relx=0.52,rely=0.48)
    l7 = Button(root,text="New User Click Here",command=Login,cursor=cursor,fg="white",bg="black",font=('Times New Roman',15,'bold')).place(relx=0.40,rely=0.54)


here()
root.mainloop()
