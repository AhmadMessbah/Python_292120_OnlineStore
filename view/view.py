import tkinter
from tkinter import messagebox
import tkinter as tk
import tkinter as ttk
import mysql.connector


class Login :
    def __init__(self) :
        self.window = tkinter.Tk( )
        self.window.geometry("300x300")
        self.window.title(" login Online Store")

        #username
        label = tkinter.Label( self.window, text= "username", font=("Arial") ).pack( )
        username = tkinter.Entry( self.window, font=("Arial") )
        entry = tkinter.Entry( self.window, textvariable=username ).pack( )





        #password
        label = tkinter.Label( self.window, text= "password", font=("Arial") ).pack( )
        password = tkinter.Entry( self.window, font=("Arial") ).pack( )
        entry = tkinter.Entry( self.window, textvariable=password )

        button = tkinter.Button( self.window, text= "login", font=("Arial"), width= 10, height= 10, fg= "red", bg= "" )

        def clear ():
            username.delete ( 0, END )
            passward.delete ( 0, END )

        def login ():
            if (username == '' or username == 'UserName') or (passward == '' or passward == 'Enter Password'):
                messagebox.showerror ( 'TRY AGAIN' )
            else:
                try:
                    mydb = mysql.connector.connect (
                        host = 'localhost',
                        user = 'root',
                        password = 'root123',
                        database = 'mft'
                    )
                    mycursor = mydb.cursor ( )
                except:
                    messagebox.showerror ("error failed to logi")
                return
                sql = 'use oms'
                mycursor.execute ( sql )
                sql = 'select * from login where user = %s and password =%s  '
                mycursor.execute ( sql, (username.get ( ), passward.get ( )) )
                row = mycursor.fetchone ( )
                if row == None:
                    messagebox.showerror ( 'error', 'invalid username and passwors' )
                else:
                    messagebox.showerror ( 'successfull login' )
                    win.destroy ( )
                    import content
        self.window.mainloop()

    def login_click(self) :
        Login()
