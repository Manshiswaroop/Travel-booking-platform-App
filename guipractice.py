from tkinter import *
from tkinter import ttk
import sqlite3
amt=0
rec=""

def recpt():
    pay.destroy()
    c.execute("INSERT INTO reciept  (fname,lname,pno,amt,rec,dtravel) VALUES (?,?,?,?,?,?)",(fname.get(),lname.get(),pno.get(),amt,rec,dtravel.get()))
    cur = conn.cursor()
    cur.execute("SELECT * FROM reciept")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    conn.commit()
    
    re=Tk()
    im2=PhotoImage(file="roam.png")
    re.title("TRAVEL AGENCY")
    re.geometry("900x600+250+50")
    re.config(background="#86FF29")
    
    py1=Label(re,image=im2).place(x=-10,y=0)
    py2=Label(re,text="WELCOME TO COOL TRAVELS",background="#FFCD00",fg="#29B329",font="Impact 30 bold underline",bd=4,height=2,width=30,relief=RIDGE).place(x=130,y=110)
    lr11=Label(re,text="RECIEPT",background="#86FF29",fg="#FF6600",font="Impact 25 underline",height=2,width=20,relief=FLAT).place(x=290,y=220)
    
    lr1=Label(re,text="FIRST NAME : ",background="#86FF29",fg="#FF6600",font="Bauhaus93 14 bold ",height=2,width=17,relief=FLAT).place(x=20,y=300)
    lr2=Label(re,text=fname.get(),fg="#FF6600",font="Bauhaus93 14 bold ",height=2,width=18,relief=RIDGE).place(x=200,y=300)
    
    lr3=Label(re,text="LAST NAME : ",background="#86FF29",fg="#FF6600",font="Bauhaus93 14 bold ",height=2,width=17,relief=FLAT).place(x=430,y=300)
    lr4=Label(re,text=lname.get(),fg="#FF6600",font="Bauhaus93 14 bold ",height=2,width=18,relief=RIDGE).place(x=610,y=300)
    
    lr5=Label(re,text="PHONE NO : ",background="#86FF29",fg="#FF6600",font="Bauhaus93 14 bold ",height=2,width=17,relief=FLAT).place(x=20,y=400)
    lr6=Label(re,text=pno.get(),fg="#FF6600",font="Bauhaus93 14 bold ",height=2,width=18,relief=RIDGE).place(x=200,y=400)
    
    lr7=Label(re,text="AMOUNT : ",background="#86FF29",fg="#FF6600",font="Bauhaus93 14 bold ",height=2,width=17,relief=FLAT).place(x=430,y=400)
    lr8=Label(re,text=amt,fg="#FF6600",font="Bauhaus93 14 bold ",height=2,width=18,relief=RIDGE).place(x=610,y=400)
    
    lr9=Label(re,text="ITEM : ",background="#86FF29",fg="#FF6600",font="Bauhaus93 14 bold ",height=2,width=17,relief=FLAT).place(x=150,y=500)
    lr10=Label(re,text=rec,fg="#FF6600",font="Bauhaus93 14 bold ",height=2,width=35,relief=RIDGE).place(x=300,y=500)
def packg():
    p=Toplevel(root)
    im1=PhotoImage(file="roam.png")
    p.title("TRAVEL AGENCY")
    p.geometry("1000x700+150+0")
    p.config(background="#86FF29")
    
    pl9=Label(p,image=im1).place(x=-10,y=0)
    pl8=Label(p,text="WELCOME TO COOL TRAVELS",background="#FFCD00",fg="#29B329",font="Impact 30 bold underline",bd=4,height=2,width=30,relief=RIDGE).place(x=170,y=110)
    
    pl1=Label(p,text="Himachal with Shimla and Manali(7D|6N)",background="#FFCD00",fg="#0009FF",font="Bauhaus93 10 bold ",height=2,width=40,relief=RAISED,bd=4).place(x=28,y=220)
    pl4=Label(p,text="Day 1 - Road trip from Chandigarh to Shimla and Spend the rest of the day at Hotel"
    +"\nDay 2 - Visit Vice Regal Lodge, Mall Roadand Kufri\nDay 3 - Leave for Manali. Spend the evening strolling Manali Market"
    +"\nDay 4 - Full day tour of Manali. Visit Hadimba Devi temple, Jagatsukh and Vashist Kund                                     \nDay 5 - Day at lesiures Enjoy scienic beauty of Himachal\nDay 6 - Return to Chandigarh" ,
    justify=LEFT,background="#FFCD00",fg="#0009FF",font="Bauhaus93 8 bold ",height=7,width=90,relief=SUNKEN).place(x=28,y=265)
    
    pl2=Label(p,text="Kerala- Lover's Paradise(6D|5N)",background="#FFCD00",fg="#0009FF",font="Bauhaus93 10 bold ",height=2,width=40,relief=RAISED,bd=4).place(x=28,y=380)
    pl5=Label(p,text="Day 1 - Transfer from Cochin to Munnar. Enroute visit Valara Waterfalls, tea plantations at Devikulam"
    +"\nDay 2 - Sightsseing tour of Munnar, visit Tata Tea Museum and Eravikulam National Park"
    +"\nDay 3 - Drive to Thekkady, visit Chilli Spice Garde,boat cruise at Periyar Lake"
    +"\nDay 4 - Proceed to Allepey, Enjoy rest of the day in Houseboat"
    +"\nDay 5 - Return to Cochin by road",justify=LEFT,background="#FFCD00",fg="#0009FF",font="Bauhaus93 8 bold ",height=7,width=90,relief=SUNKEN).place(x=28,y=425)
    
    pl3=Label(p,text="Best Of Kashmir (5D|5N)",background="#FFCD00",fg="#0009FF",font="Bauhaus93 10 bold ",height=2,width=40,relief=RAISED,bd=4).place(x=28,y=540)
    pl6=Label(p,text="Day 1 - Arrive at Srinagar. Head to the hotel. Head for the Shikara ride at Dal Lake.                                                \nDay 2 - Proceed to Pahalgam which offers breathtaking views of alpine peaks"
    +"\nDay 3 - Proceed to Gulmarg at standard elevation of 2,690m, visit the world's highest golf course"
    +"\nDay 4 - Proceed to Srinagar for local sight seeing, explore the famous Mughal Gardens and Cheshma Shahi.\nDay 5 - Embark on an excursion to Sonmarg. "
    +" Later enjoy sightseeing atThajwas Galcier, Zero Point." ,justify=LEFT,background="#FFCD00",fg="#0009FF",font="Bauhaus93 8 bold ",height=7,width=90,relief=SUNKEN).place(x=28,y=585)
   
    pb1=Button(p,text="BOOK",command=packgbookh,background="#FFCD00",fg="#29B329",font="PoorRichard 15 bold ",bd=4,height=1,width=15,activebackground="#1BEBF2",relief=GROOVE).place(x=700,y=275)
    pb2=Button(p,text="BOOK",command=packgbookke,background="#FFCD00",fg="#29B329",font="PoorRichard 15 bold ",bd=4,height=1,width=15,activebackground="#1BEBF2",relief=GROOVE).place(x=700,y=430)
    pb3=Button(p,text="BOOK",command=packgbookka,background="#FFCD00",fg="#29B329",font="PoorRichard 15 bold ",bd=4,height=1,width=15,activebackground="#1BEBF2",relief=GROOVE).place(x=700,y=590)
    p.mainloop()

def packgbookh():
    global amt
    global rec
    amt=22000
    rec="Himachal with Shimla and Manali"
    root.destroy()

def packgbookke():
    global amt
    global rec
    amt=30000
    rec="Kerala - Lover's Paradise (Couples)"    
    root.destroy()

def packgbookka():
    global amt
    global rec
    amt=50000
    rec="Best of Kashmir"
    root.destroy()

def flight():
    fl=Toplevel(root)
    im1=PhotoImage(file="roam.png")
    fl.title("TRAVEL AGENCY")
    fl.geometry("700x700+350+10")
    fl.config(background="#86FF29")
   
    fl1=Label(fl,text="WELCOME TO COOL TRAVELS",background="#FFCD00",fg="#29B329",font="Impact 30 bold underline",bd=4,height=2,width=30,relief=RIDGE).place(x=28,y=220)
    fl2=Label(fl,image=im).place(x=-10,y=0)
    fl3=Label(fl,text="Our Airline Partner   -   INDIGO Airlines",background="#86FF29",fg="#FF6600",font="Bauhaus93 20 bold ",height=2,width=40,relief=FLAT).place(x=20,y=350)
    fl4=Label(fl,text="SOURCE:",background="#86FF29",fg="#FF6600",font="Bauhaus93 15 bold ",height=2,width=15,relief=FLAT).place(x=20,y=460)
    fl5=Label(fl,text="CHOOSE A DESTINATION -",background="#86FF29",fg="#FF6600",font="Bauhaus93 15 bold ",height=2,width=25,relief=FLAT).place(x=330,y=410)
    
    fl6=Label(fl,text="MUMBAI",background="#FFCD00",fg="#29B329",font="PoorRichard 15 bold ",bd=4,height=1,width=15,activebackground="#1BEBF2",relief=GROOVE).place(x=20,y=500)
    flb1=Button(fl,text="DELHI",command=flightd,background="#FFCD00",fg="#29B329",font="PoorRichard 15 bold ",bd=4,height=1,width=15,activebackground="#1BEBF2",relief=GROOVE).place(x=330,y=460)
    flb2=Button(fl,text="BENGALURU",command=flightb,background="#FFCD00",fg="#29B329",font="PoorRichard 15 bold ",bd=4,height=1,width=15,activebackground="#1BEBF2",relief=GROOVE).place(x=330,y=520)
    flb3=Button(fl,text="KOLKATA",command=flightk,background="#FFCD00",fg="#29B329",font="PoorRichard 15 bold ",bd=4,height=1,width=15,activebackground="#1BEBF2",relief=GROOVE).place(x=330,y=580)
    fl3=Label(fl,text="Rs.6000",background="#86FF29",fg="#FF6600",font="Bauhaus93 15 bold ",height=2,width=10,relief=FLAT).place(x=550,y=460)
    fl3=Label(fl,text="Rs.7000",background="#86FF29",fg="#FF6600",font="Bauhaus93 15 bold ",height=2,width=10,relief=FLAT).place(x=550,y=520)
    fl3=Label(fl,text="Rs,.6000",background="#86FF29",fg="#FF6600",font="Bauhaus93 15 bold ",height=2,width=10,relief=FLAT).place(x=550,y=580)
    fl.mainloop()

def flightd():   
    global amt
    global rec 
    amt=6000
    rec="Mumbai to Delhi Flight"
    root.destroy()

def flightb():
    global amt
    global rec
    amt=7000
    rec="Mumbai To Banglore Flight"
    root.destroy()

def flightk():
    global amt
    global rec
    amt=6000
    rec="Mumbai To Kolkata Flight"
    root.destroy()

def hotels():
    ht=Toplevel(root)
    im1=PhotoImage(file="roam.png")
    ht.title("TRAVEL AGENCY")
    ht.geometry("700x700+350+10")
    ht.config(background="#86FF29")
    htl1=Label(ht,text="WELCOME TO COOL TRAVELS",background="#FFCD00",fg="#29B329",font="Impact 30 bold underline",bd=4,height=2,width=30,relief=RIDGE).place(x=28,y=220)
    htl2=Label(ht,image=im1).place(x=-10,y=0)
    
    htl0=Label(ht,text="CHOOSE A HOTEL",background="#86FF29",fg="#FF6600",font="Bauhaus93 15 bold ",height=2,width=30,relief=FLAT).place(x=150,y=350)
    htl3=Label(ht,text="Rs.12000",background="#86FF29",fg="#FF6600",font="Bauhaus93 15 bold ",height=2,width=25,relief=FLAT).place(x=400,y=400)
    htl3=Label(ht,text="Rs.10000",background="#86FF29",fg="#FF6600",font="Bauhaus93 15 bold ",height=2,width=25,relief=FLAT).place(x=400,y=450)
    htl4=Label(ht,text="Rs.11000",background="#86FF29",fg="#FF6600",font="Bauhaus93 15 bold ",height=2,width=25,relief=FLAT).place(x=400,y=500)
    
    htb1=Button(ht,text="Taj Mahal Palace Hotel",command=hotelt,background="#FFCD00",fg="#29B329",font="PoorRichard 15 bold ",bd=4,height=1,width=25,activebackground="#1BEBF2",relief=GROOVE).place(x=180,y=400)
    htb2=Button(ht,text="The Lalit, Mumbai",command=hotell,background="#FFCD00",fg="#29B329",font="PoorRichard 15 bold ",bd=4,height=1,width=25,activebackground="#1BEBF2",relief=GROOVE).place(x=180,y=450)
    htb3=Button(ht,text="Trident International Hotel",command=hoteltr,background="#FFCD00",fg="#29B329",font="PoorRichard 15 bold ",bd=4,height=1,width=25,activebackground="#1BEBF2",relief=GROOVE).place(x=180,y=500)
    ht.mainloop()

def hotelt():
    global amt
    global rec
    amt=12000
    rec="Taj International Hotel"
    root.destroy()

def hotell():
    global amt
    global rec
    amt=10000
    rec="Lalit International Hotel"
    root.destroy()

def hoteltr():
    global amt
    global rec
    amt=11000
    rec="Trident International Hotel"
    root.destroy()

conn=sqlite3.connect("data.db")
c = conn.cursor()
c.execute('''CREATE TABLE if not exists reciept 
             (id integer primary key autoincrement,fname text,lname text,pno number,amt number,rec text,dtravel text)''')


root=Tk()
im=PhotoImage(file="roam.png")
root.title("TRAVEL AGENCY")
root.geometry("700x600+350+50")
root.config(background="#004191")

r1=Label(root,text="WELCOME TO COOL TRAVELS",background="#FFCD00",fg="#29B329",font="Impact 30 bold underline",bd=4,height=2,width=30,relief=RIDGE).place(x=28,y=220)
r2=Label(root,image=im).place(x=-10,y=0)

b3=Button(root,text="Packages",command=packg,background="#FFCD00",fg="#29B329",font="Stencil 15 bold ",bd=4,height=1,width=20,activebackground="#1BEBF2",relief=GROOVE).place(x=220,y=350)
b4=Button(root,text="Flight Booking",command=flight,background="#FFCD00",fg="#29B329",font="Stencil 15 bold ",bd=4,height=1,width=20,activebackground="#1BEBF2",relief=GROOVE).place(x=220,y=400)
b5=Button(root,text="Hotels",command=hotels,background="#FFCD00",fg="#29B329",font="Stencil 15 bold ",bd=4,height=1,width=20,activebackground="#1BEBF2",relief=GROOVE).place(x=220,y=450)
b6=Button(root,text="About Us",command=hotels,background="#FFCD00",fg="#29B329",font="Stencil 15 bold ",bd=4,height=1,width=20,activebackground="#1BEBF2",relief=GROOVE).place(x=220,y=500)

root.mainloop()


pay=Tk()
im1=PhotoImage(file="roam.png")
pay.title("TRAVEL AGENCY")
pay.geometry("900x600+250+50")
pay.config(background="#86FF29")

py1=Label(pay,image=im1).place(x=-10,y=0)
py2=Label(pay,text="WELCOME TO COOL TRAVELS",background="#FFCD00",fg="#29B329",font="Impact 30 bold underline",bd=4,height=2,width=30,relief=RIDGE).place(x=130,y=110)

fname=StringVar()
lname=StringVar()
pno=StringVar()
creno=StringVar()
cvv=StringVar()
hname=StringVar()
dtravel=StringVar()
dexpiry=StringVar()

le1=Label(pay,text="FIRST NAME",background="#86FF29",fg="#FF6600",font="Bauhaus93 13 bold ",height=2,width=17,relief=FLAT).place(x=20,y=220)
en1=Entry(pay,textvariable=fname,font="Bauhaus93 13 bold ",width=17,relief=SUNKEN).place(x=200,y=227)

le2=Label(pay,text="LAST NAME",background="#86FF29",fg="#FF6600",font="Bauhaus93 13 bold ",height=2,width=17,relief=FLAT).place(x=430,y=220)
en2=Entry(pay,textvariable=lname,font="Bauhaus93 13 bold ",width=17,relief=SUNKEN).place(x=620,y=227)

le3=Label(pay,text="PHONE NUMBER",background="#86FF29",fg="#FF6600",font="Bauhaus93 13 bold ",height=2,width=17,relief=FLAT).place(x=20,y=260)
en3=Entry(pay,textvariable=pno,font="Bauhaus93 13 bold ",width=17,relief=SUNKEN).place(x=200,y=267)

le4=Label(pay,text="DATE OF TRAVEL",background="#86FF29",fg="#FF6600",font="Bauhaus93 13 bold ",height=2,width=17,relief=FLAT).place(x=430,y=260)
en4=Entry(pay,textvariable=dtravel,font="Bauhaus93 13 bold ",width=17,relief=SUNKEN).place(x=620,y=267)

le5=Label(pay,text="CREDIT CARD NO",background="#86FF29",fg="#FF6600",font="Bauhaus93 13 bold ",height=2,width=17,relief=FLAT).place(x=20,y=300)
en5=Entry(pay,textvariable=creno,font="Bauhaus93 13 bold ",width=17,relief=SUNKEN).place(x=200,y=307)

le6=Label(pay,text="HOLDER'S NAME",background="#86FF29",fg="#FF6600",font="Bauhaus93 13 bold ",height=2,width=17,relief=FLAT).place(x=430,y=300)
en6=Entry(pay,textvariable=hname,font="Bauhaus93 13 bold ",width=17,relief=SUNKEN).place(x=620,y=307)

le7=Label(pay,text="CVV",background="#86FF29",fg="#FF6600",font="Bauhaus93 13 bold ",height=2,width=5,relief=FLAT).place(x=80,y=340)
en7=Entry(pay,textvariable=cvv,font="Bauhaus93 13 bold ",width=17,relief=SUNKEN).place(x=200,y=347)

le8=Label(pay,text="DATE OF EXPIRY(MM/YY)",background="#86FF29",fg="#FF6600",font="Bauhaus93 13 bold ",height=2,width=20,relief=FLAT).place(x=400,y=340)
en8=Entry(pay,textvariable=dexpiry,font="Bauhaus93 13 bold ",width=17,relief=SUNKEN).place(x=620,y=347)


bn1=Button(pay,text="PAY",command=recpt,background="#FFCD00",fg="#29B329",font="PoorRichard 15 bold ",bd=4,height=1,width=15,activebackground="#1BEBF2",relief=GROOVE).place(x=320,y=450)


pay.mainloop()
