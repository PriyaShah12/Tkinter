from tkinter import ttk
from tkinter import *
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
        self.mainmenubar = Menu(self, tearoff=0)
        self.config(menu=self.mainmenubar)
        return self.mainmenubar

    def myfunc(self):
        print("menudone")

    # def add_label_to_main_menu(self, menu_option_name, inner_labels):
    #     menu_created = Menu(self.mainmenubar, tearoff=0)
    #     for inner_label_name in inner_labels:
    #         menu_created.add_command(label=inner_label_name, command=self.myfunc)
    #     self.config(menu=self.mainmenubar)
    #     self.mainmenubar.add_cascade(label=menu_option_name, menu=menu_created)
    #
    def add_main_menu_options(self, menu_name):
        self.menu_created = Menu(self.mainmenubar)
        self.mainmenubar.add_cascade(label=menu_name, menu=self.menu_created)
        return self.menu_created

    #
    # def add_sub_menu_option_to_main_menu(self, top_menu_name, inner_option_name): #method_to_be_called):
    #     menu_created = self.add_main_menu_options(top_menu_name)
    #     if menu_created == top_menu_name:
    #         print("*********************")
    #         top_menu_name.add_command(label=inner_option_name) #command=method_to_be_called)
    #         self.config(menu=self.mainmenubar)

    def add_label(self,fg_color,bg_color,  text_for_label, anchor_side):
        l = Label(self, fg=fg_color, text=text_for_label, bg=bg_color).pack(anchor=anchor_side)

    def add_button(self,fg_color, text_for_button ):
        my_button = Button(self, fg=fg_color, text=text_for_button)
        my_button.pack(side=TOP)
        print("#################################")
        print(my_button)
        # return self.my_button
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





if __name__ == "__main__":
  window = My_Gui("First Gui", "./icon1.ico")
  window.add_statusBar()
  window.add_menubar()
  window.add_main_menu_options("File")
  window.add_main_menu_options("Edit")
  window.add_main_menu_options("View")
  # window.add_sub_menu_option_to_main_menu("File", "OpenFile")
  window.add_label("red","white", "Click Below button for facts!", "n")
  window.add_button("red","Click Me!")
  window.add_enter_box()
  # window.clickme()
  # window.bind("<Button-1>", clickme())


  window.mainloop()



