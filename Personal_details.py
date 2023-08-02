from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox
from EditProfiles import Editprofiles

class Personal_details:

    def __init__(self, peronaldetails_page):
        self.personaldetails_page=peronaldetails_page
        self.personaldetails_page.geometry("1920x1080+0+0")
        self.personaldetails_page.title("Personal Details")

        # Variables
        self.var_firstname=StringVar()
        self.var_lastname=StringVar()
        self.var_location=StringVar()
        self.var_gender=StringVar()
        self.var_currency=StringVar()
        self.var_dob= StringVar()
        self.var_experiencemonth=StringVar()
        self.var_experienceyear=StringVar()
        self.var_githublink=StringVar()
        self.var_linkedinlink=StringVar()
        self.var_twitterlink=StringVar()

        #____________________________________________________#

        # ____left frame_____
        details_frame  =Frame(self.personaldetails_page, bd=2,bg="#6007cb")
        details_frame.place(x=10,y=0, width=180,height=900)

        # buttons on left frame
        b1 = Button(details_frame, text="Dashboard", font=("times new roman", 13), relief="flat", bg="white", fg="Black", anchor="center", cursor="hand2")
        b1.place(x=3, y=10, width=170, height=30)

        b2 = Button(details_frame, text="Edit Profiles",command=self.Editprofile, font=("times new roman", 13), relief="flat", bg="white", fg="Black", anchor="center", cursor="hand2")
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

        personaldetails_frame = LabelFrame(self.personaldetails_page,text="Personal Details", font=("times new roman", 15), bd=1.5, bg="#F9F9F9")
        personaldetails_frame.place(x=300, y=50, width=1100, height=700)

        #_________________________#

        first_name = Label(personaldetails_frame, text="First Name", font=("times new roman", 15), bg="#F9F9F9", fg="black", anchor="w")
        first_name.place(x=30, y=10, width=150, height=30)
        
        firstname = Entry(personaldetails_frame,textvariable=self.var_firstname, bg="#FFFFFF",bd=2, relief="ridge", width=50)
        firstname.place(x=30, y=40, width=400, height=30)

        last_name = Label(personaldetails_frame, text="Last Name", font=("times new roman", 15), bg="#F9F9F9", fg="black", anchor="w")
        last_name.place(x=560, y=10, width=150, height=30)
        
        lastname = Entry(personaldetails_frame,textvariable=self.var_lastname, bg="#FFFFFF",bd=2, relief="ridge", width=50)
        lastname.place(x=560, y=40, width=400, height=30)

        gender = Label(personaldetails_frame, text="Gender", font=("times new roman", 15), bg="#F9F9F9", fg="black",anchor="w")
        gender.place(x=30, y=90, width=150, height=30)
        
        gender_dropdown = ttk.Combobox(personaldetails_frame, width=50, textvariable=self.var_gender)
        gender_dropdown["values"]=("Male","Female", "Not to Mention")
        gender_dropdown.place(x=30, y=120, width=400, height=30)

        currency = Label(personaldetails_frame, text="Currency", font=("times new roman", 15), bg="#F9F9F9", fg="black", anchor="w")
        currency.place(x=560, y=90, width=150, height=30)
        
        currency_dropdown = ttk.Combobox(personaldetails_frame, width=50,font=("times new roman", 15), textvariable=self.var_currency)
        currency_dropdown["values"]=("inr", "usd")
        currency_dropdown.place(x=560, y=120, width=400, height=30)

        location = Label(personaldetails_frame, text="Location", font=("times new roman", 15), anchor="w",bg="#F9F9F9", fg="black")
        location.place(x=30, y=170, width=100, height=30)

        loc_combobox = ttk.Combobox(personaldetails_frame,font=("times new roman", 15), width=20, textvariable=self.var_location)
        loc_combobox["values"] =("Enter Location", "Bangalore", "Delhi", "Kashmir", "Pune", "Belgaum")
        loc_combobox.current(0)
        loc_combobox.place(x=30,y=200, width=930, height=30)

        date_of_birth =Label(personaldetails_frame, text="Date of Birth",font=("times new roman", 15), anchor="w",bg="#F9F9F9", fg="black")
        date_of_birth.place(x=30, y=250, width=150, height=30)

        dob = Entry(personaldetails_frame, font=("times new roman", 15), bd=2, relief="ridge", textvariable=self.var_dob)
        dob.place(x=30, y=280, width=400, height=30)

        experience_month = Label(personaldetails_frame, text="Experience Month", font=("times new roman", 15), anchor="w",bg="#F9F9F9", fg="black")
        experience_month.place(x=30, y=330, width=150, height=30)

        experiencemonth_combobox = ttk.Combobox(personaldetails_frame,font=("times new roman", 15), width=20, textvariable=self.var_experiencemonth)
        experiencemonth_combobox["values"] =("Select Month","January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
        experiencemonth_combobox.current(0)
        experiencemonth_combobox.place(x=30,y=360, width=400, height=30)

        experience_year =Label(personaldetails_frame, text="Year",font=("times new roman", 15), anchor="w",bg="#F9F9F9", fg="black")
        experience_year.place(x=560, y=330, width=150, height=30)

        experience_year = Entry(personaldetails_frame, font=("times new roman", 15), bd=2, relief="ridge", textvariable=self.var_experienceyear)
        experience_year.place(x=560, y=360, width=400, height=30)

        fresher_checkbox = ttk.Checkbutton(personaldetails_frame, text=" Iam Fresher", state="disabled")
        fresher_checkbox.place(x=30, y=400, width=150, height=30)

        social_media_link =Label(personaldetails_frame, text="Social Media Link",font=("times new roman", 15), anchor="w",bg="#F9F9F9", fg="black")
        social_media_link.place(x=30, y=440, width=150, height=30)

        social_media_github = Entry(personaldetails_frame,font=("times new roman", 15, ), bd=2, relief="ridge", textvariable=self.var_githublink)
        social_media_github.insert(END, "Github Link")
        social_media_github.place(x=30, y=480, width=400, height=30)

        social_media_linkedin = Entry(personaldetails_frame,font=("times new roman", 15, ), bd=2, relief="ridge", textvariable=self.var_linkedinlink)
        social_media_linkedin.insert(END, "Linkedin Link")
        social_media_linkedin.place(x=560, y=480, width=400, height=30)

        social_media_twitter = Entry(personaldetails_frame,font=("times new roman", 15, ), bd=2, relief="ridge", textvariable=self.var_twitterlink)
        social_media_twitter.insert(END, "Twitter Link")
        social_media_twitter.place(x=30, y=530, width=400, height=30)

        save = Button(personaldetails_frame, text="Save",command=self.save_details, font=("times new roman", 15, "bold"), bg="#8024F5", fg="#FFFFFE")
        save.place(x=480, y=600,width=80,height=40)

    #_____Function Edit profile____
    def Editprofile(self):
        self.editprofile_window=Toplevel(self.personaldetails_page)
        self.editprofile=Editprofiles(self.editprofile_window)

    def save_details(self):
        if self.var_firstname.get()=="" and self.var_lastname.get()=="" and self.var_location.get()=="Enter Location" and self.var_gender.get()=="" and self.var_currency.get()=="" and self.var_dob.get()=="" and self.var_experiencemonth.get()=="Select Month" and self.var_experienceyear.get()=="" and self.var_githublink.get()=="Github Link" and self.var_linkedinlink.get()=="Linkedin Link" and self.var_twitterlink.get()=="Twitter Link":
            messagebox.showwarning("Info", "Please Enter all the Required** Fields", parent=self.personaldetails_page)

        elif self.var_firstname.get()=="" or self.var_lastname.get()=="" or self.var_location.get()=="Enter Location" or self.var_dob.get()=="" or self.var_experiencemonth.get()=="Select Month" or self.var_experienceyear.get()=="" or self.var_githublink.get()=="Github Link" or self.var_linkedinlink.get()=="Linkedin Link" or self.var_twitterlink.get()=="Twitter Link" or self.var_dob.get()=="" or self.var_currency.get()=="":
            messagebox.showwarning("Info", "Please Enter the  Field Left**", parent=self.personaldetails_page)

        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="amithMYSQL@1999", database="talentplace")
                my_cur=conn.cursor()
                my_cur.execute("insert into personaldetails values (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s)", 
                                                                            (self.var_firstname.get(),
                                                                            self.var_lastname.get(),
                                                                            self.var_location.get(),
                                                                            self.var_gender.get(),
                                                                            self.var_currency.get(),
                                                                            self.var_dob.get(),
                                                                            self.var_experiencemonth.get(),
                                                                            self.var_experienceyear.get(),
                                                                            self.var_githublink.get(),
                                                                            self.var_linkedinlink.get(),
                                                                            self.var_twitterlink.get()
                                                                                 ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Personal Details Saved", parent=self.personaldetails_page)

            except Exception as es:
                messagebox.showerror("Error", f"Personal Details not saved due to {es}", parent=self.personaldetails_page)

    

if __name__ == "__main__":
    personaldetails = Tk()
    obj = Personal_details(personaldetails)
    personaldetails = mainloop()