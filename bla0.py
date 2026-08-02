from tkinter import *
from tkinter import messagebox

def calculate():
    try:
        total = int(total_entry.get())
        daily = int(daily_entry.get())

        if total <= 0 or daily <= 0:
            raise ValueError

        days = total // daily
        remaining = total % daily

        result.config(
            text=f"Complete Reading Days: {days}\nRemaining Pages: {remaining}"
        )
    except:
        messagebox.showerror("Error", "Enter valid positive integers.")

def open_planner():
    top = Toplevel(root)
    top.title("Reading Schedule Planner")
    top.geometry("350x250")

    global total_entry, daily_entry, result

    Label(top, text="Total Pages").pack(pady=5)
    total_entry = Entry(top)
    total_entry.pack()

    Label(top, text="Pages Per Day").pack(pady=5)
    daily_entry = Entry(top)
    daily_entry.pack()

    Button(top, text="Calculate", command=calculate).pack(pady=10)

    result = Label(top, text="")
    result.pack()

root = Tk()
root.title("Denomination Calculator")
root.geometry("300x150")

Button(root, text="Open Reading Planner", command=open_planner).pack(expand=True)

root.mainloop()