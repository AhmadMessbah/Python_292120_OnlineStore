from tkinter import *
import tkinter.ttk as tkk



class view_stuff:
    def __init__(self):
        self.win = Tk()
        self.win.title("view stuff")
        self.win.geometry("900x500")
        Label(self.win,text="name :",font=("Arial",20)).place(x=20,y=20)
        Label(self.win,text="brand :",font=("Arial",20)).place(x=20,y=70)
        Label(self.win,text="model :",font=("Arial",20)).place(x=20,y=120)
        Label(self.win,text="buy price :",font=("Arial",20)).place(x=20,y=170)
        Label(self.win,text="description :",font=("Arial",20)).place(x=20,y=220)

        self.tn = StringVar()
        self.ent_n = Entry(self.win,textvariable=self.tn,bg="lightgray",font=("Arial",20))
        self.ent_n.place(x=180,y=20,height = 40,width = 200)
        self.tm = StringVar()
        self.ent_m = Entry(self.win,textvariable=self.tm,bg="lightgray",font=("Arial",20))
        self.ent_m.place(x=180,y=70,height = 40,width = 200)
        self.tb = StringVar()
        self.ent_b = Entry(self.win,textvariable=self.tb,bg="lightgray",font=("Arial",20))
        self.ent_b.place(x=180,y=120,height = 40,width = 200)
        self.tp = StringVar()
        self.ent_p = Entry(self.win,textvariable=self.tp,bg="lightgray",font=("Arial",20))
        self.ent_p.place(x=180,y=170,height = 40,width = 200)
        self.td = StringVar()
        self.ent_d = Entry(self.win,textvariable=self.td,bg="lightgray",font=("Arial",20))
        self.ent_d.place(x=180,y=220,height = 150,width = 200)



        self.btn_s = Button(self.win,text="SAVE",font=("Arial",10),bg="pink")
        self.btn_s.place(x=70,y=400,height=40,width=70)
        self.btn_r = Button(self.win, text="REMOVE", font=("Arial", 10),bg="pink")
        self.btn_r.place(x=170, y=400, height=40, width=70)
        self.btn_e = Button(self.win, text="EDITE", font=("Arial", 10),bg="pink")
        self.btn_e.place(x=270, y=400, height=40, width=70)






        self.tree = tkk.Treeview(self.win,columns=("1","2","3","4","5"), show="headings")
        self.tree.place(x=420,y=20)

        self.tree.heading("1",text="name")
        self.tree.heading("2",text="brand")
        self.tree.heading("3",text="model")
        self.tree.heading("4",text="buy price")
        self.tree.heading("5",text="description")
        self.tree.column("1",width=90)
        self.tree.column("2",width=90)
        self.tree.column("3",width=90)
        self.tree.column("4",width=90)
        self.tree.column("5",width=90)



        self.win.mainloop()






w = view_stuff()