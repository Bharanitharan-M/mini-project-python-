from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import datetime as dt
import time as tm
import sqlite3

special_ch = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', '/', ':', ';', '"', "'", '<', '>', ',', '.', '?']

count = 0

con = sqlite3.connect('users_data.db')
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS record(First_Name text, Last_Name text, Gender text, Mobile_Number number, Email text, Aadhaar number, Address text, Nationality text, State text, Account_Number Number PRIMARY KEY , Account_Holder text, Customer_id number ,IFSC_code text, MICR number,Branch text,bank_Address text,Balance number)""")
con.commit()



    
login = Tk()
def forget(widget): 
    l9 = Label(login,text = "Enter Otp",font=('Times New Roman',13,"bold")).place(relx=0.258,rely = 0.473)
    l7 = Entry(login,font=('Times New Roman',13,"italic")).place(relx = 0.31,rely = 0.473,relwidth = 0.1,relheight = 0.03)


    
def validation():
    ifs = e9.get()
    date = dt.datetime.now()
    months = text = f"{date:%B}"
    con = sqlite3.connect('%s.db'%e8.get())
    curs = con.cursor()
    curs.execute("""CREATE TABLE IF NOT EXISTS [%s](Account_number number, Date number, Time number, Transaction_Refer text, Cerit number , Debit Number,Total_Balance number)"""%months)
    con.commit()


    if ifs == "":
        tkinter.messagebox.showerror("Check","Fill the IFSC code first")
   


    
    con = sqlite3.connect('IFSC.db')
    cur = con.cursor()
    con.commit()
    try:
        for row in cur.execute("Select * from record WHERE IFSC = ?",(ifs,)):
            mi = Label(login,text = "MICR",font = ('Times New Roman',13,"bold")).place(relx=0.56,rely = 0.63)
            e13 = Entry(login,font=("Times New Roman",13,"italic"))
            e13.place(relx = 0.64 , rely = 0.63,relwidth = 0.1, relheight = 0.03)
            e13.insert(0,row[1])

            
            br = Label(login,text = "Branch",font = ('Times New Roman',13,"bold")).place(relx=0.56,rely = 0.70)
            e10 = Entry(login,font=("Times New Roman",13,"italic"))
            e10.place(relx = 0.64 , rely = 0.70,relwidth = 0.1, relheight = 0.03)
            e10.insert(0,row[2])

            
            ba = Label(login,text="Address",font=("Times New Roman",15,"bold")).place(relx = 0.56,rely = 0.77)
            e12 = Text(login,{"height" : 5, "width" : 28, "wrap": WORD},font=("Times New Roman",13,"italic"))
            e12.place(relx = 0.64 ,rely=0.77)
            e12.insert(INSERT,row[3])
        count = 1
    except Exception as ep:
           tkinter.messagebox.showerror('System Error', ep)



           
    first = e1.get()
    last = e2.get()
    phon = e3.get()
    ad = e6.get()
    country = e7.get()
    acc = e8.get()
    mail = e4.get()
    sta = monthchoosen.get()
    gen = radio.get()
    addres = e5.get("1.0", "end-1c")
    ifs = e9.get()
    acch = e19.get()
    cus = e20.get()
    bal = 1000












    try:
        
        if ( first and  last and  phon and  ad and  country and  acc and  mail and  sta and  gen and  addres and  ifs and acch and cus) == "":
            msg = "All field shoud be fill"
        elif any(ch.isdigit()  for ch in first and last):
            msg = "Name should not contain number"
        elif any(ch.isdigit()  for ch in country):
            msg = "Country should not contain number"
        elif any(ch.isalpha() for ch in phon):
            msg = "Phone not contain letter"
        elif (len(phon)<=9):
            msg = "phone should contain 10 digit"
        elif (len(phon)>=11):
            msg = "phone should contain more than 10 digit"
        elif not any(ch in special_ch for ch in mail):
            msg = "please check the mail!It's not valid"
        elif len(ad) < 12:
            msg = "Aadhaar number should contain 12 digit"
        elif any(ch.isalpha() for ch in ad):
            msg = "Aadhaar number not contain letter"
        elif len(ad) > 12:
            msg = "Aadhaar number should contain more than 12 digit"
        elif len(acc) < 13:
            msg = "Account number should contain 13 digit"
        elif len(acc) > 13:
            msg = "Account number should contain more than 13 digit"
        elif any(ch.isalpha() for ch in acc):
            msg = "Account number not contain letter"
        elif any(ch.isdigit()  for ch in acch):
            msg = "Account Holder should not contain number"
        elif any(ch.isalpha() for ch in cus):
            msg = "Customber Id not contain letter"
        else:
            msg = "hi"
            count = 1
    except Exception as ep:
        tkinter.messagebox.showerror('error', ep)
    else:
        tkinter.messagebox.showinfo('User Error', msg)


        
    counter = 0
    if msg == "hi":
        counters = 0 
        try:
            con = sqlite3.connect('users_data.db')
            cur = con.cursor()
            cur.execute("INSERT INTO record VALUES (:First_Name, :Last_Name, :Gender , :Mobile_Number , :Email, :Aadhaar , :Address , :Nationality , :State, :Account_Number ,:Account_Holder,:Customer_id, :IFSC_code,:MICR, :Branch, :bank_Address, :Balance)", {
                            'First_Name': e1.get(),
                            'Last_Name': e2.get(),
                            'Gender': radio.get(),
                            'Mobile_Number': e3.get(),
                            'Email': e4.get(),
                            'Aadhaar': e6.get(),
                            'Address' : addres,
                            'Nationality' :e7.get(),
                            'State' :  monthchoosen.get(),
                            'Account_Number' : e8.get(),
                            'Account_Holder' : e19.get(),
                            'Customer_id' : e20.get(),
                            'IFSC_code' :e9.get(),
                            'MICR' :e13.get(),
                            'Branch' : e10.get(),
                            'bank_Address' : e12.get("1.0", "end-1c"),
                            'Balance' : bal
                            
                     
                        

            })
            con.commit()
            enter = text = f"{date:%d-%m-%y}"
            times = tm.strftime('%H:%M:%S')
            con = sqlite3.connect('%s.db'%e8.get())
            curs = con.cursor()
            curs.execute("INSERT INTO [%s] VALUES (:Account_number, :Date, :Time, :Transaction_Refer, :Cerit,:Debit, :Total_Balance)"%months,{
                'Account_number' : e8.get(),
                'Date' : enter,
                'Time' : times,
                'Transaction_Refer' : "Initial amount",
                'Cerit' : bal,
                'Debit' : "-",
                'Total_Balance' : bal
                
                
            })
            con.commit()
    
        except sqlite3.IntegrityError as er:
            msgg = "Account Already Exist!!"
            tkinter.messagebox.showerror('Check The Account number', msgg)
            counters = 1
        except Exception as ep:
           tkinter.messagebox.showerror('System Error', ep)
        if counters == 0:
            tkinter.messagebox.showinfo('confirmation', 'Record Saved')
    
        

def signup():
    login.destroy()
    import sign



 
login.config(bg="light green")
width= login.winfo_screenwidth() 
height= login.winfo_screenheight()
login.geometry("%dx%d" % (width, height))
login.title("Login page")
cursor = ["hand2"]
radio = StringVar()
radio.set("Male")
addr = StringVar()



    


separator = ttk.Separator(login, orient='vertical')
separator.place(relx=0.01, rely=0.17, relwidth=0.45, relheight=0.8)
per = Label(login,text="Personal Information",font=("Times New Roman",20,"bold")).place(relx = 0.012,rely = 0.176)





    
fname = Label(login,text='First Name',font=('Times New Roman',15,"bold")).place(relx=0.03,rely= 0.25)
e1 = Entry(login,font=('Times New Roman',13,"italic"))
e1.place(relx = 0.11,rely = 0.25,relwidth = 0.1,relheight = 0.03)
lname = Label(login,text='Last Name',font=('Times New Roman',15,"bold")).place(relx=0.22,rely= 0.25)
e2 = Entry(login,font=('Times New Roman',13,"italic"))
e2.place(relx = 0.29,rely = 0.25,relwidth = 0.11,relheight = 0.03)
asper = Label(login,text="*as per in pass book",font=('Microsoft Yi Baiti',13,"italic")).place(relx = 0.03,rely = 0.30)



dob = Label(login,text="DOB",font=("Times New Roman",15,"bold")).place(relx = 0.03, rely = 0.35)




gender = Label(login,text="Gender",font=("Times New Roman",15,"bold")).place(relx = 0.03, rely = 0.41)
c1 = Radiobutton(login,text="Male",variable = radio,value="Male",font=("Times New Roman",15)).place(relx = 0.11, rely = 0.41)
c1 = Radiobutton(login,text="Female",variable = radio,value="Female",font=("Times New Roman",15)).place(relx = 0.161, rely = 0.41)
c1 = Radiobutton(login,text="Other",variable = radio,value="Other",font=("Times New Roman",15)).place(relx = 0.221, rely = 0.41)




pho = Label(login,text="Pho Number",font=('Times New Roman',15,"bold")).place(relx=0.03,rely= 0.47)
e3 = Entry(login,font=('Times New Roman',13,"italic"))
e3.place(relx = 0.11,rely = 0.473,relwidth = 0.1,relheight = 0.03)
l8 = Button(login,text="Get Otp",font=("Times New Roman",13),command=lambda:forget(l8)).place(relx=0.213,rely = 0.47)




email = Label(login,text="Email id",font=('Times New Roman',15,"bold")).place(relx=0.03,rely= 0.53)
e4 = Entry(login,font=('Times New Roman',13,"italic"))
e4.place(relx = 0.11,rely = 0.533,relwidth = 0.165,relheight = 0.03)
button = Button(login,text="Verify",font=("Times New Roman",13)).place(relx = 0.276,rely = 0.528)



aadhar = Label(login,text = "Aadhar No",font=("Times New Roman",15,"bold")).place(relx = 0.03,rely =0.59)
e6 = Entry(login,font=("Times New Roman",15,"bold"))
e6.place(relx = 0.11,rely = 0.59,relwidth = 0.165,relheight = 0.03)


 
address = Label(login,text="Address",font=("Times New Roman",15,"bold")).place(relx = 0.03,rely = 0.65)
e5 = Text(login,{"height" : 5, "width" : 28, "wrap": WORD},font=("Times New Roman",13,"italic"))
e5.place(relx = 0.11 ,rely=0.65)



nation = Label(login,text = "Nationality",font=("Times New Roman",15,"bold")).place(relx = 0.03 ,rely = 0.79)
e7 = Entry(login,text="India",font=("Times New Roman",15,"bold"))
e7.place(relx = 0.11,rely = 0.79,relwidth = 0.165,relheight = 0.03)


    
state = Label(login,text="State",font=("Times New Roman",15,"bold")).place(relx = 0.03,rely = 0.848)
n = StringVar() 
monthchoosen = ttk.Combobox(login, width = 20, textvariable = n)
monthchoosen['values'] = (' Tamil Nadu',  
                          ' Andhra Pradesh', 
                          ' Arunachal Pradesh', 
                          ' Assam', 
                          ' Bihar', 
                          ' Kerala', ) 
monthchoosen.place(relx = 0.11,rely = 0.85)
monthchoosen.current()
print(monthchoosen.get())
    


separator = ttk.Separator(login, orient='vertical')
separator.place(relx=0.53, rely=0.17, relwidth=0.45, relheight=0.8)


bank = Label(login,text = "Account Details",font=("Times New Roman",20,"bold")).place(relx = 0.535,rely = 0.176)


acc = Label(login,text='Acc Number',font=('Times New Roman',15,"bold")).place(relx=0.56,rely= 0.25)
e8 = Entry(login,font=('Times New Roman',13,"italic"))
e8.place(relx = 0.64,rely = 0.25,relwidth = 0.1,relheight = 0.03)
dig = Label(login,text="*13 digit of number",font=('Microsoft Yi Baiti',13,"italic")).place(relx = 0.56,rely = 0.30)


hn = Label(login,text='Holder Name',font=('Times New Roman',15,"bold")).place(relx=0.56,rely= 0.35)
e19 = Entry(login,font=('Times New Roman',13,"italic"))
e19.place(relx = 0.64,rely = 0.35,relwidth = 0.1,relheight = 0.03)



cn = Label(login,text='Customer ID',font=('Times New Roman',15,"bold")).place(relx=0.56,rely= 0.42)
e20 = Entry(login,font=('Times New Roman',13,"italic"))
e20.place(relx = 0.64,rely = 0.42,relwidth = 0.1,relheight = 0.03)




acc = Label(login,text = "Bank Details",font=("Times New Roman",20,"bold")).place(relx = 0.535,rely = 0.49)


ifsc = Label(login,text="IFSC code",font=("Times New Roman",15,"bold")).place(relx = 0.56,rely=0.56)
e9 = Entry(login,font=("Times New Roman",13,"italic"))
e9.place(relx = 0.64 , rely = 0.56,relwidth = 0.1, relheight = 0.03)
l18 = Button(login,text="Get IFSC code and Submit",font=("Times New Roman",13),command=validation).place(relx=0.742,rely = 0.553)







    
wel = Label(login,text = "BM Bank Ltd",font=("Times new Roman",25,"bold"),bg = "orange").place(relx = 0.43,rely=0.0)
msg = Label(login, text = "This is only for new Account",font=("Times new Roman",25,"bold"),bg = "orange").place(relx = 0.38,rely=0.06)











login.mainloop()



















