from tkinter import *
from tkinter import ttk
root=Tk()
##login=PhotoImage(file='source.gif')
##resize=login.subsample(10,10)
en1=ttk.Entry(root,width=30)
en1.pack()
en2=ttk.Entry(root,width=30)
en2.pack()
def plus(x,y):
    print(x+y)
    en1.delete(0,END)
    en2.delete(0,END)
def minus(x,y):
    print(x-y)
    en1.delete(0,END)
    en2.delete(0,END)

def times(x,y):
    print(x*y)
    en1.delete(0,END)
    en2.delete(0,END)
def division(x,y):
    print(x/y)
    en1.delete(0,END)
    en2.delete(0,END)
    
    
pls=ttk.Button(root,text='+')
pls.pack()
pls.config(command=lambda:plus(int(en1.get()),int(en2.get())))

mins=ttk.Button(root,text='-')
mins.pack()
mins.config(command=lambda:minus(int(en1.get()),int(en2.get())))


tims=ttk.Button(root,text='*')
tims.pack()
tims.config(command=lambda:times(int(en1.get()),int(en2.get())))


divide=ttk.Button(root,text='/')
divide.pack()
divide.config(command=lambda:division(int(en1.get()),int(en2.get())))
##def buttonpress(event):
##    print('clicked')
##pls.bind('<ButtonPress>',buttonpress)
style=ttk.Style()
##print(style.theme_names())


style.theme_use('winnative')
style.configure("TButton" , foreground='red')
style.configure("info.TButton" ,background='blue' , font=('Arial',18,'bold'))

pls.configure(style='info.TButton')
style.configure("div.TButton" ,background='green' , font=('Arial',18,'bold'))

divide.configure(style='div.TButton')
style.configure("tims.TButton" ,background='black' , font=('Arial',18,'bold'))

tims.configure(style='tims.TButton')
style.configure("mins.TButton" ,background='grey' , font=('Arial',18,'bold'))
mins.configure(style='mins.TButton')





