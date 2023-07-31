from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Sign_up:


    def __init__(self, signup_page):
        self.signup_page = signup_page
        self.signup_page.geometry("1920x1080+0+0")
        self.signup_page.title("Sign_Up")

        # Side image

        side_image = Image.open( r"C:\Users\Amith\Desktop\New folder\Photo\img2.jpg")
        side_image = side_image.resize((700,1080), Image.Resampling.LANCZOS)
        self.side_image = ImageTk.PhotoImage(side_image)

        side_img = Label(self.signup_page, image = self.side_image)
        side_img.place(x=0, y=0, width=700, height=1080)
        
        # log-in:
        login_button = Button(self.signup_page, text="Log-in", font=("times new roman", 15,"bold", "underline"), foreground="#6007cb", cursor="hand2", relief="flat")
        login_button.place(x=1420, y=0, width=85, height=40)

        # frame for Sing-Up

        signup_frame = LabelFrame(self.signup_page,bd=1, relief="flat", text="Join our Community", font=("times new roman", 15,"bold" ,"underline"), background="white", foreground="#6007cb")
        signup_frame.place(x=900, y=200, width=500, height=500)

        # Location label/Combo box:
        # location = Label(signup_frame, text="Location", font=("times new roman", 15), anchor="w")
        # location.grid(row=0, column=0)

        # loc_combobox = ttk.Combobox(signup_frame, font=("times new roman", 15), width=20)
        # loc_combobox["values"] =("Enter Location", "Bangalore", "Delhi", "Kashmir", "Pune", "Belgaum")
        # loc_combobox.current(0)
        # loc_combobox.grid(row=0,column=3)

        """As there are so many dis-advantages using GRID so i am using manually for all the field, x and y ratio thing."""

        # INSIDE FRAME ALL THE DETAILS

        firstname = Label(signup_frame, text="First Name", font=("times new roman", 15), anchor="w",background="white")
        firstname.place(x=20, y=10, width=100, height=15)

        firstname_textbox = Entry(signup_frame, font=("times new roman", 15),bd=2)
        firstname_textbox.place(x=20, y=40, width=170, height=30)

        lastname = Label(signup_frame, text="Last Name", font=("times new roman", 15), anchor="w",background="white")
        lastname.place(x=300, y=10, width=100, height=15)

        lastname_textbox = Entry(signup_frame, font=("times new roman", 15),bd=2)
        lastname_textbox.place(x=300, y=40, width=170, height=30)

        Email_id = Label(signup_frame, text="Email", font=("times new roman", 15), anchor="w",background="white")
        Email_id.place(x=20, y=110, width=100, height=15)

        email_id_textbox = Entry(signup_frame, font=("times new roman", 15),bd=2)
        email_id_textbox.place(x=20, y=140, width=250, height=30)

        location = Label(signup_frame, text="Location", font=("times new roman", 15), anchor="w",background="white")
        location.place(x=20, y=210, width=100, height=15)

        loc_combobox = ttk.Combobox(signup_frame, font=("times new roman", 15), width=20)
        loc_combobox["values"] =("Enter Location", "Bangalore", "Delhi", "Kashmir", "Pune", "Belgaum")
        loc_combobox.current(0)
        loc_combobox.place(x=20,y=240, width=170, height=30)

        Password = Label(signup_frame, text="Password", font=("times new roman", 15), anchor="w",background="white")
        Password.place(x=20, y=310, width=100, height=15)

        password_textbox = Entry(signup_frame, font=("times new roman", 15), bd=2)
        password_textbox.place(x=20, y=335, width=250, height=30)

        # SignUp:
        signup_button = Button(signup_frame, text="Sign-Up", font=("times new roman", 15,"bold"), background="#6007cb", cursor="hand2", relief="flat", foreground="white")
        signup_button.place(x=190, y=410, width=150, height=40)

        # SignUp:
        signup_button = Button(signup_frame, text="Sign-Up", font=("times new roman", 15,"bold"), background="#6007cb", cursor="hand2", relief="flat", foreground="white")
        signup_button.place(x=190, y=410, width=150, height=40)

        

if __name__ == "__main__":
    signup_page = Tk()
    obj = Sign_up(signup_page)
    signup_page = mainloop()

