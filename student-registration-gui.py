import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class studentRegistration:

    def __init__ (self,window):
        #self.window=window

        self.label=tk.Label(
        window,
        text="Student Registration Form",
        font=("Montserrat",19),
        #justify="center"
        bg="pink"
        )
        self.label.pack(pady=30)

        self.fill_frame=tk.Frame(
            window
            )
        self.fill_frame.pack()

        self.name_label=tk.Label(
            self.fill_frame,
            text="Name: ",
            font=("Poppins",14)
        )
        self.name_label.grid(row=0, column=0, padx=(0,50),pady=4)

        self.name_entry=tk.Entry(
            self.fill_frame,
            font=("Poppins",12),
        )
        self.name_entry.grid(row=0, column=1 )

        self.roll_label=tk.Label(
            self.fill_frame,
            text="Roll no: ",
            font=("Poppins",14)
        )
        self.roll_label.grid(row=1, column=0, padx=(0,50),pady=4)

        self.roll_entry=tk.Entry(
            self.fill_frame,
            font=("Poppins",12)
        )
        self.roll_entry.grid(row=1, column=1,)

        self.age_label=tk.Label(
            self.fill_frame,
            text="age: ",
            font=("poppins",14),
            justify="left"
        )
        self.age_label.grid(row=2, column=0, padx=(0,50),pady=4)

        self.age_entry=tk.Entry(
            self.fill_frame,
            font=("poppins",14)
        )
        self.age_entry.grid(row=2, column=1)

        self.course_label=tk.Label(
            self.fill_frame,
            text="course:",
            font=("poppins",14)
        )
        self.course_label.grid(row=3, column=0, padx=(0,50),pady=4)

        self.course_menu=ttk.Combobox(
            self.fill_frame,
            font=("poppins",12),
            values=["BA","BBA","BCA","BTECH"]
        )
        self.course_menu.grid(row=3,column=1)

        self.gender_label=tk.Label(
            self.fill_frame,
            text="gender: ",
            font=("poppins",14)
        )
        self.gender_label.grid(row=4, column=0, padx=(0,50),pady=4)

        self.gender=tk.StringVar()

        self.radbtn_frame=tk.Frame(
            self.fill_frame
        )
        self.radbtn_frame.grid(row=4, column=1)

        self.male=tk.Radiobutton(
            self.radbtn_frame,
            text="male",
            value="male",
            variable=self.gender
        )
        self.male.grid(row=0, column=0)

        self.female=tk.Radiobutton(
            self.radbtn_frame,
            text="female",
            value="female",
            variable=self.gender
        )
        self.female.grid(row=0, column=1)

        self.others=tk.Radiobutton(
            self.radbtn_frame,
            text="others",
            value="others",
            variable=self.gender
        )
        self.others.grid(row=0, column=2)

        self.skill_label=tk.Label(
            self.fill_frame,
            text="skills: ",
            font=("poppins",14)
        )
        self.skill_label.grid(row=5,column=0,padx=(0,50),pady=4)

        self.skill_frame=tk.Frame(
            self.fill_frame
        )
        self.skill_frame.grid(row=5,column=1)

        self.python_var=tk.BooleanVar()
        self.html_var=tk.BooleanVar()
        self.css_var=tk.BooleanVar()
        self.java_var=tk.BooleanVar()

        self.python_cb=tk.Checkbutton(
            self.skill_frame,
            text="python",
            variable=self.python_var,

        )
        self.python_cb.grid(row=0,column=0)

        self.html_cb=tk.Checkbutton(
            self.skill_frame,
            text="html",
            variable=self.html_var,

        )
        self.html_cb.grid(row=0,column=1)

        self.css_cb=tk.Checkbutton(
            self.skill_frame,
            text="css",
            variable=self.css_var
        )
        self.css_cb.grid(row=0,column=2)

        self.java_cb=tk.Checkbutton(
            self.skill_frame,
            text="java",
            variable=self.java_var
        )
        self.java_cb.grid(row=0,column=3)

        self.address_label=tk.Label(
            self.fill_frame,
            text="Address: ",
            font=("poppins",14)
        )
        self.address_label.grid(row=6,column=0,padx=(0,50),pady=4)

        self.address_txt=tk.Text(
            self.fill_frame,
            font=("poppins",12),
            width=30,
            height=4
        )
        self.address_txt.grid(row=6,column=1,padx=10,pady=10)

        self.register_btn=tk.Button(
            window,
            text="Register",
            height=3,
            width=10,
            font=(12),
            command=self.register
        )
        self.register_btn.pack(pady=20)

    def register(self):
        confirm=messagebox.askyesno(
            "confirmation",
            "are you sure you want to submit?"
        )
        if not confirm:
            return

        name=self.name_entry.get()
        roll=self.roll_entry.get()
        age=self.age_entry.get()
        course=self.course_menu.get()
        gnd=self.gender.get()
        address=self.address_txt.get("1.0",tk.END)
                                                 
        skills=[]
        if self.python_var.get():
            skills.append("python")
        if self.html_var.get():
            skills.append("html")
        if self.css_var.get():
            skills.append("css")
        if self.java_var.get():
            skills.append("java")

        print("Name:",name)
        print("Roll:",roll)
        print("Age:",age)
        print("Course:",course)
        print("Gender:",gnd)
        print("skills:",skills)
        print("Address:",address)

        messagebox.showinfo(
            "success",
            "registration successful"
        )

        result_window=tk.Toplevel()
        result_window.title("Student Details")
        result_window.geometry("450x450")

window=tk.Tk()
window.title("student registration form")
window.geometry("500x700")
window.configure(bg="pink")

obj=studentRegistration(window)
window.mainloop()