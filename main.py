# Todo: Need to make this Page scroll until we have as many adds, tomorrow[30/07/2023] need to add scroll bar to the self.root

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from sign_up import Sign_up

class TalentPlace:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("TalentPlace.ai")

        # yscroll = ttk.Scrollbar(self.root, orient=VERTICAL)
        # xscroll = ttk.Scrollbar(self.root, orient=HORIZONTAL)

        # xscroll.pack(side="bottom", fill=X)
        # yscroll.pack(side="right", fill=Y)

        # self.root.pack(fill=BOTH, expand=1)

        #scroll page we will learn it later..
        # scroll_page = ttk.Scrollbar(self.root, orient=VERTICAL)

        img = Image.open(
            r"C:\Users\Amith\Desktop\New folder\Photo\bgimage.png")
        img = img.resize((1550, 500), Image.Resampling.LANCZOS)
        self.image = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.image)
        f_lbl.place(x=0, y=0, width=1550, height=500)

        img1 = Image.open(
            r"C:\Users\Amith\Desktop\New folder\Photo\belowbg.jpg")
        img1 = img1.resize((500, 250), Image.Resampling.LANCZOS)
        self.image1 = ImageTk.PhotoImage(img1)

        # company name link :todo: link need to make it.
        company_name = Label(self.root, text="Talentplace.ai", font=(
            "times new roman", 15, "bold"), background="#6007cb", foreground="white")
        company_name.place(x=10, y=5, width=120, height=30)

        # headings
        title_heading = Label(f_lbl, text="Intelligent Resume To Skyrocket Your Career", font=(
            "times new roman", 25, "bold"), background="#6007cb", foreground="White")
        title_heading.place(x=450, y=100, width=700, height=50)

        para = Label(f_lbl, text="For every working professional doing any kind of work", font=(
            "times new roman", 18, "bold"), background="#6007cb", foreground="white")
        para.place(x=490, y=160, width=600, height=30)

        # Button get started
        b1 = Button(self.root, text="Get Started", font=(
            "times new roman", 20, "bold"), foreground="#6007cb", background="White", cursor="hand2", command=self.Sign_Up)
        b1.place(x=700, y=250, width=180, height=35)

        # down page
        s_lbl = Label(self.root, image=self.image1)
        s_lbl.place(x=950, y=530, width=500, height=250)

        para1 = Label(self.root, text="Download as a", font=(
            "times new roman", 35, "bold"), foreground="black", anchor="w")
        para1.place(x=170, y=530, width=300, height=40)

        para1 = Label(self.root, text="resume or share the", font=(
            "times new roman", 35, "bold"), foreground="black", anchor="w")
        para1.place(x=165, y=575, width=400, height=40)

        para1 = Label(self.root, text="link online for quick", font=(
            "times new roman", 35, "bold"), foreground="black", anchor="w")
        para1.place(x=160, y=620, width=460, height=45)

        para1 = Label(self.root, text="access and more", font=(
            "times new roman", 35, "bold"), foreground="black", anchor="w")
        para1.place(x=165, y=665, width=400, height=40)

        para1 = Label(self.root, text="engagement", font=(
            "times new roman", 35, "bold"), foreground="black", anchor="w")
        para1.place(x=165, y=705, width=400, height=55)

    "============Functions============"

    def Sign_Up(self):
        self.signup_window  = Toplevel(self.root)
        self.signup = Sign_up(self.signup_window)


if __name__ == "__main__":

    root = Tk()
    "-> creating an object of root for Tk()"
    obj = TalentPlace(root)
    root = mainloop()
