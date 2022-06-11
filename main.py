from tkinter import *
root = Tk()
root.geometry('960x760')
root.configure(background='grey')

potstore = 0

def bet_set():
    bet1 = bet_setting_1.get()
    bet_display_1.delete(0, END)
    bet_display_1.insert(0, '$' + str(bet1))
    bet2 = bet_setting_2.get()
    bet_display_2.delete(0, END)
    bet_display_2.insert(0, '$' + str(bet2))
    bet3 = bet_setting_3.get()
    bet_display_3.delete(0, END)
    bet_display_3.insert(0, '$' + str(bet3))
    bet4 = bet_setting_4.get()
    bet_display_4.delete(0, END)
    bet_display_4.insert(0, '$' + str (bet4))
    bet5 = bet_setting_5.get()
    bet_display_5.delete(0, END)
    bet_display_5.insert(0, '$' + str(bet5))
    bet6 = bet_setting_6.get()
    bet_display_6.delete(0, END)
    bet_display_6.insert(0, '$' + str(bet6))
    pot = potstore + float(bet1)+float(bet2)+float(bet3)+float(bet4)+float(bet5)+float(bet6)
    pot_display.delete(0, END)
    pot_display.insert(0, 'Pot: $' + str(pot))

    stack1 = stack_setting_1.get()
    stack_display_1.delete(0, END)
    stack_display_1.insert(0, '$' + str(float(stack1) - float(bet1)))
    stack2 = stack_setting_2.get()
    stack_display_2.delete(0, END)
    stack_display_2.insert(0, '$' + str(float(stack2) - float(bet2)))
    stack3 = stack_setting_3.get()
    stack_display_3.delete(0, END)
    stack_display_3.insert(0, '$' + str(float(stack3) - float(bet3)))
    stack4 = stack_setting_4.get()
    stack_display_4.delete(0, END)
    stack_display_4.insert(0, '$' + str(float(stack4) - float(bet4)))
    stack5 = stack_setting_5.get()
    stack_display_5.delete(0, END)
    stack_display_5.insert(0, '$' + str(float(stack5) - float(bet5)))
    stack6 = stack_setting_6.get()
    stack_display_6.delete(0, END)
    stack_display_6.insert(0, '$' + str(float(stack6) - float(bet6)))

def set_flop():
    global potstore
    flop = flopi.get()
    b1 = flop[0]
    b2 = flop[2]
    b3 = flop[4]
    if flop[1] == 'c':
        bc1.config(fg='green', font=('Arial', 18, 'bold'))
        bc1.delete(0, END)
        bc1.insert(0, b1)
    elif flop[1] == 'd':
        bc1.config(fg='blue', font=('Arial', 18, 'bold'))
        bc1.delete(0, END)
        bc1.insert(0, b1)
    elif flop[1] == 'h':
        bc1.config(fg='red', font=('Arial', 18, 'bold'))
        bc1.delete(0, END)
        bc1.insert(0, b1)
    else:
        bc1.config(font=('Arial', 18, 'bold'))
        bc1.delete(0, END)
        bc1.insert(0, b1)

    if flop[3] == 'c':
        bc2.config(fg='green', font=('Arial', 18, 'bold'))
        bc2.delete(0, END)
        bc2.insert(0, b2)
    elif flop[3] == 'd':
        bc2.config(fg='blue', font=('Arial', 18, 'bold'))
        bc2.delete(0, END)
        bc2.insert(0, b2)
    elif flop[3] == 'h':
        bc2.config(fg='red', font=('Arial', 18, 'bold'))
        bc2.delete(0, END)
        bc2.insert(0, b2)
    else:
        bc2.config(font=('Arial', 18, 'bold'))
        bc2.delete(0, END)
        bc2.insert(0, b2)

    if flop[5] == 'c':
        bc3.config(fg='green', font=('Arial', 18, 'bold'))
        bc3.delete(0, END)
        bc3.insert(0, b3)
    elif flop[5] == 'd':
        bc3.config(fg='blue', font=('Arial', 18, 'bold'))
        bc3.delete(0, END)
        bc3.insert(0, b3)
    elif flop[5] == 'h':
        bc3.config(fg='red', font=('Arial', 18, 'bold'))
        bc3.delete(0, END)
        bc3.insert(0, b3)
    else:
        bc3.config(font=('Arial', 18, 'bold'))
        bc3.delete(0, END)
        bc3.insert(0, b3)
    bets=bet_setting_1.get()
    pot=pot_display.get()
    potstore= float(bet_setting_1.get()) + float(bet_setting_2.get()) + float(bet_setting_3.get()) + float(bet_setting_4.get()) + float(bet_setting_5.get()) + float(bet_setting_6.get())
    print(potstore)
    stack_setting_1.insert(0, float(stack_setting_1.get()) - float(bet_setting_1.get()))
    stack_setting_2.insert(0, float(stack_setting_2.get()) - float(bet_setting_2.get()))
    stack_setting_3.insert(0, float(stack_setting_3.get()) - float(bet_setting_3.get()))
    stack_setting_4.insert(0, float(stack_setting_4.get()) - float(bet_setting_4.get()))
    stack_setting_5.insert(0, float(stack_setting_5.get()) - float(bet_setting_5.get()))
    stack_setting_6.insert(0, float(stack_setting_6.get()) - float(bet_setting_6.get()))
    pot_display.delete(0, END)
    pot_display.insert(0, str(pot))
    bet_display_1.delete(0, END)
    bet_display_2.delete(0, END)
    bet_display_3.delete(0, END)
    bet_display_4.delete(0, END)
    bet_display_5.delete(0, END)
    bet_display_6.delete(0, END)
    bet_setting_1.delete(0, END)
    bet_setting_2.delete(0, END)
    bet_setting_3.delete(0, END)
    bet_setting_4.delete(0, END)
    bet_setting_5.delete(0, END)
    bet_setting_6.delete(0, END)
    bet_setting_1.insert(0, 0)
    bet_setting_2.insert(0, 0)
    bet_setting_3.insert(0, 0)
    bet_setting_4.insert(0, 0)
    bet_setting_5.insert(0, 0)
    bet_setting_6.insert(0, 0)


def set_turn():
    global potstore
    turn = turni.get()
    t1 = turn[0]
    if turn[1] == 'c':
        bc4.config(fg='green', font=('Arial', 18, 'bold'))
        bc4.delete(0, END)
        bc4.insert(0, t1)
    elif turn[1] == 'd':
        bc4.config(fg='blue', font=('Arial', 18, 'bold'))
        bc4.delete(0, END)
        bc4.insert(0, t1)
    elif turn[1] == 'h':
        bc4.config(fg='red', font=('Arial', 18, 'bold'))
        bc4.delete(0, END)
        bc4.insert(0, t1)
    else:
        bc4.config(font=('Arial', 18, 'bold'))
        bc4.delete(0, END)
        bc4.insert(0, t1)
    potstore = potstore + float(bet_setting_1.get()) + float(bet_setting_2.get()) + float(bet_setting_3.get()) + float(bet_setting_4.get()) + float(bet_setting_5.get()) + float(bet_setting_6.get())
    s1 = float(stack_setting_1.get())
    s2 = float(stack_setting_2.get())
    s3 = float(stack_setting_3.get())
    s4 = float(stack_setting_4.get())
    s5 = float(stack_setting_5.get())
    s6 = float(stack_setting_6.get())
    stack_setting_1.delete(0, END)
    stack_setting_2.delete(0, END)
    stack_setting_3.delete(0, END)
    stack_setting_4.delete(0, END)
    stack_setting_5.delete(0, END)
    stack_setting_6.delete(0, END)
    stack_setting_1.insert(0, s1 - float(bet_setting_1.get()))
    stack_setting_2.insert(0, s2 - float(bet_setting_2.get()))
    stack_setting_3.insert(0, s3 - float(bet_setting_3.get()))
    stack_setting_4.insert(0, s4 - float(bet_setting_4.get()))
    stack_setting_5.insert(0, s5 - float(bet_setting_5.get()))
    stack_setting_6.insert(0, s6 - float(bet_setting_6.get()))
    bet_display_1.delete(0, END)
    bet_display_2.delete(0, END)
    bet_display_3.delete(0, END)
    bet_display_4.delete(0, END)
    bet_display_5.delete(0, END)
    bet_display_6.delete(0, END)
    bet_setting_1.delete(0, END)
    bet_setting_2.delete(0, END)
    bet_setting_3.delete(0, END)
    bet_setting_4.delete(0, END)
    bet_setting_5.delete(0, END)
    bet_setting_6.delete(0, END)
    bet_setting_1.insert(0, 0)
    bet_setting_2.insert(0, 0)
    bet_setting_3.insert(0, 0)
    bet_setting_4.insert(0, 0)
    bet_setting_5.insert(0, 0)
    bet_setting_6.insert(0, 0)

def set_river():
    river = riveri.get()
    global potstore
    r1 = river[0]
    if river[1] == 'c':
        bc5.config(fg='green', font=('Arial', 18, 'bold'))
        bc5.delete(0, END)
        bc5.insert(0, r1)
    elif river[1] == 'd':
        bc5.config(fg='blue', font=('Arial', 18, 'bold'))
        bc5.delete(0, END)
        bc5.insert(0, r1)
    elif river[1] == 'h':
        bc5.config(fg='red', font=('Arial', 18, 'bold'))
        bc5.delete(0, END)
        bc5.insert(0, r1)
    else:
        bc5.config(font=('Arial', 18, 'bold'))
        bc5.delete(0, END)
        bc5.insert(0, r1)
    potstore = potstore + float(bet_setting_1.get()) + float(bet_setting_2.get()) + float(bet_setting_3.get()) + float(
        bet_setting_4.get()) + float(bet_setting_5.get()) + float(bet_setting_6.get())
    s1 = float(stack_setting_1.get())
    s2 = float(stack_setting_2.get())
    s3 = float(stack_setting_3.get())
    s4 = float(stack_setting_4.get())
    s5 = float(stack_setting_5.get())
    s6 = float(stack_setting_6.get())
    stack_setting_1.delete(0, END)
    stack_setting_2.delete(0, END)
    stack_setting_3.delete(0, END)
    stack_setting_4.delete(0, END)
    stack_setting_5.delete(0, END)
    stack_setting_6.delete(0, END)
    stack_setting_1.insert(0, s1 - float(bet_setting_1.get()))
    stack_setting_2.insert(0, s2 - float(bet_setting_2.get()))
    stack_setting_3.insert(0, s3 - float(bet_setting_3.get()))
    stack_setting_4.insert(0, s4 - float(bet_setting_4.get()))
    stack_setting_5.insert(0, s5 - float(bet_setting_5.get()))
    stack_setting_6.insert(0, s6 - float(bet_setting_6.get()))
    bet_display_1.delete(0, END)
    bet_display_2.delete(0, END)
    bet_display_3.delete(0, END)
    bet_display_4.delete(0, END)
    bet_display_5.delete(0, END)
    bet_display_6.delete(0, END)
    bet_setting_1.delete(0, END)
    bet_setting_2.delete(0, END)
    bet_setting_3.delete(0, END)
    bet_setting_4.delete(0, END)
    bet_setting_5.delete(0, END)
    bet_setting_6.delete(0, END)
    bet_setting_1.insert(0, 0)
    bet_setting_2.insert(0, 0)
    bet_setting_3.insert(0, 0)
    bet_setting_4.insert(0, 0)
    bet_setting_5.insert(0, 0)
    bet_setting_6.insert(0, 0)

def set_holes():
    holes = holecardsi.get()
    h1 = holes[0]
    h2 = holes[2]
    if holes[1] == 'c':
        hc1.config(fg='green', font=('Arial', 18, 'bold'))
        hc1.delete(0, END)
        hc1.insert(0, h1)
    elif holes[1] == 'd':
        hc1.config(fg='blue', font=('Arial', 18, 'bold'))
        hc1.delete(0, END)
        hc1.insert(0, h1)
    elif holes[1] == 'h':
        hc1.config(fg='red', font=('Arial', 18, 'bold'))
        hc1.delete(0, END)
        hc1.insert(0, h1)
    else:
        hc1.config(font=('Arial', 18, 'bold'))
        hc1.delete(0, END)
        hc1.insert(0, h1)

    if holes[3] == 'c':
        hc2.config(fg='green', font=('Arial', 18, 'bold'))
        hc2.delete(0, END)
        hc2.insert(0, h2)
    elif holes[3] == 'd':
        hc2.config(fg='blue', font=('Arial', 18, 'bold'))
        hc2.delete(0, END)
        hc2.insert(0, h2)
    elif holes[3] == 'h':
        hc2.config(fg='red', font=('Arial', 18, 'bold'))
        hc2.delete(0, END)
        hc2.insert(0, h2)
    else:
        hc2.config(font=('Arial', 18, 'bold'))
        hc2.delete(0, END)
        hc2.insert(0, h2)

    return None
global a
a=0
global b
b=0

def clickbu1():
    if bu1.config('bg')[-1]!='red':
        bu1.config(bg='red')
    else:
        bu1.config(bg='light gray')

def clickbu2():
    if bu2.config('bg')[-1]!='red':
        bu2.config(bg='red')
    else:
        bu2.config(bg='light gray')

def clickbu3():
    if bu3.config('bg')[-1]!='red':
        bu3.config(bg='red')
    else:
        bu3.config(bg='light gray')

def clickbu4():
    if bu4.config('bg')[-1]!='red':
        bu4.config(bg='red')
    else:
        bu4.config(bg='light gray')

def clickbu5():
    if bu5.config('bg')[-1]!='red':
        bu5.config(bg='red')
    else:
        bu5.config(bg='light gray')

def clickbu6():
    if bu6.config('bg')[-1]!='red':
        bu6.config(bg='red')
    else:
        bu6.config(bg='light gray')

def clickback1():
    if back1.config('bg')[-1]=='orange':
        back1.config(bg='light gray')
    else:
        back1.config(bg='orange')

def clickback2():
    if back2.config('bg')[-1]=='orange':
        back2.config(bg='light gray')
    else:
        back2.config(bg='orange')

def clickback3():
    if back3.config('bg')[-1]=='orange':
        back3.config(bg='light gray')
    else:
        back3.config(bg='orange')

def clickback4():
    if back4.config('bg')[-1]=='orange':
        back4.config(bg='light gray')
    else:
        back4.config(bg='orange')

def clickback5():
    if back5.config('bg')[-1]=='orange':
        back5.config(bg='light gray')
    else:
        back5.config(bg='orange')

def clickback6():
    if back6.config('bg')[-1]=='orange':
        back6.config(bg='light gray')
    else:
        back6.config(bg='orange')

def set_stacks():
    stacks = float(setstacksentry.get())
    stack_setting_1.delete(0, END)
    stack_setting_2.delete(0, END)
    stack_setting_3.delete(0, END)
    stack_setting_4.delete(0, END)
    stack_setting_5.delete(0, END)
    stack_setting_6.delete(0, END)
    stack_setting_1.insert(0, stacks)
    stack_setting_2.insert(0, stacks)
    stack_setting_3.insert(0, stacks)
    stack_setting_4.insert(0, stacks)
    stack_setting_5.insert(0, stacks)
    stack_setting_6.insert(0, stacks)


def clear():
    global potstore
    potstore = 0
    stack_setting_1.delete(0, END)
    stack_setting_2.delete(0, END)
    stack_setting_3.delete(0, END)
    stack_setting_4.delete(0, END)
    stack_setting_5.delete(0, END)
    stack_setting_6.delete(0, END)
    stack_setting_1.insert(0, 1000)
    stack_setting_2.insert(0, 1000)
    stack_setting_3.insert(0, 1000)
    stack_setting_4.insert(0, 1000)
    stack_setting_5.insert(0, 1000)
    stack_setting_6.insert(0, 1000)
    bet_setting_1.delete(0, END)
    bet_setting_2.delete(0, END)
    bet_setting_3.delete(0, END)
    bet_setting_4.delete(0, END)
    bet_setting_5.delete(0, END)
    bet_setting_6.delete(0, END)
    bet_setting_1.insert(0, 0)
    bet_setting_2.insert(0, 0)
    bet_setting_3.insert(0, 0)
    bet_setting_4.insert(0, 0)
    bet_setting_5.insert(0, 0)
    bet_setting_6.insert(0, 0)
    bet_display_1.delete(0, END)
    bet_display_2.delete(0, END)
    bet_display_3.delete(0, END)
    bet_display_4.delete(0, END)
    bet_display_5.delete(0, END)
    bet_display_6.delete(0, END)
    stack_display_1.delete(0, END)
    stack_display_2.delete(0, END)
    stack_display_3.delete(0, END)
    stack_display_4.delete(0, END)
    stack_display_5.delete(0, END)
    stack_display_6.delete(0, END)
    bc1.delete(0, END)
    bc2.delete(0, END)
    bc3.delete(0, END)
    bc4.delete(0, END)
    bc5.delete(0, END)
    hc1.delete(0, END)
    hc2.delete(0, END)
    pot_display.delete(0, END)
    pot_display.insert(0, 0)
    back1.config(bg=('orange'))
    back2.config(bg=('orange'))
    back3.config(bg=('orange'))
    back4.config(bg=('orange'))
    back5.config(bg=('orange'))
    back6.config(bg=('orange'))
    back6.config(bg=('orange'))
    bu1.config(bg='red')
    pot_display.delete(0, END)

def BUvsBBSRP():
    bet_setting_2.delete(0, END)
    bet_setting_2.insert(0, '5')
    bet_setting_3.delete(0, END)
    bet_setting_3.insert(0, '10')
    holecardsi.delete(0, END)
    holecardsi.insert(0,'AcTc')
    flopi.delete(0, END)
    flopi.insert(0,"2c4dJh")
    bu1.config(bg='red')




bet_display_1 = Entry(root, width=10)
bet_display_1 = Entry(root, width=10)
bet_display_2 = Entry(root, width=10)
bet_display_3 = Entry(root, width=10)
bet_display_4 = Entry(root, width=10)
bet_display_5 = Entry(root, width=10)
bet_display_6 = Entry(root, width=10)


bet_setting_1 = Entry(root, width=10)
bet_setting_1.insert(0, 0)
bet_setting_2 = Entry(root, width=10)
bet_setting_2.insert(0, 0)
bet_setting_3 = Entry(root, width=10)
bet_setting_3.insert(0, 0)
bet_setting_4 = Entry(root, width=10)
bet_setting_4.insert(0, 0)
bet_setting_5 = Entry(root, width=10)
bet_setting_5.insert(0, 0)
bet_setting_6 = Entry(root, width=10)
bet_setting_6.insert(0, 0)

pot_display = Entry(root, width=18, bd=0)
pot_display.config(bg="grey", fg="white")

stack_setting_1 = Entry(root, width=10)
stack_setting_1.insert(0, 1000)
stack_setting_2 = Entry(root, width=10)
stack_setting_2.insert(0, 1000)
stack_setting_3 = Entry(root, width=10)
stack_setting_3.insert(0, 1000)
stack_setting_4 = Entry(root, width=10)
stack_setting_4.insert(0, 1000)
stack_setting_5 = Entry(root, width=10)
stack_setting_5.insert(0, 1000)
stack_setting_6 = Entry(root, width=10)
stack_setting_6.insert(0, 1000)


stack_display_1 = Entry(root, width=10, bd=0)
stack_display_2 = Entry(root, width=10, bd=0)
stack_display_3 = Entry(root, width=10, bd=0)
stack_display_4 = Entry(root, width=10, bd=0)
stack_display_5 = Entry(root, width=10, bd=0)
stack_display_6 = Entry(root, width=10, bd=0)

stack_display_1.config(bg="grey", fg="white", font="bold")
stack_display_2.config(bg="grey", fg="white", font="bold")
stack_display_3.config(bg="grey", fg="white", font="bold")
stack_display_4.config(bg="grey", fg="white", font="bold")
stack_display_5.config(bg="grey", fg="white", font="bold")
stack_display_6.config(bg="grey", fg="white", font="bold")
bet_display_1.config(bg="grey", fg="white", font="bold", bd=0)
bet_display_2.config(bg="grey", fg="white", font="bold", bd=0)
bet_display_3.config(bg="grey", fg="white", font="bold", bd=0)
bet_display_4.config(bg="grey", fg="white", font="bold", bd=0)
bet_display_5.config(bg="grey", fg="white", font="bold", bd=0)
bet_display_6.config(bg="grey", fg="white", font="bold", bd=0)




Button(root, text='Set bets', command = bet_set).place(x=740,y=496)
Button(root, text='set_flop', command= set_flop).place(x=880,y=530)
Button(root, text='set_turn', command= set_turn).place(x=880,y=555)
Button(root, text='set_river', command= set_river).place(x=880,y=580)
Button(root, text='set_holes', command= set_holes).place(x=880,y=496)
Button(root, text='CLEAR', command=clear).place(x=1,y=1)


player1label = Label(root, text='Hero', font=(None,17)).place(x=150,y=450)
player2label = Label(root, text='player2', font=(None,17)).place(x=250,y=450)
player3label = Label(root, text='player3', font=(None,17)).place(x=350,y=450)
player4label = Label(root, text='player4', font=(None,17)).place(x=450,y=450)
player5label = Label(root, text='player5', font=(None,17)).place(x=550,y=450)
player6label = Label(root, text='player6', font=(None,17)).place(x=650,y=450)

stacklabel = Label(root, text='stack', font=(None,17)).place(x=20,y=490)
betlabel = Label(root, text='bet', font=(None,17)).place(x=20,y=530)

stack_setting_1.place(x=150, y=490)
stack_setting_2.place(x=250, y=490)
stack_setting_3.place(x=350, y=490)
stack_setting_4.place(x=450, y=490)
stack_setting_5.place(x=550, y=490)
stack_setting_6.place(x=650, y=490)

bet_setting_1.place(x=150, y=530)
bet_setting_2.place(x=250, y=530)
bet_setting_3.place(x=350, y=530)
bet_setting_4.place(x=450, y=530)
bet_setting_5.place(x=550, y=530)
bet_setting_6.place(x=650, y=530)

stack_display_1.place(x=420, y=400)
stack_display_2.place(x=100,y=380)
stack_display_3.place(x=100,y=50)
stack_display_4.place(x=400,y=50)
stack_display_5.place(x=800,y=50)
stack_display_6.place(x=800,y=380)

bet_display_1.place(x=400, y=300)
bet_display_2.place(x=250, y=300)
bet_display_3.place(x=250, y=120)
bet_display_4.place(x=400, y=120)
bet_display_5.place(x=650, y=120)
bet_display_6.place(x=616, y=300)

pot_display.place(x=420, y=180)

bu1 = Button(root, text='', command = None)
bu1.config(command=clickbu1)


bu2 = Button(root, text='', command = None)
bu2.config(command=clickbu2)


bu3 = Button(root, text='', command = None)
bu3.config(command=clickbu3)


bu4 = Button(root, text='', command = None)
bu4.config(command=clickbu4)


bu5 = Button(root, text='', command = None)
bu5.config(command=clickbu5)


bu6 = Button(root, text='', command = None)
bu6.config(command=clickbu6)

bu1.place(x=381,y=335)
bu2.place(x=100,y=410)
bu3.place(x=100,y=80)
bu4.place(x=400,y=80)
bu5.place(x=800,y=80)
bu6.place(x=800,y=410)

back1 = Button(root, text='', command = None, bg='orange')
back1.config(command=clickback1)


back2 = Button(root, text='', command = None, bg='orange')
back2.config(command=clickback2)

setstacksentry = Entry(root, width=10)
setstacksentry.place(x=150, y=570)
setstacksentry.insert(0,1000)
setstacksbutton = Button(root, text='set stacks', command = set_stacks, font=(None,17)).place(x=20, y=570)



back3 = Button(root, text='', command = None, bg='orange')
back3.config(command=clickback3)


back4 = Button(root, text='', command = None, bg='orange')
back4.config(command=clickback4)


back5 = Button(root, text='', command = None, bg='orange')
back5.config(command=clickback5)


back6 = Button(root, text='', command = None, bg='orange')
back6.config(command=clickback6)


back2.place(x=100,y=350)
back3.place(x=100,y=20)
back4.place(x=400,y=20)
back5.place(x=800,y=20)
back6.place(x=800,y=350)

hc1 = Entry(root, width=2, font="Arial 18")
hc2 = Entry(root, width=2, font="Arial 18")

bc1 = Entry(root, width=2, font="Arial 18")
bc2 = Entry(root, width=2, font="Arial 18")
bc3 = Entry(root, width=2, font="Arial 18")
bc4 = Entry(root, width=2, font="Arial 18")
bc5 = Entry(root, width=2, font="Arial 18")

holecardsi = Entry(root, width=4)
flopi = Entry(root, width = 10)
turni = Entry(root, width=2)
riveri = Entry(root, width =2)

hc1.place(x=423,y=350)
hc2.place(x=483,y=350)

bc1.place(x=329,y=215)
bc2.place(x=391,y=215)
bc3.place(x=454,y=215)
bc4.place(x=517,y=215)
bc5.place(x=578,y=215)



holecardsi.place (x=800,y=500)
flopi.place(x=800,y=520)
turni.place(x=800,y=545)
riveri.place(x=800,y=570)
baton = Button(root, text='BUVBB', command=BUvsBBSRP)
baton.place(x=0,y=100)



root.mainloop()









