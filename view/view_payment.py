from tkinter import *

import tkinter.ttk as ttk
import tkinter.messagebox as msg


class View_Payment:
    def __init__(self):
        self.win = Tk()
        self.win.title("payment")
        self.win.geometry("800x700")

        Label(self.win, text="you are in payment", font=("sega", 20), fg = 'grey19',bg='honeydew2').pack()
        #name
        self.tn = StringVar ( )
        Label ( self.win, text = "name :", font = ("Arial", 10) ).place ( x = 20, y = 20 )
        self.ent_n = Entry ( self.win, textvariable = self.tn, bg = "lightgray", font = ("Arial", 10) )
        self.ent_n.place ( x = 100, y = 20, height = 40, width = 90 )

        #model
        self.tm = StringVar ( )
        Label ( self.win, text = "model :", font = ("Arial", 10) ).place ( x = 20, y = 70 )
        self.ent_m = Entry ( self.win, textvariable = self.tm, bg = "lightgray", font = ("Arial", 10) )
        self.ent_m.place ( x = 100, y = 70, height = 40, width = 90 )

        #descripstion
        self.td = StringVar ( )
        Label ( self.win, text = "description :", font = ("Arial", 10) ).place ( x = 20, y = 170)
        self.ent_d = Entry ( self.win, textvariable = self.td, bg = "lightgray", fg = 'black', font = ("Arial", 20) )
        self.ent_d.place ( x = 100, y = 170, height = 100, width = 120 )

        #buy_price
        self.tp = StringVar ( )
        Label ( self.win, text = "buy price :", font = ("Arial", 10) ).place ( x = 20, y = 120 )
        self.ent_p = Entry ( self.win, textvariable = self.tp, bg = "lightgray", font = ("Arial", 10) )
        self.ent_p.place ( x = 100, y = 120, height = 40, width = 90 )

        #buttons
        self.btn_in = Button(self.win, text="Add a Product",font=("Arial",8),bg='old lace', fg='black', command=self.user_view)
        self.btn_in.place(x=370, y=400, height=40, width=90)

        self.btn_up = Button(self.win, text="Delete a Product",font=("Arial",8),bg='honeydew2', fg='black', command=self.user_view)
        self.btn_up.place(x=70,y=400,height=40,width=90)

        self.btn_up = Button(self.win, text="update a product",font=("Arial",8),bg="misty rose", fg='black', command=self.user_view)
        self.btn_up.place(x=170, y=400, height=40, width=90)

        self.btn_up = Button(self.win, text="find a Product",font=("Arial",8),bg='lavender blush2', fg='black', command=self.user_view)
        self.btn_up.place(x=270, y=400, height=40, width=90)


        self.table = ttk.Treeview(self.win,columns=("id", "Name" , "Model" ,"buy_price" , "description") , show="headings")
        self.table.place(x=400  , y=105 )
        self.table.column("id", width=60)
        self.table.column("Name", width=60)
        self.table.column("Model", width=60)
        self.table.column("buy_price", width=60)
        self.table.column("description", width=70)

        self.table.heading("id", text="id")
        self.table.heading("Name", text="Name")
        self.table.heading("Model", text="Model")
        self.table.heading("buy_price", text="Buy Price")
        self.table.heading("description", text="description")



        self.win.mainloop()

    def user_view(self):
        self.user_win = Tk()
        self.user_win.geometry("400x400")
        self.pd_values = ["product1","product2","product3","product4","product5"]
        self.cmb_pd = ttk.Combobox(self.user_win,values=self.pd_values)
        self.cmb_pd.pack()

        self.user_win.mainloop()

    def sing_in(self):
        if self.en.get() == "amirali" and self.ex.get() == "10484360":
            self.win.destroy()
            self.user_view()
        elif self.en.get() == "alireza" and self.ex.get() == "3082419":
            self.win.destroy()
            self.user_view()
        elif self.en.get() == "mamad" and self.ex.get() == "13851385":
            self.win.destroy()
            self.user_view()
        elif self.en.get() == "" and self.ex.get() == "":
            msg.showerror("خطا" , "نام کاربری یا رمز نباید خالی باشد")
        else:
            msg.showerror("حطا", "نام کاربری یا رمز اشتباه میباشد")

    def sing_up(self):
        if self.en.get() == "" and self.ex.get() == "":
           msg.showerror("خطا" , "نام کاربری یا رمز نباید خالی باشد")



test = View_Payment()

