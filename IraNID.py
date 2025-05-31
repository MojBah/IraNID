import tkinter as tk
from tkinter import messagebox

def check_code_meli(code):
    code = str(code)
    L = len(code)
    if L < 8 or int(code) == 0:
        return False
    code = ('0000' + code)[L + 4 - 10:]
    if int(code[3:9]) == 0:
        return False
    c = int(code[9])
    s = 0
    for i in range(9):
        s += int(code[i]) * (10 - i)
    s = s % 11
    return (s < 2 and c == s) or (s >= 2 and c == (11 - s))

def validate():
    code = entry.get()
    if check_code_meli(code):
        messagebox.showinfo("نتیجه", "کد معتبر است.")
    else:
        messagebox.showerror("نتیجه", "کد نامعتبر است.")

root = tk.Tk()
root.title("بررسی صحت کد ملی")
root.geometry("400x200")  # این خط اندازه پنجره را بزرگ‌تر می‌کند

tk.Label(root, text="کد ملی را وارد کنید:", font=("Tahoma", 14)).pack(padx=10, pady=20)
entry = tk.Entry(root, font=("Tahoma", 14), width=25)
entry.pack(padx=10, pady=10)

tk.Button(root, text="بررسی", command=validate, font=("Tahoma", 12), width=15).pack(padx=10, pady=10)

root.mainloop()