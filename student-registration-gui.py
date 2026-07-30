import tkinter as tk
from tkinter import ttk

class studentRegistration:

    def __init__ (self,window):
        self.window=window

    def register(self):
    
        name=self.name_entry.get()
        roll=self.roll_entry.get()
        age=self.age_entry.get()
        course=self.course_menu.get()
        gnd=self.gender.get()
        address=self.address_txt.get("1.0",tk.END)
                                                 
        skills=[]
        if python_var.get():
            skills.append("python")
        if html_var.get():
            skills.append("html")
        if css_var.get():
            skills.append("css")
        if java_var.get():
            skills.append("java")

        print("Name:", self.name)
        print("Roll:", self.roll)
        print("Age:", self.age)
        print("Course:", self.course)
        print("Gender:",self. self.gnd)
        print("skills:",self.skills)
        print("Address:", self.address)

    self.label=tk.Label(
    window,
    text="Student Registration Form",
    font=("Montserrat",19),
    #justify="center"
    bg="pink"
    )
    label.pack(pady=30)

    self.fill_frame=tk.Frame(
        window
        )
    fill_frame.pack()

    self.name_label=tk.Label(
        fill_frame,
        text="Name: ",
        font=("Poppins",14)
    )
    name_label.grid(row=0, column=0, padx=(0,50),pady=4)

    self.name_entry=tk.Entry(
        fill_frame,
        font=("Poppins",12),
    )
    name_entry.grid(row=0, column=1 )

    self.roll_label=tk.Label(
        fill_frame,
        text="Roll no: ",
        font=("Poppins",14)
    )
    roll_label.grid(row=1, column=0, padx=(0,50),pady=4)

    self.roll_entry=tk.Entry(
        fill_frame,
        font=("Poppins",12)
    )
    roll_entry.grid(row=1, column=1,)

    self.age_label=tk.Label(
        fill_frame,
        text="age: ",
        font=("poppins",14),
        justify="left"
    )
    age_label.grid(row=2, column=0, padx=(0,50),pady=4)

    self.age_entry=tk.Entry(
        fill_frame,
        font=("poppins",14)
    )
    age_entry.grid(row=2, column=1)

    self.course_label=tk.Label(
        fill_frame,
        text="course:",
        font=("poppins",14)
    )
    course_label.grid(row=3, column=0, padx=(0,50),pady=4)

    self.course_menu=ttk.Combobox(
        fill_frame,
        font=("poppins",12),
        values=["BA","BBA","BCA","BTECH"]
    )
    course_menu.grid(row=3,column=1)

    self.gender_label=tk.Label(
        fill_frame,
        text="gender: ",
        font=("poppins",14)
    )
    gender_label.grid(row=4, column=0, padx=(0,50),pady=4)

    self.gender=tk.StringVar()

    self.radbtn_frame=tk.Frame(
        fill_frame
    )
    radbtn_frame.grid(row=4, column=1)

    self.male=tk.Radiobutton(
        radbtn_frame,
        text="male",
        value="male",
        variable=gender
    )
    male.grid(row=0, column=0)

    self.female=tk.Radiobutton(
        radbtn_frame,
        text="female",
        value="female",
        variable=gender
    )
    female.grid(row=0, column=1)

    self.others=tk.Radiobutton(
        radbtn_frame,
        text="others",
        value="others",
        variable=gender
    )
    others.grid(row=0, column=2)

    self.skill_label=tk.Label(
        fill_frame,
        text="skills: ",
        font=("poppins",14)
    )
    skill_label.grid(row=5,column=0,padx=(0,50),pady=4)

    self.skill_frame=tk.Frame(
        fill_frame
    )
    skill_frame.grid(row=5,column=1)

    self.python_var=tk.BooleanVar()
    self.html_var=tk.BooleanVar()
    self.css_var=tk.BooleanVar()
    self.java_var=tk.BooleanVar()

    self.python_cb=tk.Checkbutton(
        skill_frame,
        text="python",
        variable=python_var,
    
    )
    self.python_cb.grid(row=0,column=0)

    self.html_cb=tk.Checkbutton(
        skill_frame,
        text="html",
        variable=html_var,
    
    )
    self.html_cb.grid(row=0,column=1)

    self.css_cb=tk.Checkbutton(
        skill_frame,
        text="css",
        variable=css_var
    )
    self.css_cb.grid(row=0,column=2)

    self.java_cb=tk.Checkbutton(
        skill_frame,
        text="java",
        variable=java_var
    )
    self.java_cb.grid(row=0,column=3)

    self.address_label=tk.Label(
        fill_frame,
        text="Address: ",
        font=("poppins",14)
    )
    address_label.grid(row=6,column=0,padx=(0,50),pady=4)

    self.address_txt=tk.Text(
        fill_frame,
        font=("poppins",12),
        width=30,
        height=4
    )
    address_txt.grid(row=6,column=1,padx=10,pady=10)

    self.register_btn=tk.Button(
        window,
        text="Register",
        height=3,
        width=10,
        font=(12),
        command=self.register
    )
    register_btn.pack(pady=20)

window=tk.Tk()
obj=studentRegistration(window)

window.title("student registration form")
window.geometry("500x700")
window.configure(bg="pink")



window.mainloop()