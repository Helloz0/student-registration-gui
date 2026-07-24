import tkinter as tk
window=tk.Tk()
window.title("student registration form")
window.geometry("500x700")

label=tk.Label(
    window,
    text="Student Registration Form",
    font=("Montserrat",19),
    #justify="center"
    )
label.pack()

fill_frame=tk.Frame(window)
fill_frame.pack()

name_label=tk.Label(
    fill_frame,
    text="Name: ",
    font=("arial",14)
)
name_label.grid(row=0, column=0, padx=10)

name_entry=tk.Entry(
    fill_frame,
    font=("arial",14),
    justify="left"
)
name_entry.grid(row=0, column=1, padx=10 )


window.mainloop()
