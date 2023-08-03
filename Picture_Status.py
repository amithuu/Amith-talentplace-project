from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector


class Picture_status:

    def __init__(self, picture_page):
        self.picture_page = picture_page
        self.picture_page.geometry("1920x1080+0+0")
        self.picture_page.title(" Edit Picture")


        #____________________________________________________#

        # ____left frame_____
        details_frame  =Frame(self.picture_page, bd=2,bg="#6007cb")
        details_frame.place(x=10,y=0, width=180,height=900)

        # buttons on left frame
        b1 = Button(details_frame, text="Dashboard", font=("times new roman", 13), relief="flat", bg="white", fg="Black", anchor="center", cursor="hand2")
        b1.place(x=3, y=10, width=170, height=30)

        b2 = Button(details_frame, text="Edit Profiles", font=("times new roman", 13), relief="flat", bg="white", fg="Black", anchor="center", cursor="hand2")
        b2.place(x=3, y=60, width=170, height=30)

        b3 = Button(details_frame, text="My profile", font=("times new roman", 13), relief="flat", bg="white", fg="black", anchor="center", cursor="hand2")
        b3.place(x=3, y=110, width=170, height=30)


        b4 = Button(details_frame, text="Settings", font=("times new roman", 13), relief="flat", bg="white", fg="black", anchor="center", cursor="hand2")
        b4.place(x=3, y=160, width=170, height=30)

        b5 = Button(details_frame, text="Personal Assessment", font=("times new roman", 13), relief="flat", bg="white", fg="Black", anchor="center", cursor="hand2")
        b5.place(x=3, y=210, width=170, height=30)

        b6 = Button(details_frame, text="Resumes", font=("times new roman", 13), relief="flat", bg="white", fg="black", anchor="center", cursor="hand2")
        b6.place(x=3, y=260, width=170, height=30)

        b7 = Button(details_frame, text="Membership", font=("times new roman", 13), relief="flat", bg="white", fg="Black", anchor="center", cursor="hand2")
        b7.place(x=3, y=310, width=170, height=30)

        b8 = Button(details_frame, text="Notification", font=("times new roman", 13), relief="flat", bg="white", fg="black", anchor="center", cursor="hand2")
        b8.place(x=3, y=360, width=170, height=30)
        
        #_______________________________________#

        personaldetails_frame = LabelFrame(self.picture_page,text="Upload Picture", font=("times new roman", 15), bd=1.5, bg="#F9F9F9")
        personaldetails_frame.place(x=300, y=50, width=1100, height=700)

        #_________________________#

        

if __name__=="__main__":
    picture = Tk()
    obj =Picture_status(picture)
    picture = mainloop()
