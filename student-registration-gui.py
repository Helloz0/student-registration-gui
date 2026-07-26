import tkinter as tk
from tkinter import ttk
window=tk.Tk()
window.title("student registration form")
window.geometry("500x700")
window.configure(bg="pink")

label=tk.Label(
    window,
    text="Student Registration Form",
    font=("Montserrat",19),
    #justify="center"
    )
label.pack(pady=30)

fill_frame=tk.Frame(
    window
    )
fill_frame.pack()

name_label=tk.Label(
    fill_frame,
    text="Name: ",
    font=("Poppins",14)
)
name_label.grid(row=0, column=0, padx=(0,50))

name_entry=tk.Entry(
    fill_frame,
    font=("Poppins",12),
)
name_entry.grid(row=0, column=1 )

roll_label=tk.Label(
    fill_frame,
    text="Roll no: ",
    font=("Poppins",14)
)
roll_label.grid(row=1, column=0, padx=(0,50))

roll_entry=tk.Entry(
    fill_frame,
    font=("Poppins",12)
)
roll_entry.grid(row=1, column=1,)

age_label=tk.Label(
    fill_frame,
    text="age: ",
    font=("poppins",14)
)
age_label.grid(row=2, column=0, padx=(0,50))

age_entry=tk.Entry(
    fill_frame,
    font=("poppins",14)
)
age_entry.grid(row=2, column=1)

course_label=tk.Label(
    fill_frame,
    text="course:",
    font=("poppins",14)
)
course_label.grid(row=3, column=0, padx=(0,50))

course_menu=ttk.Combobox(
    fill_frame,
    font=("poppins",12),
    values=["BA","BBA","BCA","BTECH"]
)
course_menu.grid(row=3,column=1)

gender_label=tk.Label(
    fill_frame,
    text="gender: ",
    font=("poppins",14)
)
gender_label.grid(row=4, column=0, padx=(0,50))

gender=tk.StringVar()

radbtn_frame=tk.Frame(
    fill_frame
)
radbtn_frame.grid(row=4, column=1)

male=tk.Radiobutton(
    radbtn_frame,
    text="male",
    value="male",
    variable=gender
)
male.grid(row=0, column=0)

female=tk.Radiobutton(
    radbtn_frame,
    text="female",
    value="female",
    variable=gender
)
female.grid(row=0, column=1)

others=tk.Radiobutton(
    radbtn_frame,
    text="others",
    value="others",
    variable=gender
)
others.grid(row=0, column=2)

skill_label=tk.Label(
    fill_frame,
    text="skills: ",
    font=("poppins",14)
)
skill_label.grid(row=5,column=0,padx=(0,50))

skill_frame=tk.Frame(
    fill_frame
)
skill_frame.grid(row=5,column=1)

python_var=tk.BooleanVar
html_var=tk.BooleanVar
css_var=tk.BooleanVar
java_var=tk.BooleanVar

python_cb=tk.Checkbutton(
    skill_frame,
    text="python",
    variable=python_var,
   
)
python_cb.grid(row=0,column=0)

html_cb=tk.Checkbutton(
    skill_frame,
    text="html",
    variable=html_var,
   
)
html_cb.grid(row=0,column=1)

css_cb=tk.Checkbutton(
    skill_frame,
    text="something something",
    variable=css_var
)
css_cb.grid(row=0,column=2)

java_cb=tk.Checkbutton(
    skill_frame,
    text="java",
    variable=java_var
)
java_cb.grid(row=0,column=3)


window.mainloop()
