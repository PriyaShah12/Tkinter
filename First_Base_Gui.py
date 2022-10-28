from tkinter import *
import tkinter as tk
import tkinter.messagebox as tmsg
from all_functions import Jsondata_Class_Page


class My_Gui(Tk):

    def __init__(self, title_of_page, icon_for_page):

        self.button=""

        super().__init__()
        self.geometry("800x600")
        self.minsize(500, 500)
        self.maxsize(1200, 1200)
        self.title(title_of_page)
        self.wm_iconbitmap(icon_for_page)

    def add_statusBar(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusbar = Label(self, textvariable=self.var, relief=SUNKEN, anchor="w")
        self.statusbar.pack(side=BOTTOM, fill=X)

    def add_menubar(self):
        self.mainmenu = Menu(self, tearoff=0)
        self.config(menu=self.mainmenu)
        return self.mainmenu

    def myfunc(self):
        print("menudone")

    def add_main_menu_options(self, menu_name):
        self.sub_menu = Menu(self.mainmenu, tearoff=0)
        # self.mainmenu.add_cascade(label=menu_name, menu=self.sub_menu)
        return self.sub_menu

    def add_label(self,fg_color,bg_color,  text_for_label, anchor_side):
        my_label = Label(self, fg=fg_color, text=text_for_label, bg=bg_color)
        my_label.pack(anchor=anchor_side)

    def add_button(self,fg_color, text_for_button ):
        my_button = Button(self, fg=fg_color, text=text_for_button)
        my_button.pack(side=TOP)
        my_button.bind("<Button-1>", self.clickme)

    def add_enter_box(self):
        self.scvalue = StringVar()
        self.scvalue.set("")
        self.screen = Entry(self, textvariable=self.scvalue, font="lucida 10 bold")
        self.screen.pack(fill=X, pady=2, padx=2, ipadx=2)

    def clickme(self, event):
        global scvalue
        text = Jsondata_Class_Page.get_fact_text()
        print("*******************", text, "**********************")
        if text != "":
            self.scvalue.set(text)
            self.screen.update()

    def add_text_box_with_scroll_bar(self):
        text = Text(self, font= "lucida 17", foreground="black", background="orange", width=30, height=10) #, height=8, width=40)
        scroll = Scrollbar(self)
        text.configure(yscrollcommand=scroll.set)
        text.pack(side=LEFT)
        scroll.config(command=text.yview)
        scroll.pack(side=RIGHT, fill=Y)

    def insert_text_in_text_box(self, insert_text):
        text = Text(self)
        text.insert(END, insert_text)
        text.pack()


    def add_radio_button(self):
        var = StringVar()
        var.set("Radio")  # will uncheck all radio button
        Label(self, text="Which is your favourite language?", pady=15, font="lucida 9 bold", justify=LEFT).pack(
            anchor="w")

        radio = Radiobutton(self, text="Python", padx=3, variable=var, value="Python").pack(anchor="w")
        radio = Radiobutton(self, text="Java", padx=3, variable=var, value="Java").pack(anchor="w")
        radio = Radiobutton(self, text=".NET", padx=3, variable=var, value=".NET").pack(anchor="w")
        radio = Radiobutton(self, text="C++", padx=3, variable=var, value="C++").pack(anchor="w")

        def get_language():
            tmsg.showinfo("Language", f"The Language you selected {var.get()},is very easy language")

        Button(text="Know about language you selected!", command=get_language, pady=2).pack(anchor="w")

    def create_file_menu_for_drop_down(self):
        self.sub_menu = self.add_main_menu_options("File")
        self.sub_menu.add_command(label="New Project")
        self.sub_menu.add_command(label="Save")
        self.sub_menu.add_command(label="Delete")
        self.sub_menu.add_separator()
        self.sub_menu.add_command(label="Open file")
        self.sub_menu.add_command(label="Close file")#, command=myfuncformenu)
        self.config(menu=self.mainmenu)
        self.mainmenu.add_cascade(label="File", menu=self.sub_menu)

    def create_edit_menu_for_drop_down(self):
        self.sub_menu = self.add_main_menu_options("File")
        self.sub_menu.add_command(label="Cut")
        self.sub_menu.add_command(label="Copy")
        self.sub_menu.add_command(label="Paste")
        self.sub_menu.add_separator()
        self.sub_menu.add_command(label="Redo")
        self.sub_menu.add_command(label="Close file")#, command=myfuncformenu)
        self.config(menu=self.mainmenu)
        self.mainmenu.add_cascade(label="Edit", menu=self.sub_menu)

    def create_help_menu_for_drop_down(self):
        self.sub_menu = self.add_main_menu_options("Help")
        self.sub_menu.add_command(label="Submit Feedback", command=self.myfuncforhelpmenu)
        self.sub_menu.add_command(label="Help", command=self.my_retry_pop_up)
        self.sub_menu.add_separator()
        self.sub_menu.add_command(label="Tip of the day", command=self.help_msg)
        self.config(menu=self.mainmenu)
        self.mainmenu.add_cascade(label="Help", menu=self.sub_menu)

    def myfuncforhelpmenu(self):
        value = tmsg.askquestion("Experience feedback",
                                 "Was your experience using this GUI good?")  # exp 1st value will be label of popup
        if value == "yes":
            msg = "Great!!"
        else:
            msg = "Let us know how we can improve."
        tmsg.showinfo("Experience", msg)

    def my_retry_pop_up(self):
        value = tmsg.askretrycancel("Do you have any questions?", "We cant help you with this request")
        if value:  # means true
            msg = "Sorry, try again!"
        else:
            msg = "Thanks!!"
        tmsg.showinfo("Help", msg)

    def help_msg(self):
        tmsg.showinfo("Tip", "Keep learning to be successful")

if __name__ == "__main__":
  window = My_Gui("My First Gui", "./icon1.ico")
  window.add_statusBar()
  window.add_menubar()
  window.add_label("red","white", "Click Below button for facts!", "n")
  window.add_button("red","Click Me!")
  window.add_enter_box()
  window.add_text_box_with_scroll_bar()
  # window.insert_text_in_text_box("Welcome to first GUI by Priya!")
  window.add_radio_button()
  window.create_file_menu_for_drop_down()
  window.create_edit_menu_for_drop_down()
  window.create_help_menu_for_drop_down()


  window.mainloop()



