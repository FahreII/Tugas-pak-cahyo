import tkinter as tk
from tkinter import messagebox

def login():
    try:
        user = entry_user.get()
        pwd = entry_pass.get()

        if user == "" or pwd == "":
            raise ValueError("kosong")

        if user == "a" and pwd == "1":
            messagebox.showinfo("Login", "Login Berhasil!")
        else:
            messagebox.showerror("Login", "Username atau Password salah")

    except ValueError:
        messagebox.showwarning("Peringatan", "Username dan Password tidak boleh kosong")

root = tk.Tk()
root.title("Login")
root.geometry("360x640")

tk.Label(root, text="LOGIN",font=18,pady=80).pack()

tk.Label(root, text="Username").pack()
entry_user = tk.Entry(root, width=30)
entry_user.pack()

tk.Label(root, text="Password").pack()
entry_pass = tk.Entry(root,show="•", width=30)
entry_pass.pack()

tk.Button(root, text="Log in",bg="#1581BF",width=25, command=login).pack(pady=10)
tk.Label(root, text="Lupa kata sandi",fg="#229FE7",pady=20,).pack()

root.mainloop()