from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox

class Login:

    def __init__(self,login_page):
        self.login_page=login_page
        self.login_page.geometry("1920x1080+0+0")
        self.login_page.title("Login")

        #__ variables___
        self.var_emailid = StringVar()
        self.var_password = StringVar()

        # Image at the right side

        left_image = Image.open(r"C:\Users\Amith\Desktop\New folder\Photo\wallpaperflare.com_wallpaper.jpg")
        left_image=left_image.resize((1920,1080), Image.Resampling.LANCZOS)
        self.left_bg_image = ImageTk.PhotoImage(left_image)

        bg_image = Label(self.login_page,image=self.left_bg_image)
        bg_image.place(x=0, y=0, width=1920, height=1080)

        # image at right side
        right_image = Image.open(r"C:\Users\Amith\Desktop\New folder\Photo\login.jpg")
        right_image=right_image.resize((600,600), Image.Resampling.LANCZOS)
        self.right_bg__image= ImageTk.PhotoImage(right_image)

        bg_image_right=Label(bg_image, image =self.right_bg__image)
        bg_image_right.place(x=100, y=100, width=600, height=600)

        text_name = Label(bg_image_right, text="Log_in to your Account", font=("times new roman", 30, "bold"), relief="flat", fg="#6007cb", bg="white")
        text_name.place(x=40, y=50, width=500, height=50)

        email_enter = Entry(bg_image, text="Enter email id",textvariable=self.var_emailid,font = ("times new roman", 15, "bold"),relief="flat",bg="#e8e0df", fg="#898385", justify="left")
        email_enter.insert(0, "Enter Email ID")
        email_enter.pack()
        email_enter.place(x=1050, y=200, width=200, height=30)

        password_text = Entry(bg_image, text="Password",textvariable=self.var_password ,font=("times new roman", 15, "bold"), relief="flat", justify="left",bg="#e8e0df", fg="#898385")
        password_text.insert(0,"Enter Password")
        password_text.pack()
        password_text.place(x=1150, y=300, width=200, height=30)

        login_button = Button(bg_image, text="Log_in", font=("times new roman", 15, "bold"), fg="white",bg="#6007cb",cursor="hand2", relief="flat", command=self.login_message)
        login_button.place(x=1200, y=400, width=200, height=30)

    def login_message(self):
        if self.var_emailid.get()=="Enter Email ID" and self.var_password.get()=="Enter Password":
            messagebox.showwarning("Warning", "Please enter all the details", parent=self.login_page)

        elif self.var_emailid.get()=="Enter Email ID" or "":
            messagebox.showwarning("Warning", "Please enter email id", parent=self.login_page)

        elif self.var_password.get()=="Enter Password" or "":
            messagebox.showwarning("Warning", "Please enter password", parent=self.login_page)

        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="amithMYSQL@1999", database="talentplace")
                my_cur = conn.cursor()
                my_cur.execute("insert into login values(%s, %s)", (self.var_emailid.get(), self.var_password.get()))

                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Logged in successful", parent=self.login_page)
            except Exception as es:
                messagebox.showerror("Error", f"Logged in failed sue to{es}", parent=self.login_page)
                                           

if __name__ == "__main__":
    login_page = Tk()
    obj = Login(login_page)
    login_page=mainloop()

