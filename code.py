from Tkinter import *
root=Tk()

v1=IntVar()
v2=IntVar()
v3=IntVar()
v4=IntVar()
v5=IntVar()
v6=IntVar()
v7=IntVar()
v8=IntVar()
v9=IntVar()
v10=IntVar()
v11=IntVar()
v12=IntVar()
v13=IntVar()
v14=IntVar()
v15=IntVar()
v16=IntVar()
v17=IntVar()
v18=IntVar()
v19=IntVar()
v20=IntVar()
v21=IntVar()
v22=IntVar()
e1=IntVar()
#total=str(((int)(v1.get())*(int)(e1.get()))+((int)(v2.get())*(int)(e2.get()))+((int)(v3.get())*(int)(e3.get()))+((int)(v4.get())*(int)(e4.get()))+((int)(v5.get())*(int)(e5.get()))+((int)(v6.get())*(int)(e6.get()))+((int)(v7.get())*(int)(e7.get()))+((int)(v8.get())*(int)(e8.get()))+((int)(v9.get())*(int)(e9.get()))+((int)(v10.get())*(int)(e10.get()))+((int)(v11.get())*(int)(e11.get()))+((int)(v12.get())*(int)(e12.get()))+((int)(v13.get())*(int)(e13.get()))+((int)(v14.get())*(int)(e14.get()))+((int)(v15.get())*(int)(e15.get()))+((int)(v16.get())*(int)(e16.get()))+((int)(v17.get())*(int)(e17.get()))+((int)(v18.get())*(int)(e18.get()))+((int)(v19.get())*(int)(e19.get()))+((int)(v20.get())*(int)(e20.get()))+((int)(v21.get())*(int)(e21.get()))+((int)(v22.get())*(int)(e22.get())))
def place():
    print "order placed"
    
    total=(v1.get()*(int)(e1.get()))
    print total
    #total=str(((int)(v1.get())*(int)(e1.get()))+((int)(v2.get())*(int)(e2.get()))+((int)(v3.get())*(int)(e3.get()))+((int)(v4.get())*(int)(e4.get()))+((int)(v5.get())*(int)(e5.get()))+((int)(v6.get())*(int)(e6.get()))+((int)(v7.get())*(int)(e7.get()))+((int)(v8.get())*(int)(e8.get()))+((int)(v9.get())*(int)(e9.get()))+((int)(v10.get())*(int)(e10.get()))+((int)(v11.get())*(int)(e11.get()))+((int)(v12.get())*(int)(e12.get()))+((int)(v13.get())*(int)(e13.get()))+((int)(v14.get())*(int)(e14.get()))+((int)(v15.get())*(int)(e15.get()))+((int)(v16.get())*(int)(e16.get()))+((int)(v17.get())*(int)(e17.get()))+((int)(v18.get())*(int)(e18.get()))+((int)(v19.get())*(int)(e19.get()))+((int)(v20.get())*(int)(e20.get()))+((int)(v21.get())*(int)(e21.get()))+((int)(v22.get())*(int)(e22.get())))
    root5=Toplevel()
    
    Label(root5,text="total bill = ").pack()
    root5.mainloop()
    
def breakfast():
    #root.destroy()
    root1=Toplevel()
    root1.geometry("500x500")
    a1=PhotoImage(file='breakfastmenu.gif')
    Label(root1,image=a1).place(x=0,y=0)
    def place1():
        total=(v1.get()*(int)(e1.get())+v2.get()*(int)(e2.get())+v3.get()*(int)(e3.get()))
        #total=str(((v1.get())*(e1.get()))+((v2.get())*(e2.get()))+((v3.get())*(e3.get()))+((v4.get())*(e4.get()))+((v5.get())*(e5.get()))+((v6.get())*(e6.get()))+((int)(v7.get())*(int)(e7.get()))+((int)(v8.get())*(int)(e8.get()))+((int)(v9.get())*(int)(e9.get()))+((int)(v10.get())*(int)(e10.get()))+((int)(v11.get())*(int)(e11.get()))+((int)(v12.get())*(int)(e12.get()))+((int)(v13.get())*(int)(e13.get()))+((int)(v14.get())*(int)(e14.get()))+((int)(v15.get())*(int)(e15.get()))+((int)(v16.get())*(int)(e16.get()))+((int)(v17.get())*(int)(e17.get()))+((int)(v18.get())*(int)(e18.get()))+((int)(v19.get())*(int)(e19.get()))+((int)(v20.get())*(int)(e20.get()))+((int)(v21.get())*(int)(e21.get()))+((int)(v22.get())*(int)(e22.get())))
        #place1(total)
    def exi():
        root1.destroy()
    #######################veg check box############################
    Checkbutton(root1,text="        Poha",variable=v1,onvalue=30,bg="wheat").place(x=20,y=110)
    Label(root1,text="Rs 30",bg="wheat").place(x=155,y=110)
    e1=Entry(root1,width=3,bg="wheat")
    e1.place(x=220,y=110)
    e1.insert(0,'0')
    Checkbutton(root1,text="        BreadPakoda       Rs 45",variable=v2,onvalue=45,bg="lightsalmon").place(x=20,y=142)
    e2=Entry(root1,width=3,bg="wheat")
    e2.place(x=220,y=142)
    Checkbutton(root1,text="        Parantha",variable=v3,onvalue=30,bg="wheat").place(x=20,y=174)
    Label(root1,text="Rs 35",bg="wheat").place(x=155,y=174)
    e3=Entry(root1,width=3,bg="wheat").place(x=220,y=174)
    Checkbutton(root1,text="        Idli sambhar         Rs 60",variable=v4,onvalue=45,bg="lightsalmon").place(x=20,y=209)
    e4=Entry(root1,width=3,bg="wheat").place(x=220,y=209)
    Checkbutton(root1,text="        Cutlet",variable=v5,onvalue=30,bg="wheat").place(x=20,y=241)
    Label(root1,text="Rs 40",bg="wheat").place(x=155,y=241)
    e5=Entry(root1,width=3,bg="wheat").place(x=220,y=241)
    Checkbutton(root1,text="        Chole Kulche       Rs 50",variable=v6,onvalue=45,bg="lightsalmon").place(x=20,y=272)
    e6=Entry(root1,width=3,bg="wheat").place(x=220,y=272)
    Checkbutton(root1,text="        Vada Pav",variable=v7,onvalue=30,bg="wheat").place(x=20,y=305)
    Label(root1,text="Rs 25",bg="wheat").place(x=155,y=305)
    e7=Entry(root1,width=3,bg="wheat").place(x=220,y=305)
    Checkbutton(root1,text="        Samosa(2)            Rs 25",variable=v8,onvalue=45,bg="lightsalmon").place(x=20,y=337)
    e8=Entry(root1,width=3,bg="wheat").place(x=220,y=337)
    
    Checkbutton(root1,text="        Sprouts(fried)      Rs 50",variable=v9,onvalue=30,bg="wheat").place(x=20,y=369)
    e9=Entry(root1,width=3,bg="wheat").place(x=220,y=369)
    Checkbutton(root1,text="        Kachori(2)            Rs 30",variable=v10,onvalue=45,bg="lightsalmon").place(x=20,y=401)
    e10=Entry(root1,width=3,bg="wheat").place(x=220,y=401)
    Checkbutton(root1,text="        Dosa",variable=v11,onvalue=30,bg="wheat").place(x=20,y=433)
    Label(root1,text="Rs 45",bg="wheat").place(x=155,y=433)
    e11=Entry(root1,width=3,bg="wheat").place(x=220,y=433)
    ############################### Non veg check box###########################################################################################
    Checkbutton(root1,text="        Boiled Egg(2)",variable=v12,onvalue=30,bg="wheat").place(x=260,y=110)
    
    Label(root1,text="Rs 25",bg="wheat").place(x=415,y=112)
    e12=Entry(root1,width=3,bg="wheat").place(x=470,y=112)
    Checkbutton(root1,text="        Egg Roll                      Rs 40",variable=v13,onvalue=30,bg="lightsalmon").place(x=260,y=142)
    e13=Entry(root1,width=3,bg="wheat").place(x=470,y=142)
    Checkbutton(root1,text="        Chicken Nuggets(4)",variable=v14,onvalue=30,bg="wheat").place(x=260,y=174)
    Label(root1,text="Rs 100",bg="wheat").place(x=415,y=176)
    e14=Entry(root1,width=3,bg="wheat").place(x=470,y=176)
    Checkbutton(root1,text="        Omelette(3)                Rs 30",variable=v15,onvalue=30,bg="lightsalmon").place(x=260,y=209)
    e15=Entry(root1,width=3,bg="wheat").place(x=470,y=209)
    Checkbutton(root1,text="        Chicken Popcorn",variable=v16,onvalue=30,bg="wheat").place(x=260,y=241)
    Label(root1,text="Rs 70",bg="wheat").place(x=415,y=241)
    e16=Entry(root1,width=3,bg="wheat").place(x=470,y=241)
    Checkbutton(root1,text="        Chicken Roll               Rs 60",variable=v17,onvalue=30,bg="lightsalmon").place(x=260,y=272)
    e17=Entry(root1,width=3,bg="wheat").place(x=470,y=272)
    Checkbutton(root1,text="        Hunger Kabab",variable=v18,onvalue=30,bg="wheat").place(x=260,y=305)
    Label(root1,text="Rs 60",bg="wheat").place(x=415,y=305)
    e18=Entry(root1,width=3,bg="wheat").place(x=470,y=305)
    Checkbutton(root1,text="        Mutton Soup              Rs 55",variable=v19,onvalue=30,bg="lightsalmon").place(x=260,y=337)
    e19=Entry(root1,width=3,bg="wheat").place(x=470,y=337)
    Checkbutton(root1,text="        Sandwich",variable=v20,onvalue=30,bg="wheat").place(x=260,y=369)
    Label(root1,text="Rs 45",bg="wheat").place(x=415,y=369)
    e20=Entry(root1,width=3,bg="wheat").place(x=470,y=369)
    Checkbutton(root1,text="        Chicken Puttu            Rs 60",variable=v21,onvalue=30,bg="lightsalmon").place(x=260,y=401)
    e21=Entry(root1,width=3,bg="wheat").place(x=470,y=401)
    Checkbutton(root1,text="        Egg Upma",variable=v22,onvalue=30,bg="wheat").place(x=260,y=433)
    Label(root1,text="Rs 50",bg="wheat").place(x=415,y=433)
    e22=Entry(root1,width=3,bg="wheat").place(x=470,y=433)
    Button(root1,text="Exit",command=exi).place(x=50,y=470)
    Button(root1,text="Place order",command=place).place(x=100,y=470) 
    
    root1.mainloop()
def lunch():
    root2=Toplevel()
    root2.geometry("500x500")
    a2=PhotoImage(file='lunchmenu2.gif')
    Label(root2,image=a2 ).place(x=0,y=0)
    def exi():
        root2.destroy()
    #######################veg check box##########################################################################################
    Label(root2,text="Qty",bg="crimson").place(x=220,y=80)
    Checkbutton(root2,text="        Chapati",variable=v1,onvalue=10,bg="lightpink").place(x=20,y=110)
    Label(root2,text="Rs 10",bg="lightpink").place(x=155,y=110)
    e1=Entry(root2,width=3,bg="lightpink").place(x=220,y=110)
    Checkbutton(root2,text="        Nan                       Rs 25",variable=v2,onvalue=25,bg="crimson").place(x=20,y=142)
    e2=Entry(root2,width=3,bg="crimson").place(x=220,y=142)
    Checkbutton(root2,text="        Dal Makhani",variable=v3,onvalue=70,bg="lightpink").place(x=20,y=174)
    Label(root2,text="Rs 70",bg="lightpink").place(x=155,y=174)
    e3=Entry(root2,width=3,bg="lightpink").place(x=220,y=174)
    Checkbutton(root2,text="        Matar Paneer       Rs 95",variable=v4,onvalue=95,bg="crimson").place(x=20,y=209)
    e4=Entry(root2,width=3,bg="crimson").place(x=220,y=209)
    Checkbutton(root2,text="        Kaju Curry",variable=v5,onvalue=120,bg="lightpink").place(x=20,y=241)
    Label(root2,text="Rs 120",bg="lightpink").place(x=155,y=241)
    e5=Entry(root2,width=3,bg="lightpink").place(x=220,y=241)
    Checkbutton(root2,text="        Malai Kofta          Rs 100",variable=v6,onvalue=100,bg="crimson").place(x=20,y=272)
    e6=Entry(root2,width=3,bg="crimson").place(x=220,y=272)
    Checkbutton(root2,text="        Shahi Paneer",variable=v7,onvalue=120,bg="lightpink").place(x=20,y=305)
    Label(root2,text="Rs 120",bg="lightpink").place(x=155,y=305)
    e7=Entry(root2,width=3,bg="lightpink").place(x=220,y=305)
    Checkbutton(root2,text="        Kadai Paneer        Rs 130",variable=v8,onvalue=130,bg="crimson").place(x=20,y=337)
    e8=Entry(root2,width=3,bg="crimson").place(x=220,y=337)
    
    Checkbutton(root2,text="        Mix Veg                Rs 80",variable=v9,onvalue=80,bg="lightpink").place(x=20,y=369)
    e9=Entry(root2,width=3,bg="lightpink").place(x=220,y=369)
    Checkbutton(root2,text="        Jeera Rice             Rs 60",variable=v10,onvalue=60,bg="crimson").place(x=20,y=401)
    e10=Entry(root2,width=3,bg="crimson").place(x=220,y=401)
    Checkbutton(root2,text="        Kothe",variable=v11,onvalue=90,bg="lightpink").place(x=20,y=433)
    Label(root2,text="Rs 90",bg="lightpink").place(x=155,y=433)
    e11=Entry(root2,width=3,bg="lightpink").place(x=220,y=433)
    ############################### Non veg check box###########################################################################################
    Label(root2,text="Qty",bg="crimson").place(x=470,y=80)
    Checkbutton(root2,text="        Mutton Korma",variable=v12,onvalue=320,bg="lightpink").place(x=260,y=110)
    
    Label(root2,text="Rs 320",bg="lightpink").place(x=415,y=112)
    e12=Entry(root2,width=3,bg="lightpink").place(x=470,y=112)
    Checkbutton(root2,text="        Fish Biryani                 Rs 150",variable=v13,onvalue=150,bg="crimson").place(x=260,y=142)
    e13=Entry(root2,width=3,bg="crimson").place(x=470,y=142)
    Checkbutton(root2,text="        Grilled Chihcken",variable=v14,onvalue=350,bg="lightpink").place(x=260,y=174)
    Label(root2,text="Rs 350",bg="lightpink").place(x=415,y=176)
    e14=Entry(root2,width=3,bg="lightpink").place(x=470,y=176)
    Checkbutton(root2,text="        Butter Chicken           Rs 360",variable=v15,onvalue=360,bg="crimson").place(x=260,y=209)
    e15=Entry(root2,width=3,bg="crimson").place(x=470,y=209)
    Checkbutton(root2,text="        Nihari Ghosht",variable=v16,onvalue=300,bg="lightpink").place(x=260,y=241)
    Label(root2,text="Rs 300",bg="lightpink").place(x=415,y=241)
    e16=Entry(root2,width=3,bg="lightpink").place(x=470,y=241)
    Checkbutton(root2,text="        Chicken Biryani         Rs 190",variable=v17,onvalue=190,bg="crimson").place(x=260,y=272)
    e17=Entry(root2,width=3,bg="crimson").place(x=470,y=272)
    Checkbutton(root2,text="        Chicken Curry",variable=v18,onvalue=280,bg="lightpink").place(x=260,y=305)
    Label(root2,text="Rs 280",bg="lightpink").place(x=415,y=305)
    e18=Entry(root2,width=3,bg="lightpink").place(x=470,y=305)
    Checkbutton(root2,text="        Kolhapuri chicken     Rs 340",variable=v19,onvalue=340,bg="crimson").place(x=260,y=337)
    e19=Entry(root2,width=3,bg="crimson").place(x=470,y=337)
    Checkbutton(root2,text="        Shami Kabab",variable=v20,onvalue=300,bg="lightpink").place(x=260,y=369)
    Label(root2,text="Rs 300",bg="lightpink").place(x=415,y=369)
    e20=Entry(root2,width=3,bg="lightpink").place(x=470,y=369)
    Checkbutton(root2,text="        Mutton Curry            Rs 310",variable=v21,onvalue=310,bg="crimson").place(x=260,y=401)
    e21=Entry(root2,width=3,bg="crimson").place(x=470,y=401)
    Checkbutton(root2,text="        Garlic chicken",variable=v22,onvalue=380,bg="lightpink").place(x=260,y=433)
    Label(root2,text="Rs 380",bg="lightpink").place(x=415,y=433)
    e22=Entry(root2,width=3,bg="lightpink").place(x=470,y=433)
    Button(root2,text="Exit",command=exi).place(x=50,y=470)
    Button(root2,text="Place order",command=place).place(x=100,y=470)
    root2.mainloop()
def snacks():
    root3=Toplevel()
    root3.geometry("500x500")
    a3=PhotoImage(file='snacksmenu.gif')
    Label(root3,image=a3).place(x=0,y=0)
    def exi():
        root3.destroy()
    #Label(root3,text="asjhdbajsbdkajsdnkjn",bg="bisque").place(x=100,y=100)
    #Label(root3,text="asjhdbajsbdkajsdnkjasdfasdklfln",bg="sandybrown").place(x=200,y=200)
    #######################veg check box##########################################################################################
    Label(root3,text="Qty",bg="sandybrown").place(x=220,y=80)
    Checkbutton(root3,text="        Momos",variable=v1,onvalue=40,bg="bisque").place(x=20,y=110)
    Label(root3,text="Rs 40",bg="bisque").place(x=155,y=110)
    e1=Entry(root3,width=3,bg="bisque").place(x=220,y=110)
    Checkbutton(root3,text="        Maggi                   Rs 35",variable=v2,onvalue=35,bg="sandybrown").place(x=20,y=142)
    e2=Entry(root3,width=3,bg="sandybrown").place(x=220,y=142)
    Checkbutton(root3,text="        Noodles",variable=v3,onvalue=50,bg="bisque").place(x=20,y=174)
    Label(root3,text="Rs 50",bg="bisque").place(x=155,y=174)
    e3=Entry(root3,width=3,bg="bisque").place(x=220,y=174)
    Checkbutton(root3,text="        Aloo tikki              Rs 45",variable=v4,onvalue=45,bg="sandybrown").place(x=20,y=209)
    e4=Entry(root3,width=3,bg="sandybrown").place(x=220,y=209)
    Checkbutton(root3,text="        Chole Bhature",variable=v5,onvalue=60,bg="bisque").place(x=20,y=241)
    Label(root3,text="Rs 60",bg="bisque").place(x=155,y=241)
    e5=Entry(root3,width=3,bg="bisque").place(x=220,y=241)
    Checkbutton(root3,text="        Utpam                   Rs 100",variable=v6,onvalue=100,bg="sandybrown").place(x=20,y=272)
    e6=Entry(root3,width=3,bg="sandybrown").place(x=220,y=272)
    Checkbutton(root3,text="        Dhokla",variable=v7,onvalue=70,bg="bisque").place(x=20,y=305)
    Label(root3,text="Rs 70",bg="bisque").place(x=155,y=305)
    e7=Entry(root3,width=3,bg="bisque").place(x=220,y=305)
    Checkbutton(root3,text="        Manchurian         Rs 110",variable=v8,onvalue=110,bg="sandybrown").place(x=20,y=337)
    e8=Entry(root3,width=3,bg="sandybrown").place(x=220,y=337)
    
    Checkbutton(root3,text="        Pizza                     Rs 180",variable=v9,onvalue=180,bg="bisque").place(x=20,y=369)
    e9=Entry(root3,width=3,bg="bisque").place(x=220,y=369)
    Checkbutton(root3,text="        Burger                  Rs 60",variable=v10,onvalue=60,bg="sandybrown").place(x=20,y=401)
    e10=Entry(root3,width=3,bg="sandybrown").place(x=220,y=401)
    Checkbutton(root3,text="        Garlic Bread",variable=v11,onvalue=90,bg="bisque").place(x=20,y=433)
    Label(root3,text="Rs 90",bg="bisque").place(x=155,y=433)
    e11=Entry(root3,width=3,bg="bisque").place(x=220,y=433)
    ############################### Non veg check box###########################################################################################
    Label(root3,text="Qty",bg="sandybrown").place(x=470,y=80)
    Checkbutton(root3,text="        Chicken Momos",variable=v12,onvalue=80,bg="bisque").place(x=260,y=110)
    
    Label(root3,text="Rs 80",bg="bisque").place(x=415,y=112)
    e12=Entry(root3,width=3,bg="bisque").place(x=470,y=112)
    Checkbutton(root3,text="        Egg Maggi                  Rs 50",variable=v13,onvalue=50,bg="sandybrown").place(x=260,y=142)
    e13=Entry(root3,width=3,bg="sandybrown").place(x=470,y=142)
    Checkbutton(root3,text="        Chickpea",variable=v14,onvalue=90,bg="bisque").place(x=260,y=174)
    Label(root3,text="Rs 90",bg="bisque").place(x=415,y=176)
    e14=Entry(root3,width=3,bg="bisque").place(x=470,y=176)
    Checkbutton(root3,text="        Egg Bonda                  Rs 60",variable=v15,onvalue=60,bg="sandybrown").place(x=260,y=209)
    e15=Entry(root3,width=3,bg="sandybrown").place(x=470,y=209)
    Checkbutton(root3,text="        Chicken Nuggets",variable=v16,onvalue=130,bg="bisque").place(x=260,y=241)
    Label(root3,text="Rs 130",bg="bisque").place(x=415,y=241)
    e16=Entry(root3,width=3,bg="bisque").place(x=470,y=241)
    Checkbutton(root3,text="        Fish Pakori                  Rs 150",variable=v17,onvalue=150,bg="sandybrown").place(x=260,y=272)
    e17=Entry(root3,width=3,bg="sandybrown").place(x=470,y=272)
    Checkbutton(root3,text="        Chicken Cutlet",variable=v18,onvalue=120,bg="bisque").place(x=260,y=305)
    Label(root3,text="Rs 120",bg="bisque").place(x=415,y=305)
    e18=Entry(root3,width=3,bg="bisque").place(x=470,y=305)
    Checkbutton(root3,text="        Chicken Pizza             Rs 220",variable=v19,onvalue=220,bg="sandybrown").place(x=260,y=337)
    e19=Entry(root3,width=3,bg="sandybrown").place(x=470,y=337)
    Checkbutton(root3,text="        Chicken Burger",variable=v20,onvalue=90,bg="bisque").place(x=260,y=369)
    Label(root3,text="Rs 90",bg="bisque").place(x=415,y=369)
    e20=Entry(root3,width=3,bg="bisque").place(x=470,y=369)
    Checkbutton(root3,text="        Chicken Fingers         Rs 160",variable=v21,onvalue=160,bg="sandybrown").place(x=260,y=401)
    e21=Entry(root3,width=3,bg="sandybrown").place(x=470,y=401)
    Checkbutton(root3,text="        Chicken Macaroni",variable=v22,onvalue=110,bg="bisque").place(x=260,y=433)
    Label(root3,text="Rs 110",bg="bisque").place(x=415,y=433)
    e22=Entry(root3,width=3,bg="bisque").place(x=470,y=433)
    Button(root3,text="Exit",command=exi).place(x=50,y=470)
    Button(root3,text="Place order",command=place).place(x=100,y=470)
    root3.mainloop()
def dinner():
    root=Tk()
    root.geometry("500x500")

a=PhotoImage(file='testfront.gif')
root.geometry("700x700")
Label(root,image=a).place(x=0,y=0)
button = Button(root, text="Click me!")
img = PhotoImage(file="breakfast.gif")
button.config(image=img,bd=0,command=breakfast)
button.place(x=20,y=87)
button = Button(root, text="Click me!")
img1 = PhotoImage(file="lunch.gif")
button.config(image=img1,bd=0,command=lunch)
button.place(x=450,y=140)
button = Button(root, text="Click me!")
img2 = PhotoImage(file="snacks.gif")
button.config(image=img2,bd=0,command=snacks)
button.place(x=20,y=370)
button = Button(root, text="Click me!")
img3 = PhotoImage(file="dinner.gif")
button.config(image=img3,bd=0,command=dinner)
button.place(x=400,y=450)
root.mainloop()
