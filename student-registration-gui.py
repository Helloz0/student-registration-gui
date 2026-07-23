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

name=tk.Label(
    fill_frame,
    text="Name: ",
    font=("arial",14),
    justify="left"
)
name.grid(row=0, column=0)

name=tk.Entry(
    fill_frame,
    font=("arial",14),
    justify="right"
)
name.grid(row=0, column=1)


window.mainloop()
