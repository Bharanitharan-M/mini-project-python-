from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import sqlite3


verf = Tk()
verf.config(bg="light green")
width= verf.winfo_screenwidth() 
height= verf.winfo_screenheight()
verf.geometry("%dx%d" % (width, height))
verf.title("Verfication Page")
cursor = ["hand2"]

def new():
    verf.destroy()
    import mangaer

def ifsc():
    e = 1
    encount = 0
    global e13
    global e14
    global e10
    global e12

    
    if e == 1:
        separator = ttk.Separator(verf, orient='vertical')
        separator.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)
        ifs = Label(verf,text = "IFSC",font = ('Times New Roman',13,"bold")).place(relx=0.27,rely = 0.23)
        e13 = Entry(verf,font=("Times New Roman",13,"italic"))
        e13.place(relx = 0.32 , rely = 0.23,relwidth = 0.1, relheight = 0.03)



        
        mi = Label(verf,text = "MICR",font = ('Times New Roman',13,"bold")).place(relx=0.27,rely = 0.30)
        e14 = Entry(verf,font=("Times New Roman",13,"italic"))
        e14.place(relx = 0.32 , rely = 0.30,relwidth = 0.1, relheight = 0.03)


        
        br = Label(verf,text = "Branch",font = ('Times New Roman',13,"bold")).place(relx=0.27,rely = 0.37)
        e10 = Entry(verf,font=("Times New Roman",13,"italic"))
        e10.place(relx = 0.32 , rely = 0.37,relwidth = 0.1, relheight = 0.03)

        
        ba = Label(verf,text="Address",font=("Times New Roman",15,"bold")).place(relx = 0.27,rely = 0.44)
        e12 = Text(verf,{"height" : 5, "width" : 28, "wrap": WORD},font=("Times New Roman",13,"italic"))
        e12.place(relx = 0.32 ,rely=0.44)



        
        bu = Button(verf,text = "UPDATE",font=("Times New Roman",15,"bold"),command  = sub,bg = "black",fg = "white",cursor = cursor).place(relx = 0.4,rely = 0.58)
        
def sub():
    global e13
    global e14
    global e10
    global e12
    ecount = 0
    ifsce = e13.get()
    mic = e14.get()
    branch = e10.get()
    addre = e12.get("1.0", "end-1c")
    


    
    if (len(ifsce) and len(mic) and len(branch) and len(addre)) == 0:
        msge = "All field should be fill"
        ecount = 1
    elif any(ch.isalpha() for ch in mic):
        msge = "MICR not contain letter"
        ecount = 1
    elif any(ch.isdigit() for ch in branch):
        msge = "Branch not number"
        ecount = 1


    if ecount == 0:
            
            con = sqlite3.connect('IFSC.db')
            cur = con.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS record(IFSC text PRIMARY KEY, MICR number , Branch text, Address text)""")
            con.commit()

            try:
               
                
                con = sqlite3.connect('IFSC.db')
                cur = con.cursor()
                cur.execute("INSERT INTO record VALUES (:IFSC_Code, :MICR, :Branch , :Address)", {
                                'IFSC_Code': e13.get(),
                                'MICR': e14.get(),
                                'Branch': e10.get(),
                                'Address': e12.get("1.0", "end-1c")

                })
                con.commit()
                tkinter.messagebox.showinfo('confirmation', 'Record Saved')
            except sqlite3.IntegrityError as er:
               msgg = "IFSC code Already Exist!!"
               tkinter.messagebox.showerror('Check The Account number', msgg)
            except Exception as ep:
               tkinter.messagebox.showerror('System Error', ep)
    else:
        tkinter.messagebox.showerror("Input error",msge)
    


    


    

    
   










ti = Label(verf ,text = "BM Bank LTD",font = ("Times New Roman",30,"bold"),bg = "orange").place(relx = 0.45,rely = 0)



l1  = Button(verf ,text = "Click Here",font = ("Times New Roman",15),bg = "Black", fg = "White",cursor = cursor,command = ifsc).place(relx = 0.001 ,rely = 0.06)
l2 = Label(verf ,text = "for update the IFSC code",font = ("Times New Roman",20),bg = "orange").place(relx = 0.07 ,rely = 0.06)
l3  = Button(verf ,text = "Click Here",font = ("Times New Roman",15),bg = "Black", fg = "White",cursor = cursor,command = new).place(relx = 0.001 ,rely = 0.12)
l4 = Label(verf ,text = "for update the new user",font = ("Times New Roman",20),bg = "orange").place(relx = 0.07 ,rely = 0.12)

