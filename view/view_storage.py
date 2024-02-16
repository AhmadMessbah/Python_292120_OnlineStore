from tkinter import *

import tkinter.ttk as ttk
import tkinter.messagebox as msg


class view_storage:
    def __init__(self):
        self.win = Tk()
        self.win.title("Storage")
        self.win.geometry("800x700")

        Label(self.win, text="you are in Storage", font=("sega", 20), fg = 'grey19',bg='honeydew2').pack()
        #count
        self.tn = StringVar ( )
        Label ( self.win, text = "count :", font = ("Arial", 10) ).place ( x = 20, y = 20 )
        self.ent_n = Entry ( self.win, textvariable = self.tn, bg = "lightgray", font = ("Arial", 10) )
        self.ent_n.place ( x = 100, y = 20, height = 40, width = 90 )

        #stuff
        self.tm = StringVar ( )
        Label ( self.win, text = "stuff :", font = ("Arial", 10) ).place ( x = 20, y = 70 )
        self.ent_m = Entry ( self.win, textvariable = self.tm, bg = "lightgray", font = ("Arial", 10) )
        self.ent_m.place ( x = 100, y = 70, height = 40, width = 90 )



        #buttons
        self.btn_in = Button(self.win, text="Add a Product",font=("Arial",8),bg='old lace', fg='black', command=self.user_view)
        self.btn_in.place(x=370, y=400, height=40, width=90)

        self.btn_up = Button(self.win, text="Delete a Product",font=("Arial",8),bg='honeydew2', fg='black', command=self.user_view)
        self.btn_up.place(x=70,y=400,height=40,width=90)

        self.btn_up = Button(self.win, text="update a product",font=("Arial",8),bg="misty rose", fg='black', command=self.user_view)
        self.btn_up.place(x=170, y=400, height=40, width=90)

        self.btn_up = Button(self.win, text="find a Product",font=("Arial",8),bg='lavender blush2', fg='black', command=self.user_view)
        self.btn_up.place(x=270, y=400, height=40, width=90)


        self.table = ttk.Treeview(self.win,columns=("id", "count" , "stuff" ) , show="headings")
        self.table.place(x=400  , y=105 )
        self.table.column("id", width=60)
        self.table.column("count", width=60)
        self.table.column("stuff", width=60)


        self.table.heading("id", text="id")
        self.table.heading("count", text="Name")
        self.table.heading("stuff", text="Model")




        self.win.mainloop()

    def user_view(self):
        self.user_win = Tk()
        self.user_win.geometry("400x400")
        self.pd_values = ["product1","product2","product3"]
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



test = view_storage()

