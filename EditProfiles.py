from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Editprofiles:

    def __init__(self, editprofile_page):

        self.editprofile_page=editprofile_page
        self.editprofile_page.geometry("1920x1080+0+0")
        self.editprofile_page.title("EditProfile")

        # ____left frame_____
        left_frame  =Frame(self.editprofile_page, bd=2,bg="#6007cb")
        left_frame.place(x=10,y=0, width=180,height=900)

        # buttons on left frame
        b1 = Button(left_frame, text="Personal Details", font=("times new roman", 13, "bold"), relief="flat", bg="white", fg="Black", anchor="center", cursor="hand2")
        b1.place(x=0, y=100, width=175, height=30)

        b2 = Button(left_frame, text="Settings", font=("times new roman", 13, "bold"), relief="flat", bg="white", fg="black", anchor="center", cursor="hand2")
        b2.place(x=0, y=140, width=175, height=30)


        right_frame  =Frame(self.editprofile_page, bd=2,bg="blue")
        right_frame.place(x=1350,y=0, width=200,height=900)

        details_frame = LabelFrame(self.editprofile_page, text="Personal Details", font=("times new roman", 15), bd=1)
        details_frame.place(x=400, y=100, width=800, height=650)






if __name__ == "__main__":
    editprofile = Tk()
    obj=Editprofiles(editprofile)
    editprofile = mainloop()


