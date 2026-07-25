import tkinter as tk
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
    font=("Poppins",14),
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
    font=("Poppins",14)
)
roll_entry.grid(row=1, column=1,)



window.mainloop()
