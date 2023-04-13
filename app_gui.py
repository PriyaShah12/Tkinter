from tkinter import *

root = Tk()
root.geometry("800x800")
def getvals():
    print("Recording data-----")
    with open ("records.txt", "w") as f:
        f.write(f"{namevalue.get(), agevalue.get(), gendervalue.get()}")
Label(root, text="Welcome to Facts GUI", background="Grey", foreground="black").grid(row=0, column=3)
name = Label(root, text="Name")
age = Label(root, text="Age")
gender = Label(root, text="Gender")

name.grid(row=1, column=3)
age.grid(row=2, column=3)
gender.grid(row=3, column=3)

namevalue = StringVar()
agevalue = IntVar()
gendervalue = StringVar()
bankaccount = IntVar()

nameentry = Entry(root, textvariable=namevalue)
ageentry = Entry(root, textvariable=agevalue)
genderentry = Entry(root, textvariable=gendervalue)

nameentry.grid(row=1, column=5)
ageentry.grid(row=2, column=5)
genderentry.grid(row=3, column=5)

bankentry = Checkbutton(text="DO you have saving account in abcbank?", variable=bankaccount)
bankentry.grid(row=4, column=5)

Button(text="Submit Form", command= getvals).grid(row=5, column=5)
root.mainloop()

