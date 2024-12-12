import threading
import tkinter as tk
from tkinter import messagebox, simpledialog
from db import DB
from atm import ATM

def createGUI():
    def startApp():
        try:
            numThreads = int(entredThreads.get())
            if numThreads <= 0:
                raise ValueError("Number of threads must be positive.")
            for i in range(1, numThreads + 1):
                ATM(i, root)
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))

    def createUser():
        userName = simpledialog.askstring("Create User", "Enter user name:")
        if not userName:
            messagebox.showerror("Error", "User name cannot be empty.")
            return

        initialBalance = simpledialog.askfloat("Create User", "Enter initial balance:")
        if initialBalance is None or initialBalance < 0:
            messagebox.showerror("Error", "Invalid initial balance.")
            return
        db = DB()
        try:
            userID = db.addUserToDatabase(userName, initialBalance)
            messagebox.showinfo("Success", f"User {userName} created with ID {userID} and balance {initialBalance}.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    root = tk.Tk()
    root.title("ATM Simulator")

    tk.Label(root, text="Enter number of threads (ATMs):").pack(pady=5)
    entredThreads = tk.Entry(root)
    entredThreads.pack(pady=5)

    tk.Button(root, text="Create User", command=createUser).pack(pady=10)

    tk.Button(root, text="Start Simulation", command=startApp).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    createGUI()