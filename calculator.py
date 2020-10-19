from tkinter import*
import tkinter.messagebox as tmsg
import math as m

window=Tk()
window.geometry('510x490')
window.maxsize(510,490)
window.minsize(510,490)
window.title('RB calculator')

font=('Verdana',18,'bold ')

def clear():
    ex = display.get()
    ex = ex[0:len(ex)- 1]
    display.delete(0,END)
    display.insert(0,ex)


def all_clear():
    display.delete(0,END)

def clickfunction(event):
    b=event.widget
    text=b['text']
   # print(text)

    if text =='=':
        try:
            ex=display.get()
            anser=eval(ex)
            display.delete(0,END)
            display.insert(0,anser)

        except Exception as e:
            print(e)
            tmsg.showerror('Error',e)

        return

    display.insert(END, text)

pic=PhotoImage(file='img/cal 4.png')
headinglabel=Label(window,image=pic)
headinglabel.pack(side=TOP,pady=5)

heading=Label(window,text='STUDENT CALCULATOR',font=('Verdana',15,'bold italic underline'),bg='maroon',fg='white')
heading.pack(side=TOP)

display=Entry(window,font=font,justify=RIGHT,borderwidth=7)
display.pack(fill=X,padx=7,pady=4)

fr=Frame(window)
fr.pack(side=TOP)
temp=1
for i in range(0,3):
    for j in range(0,3):
        btn=Button(fr,text=str(temp),font=font,width=6,relief=SOLID,activebackground='orange')
        btn.grid(row=i,column=j,padx=3,pady=7)
        temp=temp+1
        btn.bind('<Button-1>',clickfunction)

b1=Button(fr,text='0',font=font,width=6,relief=SOLID ,activebackground='orange')
b1.grid(row=3,column=0,padx=3,pady=7)
b1.bind('<Button-1>',clickfunction)

b2=Button(fr,text='.',font=font,width=6,relief=SOLID,activebackground='orange')
b2.grid(row=3,column=1,padx=3,pady=7)
b2.bind('<Button-1>',clickfunction)

b3=Button(fr,text='=',font=font,width=6,relief=SOLID,activebackground='orange' )
b3.grid(row=3,column=2,padx=3,pady=7)
b3.bind('<Button-1>',clickfunction)

b4=Button(fr,text='+',font=font,width=6,relief=SOLID, activebackground='orange')
b4.grid(row=0,column=3,padx=3,pady=7)
b4.bind('<Button-1>',clickfunction)

b5=Button(fr,text='-',font=font,width=6,relief=SOLID, activebackground='orange')
b5.grid(row=1,column=3,padx=3,pady=7)
b5.bind('<Button-1>',clickfunction)

b6=Button(fr,text='*',font=font,width=6,relief=SOLID,activebackground='orange')
b6.grid(row=2,column=3,padx=3,pady=7)
b6.bind('<Button-1>',clickfunction)

b7=Button(fr,text='/',font=font,width=6,relief=SOLID,activebackground='orange')
b7.grid(row=3,column=3,padx=3,pady=7)
b7.bind('<Button-1>',clickfunction)

b8=Button(fr,text='DEL',font=font,width=14,relief=SOLID,bg='blue',command=clear)
b8.grid(row=4,column=0,padx=3,pady=7,columnspan=2)


b9=Button(fr,text='AC',font=font,width=13,relief=SOLID,bg='blue',command=all_clear)
b9.grid(row=4,column=2,padx=3,pady=7,columnspan=2)

#########################################################
#Here i use sc button and sc functions:

scFrame = Frame(window)

def  sc(event):
    sce=event.widget
    sce=sce['text']
    print(sce)
    ex=display.get()

    if sce=='sinθ':
      answr= str(m.sin(m.radians(int(ex))))
      print(answr)

    elif sce=='cosθ':
        answr = str(m.cos(m.radians(int(ex))))
        print(answr)

    elif sce == 'tanθ':
        answr = str(m.tan(m.radians(int(ex))))
        print(answr)

    elif sce == '^':
        base,pow=ex.split(',')
        answr=str(m.pow(int(base),int(pow)))
        print(answr)

    elif sce == '√':
        answr=str(m.sqrt(int(ex)))
        print(answr)

##work convart redian  form degree
    elif sce == 'toRed':
        answr = str(m.radians(float(ex)))
        print('work tored')
##work convart degree form redian
    elif sce == 'toDeg':
         answr=str(m.degrees(float(ex)))
         print('work todeg')

    elif sce=='X!':
        answr=str(m.factorial(int(ex)))
        print(answr)

    display.delete(0,END)
    display.insert(0,answr)

normalmode=True
def sc_mode():
    print('ok done')
    global normalmode
    if normalmode:
       fr.pack_forget()
       scFrame.pack(side=TOP,pady=15)
       fr.pack(side=TOP)
       window.geometry('510x615')
       window.maxsize(510,615)
       window.minsize(510,615)
       normalmode=False

    else:
        scFrame.pack_forget()
        window.geometry('500x500')
        print('normal modee')

b10 = Button(scFrame, text='√', font=font, width=6, relief='ridge', activebackground='orange')
b10.grid(row=0, column=0)
b10.bind('<Button-1>', sc)

b11 = Button(scFrame, text='^', font=font, width=6, relief='ridge', activebackground='orange')
b11.grid(row=0, column=1)
b11.bind('<Button-1>', sc)

b12 = Button(scFrame, text='X!', font=font, width=6, relief='ridge', activebackground='orange')
b12.grid(row=0, column=2)
b12.bind('<Button-1>', sc)

b13 = Button(scFrame, text='toRed', font=font, width=6, relief='ridge', activebackground='orange')
b13.grid(row=0, column=3)
b13.bind('<Button-1>', sc)

b14 = Button(scFrame, text='toDeg', font=font, width=6, relief='ridge', activebackground='orange')
b14.grid(row=1, column=0)
b14.bind('<Button-1>', sc)

b15 = Button(scFrame, text='sinθ', font=font, width=6, relief='ridge', activebackground='orange')
b15.grid(row=1, column=1)
b15.bind('<Button-1>', sc)

b16= Button(scFrame, text='cosθ', font=font, width=6, relief='ridge', activebackground='orange')
b16.grid(row=1, column=2)
b16.bind('<Button-1>', sc)

b17 = Button(scFrame, text='tanθ', font=font, width=6, relief='ridge', activebackground='orange')
b17.grid(row=1, column=3)
b17.bind('<Button-1>', sc)



menubar=Menu(window,font=('Georgia',8,'bold'))
mode=Menu(menubar,tearoff=0)
mode.add_checkbutton(label='SCIENTIFIC MODE',command=sc_mode)
menubar.add_cascade(label='MODE',menu=mode)
window.config(menu=menubar)


window.mainloop()





