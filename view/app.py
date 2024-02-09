import tkinter
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk


class Application :
    def __init__(self) :
        self.window = tkinter.Tk( )
        self.window.geometry("300x300")
        self.window.title(" welcome")

        #username
        label = tkinter.Label( self.window, text= "username", font=("Arial") ).pack( )
        username = tkinter.Entry( self.window, font=("Arial") )




        #password
        label = tkinter.Label( self.window, text= "password", font=("Arial") ).pack( )
        password = tkinter.Entry( self.window, font=("Arial") ).pack( )


        button = tkinter.Button( self.window, text= "login", font=("Arial"), width= 10, height= 10, fg= "red", bg= "" )
        button(self.window , width=8 , text="save").pack()
        button(self.window , width=8 , text="edit").pack()
        button ( self.window, width = 8, text = "remove" ).pack ( )
        button ( self.window, width = 8, text = "find" ).pack ( )

        self.window.mainloop()


    # def login_click(self) :
    #     Application()