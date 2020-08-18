from tkinter import *
from tkinter import messagebox
import tkinter.messagebox as tkMessageBox


from firebase import firebase
firebase = firebase.FirebaseApplication('https://flight-planer-crescentsat.firebaseio.com')


def about_us():
    messagebox.showinfo("About us", "Developed by Naveen Maheswaran & Harishankar (CrescentSAT) \nCopyright@ Space kidz India")


def stop():
    print("lal")

def fire_data():
    checkA11 = firebase.get('/checklist', '/check1')
    checkA12 = firebase.get('/checklist', '/check2')
    checkA13 = firebase.get('/checklist', '/check3')
    checkB11 = firebase.get('/checklist', '/check4')
    checkB12 = firebase.get('/checklist', '/check5')
    checkB13 = firebase.get('/checklist', '/check6')
    checkC11 = firebase.get('/checklist', '/check7')
    checkC12 = firebase.get('/checklist', '/check8')
    checkC13 = firebase.get('/checklist', '/check9')
    if checkA11 == 1:
        A11Entry.configure(bg="light green")
    else:
        A11Entry.configure(bg="Red")
        ###
    if checkA12 == 1:
        A12Entry.configure(bg="light green")
    else:
        A12Entry.configure(bg="Red")
        ###
    if checkA13 == 1:
        A13Entry.configure(bg="light green")
    else:
        A13Entry.configure(bg="Red")
        ###
    if checkB11 == 1:
        B11Entry.configure(bg="light green")
    else:
        B11Entry.configure(bg="Red")
    ##
    if checkB12 == 1:
        B12Entry.configure(bg="light green")
    else:
        B12Entry.configure(bg="Red")
    ##
    if checkB13 == 1:
        B13Entry.configure(bg="light green")
    else:
        B13Entry.configure(bg="Red")
        ##
    if checkC11 == 1:
        C11Entry.configure(bg="light green")
    else:
        C11Entry.configure(bg="Red")
    ##
    if checkC12 == 1:
        C12Entry.configure(bg="light green")
    else:
        C12Entry.configure(bg="Red")
    ##
    if checkC13 == 1:
        C13Entry.configure(bg="light green")
    else:
        C13Entry.configure(bg="Red")

    if checkA11 == 1 and checkA12 == 1 and checkA12 == 1 and checkB11 == 1 and checkB12 ==1 and checkB13 == 1 and checkC11 == 1 and checkC12 == 1 and checkC13 == 1:
        messagebox.showinfo("Launch Info","Launch Authorised.")


    root.after(2000, fire_data)




root = Tk()
root.geometry("1920x1080")
root.title("CrescentSAT Ground Station")
root.configure(background='black')

menubar = Menu(root)
root.configure(menu=menubar)
submenu_help = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=submenu_help)
submenu_help.add_command(label="About", command=about_us)

tops = Frame(root, width=1600, height=50, bg="black")
titleLabel = Label(tops, font=('Segoe UI',50, 'bold'), text="FLIGHT CHECKLIST", fg="steel blue", bg="black", bd="10", anchor='w')
titleLabel.grid(row=0,column=0)
tops.pack(side=TOP)

entries = Frame(root, width=1550, height=600, bg="black", relief=SUNKEN)

a11 = "One"
a12=IntVar()
a13=IntVar()
b11=IntVar()
b12=IntVar()
b13=IntVar()
c11=IntVar()
c12=IntVar()
c13=IntVar()


A11Entry = Button(entries, font=('Segoe UI', 20, 'bold'), text=a11, bd=10, bg="red", justify='center', relief="sunken",width = 18)
A11Entry.grid(row=0, column=0,padx=70, pady=40)

A12Entry = Button(entries, font=('Segoe UI', 20, 'bold'), text=a12, bd=10, bg="red", justify='center', relief="sunken",width = 18)
A12Entry.grid(row=0, column=1,padx=70, pady=40)

A13Entry = Button(entries, font=('Segoe UI', 20, 'bold'), text=a13, bd=10, bg="red", justify='center', relief="sunken",width = 18)
A13Entry.grid(row=0, column=2,padx=70, pady=40)


B11Entry = Button(entries, font=('Segoe UI', 20, 'bold'), text=b11, bd=10, bg="red", justify='center', relief="sunken",width = 18)
B11Entry.grid(row=1, column=0,padx=70, pady=40)

B12Entry = Button(entries, font=('Segoe UI', 20, 'bold'), text=b12, bd=10, bg="red", justify='center', relief="sunken",width = 18)
B12Entry.grid(row=1, column=1,padx=70, pady=40)

B13Entry = Button(entries, font=('Segoe UI', 20, 'bold'), text=b13, bd=10, bg="red", justify='center', relief="sunken",width = 18)
B13Entry.grid(row=1, column=2,padx=70, pady=40)


C11Entry = Button(entries, font=('Segoe UI', 20, 'bold'), text=c11, bd=10, bg="red", justify='center', relief="sunken",width = 18)
C11Entry.grid(row=2, column=0,padx=70, pady=40)

C12Entry = Button(entries, font=('Segoe UI', 20, 'bold'), text=c12, bd=10, bg="red", justify='center', relief="sunken",width = 18)
C12Entry.grid(row=2, column=1,padx=70, pady=40)

C13Entry = Button(entries, font=('Segoe UI', 20, 'bold'), text=c13, bd=10, bg="red", justify='center', relief="sunken",width = 18)
C13Entry.grid(row=2, column=2,padx=70, pady=40)


entries.pack(side=LEFT)


root.after(2000,fire_data)

root.mainloop()