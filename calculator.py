import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")
root.configure(bg="green")

# Entry box (IMPORTANT: grid on a separate line)
entry1 = tk.Entry(
    root,
    font=("Arial", 24),
    bg="black",
    fg="yellow",
    bd=0,
    justify="right"
)
entry1.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

# Button labels
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

# Functions
def press(value):
    entry1.insert(tk.END, value)

def clear():
    entry1.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry1.get())
        entry1.delete(0, tk.END)
        entry1.insert(0, result)
    except:
        entry1.delete(0, tk.END)
        entry1.insert(0, "Error")

# Clear button
tk.Button(
    root,
    text="C",
    font=("Arial", 20),
    command=clear,
    bg="red",
    fg="violet",
    width=9,
    height=2
).grid(row=1, column=0, columnspan=4, padx=6, pady=6)

# Create buttons
row = 2
col = 0

for b in buttons:
    if b == "=":
        cmd = calculate
    else:
        cmd = lambda x=b: press(x)

    tk.Button(
        root,
        text=b,
        font=("Arial", 20),
        command=cmd,
        width=9,
        height=2,
        bd=0,
        bg="pink" if b in {"+", "-", "*", "/", "="} else "black",
        fg="blue"
    ).grid(row=row, column=col, padx=6, pady=6)

    col += 1
    if col == 4:
        col = 0
        row += 1

root.mainloop()