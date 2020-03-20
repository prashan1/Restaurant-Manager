import parser
from  tkinter import *
import tkinter as tk
from tkinter import messagebox
import time

class Restaurant:
    def __init__(self,root):
        self.root = root
        self.root.config(background='#091833')
        self.root.geometry('1200x500+0+0')

     
        #----------------------------------TITLEFRAME------------------------------------------------------------
        self.Title = Label(self.root ,bd = 0 , text = "RESTAURANT MANAGEMENT SYSTEM", font = ("arial" , 25 , 'normal') ,fg = "#f2a343" , bg ='#091833')
        self.Title.place( relx = 0.24 , rely = 0.03)

        LocalTime = Label(self.root ,bd = 0 , text = time.asctime(time.localtime(time.time())) , font = ("arial" , 15 , 'normal') ,fg = "steel blue" , bg ='#091833')
        LocalTime.place( relx = 0.36 , rely = 0.12)

        #----------------------------------ENTRYFRAME------------------------------------------------------------

        self.c1Entry = Label(self.root ,bd = 0 , text = "Chole Bhature: ", font = ("arial" , 15 , 'normal'), fg = 'white', bg ='#091833')
        self.c1Entry.place( relx = 0.04 , rely = 0.21)
        c1Entry = Entry( self.root , font = ("arial",12,"bold"),width = 25)
        c1Entry.place(relx = 0.18 , rely = 0.21)

        self.c2Entry = Label(self.root ,bd = 0 , text = "Biryani: ", font = ("arial" , 15 , 'normal'), fg = 'white', bg ='#091833')
        self.c2Entry.place( relx = 0.04 , rely = 0.28)
        c2Entry = Entry( self.root , font = ("arial",12,"bold"),width = 25)
        c2Entry.place(relx = 0.18 , rely = 0.28)

        self.c3Entry = Label(self.root ,bd = 0 , text = "Chk Tikka Masala: ", font = ("arial" , 15 , 'normal'), fg = 'white', bg ='#091833')
        self.c3Entry.place( relx = 0.04 , rely = 0.36)
        c3Entry = Entry( self.root , font = ("arial",12,"bold"),width = 25)
        c3Entry.place(relx = 0.18 , rely = 0.36)

        self.c4Entry = Label(self.root ,bd = 0 , text = "Fried Potato: ", font = ("arial" , 15 , 'normal'), fg = 'white', bg ='#091833')
        self.c4Entry.place( relx = 0.04 , rely = 0.44)
        c4Entry = Entry( self.root , font = ("arial",12,"bold"),width = 25)
        c4Entry.place(relx = 0.18 , rely = 0.44)

        self.c5Entry = Label(self.root ,bd = 0 , text = "Sizzling aalu: ", font = ("arial" , 15 , 'normal'), fg = 'white', bg ='#091833')
        self.c5Entry.place( relx = 0.04 , rely = 0.52)
        c5Entry = Entry( self.root , font = ("arial",12,"bold"),width = 25)
        c5Entry.place(relx = 0.18 , rely = 0.52)

        self.c6Entry = Label(self.root ,bd = 0 , text = "Drinks: ", font = ("arial" , 15 , 'normal'), fg = 'white', bg ='#091833')
        self.c6Entry.place( relx = 0.04 , rely = 0.6)
        c6Entry = Entry( self.root , font = ("arial",12,"bold"),width = 25)
        c6Entry.place(relx = 0.18 , rely = 0.6)

        self.c7Entry = Label(self.root ,bd = 0 , text = "Big King: ", font = ("arial" , 15 , 'normal'), fg = 'white', bg ='#091833')
        self.c7Entry.place( relx = 0.04 , rely = 0.68)
        c7Entry = Entry( self.root , font = ("arial",12,"bold"),width = 25)
        c7Entry.place(relx = 0.18 , rely = 0.68)

        self.c8Entry = Label(self.root ,bd = 0 , text = "Chk Burger: ", font = ("arial" , 15 , 'normal'), fg = 'white', bg ='#091833')
        self.c8Entry.place( relx = 0.04 , rely = 0.77)
        c8Entry = Entry( self.root , font = ("arial",12,"bold"),width = 25)
        c8Entry.place(relx = 0.18 , rely = 0.77)

        self.c9Entry = Label(self.root ,bd = 0 , text = "Cost: ", font = ("arial" , 15 , 'normal'), fg = 'white', bg ='#091833')
        self.c9Entry.place( relx = 0.39 , rely = 0.28)
        c9Entry = Entry( self.root , font = ("arial",12,"bold"),width = 20)
        c9Entry.place(relx = 0.52 , rely = 0.36)

        self.c10Entry = Label(self.root ,bd = 0 , text = "Service Charge: ", font = ("arial" , 15 , 'normal'), fg = 'white', bg ='#091833')
        self.c10Entry.place( relx = 0.39 , rely = 0.36)
        c10Entry = Entry( self.root , font = ("arial",12,"bold"),width = 20)
        c10Entry.place(relx = 0.52 , rely = 0.44)

        self.c11Entry = Label(self.root ,bd = 0 , text = "TAX: ", font = ("arial" , 15 , 'normal'), fg = 'white', bg ='#091833')
        self.c11Entry.place( relx = 0.39 , rely = 0.44)
        c11Entry = Entry( self.root , font = ("arial",12,"bold"),width = 20)
        c11Entry.place(relx = 0.52 , rely = 0.52)

        self.c12Entry = Label(self.root ,bd = 0 , text = "SubTotal: ", font = ("arial" , 15 , 'normal'), fg = 'white', bg ='#091833')
        self.c12Entry.place( relx = 0.39 , rely = 0.52)
        c12Entry = Entry( self.root , font = ("arial",12,"bold"),width = 20)
        c12Entry.place(relx = 0.52 , rely = 0.6)

        self.c14Entry = Label(self.root ,bd = 0 , text = "Total: ", font = ("arial" , 15 , 'normal'),fg = 'white', bg ='#091833')
        self.c14Entry.place( relx = 0.39 , rely = 0.6)
        c14Entry = Entry( self.root , font = ("arial",12,"bold"),width = 20)
        c14Entry.place(relx = 0.52 , rely = 0.28)

        #----------------------------------CALCLUFRAME------------------------------------------------------------
        self.i = 0
        def get_variables(num):
            
            Cal.insert(self.i,num)
            self.i+=1
        
        def calculate():
            entire_string = Cal.get()
            try:
                a = parser.expr(entire_string).compile()
                result = eval(a)
                Cal.delete(0,END)
                Cal.insert(0,result)
            except Exception:
                Cal.delete(0,END)
                Cal.insert(0,"Error")
            c9Entry.insert(END,0)
            c14Entry.insert(END,Cal.get())
            c12Entry.insert(END,Cal.get())
            c10Entry.insert(END,0)
            c14Entry.insert(END,Cal.get())
            c11Entry.insert(END,Cal.get())
        
        def get_operation(operator):
            
            length = len(operator)
            Cal.insert(self.i,operator)
            self.i+=length

        def clear_all():
            Cal.delete(0,END)
            c1Entry.delete(0,END)
            c2Entry.delete(0,END)
            c3Entry.delete(0,END)
            c4Entry.delete(0,END)
            c5Entry.delete(0,END)
            c6Entry.delete(0,END)
            c7Entry.delete(0,END)
            c8Entry.delete(0,END)
            c9Entry.delete(0,END)
            c10Entry.delete(0,END)
            c11Entry.delete(0,END)
            c12Entry.delete(0,END)
            c14Entry.delete(0,END)
        
        Cal = Entry( self.root , font = ("arial",12,"bold"),width = 13)
        Cal.place(relx = 0.803 , rely = 0.3)

        Button1 = Button(self.root , text = ' 7 ' , font = ("arial",10,"bold") , bg = "#2B2B52" ,fg = "#f2a343",command = lambda :get_variables(7))
        Button1.place(relx = 0.805 , rely = 0.36)

        Button1 = Button(self.root , text = ' 8 ' , font = ("arial",10,"bold") , bg = "#2B2B52" ,fg = "#f2a343",command = lambda :get_variables(8))
        Button1.place(relx = 0.830 , rely = 0.36)


        Button1 = Button(self.root , text = ' 9 ' , font = ("arial",10,"bold")  , bg = "#2B2B52" ,fg = "#f2a343",command = lambda :get_variables(9))
        Button1.place(relx = 0.855 , rely = 0.36)

        
        Button1 = Button(self.root , text = ' + ' ,height = 3, font = ("arial",10,"bold") , bg = "#2B2B52" ,fg = "#f2a343",command= lambda :get_operation("+"))
        Button1.place(relx = 0.8800 , rely = 0.36)

        Button1 = Button(self.root , text = ' 4 ' , font = ("arial",10,"bold")  , bg = "#2B2B52" ,fg = "#f2a343",command = lambda :get_variables(4))
        Button1.place(relx = 0.805 , rely = 0.422)

        Button1 = Button(self.root , text = ' 5 ' , font = ("arial",10,"bold")  , bg = "#2B2B52" ,fg = "#f2a343",command = lambda :get_variables(5))
        Button1.place(relx = 0.830 , rely = 0.422)

        Button1 = Button(self.root , text = ' 6 ' , font = ("arial",10,"bold") , bg = "#2B2B52" ,fg = "#f2a343",command = lambda :get_variables(6))
        Button1.place(relx = 0.855 , rely = 0.422)

        Button1 = Button(self.root , text = ' -- ' ,height = 3, font = ("arial",10,"bold") , bg = "#2B2B52" ,fg = "#f2a343",command= lambda :get_operation("-"))
        Button1.place(relx = 0.8800 , rely = 0.482)

        Button1 = Button(self.root , text = ' 1 ' , font = ("arial",10,"bold")  , bg = "#2B2B52" ,fg = "#f2a343",command = lambda :get_variables(1))
        Button1.place(relx = 0.805 , rely = 0.482)

        Button1 = Button(self.root , text = ' 2 ' , font = ("arial",10,"bold")  , bg = "#2B2B52" ,fg = "#f2a343",command = lambda :get_variables(2))
        Button1.place(relx = 0.830 , rely = 0.482)

        Button1 = Button(self.root , text = ' 3 ' , font = ("arial",10,"bold"), bg = "#2B2B52" ,fg = "#f2a343",command = lambda :get_variables(3))
        Button1.place(relx = 0.855 , rely = 0.482)

        Button1 = Button(self.root , text = ' 0 ' , font = ("arial",10,"bold") , width = 6 , bg = "#2B2B52" ,fg = "#f2a343",command = lambda :get_variables(0))
        Button1.place(relx = 0.805 , rely = 0.544)

        Button1 = Button(self.root , text = ' . ' , font = ("arial",10,"bold") ,width = 2, bg = "#2B2B52" ,fg = "#f2a343")
        Button1.place(relx = 0.856 , rely = 0.544)

        Button1 = Button(self.root , text = '=' , font = ("arial",10,"normal") ,width = 10,padx = -2, bg = "#f2a343" ,fg = "#091833",command=lambda :calculate())
        Button1.place(relx = 0.805 , rely = 0.606)

        Button1 = Button(self.root , text = ' X ' , font = ("arial",10,"bold") ,width = 2, bg = "#2B2B52" ,fg = "#f2a343",command= lambda :get_operation("*"))
        Button1.place(relx = 0.8800 , rely = 0.605)

        #----------------------------------BUTTONFRAME------------------------------------------------------------

        def exxit():
            exitt = messagebox.askyesno("Restaurant Management System","Are you sure ?")
            if exitt:
                self.root.destroy()

        Button1 = Button(self.root , text = ' PRICE ' , font = ("arial",10,"bold") , width =10 ,height = 1  , bg = "#f2a343" ,fg = "#091833",command=lambda :calculate())
        Button1.place(relx = 0.04 , rely = 0.89)

        
        Button2 = Button(self.root , text = ' TOTAL ' , font = ("arial",10,"bold") , width =13 ,height = 1  , bg = "#f2a343" ,fg = "#091833",command=lambda :calculate())
        Button2.place(relx = 0.15 , rely = 0.89)

        
        Button3 = Button(self.root , text = ' RESET ' , font = ("arial",10,"bold") , width =13 ,height = 1  , bg = "#f2a343" ,fg = "#091833",command=lambda :clear_all())
        Button3.place(relx = 0.28 , rely = 0.89)

        
        Button4 = Button(self.root , text = ' EXIT ' , font = ("arial",10,"bold") , width =13 ,height = 1  , bg = "#f2a343" ,fg = "#091833", command = lambda : exxit())
        Button4.place(relx = 0.41 , rely = 0.89)








        
if __name__ == "__main__":
    root = Tk()
    application = Restaurant(root)
    root.mainloop()