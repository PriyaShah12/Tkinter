import sys
from tkinter import *
# from PIL import Image, ImageTk
# from PIL.Image import *
import tkinter.messagebox as tmsg
from random import choice, seed

from all_functions import Jsondata_Class_Page

root = Tk()
root.geometry("1000x800")
root.minsize(500, 500)
root.maxsize(1200, 1200)
root.title("My first GUI")

lab = Label(text="Hello from Priya", background="white", foreground="red", padx=8, pady=8, font=("ariel",8,"bold"), borderwidth=3, relief=SUNKEN)
lab.pack(side=LEFT, anchor="nw")

frame1 = Frame(root, borderwidth=5, background="grey", relief=SUNKEN)
frame1.pack(side=TOP, fill=X)# expand=True
l1= Label(frame1, text="Page to view facts", font="Helvetica 8 bold", foreground="blue")
l1.pack()

#todo: view facts on GUI
#
# frame2 = Frame(root, borderwidth=5, background="grey", relief=SUNKEN)
# frame2.pack(side=LEFT, fill=Y)
#
# l2= Label(frame2, text="Click below button for facts")
# l2.pack()
# button1 = Button(frame2, fg= "red", text="Click Me", command=Jsondata_Class_Page.get_fact_text)
# button1.pack(side=TOP)


def func1():
    pass

# photo = PhotoImage(file="hello-image.png")
# label = Label(image=photo).pack()

# #todo:for jpeg image , install pillow
# image = Image.open("hello-image.png")
# image = image.resize((225,265), Resampling.LANCZOS)  #Image.ANTIALIAS)
# kitty_image = ImageTk.PhotoImage(image)
# label = Label(root, image=kitty_image, anchor="ne").pack(side=RIGHT)


# frame3 = Frame(root, borderwidth=5, background="red", relief=SUNKEN)
# frame3.pack(side=RIGHT, fill=Y) #anchor="nw"

# user = Label(root, text= "Username")
# pswd = Label(root, text = "Password")
# user.grid(row=1)
# pswd.grid(column=2)
#
# uservalue = StringVar()
# pswdvalue = StringVar()
#
# userentry = Entry(root, textvariable=uservalue)
# pswdentry = Entry(root, textvariable=pswdvalue)
#
# userentry.grid()
# pswdentry.grid()
def myfuncformenu():
    print("Menu created")

def myfuncforeditmenu():
    print("Menu edited")

def myfuncforhelpmenu():
    value = tmsg.askquestion("Experience feedback", "Was your experience using this GUI good?") #exp 1st value will be label of popup
    if value == "yes":
        msg = "Great!!"
    else:
        msg = "Let us know how we can improve"
    tmsg.showinfo("Experience", msg)

#todo: retry msg

def my_retry_pop_up():
    value = tmsg.askretrycancel("Do you have any questions?", "We cant help you with this request")
    if value: #means true
        msg = "Sorry, try again!"
    else:
        msg = "Thanks!!"
    tmsg.showinfo("help", msg)



#todo: to create menu without drop down
# mymenu = Menu(root)
# mymenu.add_command(label= "file", command=myfuncformenu)
# mymenu.add_command(label= "Exit", command=quit)
# root.config(menu=mymenu)

#todo: to create menu with drop down
mainmenu = Menu(root)

m1 = Menu(mainmenu, tearoff=0) #clear ---- line from dropdown
m1.add_command(label= "New Project", command=myfuncformenu)
m1.add_command(label= "Save", command=myfuncformenu)
m1.add_command(label= "Delete", command=myfuncformenu)
m1.add_separator()
m1.add_command(label= "Open file", command=myfuncformenu)
m1.add_command(label= "Close file", command=myfuncformenu)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)

#2nd
m2 = Menu(mainmenu, tearoff=0) #clear ---- line from dropdown
m2.add_command(label= "Cut", command=myfuncforeditmenu)
m2.add_command(label= "Copy", command=myfuncforeditmenu)
m2.add_command(label= "Paste", command=myfuncforeditmenu)
m2.add_separator()
m2.add_command(label= "Redo", command=myfuncforeditmenu)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit", menu=m2)

#3rd
m3 = Menu(mainmenu, tearoff=0) #clear ---- line from dropdown
m3.add_command(label= "Submit Feedback", command=myfuncforhelpmenu)
m3.add_command(label= "Help", command=my_retry_pop_up)
m3.add_command(label= "find", command=myfuncforhelpmenu)
m3.add_separator()
m3.add_command(label= "Tip of the day", command=myfuncforhelpmenu)

root.config(menu=mainmenu)
mainmenu.add_cascade(label="Help", menu=m3)

mainmenu.add_command(label="Exit", command=sys.exit)

#todo: select your age

l3= Label(root,fg= "Black", text="Select your age").pack(anchor="e")
my_slider = Scale(root, from_=0, to=100, orient=HORIZONTAL) # tickinterval=5 gives interval of 5
my_slider.set(5) # will start from 5
my_slider.pack(anchor="e")

def get_age_fact():
    tmsg.showinfo("Age facts", f"You look beautiful at age {my_slider.get()}")

Button(root, text="Know about your age!!", pady=10, command=get_age_fact).pack(anchor="e")

#todo: radio button

var = StringVar()
var.set("Radio") # will uncheck all radio button
Label(root, text="Which is your favourite language?",pady=15,  font="lucida 9 bold", justify=LEFT).pack(anchor="w")

radio = Radiobutton(root, text="Python", padx=3, variable=var, value="Python").pack(anchor="w")
radio = Radiobutton(root, text="Java", padx=3, variable=var, value="Java").pack(anchor="w")
radio = Radiobutton(root, text=".NET", padx=3, variable=var, value=".NET").pack(anchor="w")
radio = Radiobutton(root, text="C++", padx=3, variable=var, value="C++").pack(anchor="w")

def get_language():
    tmsg.showinfo("Language", f"The Language you selected {var.get()}is a very easy language")

Button(text="Know about language you selected!", command=get_language, pady=2).pack(anchor="w")

#todo: listbox

# lbx = Listbox(root)
# lbx.pack()
# lbx.insert(END, "First item of list box")
# seed(1)
# weather_list = ["Summer", "Winter", "Spring", "Autumn", "Fall"]
# def get_weather():
#         value = choice(weather_list)
#         lbx.insert(ACTIVE, f"Season-{value}")
#
# Button(text="Know today's weather", command=get_weather).pack()

#todo: adding scrollbar to list

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
lstbx = Listbox(root, yscrollcommand = scrollbar.set)
# seed(1)
weather_list = ["Summer", "Winter", "Spring", "Autumn", "Fall"]
def get_weather():
        value = choice(weather_list)
        lstbx.insert(ACTIVE, f"Season-{value}")

lstbx.pack(fill= BOTH, pady=1)
scrollbar.config(command=lstbx.yview())
Button(text="Know today's weather", command=get_weather).pack()

#todo:statusbar

statusvar = StringVar()
statusvar.set("Ready")
sbar = Label(root, textvariable=statusvar, relief=SUNKEN)
sbar.pack(side=LEFT, fill=Y)

def upload():
    statusvar.set("Busy")
    sbar.update()
    import time
    time.sleep(3)
    statusvar.set("Ready Now.....")
stats_bar_button = Button(root, text="Upload", command=upload).pack()

#todo: change Icon
# root.wm_iconbitmap("icon1.ico")

#check weidth and height of a window

width = root.winfo_width()
height = root.winfo_height()

def sizeCheck():
    tmsg.showinfo("Window Size", f"the size of window is {width} X {height}")
but_to_check_sixe_of_window = Button(frame1, text="Click to check size of window", command=sizeCheck, anchor="e").pack()

#*****************************************************************************************
scvalue = StringVar()
scvalue.set("")
screen = Entry(frame1, textvariable=scvalue, font = "lucida 10 bold")
screen.pack(fill=X, pady=2, padx=2, ipadx=2)


frame2 = Frame(frame1, borderwidth=5, background="grey", relief=SUNKEN)
frame2.pack(side=LEFT, fill=Y)

l2= Label(frame2, text="Click below button for facts", background="red")
l2.pack()
button1 = Button(frame2, fg= "red", text="Click Me")
button1.pack(side=TOP)
def click(event):
    global scvalue
    text = Jsondata_Class_Page.get_facts_text()
    print("*******************", text, "**********************")
    if text != "":
        scvalue.set(text)
        screen.update()
button1.bind("<Button-1>", click)

#todo:add text area

TextArea = Text(root, font="lucida 7")
TextArea.pack(fill=BOTH)


#todo: adding scroll bar to the page

scroll = Scrollbar(TextArea)
scroll.pack(side=LEFT, fill=Y)
scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=scroll.set)

#********************************************************************************************
root.mainloop()




