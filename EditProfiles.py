from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Editprofiles:

    def __init__(self, editprofile_page):

        self.editprofile_page=editprofile_page
        self.editprofile_page.geometry("1920x1080+0+0")
        self.editprofile_page.title("EditProfile")


        page_frame  =LabelFrame(self.editprofile_page, bd=5)
        page_frame.place(x=10,y=10, width=500,height=700)

        yscroll = ttk.Scrollbar(page_frame, orient=VERTICAL)
        xscroll = ttk.Scrollbar(page_frame, orient=HORIZONTAL)

        xscroll.pack(side="bottom", fill=X)
        yscroll.pack(side="right", fill=Y)





if __name__ == "__main__":
    editprofile = Tk()
    obj=Editprofiles(editprofile)
    editprofile = mainloop()


