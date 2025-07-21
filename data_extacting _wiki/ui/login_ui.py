import tkinter as tk
from tkinter import messagebox
import app

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login App")
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Username:").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.username_var).grid(row=0, column=1, padx=10, pady=10)
        tk.Label(self.root, text="Password:").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.password_var, show='*').grid(row=1, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Login", command=self.login).grid(row=2, column=0, padx=10, pady=10)
        tk.Button(self.root, text="Logout", command=self.logout).grid(row=2, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Show User Details", command=self.show_user_details).grid(row=3, column=0, columnspan=2, pady=10)

    def login(self):
        username = self.username_var.get()
        password = self.password_var.get()
        if app.login(username, password):
            messagebox.showinfo("Login", f"Logged in as {username}")
        else:
            messagebox.showwarning("Login Failed", "Username and password required.")

    def logout(self):
        app.logout()
        messagebox.showinfo("Logout", "Logged out.")

    def show_user_details(self):
        if app.current_user:
            messagebox.showinfo("User Details", f"Current user: {app.current_user}")
        else:
            messagebox.showinfo("User Details", "No user is currently logged in.")

if __name__ == "__main__":
    root = tk.Tk()
    app_gui = LoginApp(root)
    root.mainloop() 