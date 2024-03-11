
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import sqlite3







login = Tk()
login.config(bg="light green")
width= login.winfo_screenwidth() 
height= login.winfo_screenheight()
login.geometry("%dx%d" % (width, height))
login.title("Pass Bookpage")
cursor = ["hand2"]
radio = StringVar()
radio.set("Male")
addr = StringVar()







special_ch = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', '/', ':', ';', '"', "'", '<', '>', ',', '.', '?']


def fetch():
    label1 = Label(login,text = "Pass Book",font = ("Times New Roman",20,"bold"),bg = "light green").place(relx = 0.45,rely = 0.12)
    con = sqlite3.connect('users_data.db')
    curs = con.cursor()
    
    con = sqlite3.connect('IFSC.db')
    cur = con.cursor()
    con.commit()


    msg = ""
    password = accountn.get()
    count = 0
    if password == "":
        msg = "Account number should be fill"
        count = 1
    elif len(password) < 13:
        msg = "Account number should be 13"
        count = 1
    elif len(password) > 13:
        msg = "Account number should not greater than 13"
        count = 1
    elif any(ch.isalpha() for ch in password):
        msg = "Account number not contain letter"
        count = 1
    if count == 0:
        try:
            for row in curs.execute("Select * from record WHERE Account_Number = ?",(password,)):
                count = 1
                separator = ttk.Separator(login, orient='vertical')
                separator.place(relx=0.01, rely=0.17, relwidth=0.45, relheight=0.8)
                per = Label(login,text="Personal Information",font=("Times New Roman",20,"bold")).place(relx = 0.012,rely = 0.176)





            
                fname = Label(login,text='First Name',font=('Times New Roman',15,"bold")).place(relx=0.03,rely= 0.25)
                e1 = Entry(login,font=('Times New Roman',13,"italic"))
                e1.place(relx = 0.11,rely = 0.25,relwidth = 0.1,relheight = 0.03)
                e1.insert(0,row[0])
                lname = Label(login,text='Last Name',font=('Times New Roman',15,"bold")).place(relx=0.22,rely= 0.25)
                e2 = Entry(login,font=('Times New Roman',13,"italic"))
                e2.place(relx = 0.29,rely = 0.25,relwidth = 0.11,relheight = 0.03)
                e2.insert(0,row[1])
                asper = Label(login,text="*as per in pass book",font=('Microsoft Yi Baiti',13,"italic")).place(relx = 0.03,rely = 0.30)



                dob = Label(login,text="DOB",font=("Times New Roman",15,"bold")).place(relx = 0.03, rely = 0.35)




                gender = Label(login,text="Gender",font=("Times New Roman",15,"bold")).place(relx = 0.03, rely = 0.41)
                c1 = Radiobutton(login,text="Male",variable = radio,value="Male",font=("Times New Roman",15)).place(relx = 0.11, rely = 0.41)
                c1 = Radiobutton(login,text="Female",variable = radio,value="Female",font=("Times New Roman",15)).place(relx = 0.161, rely = 0.41)
                c1 = Radiobutton(login,text="Other",variable = radio,value="Other",font=("Times New Roman",15)).place(relx = 0.221, rely = 0.41)
                radio.set(row[2])



                pho = Label(login,text="Pho Number",font=('Times New Roman',15,"bold")).place(relx=0.03,rely= 0.47)
                e3 = Entry(login,font=('Times New Roman',13,"italic"))
                e3.place(relx = 0.11,rely = 0.473,relwidth = 0.1,relheight = 0.03)
                e3.insert(0,row[3])
                l8 = Button(login,text="Get Otp",font=("Times New Roman",13),command=lambda:forget(l8)).place(relx=0.213,rely = 0.47)




                email = Label(login,text="Email id",font=('Times New Roman',15,"bold")).place(relx=0.03,rely= 0.53)
                e4 = Entry(login,font=('Times New Roman',13,"italic"))
                e4.place(relx = 0.11,rely = 0.533,relwidth = 0.165,relheight = 0.03)
                e4.insert(0,row[4])
                button = Button(login,text="Verify",font=("Times New Roman",13)).place(relx = 0.276,rely = 0.528)



                aadhar = Label(login,text = "Aadhar No",font=("Times New Roman",15,"bold")).place(relx = 0.03,rely =0.59)
                e6 = Entry(login,font=("Times New Roman",15,"bold"))
                e6.place(relx = 0.11,rely = 0.59,relwidth = 0.165,relheight = 0.03)
                e6.insert(0,row[5])


                 
                address = Label(login,text="Address",font=("Times New Roman",15,"bold")).place(relx = 0.03,rely = 0.65)
                e5 = Text(login,{"height" : 5, "width" : 28, "wrap": WORD},font=("Times New Roman",13,"italic"))
                e5.place(relx = 0.11 ,rely=0.65)
                e5.insert(INSERT,row[6])
                



                nation = Label(login,text = "Nationality",font=("Times New Roman",15,"bold")).place(relx = 0.03 ,rely = 0.79)
                e7 = Entry(login,font=("Times New Roman",15,"bold"))
                e7.place(relx = 0.11,rely = 0.79,relwidth = 0.165,relheight = 0.03)
                e7.insert(0,row[7])

                    
                state = Label(login,text="State",font=("Times New Roman",15,"bold")).place(relx = 0.03,rely = 0.848)
                monthchoosen = Entry(login,font=("Times New Roman",15,"bold"))
                monthchoosen.place(relx = 0.11,rely = 0.85)
                monthchoosen.insert(0,row[8])

               
                    


                separator = ttk.Separator(login, orient='vertical')
                separator.place(relx=0.53, rely=0.17, relwidth=0.45, relheight=0.8)


                bank = Label(login,text = "Bank Details",font=("Times New Roman",20,"bold")).place(relx = 0.535,rely = 0.176)


                acc = Label(login,text='Acc Number',font=('Times New Roman',15,"bold")).place(relx=0.56,rely= 0.25)
                e8 = Entry(login,font=('Times New Roman',13,"italic"))
                e8.place(relx = 0.64,rely = 0.25,relwidth = 0.1,relheight = 0.03)
                e8.insert(0,row[9])
                dig = Label(login,text="*13 digit of number",font=('Microsoft Yi Baiti',13,"italic")).place(relx = 0.56,rely = 0.30)



                hn = Label(login,text='Holder Name',font=('Times New Roman',15,"bold")).place(relx=0.56,rely= 0.35)
                e19 = Entry(login,font=('Times New Roman',13,"italic"))
                e19.place(relx = 0.64,rely = 0.35,relwidth = 0.1,relheight = 0.03)
                e19.insert(0,row[10])



                cn = Label(login,text='Customer ID',font=('Times New Roman',15,"bold")).place(relx=0.56,rely= 0.42)
                e20 = Entry(login,font=('Times New Roman',13,"italic"))
                e20.place(relx = 0.64,rely = 0.42,relwidth = 0.1,relheight = 0.03)
                e20.insert(0,row[11])




                

                acc = Label(login,text = "Bank Details",font=("Times New Roman",20,"bold")).place(relx = 0.535,rely = 0.49)


                ifsc = Label(login,text="IFSC code",font=("Times New Roman",15,"bold")).place(relx = 0.56,rely=0.56)
                e9 = Entry(login,font=("Times New Roman",13,"italic"))
                e9.place(relx = 0.64 , rely = 0.56,relwidth = 0.1, relheight = 0.03)
                l18 = Button(login,text="Get IFSC code and Submit",font=("Times New Roman",13),command=validation).place(relx=0.742,rely = 0.553)
                e9.insert(0,row[12])




                mi = Label(login,text = "MICR",font = ('Times New Roman',13,"bold")).place(relx=0.56,rely = 0.63)
                e13 = Entry(login,font=("Times New Roman",13,"italic"))
                e13.place(relx = 0.64 , rely = 0.63,relwidth = 0.1, relheight = 0.03)
                e13.insert(0,row[13])

                
                br = Label(login,text = "Branch",font = ('Times New Roman',13,"bold")).place(relx=0.56,rely = 0.70)
                e10 = Entry(login,font=("Times New Roman",13,"italic"))
                e10.place(relx = 0.64 , rely = 0.70,relwidth = 0.1, relheight = 0.03)
                e10.insert(0,row[14])

                
                ba = Label(login,text="Address",font=("Times New Roman",15,"bold")).place(relx = 0.56,rely = 0.77)
                e12 = Text(login,{"height" : 5, "width" : 28, "wrap": WORD},font=("Times New Roman",13,"italic"))
                e12.place(relx = 0.64 ,rely=0.77)
                e12.insert(INSERT,row[15])




                



                    
                l21 = Button(login,text="Sign-up",font=("Times New Roman",13),bg="black",fg="white",cursor=cursor,command = validation).place(relx=0.75,rely = 0.90)
            if count != 1:
                 tkinter.messagebox.showinfo("Warning","Account number not exist")
                
        except Exception as ep:
               tkinter.messagebox.showerror('System Error', ep)
    else:
        tkinter.messagebox.showinfo("Info",msg)










def validation():
    password = pwd.get()
    password1 = pwd1.get()
    ver = (password == password1)
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

    
    
    
    
    count = 0

    

    try:
        if not any(ch in special_ch for ch in password):
            msg = 'Atleast 1 special character required in password!'
        elif ( first and  last and  phon and  ad and  country and  acc and  mail and  sta and  gen and  addres and  ifs) == "":
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
        elif not any(ch.isupper() for ch in password):
            msg = 'Atleast 1 uppercase character required!'
        elif not any(ch.islower() for ch in password):
            msg = 'Atleast 1 lowercase character required!'
        elif not any(ch.isdigit() for ch in password):
            msg = 'Atleast 1 number required!'
        elif len(password) < 8:
            msg = 'Password must be minimum of 8 characters!'
        elif ver == False:
            msg = "password not match!"
        else:
             msg = 'Success!'
             count = 1
    except Exception as ep:
        tkinter.messagebox.showerror('error', ep)
    else:
        tkinter.messagebox.showerror('User Error', msg)


    
   


    

def forget(widget): 
    l9 = Label(login,text = "Enter Otp",font=('Times New Roman',13,"bold")).place(relx=0.258,rely = 0.473)
    l7 = Entry(login,font=('Times New Roman',13,"italic")).place(relx = 0.31,rely = 0.473,relwidth = 0.1,relheight = 0.03)


    
def code():
    codew = Tk()
    codew.geometry('450x450')
    br = Label(login,text = "Branch",font = ('Times New Roman',13,"bold")).place(relx=0.56,rely = 0.41)
    e10 = Entry(login,font=("Times New Roman",13,"italic")).place(relx = 0.64 , rely = 0.41,relwidth = 0.1, relheight = 0.03)
    state = Label(login,text = "State",font = ('Times New Roman',13,"bold")).place(relx=0.56,rely = 0.47)
    e11 = Entry(login,font=("Times New Roman",13,"italic")).place(relx = 0.64 , rely = 0.47,relwidth = 0.1, relheight = 0.03)

def signup():
    login.destroy()
    import sign



 




    




wel = Label(login,text = "Welcome to BM Bank Ltd",font=("Times new Roman",25,"bold"),bg = "orange").place(relx = 0.38,rely=0.0)






up = Label(login,text = "Enter your Account number to fetch a data",font=("Times New Roman",20,"bold"),bg = "orange").place(relx = 0,rely = 0.06)
accountn = Entry(login,font=('Times New Roman',17,"italic"))
accountn.place(relx = 0.335,rely = 0.06,relwidth = 0.2,relheight = 0.044)
main = Button(login,text="Confirm",font=("Times New Roman",13),bg="black",fg="white",cursor=cursor,command = fetch).place(relx=0.54,rely = 0.06,relwidth = 0.1,relheight = 0.044)





login.mainloop()



















