from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from PD import PersonalDetail

class EditProfile:

    def __init__(self, editprofile_page):

        self.editprofile_page = editprofile_page
        self.editprofile_page.geometry("1920x1080+0+0")
        self.editprofile_page.title("EditProfile")

        # ____________________________________________________#

        # ____left frame_____
        details_frame = Frame(self.editprofile_page, bd=2, bg="#6007cb")
        details_frame.place(x=10, y=0, width=180, height=900)

        # buttons on left frame
        b1 = Button(details_frame, text="Dashboard", font=("times new roman", 13),
                    relief="flat", bg="white", fg="Black", anchor="center", cursor="hand2")
        b1.place(x=3, y=10, width=170, height=30)

        b2 = Button(details_frame, text="Edit Profiles", font=(
            "times new roman", 13), relief="flat", bg="white", fg="Black", anchor="center", cursor="hand2")
        b2.place(x=3, y=60, width=170, height=30)

        b3 = Button(details_frame, text="My profile", font=("times new roman", 13),
                    relief="flat", bg="white", fg="black", anchor="center", cursor="hand2")
        b3.place(x=3, y=110, width=170, height=30)

        b4 = Button(details_frame, text="Settings", font=("times new roman", 13),
                    relief="flat", bg="white", fg="black", anchor="center", cursor="hand2")
        b4.place(x=3, y=160, width=170, height=30)

        b5 = Button(details_frame, text="Personal Assessment", font=("times new roman", 13),
                    relief="flat", bg="white", fg="Black", anchor="center", cursor="hand2")
        b5.place(x=3, y=210, width=170, height=30)

        b6 = Button(details_frame, text="Resumes", font=("times new roman", 13),
                    relief="flat", bg="white", fg="black", anchor="center", cursor="hand2")
        b6.place(x=3, y=260, width=170, height=30)

        b7 = Button(details_frame, text="Membership", font=("times new roman", 13),
                    relief="flat", bg="white", fg="Black", anchor="center", cursor="hand2")
        b7.place(x=3, y=310, width=170, height=30)

        b8 = Button(details_frame, text="Notification", font=("times new roman", 13),
                    relief="flat", bg="white", fg="black", anchor="center", cursor="hand2")
        b8.place(x=3, y=360, width=170, height=30)

        # __________________________________________________________________________#

        right_frame = Frame(self.editprofile_page, bd=2, bg="blue")
        right_frame.place(x=1350, y=0, width=180, height=900)

        # ___________________________________________________________________________#

        details_frame = LabelFrame(self.editprofile_page, font=(
            "times new roman", 15), bd=1.5, bg="#F9F9F9")
        details_frame.place(x=300, y=100, width=900, height=620)

        # Buttons inside Frame

        b1 = Button(details_frame, text="Personal Details",command=self.Redirect_personaldetails, font=("times new roman", 13, "bold"),
                    relief="groove", bd=1, bg="#FFFFFF", fg="Black", anchor="center", cursor="hand2")
        b1.place(x=20, y=20, width=420, height=50)

        b2 = Button(details_frame, text="Picture/Status", font=("times new roman", 13, "bold"),
                    relief="groove", bd=1, bg="#FFFFFF", fg="black", anchor="center", cursor="hand2")
        b2.place(x=460, y=20, width=420, height=50)

        b3 = Button(details_frame, text="Experience", font=("times new roman", 13, "bold"),
                    relief="groove", bd=1, bg="#FFFFFF", fg="Black", anchor="center", cursor="hand2")
        b3.place(x=20, y=80, width=420, height=50)

        b4 = Button(details_frame, text="Project", font=("times new roman", 13, "bold"),
                    relief="groove", bd=1, bg="#FFFFFF", fg="black", anchor="center", cursor="hand2")
        b4.place(x=460, y=80, width=420, height=50)

        b5 = Button(details_frame, text="Education", font=("times new roman", 13, "bold"),
                    relief="groove", bd=1, bg="#FFFFFF", fg="Black", anchor="center", cursor="hand2")
        b5.place(x=20, y=140, width=420, height=50)

        b6 = Button(details_frame, text="Certificate", font=("times new roman", 13, "bold"),
                    relief="groove", bd=1, bg="#FFFFFF", fg="black", anchor="center", cursor="hand2")
        b6.place(x=460, y=140, width=420, height=50)

        b7 = Button(details_frame, text="Publication", font=("times new roman", 13, "bold"),
                    relief="groove", bd=1, bg="#FFFFFF", fg="Black", anchor="center", cursor="hand2")
        b7.place(x=20, y=200, width=420, height=50)

        b8 = Button(details_frame, text="Patent", font=("times new roman", 13, "bold"),
                    relief="groove", bd=1, bg="#FFFFFF", fg="black", anchor="center", cursor="hand2")
        b8.place(x=460, y=200, width=420, height=50)

        b9 = Button(details_frame, text="Portfolio", font=("times new roman", 13, "bold"),
                    relief="groove", bd=1, bg="#FFFFFF", fg="Black", anchor="center", cursor="hand2")
        b9.place(x=20, y=260, width=420, height=50)

        b10 = Button(details_frame, text="Voluntary Roles", font=("times new roman", 13, "bold"),
                     relief="groove", bd=1, bg="#FFFFFF", fg="black", anchor="center", cursor="hand2")
        b10.place(x=460, y=260, width=420, height=50)

        b11 = Button(details_frame, text="Honor and Awards", font=("times new roman", 13, "bold"),
                     relief="groove", bd=1, bg="#FFFFFF", fg="Black", anchor="center", cursor="hand2")
        b11.place(x=20, y=320, width=420, height=50)

        b12 = Button(details_frame, text="Causes", font=("times new roman", 13, "bold"),
                     relief="groove", bd=1, bg="#FFFFFF", fg="black", anchor="center", cursor="hand2")
        b12.place(x=460, y=320, width=420, height=50)

        b13 = Button(details_frame, text="Hobbies", font=("times new roman", 13, "bold"),
                     relief="groove", bd=1, bg="#FFFFFF", fg="Black", anchor="center", cursor="hand2")
        b13.place(x=20, y=380, width=420, height=50)

        b14 = Button(details_frame, text="Languages", font=("times new roman", 13, "bold"),
                     relief="groove", bd=1, bg="#FFFFFF", fg="black", anchor="center", cursor="hand2")
        b14.place(x=460, y=380, width=420, height=50)

        b15 = Button(details_frame, text="Cognitive Skills", font=("times new roman", 13, "bold"),
                     relief="groove", bd=1, bg="#FFFFFF", fg="Black", anchor="center", cursor="hand2")
        b15.place(x=20, y=440, width=420, height=50)

        b16 = Button(details_frame, text="Career Summary", font=("times new roman", 13, "bold"),
                     relief="groove", bd=1, bg="#FFFFFF", fg="black", anchor="center", cursor="hand2")
        b16.place(x=460, y=440, width=420, height=50)

        b17 = Button(details_frame, text="Top Skills", font=("times new roman", 13, "bold"),
                     relief="groove", bd=1, bg="#FFFFFF", fg="Black", anchor="center", cursor="hand2")
        b17.place(x=20, y=500, width=420, height=50)

        b2 = Button(details_frame, text="Save", font=("times new roman",
                    10, "bold"), relief="groove", bd=1, bg="#8024F5", fg="#FFFFFF", anchor="center", cursor="hand2")
        b2.place(x=400, y=570, width=100, height=30)

    # ___________Function edit profile_______

    def Redirect_personaldetails(self):
        self.personaldetails_window =Toplevel(self.editprofile_page)
        self.personaldetails = PersonalDetail(self.personaldetails_window)


if __name__ == "__main__":
    editprofile = Tk()
    obj = EditProfile(editprofile)
    editprofile = mainloop()
