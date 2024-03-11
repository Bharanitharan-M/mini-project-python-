from tkinter import *
from tkinter import ttk
import sqlite3
import tkinter.messagebox
import time as tm
import datetime as dt
import os


main = Tk()
main.title("Bank Application")
cursor=["hand2"]
width= main.winfo_screenwidth() 
height= main.winfo_screenheight()
main.geometry("%dx%d" % (width, height))
main.config(bg='light green')

tv = ttk.Treeview(main)



con = sqlite3.connect("users_data.db")
cur = con.cursor()
con.commit()
def passb():
    main.destroy()
    import book


def next():
    count = 0
    global acce
    global monthc
    global typec
    title  = Label(main,text = "To check Transaction",font = ("Times New Roman",20,"bold")).place(relx = 0.43, rely  = 0.114)
    separator = ttk.Separator(main, orient='vertical')
    separator.place(relx=0.02, rely=0.17, relwidth=0.95, relheight=0.8)
    acc = Label(main,text = "Account Number",font = ("Times New Roman",15,"bold")).place(relx = 0.03,rely = 0.2)
    acce = Entry(main,font=("Times New Roman",15))
    acce.place(relx = 0.13,rely = 0.2,relwidth = 0.09)
    month = Label(main,text="Select Month",font=("Times New Roman",15,"bold")).place(relx = 0.3,rely = 0.2)
    n = StringVar() 
    monthc = ttk.Combobox(main, width = 10,height = 5, textvariable = n,font=("Times New Roman",13))
    monthc['values'] = ('January',  
                                  'February ', 
                                  'March ', 
                                  'April', 
                                  'May ', 
                                  'June',
                                  'July ',
                                  'August',
                                  'September',
                                  'October',
                                  'November',
                                  'December',)

        
    monthc.place(relx = 0.39,rely = 0.202)
    monthc.current()
    type = Label(main,text="Select Type",font=("Times New Roman",15,"bold")).place(relx = 0.6,rely = 0.2)
    n1 = StringVar() 
    typec = ttk.Combobox(main, width = 10,height = 5, textvariable = n1,font=("Times New Roman",13))
    typec['values'] = ('Cerit',  
                                  'Debit', 
                                  'All', )

        
    typec.place(relx = 0.67,rely = 0.202)
    typec.current()
    


    nex = Button(main,text = "Next",font = ("Times New Roman", 15),relief = "sunken",cursor = cursor,bg = "black",fg = "white",command = then).place(relx = 0.744,rely = 0.202,relwidth = 0.05,relheight = 0.03)
    a = acce.get()
    s = monthc.get()

    
def payment():


    global label2
    global label4
    global label6
    global label8
    global label10


    title  = Label(main,text = "Make Payments",font = ("Times New Roman",20,"bold")).place(relx = 0.43, rely  = 0.114)
    separator = ttk.Separator(main, orient='vertical')
    separator.place(relx=0.02, rely=0.17, relwidth=0.95, relheight=0.8)
    
    label1 = Label(main,text = "Enter your account Number",font = ("Times New Roman",15,"bold")).place(relx = 0.355,rely = 0.2)
    label2 = Entry(main,font=("Times New Roman",15))
    label2.place(relx = 0.516,rely = 0.2,relwidth = 0.09)


    label3 = Label(main,text = "Receiver account Number",font = ("Times New Roman",15,"bold")).place(relx = 0.03,rely = 0.27)
    label4 = Entry(main,font=("Times New Roman",15))
    label4.place(relx = 0.18,rely = 0.27,relwidth = 0.09)


    label5 = Label(main,text = "IFSC Code",font = ("Times New Roman",15,"bold")).place(relx = 0.03,rely = 0.34)
    label6 = Entry(main,font=("Times New Roman",15))
    label6.place(relx = 0.18,rely = 0.34,relwidth = 0.09)



    label7 = Label(main,text = "Enter the amount",font = ("Times New Roman",15,"bold")).place(relx = 0.03,rely = 0.41)
    label8 = Entry(main,font=("Times New Roman",15))
    label8.place(relx = 0.18,rely = 0.41,relwidth = 0.09)



    label9 = Label(main,text = "Enter the MPIN",font = ("Times New Roman",15,"bold")).place(relx = 0.03,rely = 0.48)
    label10 = Entry(main,font=("Times New Roman",15),show = "*")
    label10.place(relx = 0.18,rely = 0.48,relwidth = 0.09)


    button = Button(main,text = "Proceed",font = ("Times New Roman",18),bg = "black", fg = "white",command = validation,cursor = cursor).place(relx = 0.03,rely = 0.55)
    button1 = Button(main,text = "Forget MPIN",font = ("Times New Roman",18),bg = "black", fg = "white",command = here,cursor = cursor).place(relx = 0.2,rely = 0.55)
    
    
styl = ttk.Style()
styl.configure('white.TSeparator', background='white')
def here():
    global name1
    global email1
    global passw1
    global mi
    separator = ttk.Separator(main, orient='vertical',style='white.TSeparator')
    separator.place(relx=0.4, rely=0.3, relwidth=0.4, relheight=0.5)

    l12 = Label(main,text="MPIN update",font=('Times New Roman',20,'bold')).place(relx=0.55,rely=0.25)


    
    l13 = Label(main,text="User Name",font=('Times New Roman',15,'bold'),bg = "white").place(relx=0.42,rely=0.33)
    name1 = Entry(main)
    name1.place(relx=0.52,rely=0.33,relheight=0.03,relwidth=0.2)


    
    l15 = Label(main,text="Customer ID",font=('Times New Roman',15,'bold'),bg = "white").place(relx=0.42,rely=0.40)
    email1 = Entry(main)
    email1.place(relx=0.52,rely=0.40,relheight=0.03,relwidth=0.2)



    l17 = Label(main,text="Account Number",font=('Times New Roman',15,'bold'),bg = "white").place(relx=0.42,rely=0.47)
    passw1 = Entry(main)
    passw1.place(relx=0.52,rely=0.47,relheight=0.03,relwidth=0.2)


    l18 = Label(main,text="MPIN",font=('Times New Roman',15,'bold'),bg = "white").place(relx=0.42,rely=0.54)
    mi = Entry(main)
    mi.place(relx=0.52,rely=0.54,relheight=0.03,relwidth=0.2)




    
   




   


    l7 = Button(main,text="Confirm",cursor=cursor,command = heres,fg="white",bg="black",font=('Times New Roman',15,'bold')).place(relx=0.6,rely=0.61)


def heres():
    global name1
    global email1
    global passw1
    global mi
    check_counter = 0
    name = name1.get()
    email = email1.get()
    pa = passw1.get()
    mic = mi.get()
    if len(name) == 0:
       warn = "Username can't be empty"
    else:
        check_counter += 1
    if len(email) == "":
        warn = "Customer id can't be empty"
    else:
        check_counter += 1
    if (len(mic) > 4):
        msg = "MPIN not more than four"
    else:
        check_counter += 1
    if (len(mic) < 3):
        msg = "MPIN not less than four"
    else:
        check_counter += 1
    if (len(pa)) ==  0:
        msg = "Account should be fill"
    else:
        check_counter += 1


    counter = 0
    if check_counter == 5:
        try:
            con = sqlite3.connect('users_info.db')
            curs = con.cursor()
            
            curs.execute("UPDATE record SET MPIN = ? WHERE Customer_id = ?",(mic,email))
            con.commit()
            counter = 1
        except Exception as ep:
            tkinter.messagebox.showerror("Database error",ep)
    else:
        tkinter.messagebox.showerror("Input Error",warn)
    if counter == 1:
        tkinter.messagebox.showinfo("Confirm","MPIN Updated successfully")


def then():
    
    global acce
    global monthc
    global typec
    for_count  = 1
    ccount  = 1
    a = acce.get()
    s = monthc.get()
    t = typec.get()
    bcount = 0 
    file = str(a)
    path = 'C:/Users/mbhar/OneDrive/Desktop/PROJECT/PYTHON PROJECT/Bank/%s.db'%file
    isExist = os.path.exists(path)


    
    


    ecount = 0
    if len(a) and len(s) and len(t) != 0:
        if isExist == True:
            con = sqlite3.connect('%s.db'%a)
            curs = con.cursor()
            con.commit()
            ecount = 1
        else:
            msg = "Account Number not exists"
            bcount = 1
    else:
        tkinter.messagebox.showerror("Entry Error","Account number should be fill")

    if bcount == 1:
            tkinter.messagebox.showerror("input",msg)
    if ecount == 1:
        main1 = Tk()
        main1.title("Bank Application")
        cursor=["hand2"]
        width= main1.winfo_screenwidth() 
        height= main1.winfo_screenheight()
        main1.geometry("%dx%d" % (width, height))




        
        i = 2
        try:
            
            if t == "All":
                e1 = Label(main1,text = "Mini-Statement",font = ("Times New Roman",20,"bold")).grid(row = 0,column = 3)
                e=Label(main1,width = 15,text='Account Number',borderwidth=3, relief='ridge',anchor='w',font = ("Times New Roman",18,"bold"))
                e.grid(row=1,column=0)
                e=Label(main1,width = 15,text='Date',borderwidth=3, relief='ridge',anchor='w',font = ("Times New Roman",18,"bold"))
                e.grid(row=1,column=1)
                e=Label(main1,width = 15,text='Time',borderwidth=3, relief='ridge',anchor='w',font = ("Times New Roman",18,"bold"))
                e.grid(row=1,column=2)
                e=Label(main1,width = 15,text='References',borderwidth=3, relief='ridge',anchor='w',font = ("Times New Roman",18,"bold"))
                e.grid(row=1,column=3)
                e=Label(main1,width = 15,text='Cerited amount',borderwidth=3, relief='ridge',anchor='w',font = ("Times New Roman",18,"bold"))
                e.grid(row=1,column=4)
                e=Label(main1,width = 15,text='Debited amount',borderwidth=3, relief='ridge',anchor='w',font = ("Times New Roman",18,"bold"))
                e.grid(row=1,column=5)
                e=Label(main1,width = 15,text='Total amount',borderwidth=3, relief='ridge',anchor='w',font = ("Times New Roman",18,"bold"))
                e.grid(row=1,column=6)
                run = curs.execute("SELECT * FROM %s"%s)
                for column in run:
                    for row in range(len(column)):
                        e = Label(main1,width = 15,text = column[row],borderwidth = 3,relief ="ridge",font = ("Times New Roman",19))
                        e.grid(row = i,column = row)
                        
                    i += 1
            elif t == "Cerit":
                ce = "Credit amount"
                e1 = Label(main1,text = "Mini-Statement",font = ("Times New Roman",20,"bold")).grid(row = 0,column = 3)
                e=Label(main1,width = 15,text='Account Number',borderwidth=3, relief='ridge',anchor='w',font = ("Times New Roman",18,"bold"))
                e.grid(row=1,column=0)
                e=Label(main1,width = 15,text='Date',borderwidth=3, relief='ridge',anchor='w',font = ("Times New Roman",18,"bold"))
                e.grid(row=1,column=1)
                e=Label(main1,width = 15,text='Time',borderwidth=3, relief='ridge',anchor='w',font = ("Times New Roman",18,"bold"))
                e.grid(row=1,column=2)
                e=Label(main1,width = 15,text='References',borderwidth=3, relief='ridge',anchor='w',font = ("Times New Roman",18,"bold"))
                e.grid(row=1,column=3)
                e=Label(main1,width = 15,text='Cerited amount',borderwidth=3, relief='ridge',anchor='w',font = ("Times New Roman",18,"bold"))
                e.grid(row=1,column=4)
                e=Label(main1,width = 15,text='Total amount',borderwidth=3, relief='ridge',anchor='w',font = ("Times New Roman",18,"bold"))
                e.grid(row=1,column=5)
                run = curs.execute("SELECT Account_number,Date,Time,Transaction_Refer,Cerit,Total_Balance FROM %s WHERE Transaction_Refer == ?"%s,(ce,))
                for column in run:
                    for row in range(len(column)):
                            e = Label(main1,width = 15,text = column[row],borderwidth = 3,relief ="ridge",font = ("Times New Roman",19))
                            e.grid(row = i,column = row)
                        
                    i += 1
            elif t == "Debit":
                ce = "Debit amount"
                e1 = Label(main1,text = "Mini-Statement",font = ("Times New Roman",20,"bold")).grid(row = 0,column = 3)
                e=Label(main1,width = 15,text='Account Number',borderwidth=3, relief='ridge',anchor='w',font = ("Times New Roman",18,"bold"))
                e.grid(row=1,column=0)
                e=Label(main1,width = 15,text='Date',borderwidth=3, relief='ridge',anchor='w',font = ("Times New Roman",18,"bold"))
                e.grid(row=1,column=1)
                e=Label(main1,width = 15,text='Time',borderwidth=3, relief='ridge',anchor='w',font = ("Times New Roman",18,"bold"))
                e.grid(row=1,column=2)
                e=Label(main1,width = 15,text='References',borderwidth=3, relief='ridge',anchor='w',font = ("Times New Roman",18,"bold"))
                e.grid(row=1,column=3)
                e=Label(main1,width = 15,text='Cerited amount',borderwidth=3, relief='ridge',anchor='w',font = ("Times New Roman",18,"bold"))
                e.grid(row=1,column=4)
                e=Label(main1,width = 15,text='Total amount',borderwidth=3, relief='ridge',anchor='w',font = ("Times New Roman",18,"bold"))
                e.grid(row=1,column=5)
                run = curs.execute("SELECT Account_number,Date,Time,Transaction_Refer,Debit,Total_Balance FROM %s WHERE Transaction_Refer == ?"%s,(ce,))
                for column in run:
                    for row in range(len(column)):
                            e = Label(main1,width = 15,text = column[row],borderwidth = 3,relief ="ridge",font = ("Times New Roman",19))
                            e.grid(row = i,column = row)
                        
                    i += 1
        except Exception as ep:
            tkinter.messagebox.showerror("Error",ep)
def validation():
    count = 0
    global label2
    global label4
    global label6
    global label8
    global label10
    e = 0
    a = label2.get()
    b = label4.get()
    c = label6.get()
    d = label8.get()
    e = label10.get()
    if (len(a) and len(b) and len(c) and len(d) and len(e)) == 0:
        msg = "All field should fill"
        count = 1
    elif any(ch.isalpha() for ch in a):
        msg = "Your Account should be number"
        count = 1
    elif any(ch.isalpha() for ch in b):
        msg = "Account should be number"
        count = 1
    elif any(ch.isalpha() for ch in d):
        msg = "Amount should be number"
        count = 1
    elif any(ch.isalpha() for ch in e):
        msg = "MPIN should be number"
        count = 1
    else:
        count = 0
    cmpin = 0
    if count == 0:
        try:
            con = sqlite3.connect('users_info.db')
            curs = con.cursor()
            con.commit()
            for i in curs.execute("SELECT * FROM record WHERE Account_number = ?",(a,)):
                cmpin = i[4]
                count = 0
        except Exception as ep:
            tkinter.messagebox.showerror("DataBase Error",ep)
    else:
        tkinter.messagebox.showerror("Error",msg)
        
            
            


        
    cerit_bal = 0
    user_bala = 0
    sender_bal = 0
    acount = 0
    scount = 0
    ch_bala = 0
    sch_bal = 0
    pins = int(cmpin)
    epin = int(e)
    if pins == epin:
        con = sqlite3.connect("users_data.db")
        cur = con.cursor()
        for row in cur.execute("SELECT * FROM record WHERE Account_Number = ?",(a,)):
            user_bala = row[16]
            ch_bala = user_bala
            acount = 1
        if acount == 0:
            tkinter.messagebox.showerror("User","Your Account number not exist")
            
        for row in cur.execute("SELECT * FROM record WHERE Account_Number = ?",(b,)):
            scount = 1
            if c == row[12]:
                sender_bal = row[16]
                sch_bal = sender_bal
            else:
                tkinter.messagebox.showerror("User","IFSC code is not belongs to Sender Account Number")
        if scount == 0:
            tkinter.messagebox.showerror("User","Sender Account number not exist")



        if user_bala == 0:
            tkinter.messagebox.showerror("Balance","Insufficient Balance")
        cerit_bal += int(d)
        user_bala -= int(d)
        sender_bal += int(d)
        
        
        try:
            if ch_bala > user_bala:
                date = dt.datetime.now()
                enter = text = f"{date:%d-%m-%y}"
                times = tm.strftime('%H:%M:%S')
                con = sqlite3.connect('%s.db'%a)
                months = text = f"{date:%B}"
                curss = con.cursor()
                curss.execute("INSERT INTO [%s] VALUES (:Account_number, :Date, :Time, :Transaction_Refer, :Cerit,:Debit, :Total_Balance)"%months,{
                    'Account_number' : a,
                    'Date' : enter,
                    'Time' : times,
                    'Transaction_Refer' : "Debit amount",
                    'Cerit' : "-",
                    'Debit' : d,
                     
                    'Total_Balance' : user_bala 
                    
                    
                })
                con.commit()
                con = sqlite3.connect("users_data.db")
                cur = con.cursor()
                cur.execute("UPDATE record SET Balance = ? WHERE Account_Number = ?",(user_bala,a))
                con.commit()
                
                


            if sch_bal < sender_bal:
                enters = text = f"{date:%d-%m-%y}"
                timess = tm.strftime('%H:%M:%S')
                con = sqlite3.connect('%s.db'%b)
                monthss = text = f"{date:%B}"
                curse = con.cursor()
                curse.execute("INSERT INTO [%s] VALUES (:Account_number, :Date, :Time, :Transaction_Refer, :Cerit,:Debit, :Total_Balance)"%monthss,{
                    'Account_number' : b,
                    'Date' : enters,
                    'Time' : timess,
                    'Transaction_Refer' : "Credit amount",
                    'Cerit' : cerit_bal,
                    'Debit' : "-",
                    'Total_Balance' : sender_bal
                    
                    
                })
                con.commit()
                con = sqlite3.connect("users_data.db")
                cur = con.cursor()
                cur.execute("UPDATE record SET Balance = ? WHERE Account_Number = ?",(sender_bal,b))
                con.commit()
                
               
                count = 1
        except Exception as ep:
            tkinter.messagebox.showerror("Error",ep)

            
            
    else:
        tkinter.messagebox.showerror("Error","MPIN is not match")

    if count == 1:
        
        tkinter.messagebox.showinfo("Successfull","Amount Sent successfully")
        









    
    
separator = ttk.Separator(main, orient='vertical')
separator.place(relx=0.0, rely=0, relwidth=1.0, relheight=0.1)






bu1 = Button(main,text = "To check Transaction",font = ("Times New Roman", 15),relief = "sunken",cursor = cursor,bg = "black",fg = "white",command = next).place(relx = 0.01,rely = 0.02)
bu2 = Button(main,text = "To make payment to Bank Account",font = ("Times New Roman", 15),relief = "sunken",cursor = cursor,bg = "black",fg = "white",command = payment).place(relx = 0.4,rely = 0.02)
bu3 = Button(main,text = "To view Pass Book",font = ("Times New Roman", 15),relief = "sunken",cursor = cursor,bg = "black",fg = "white",command = passb).place(relx = 0.87,rely = 0.02)








main.mainloop()
