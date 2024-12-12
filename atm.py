import tkinter as tk
import threading
from db import DB
class ATM:
    balanceLOCK = threading.Lock()
    def __init__(self, id, root):
        threadWindow = tk.Toplevel(root)
        threadWindow.title(f"ATM Thread {id}")
        logBox = tk.Text(threadWindow, width=50, height=15)
        logBox.pack(pady=10)
        tk.Label(threadWindow, text="Enter User ID:").pack()
        userIDEntred = tk.Entry(threadWindow)
        userIDEntred.pack(pady=5)
        tk.Label(threadWindow, text="Enter Amount:").pack()
        amountEntred = tk.Entry(threadWindow)
        amountEntred.pack(pady=5)
        for task in ["Deposit", "Withdraw", "Check Balance"]:
            tk.Button(
                threadWindow,
                text=task,
                command=lambda t=task: self.atmTask(t, amountEntred.get() if t != "Check Balance" else 0, logBox, userIDEntred.get())
            ).pack(pady=5)
    def atmTask(self, task, amount, logBox, userID):
        db = DB()
        try:
            amount = float(amount)
        except ValueError:
            logBox.insert(tk.END, "Invalid amount entered.\n")
            return
        try:
            userID = int(userID)
        except ValueError:
            logBox.insert(tk.END, "Invalid user ID entered.\n")
            return
        if not db.userExistsById(userID):
            logBox.insert(tk.END, "User ID does not exist.\n")
            return
        with self.balanceLOCK:
            currentBalance = db.getUserBalance(userID)
            if task == "Deposit":
                newBalance = currentBalance + amount
                db.updateBalanceInDatabase(userID, newBalance)
                logBox.insert(tk.END, f"User ID {userID} deposited {amount}. New balance: {newBalance}\n")
            elif task == "Withdraw":
                if currentBalance >= amount:
                    newBalance = currentBalance - amount
                    db.updateBalanceInDatabase(userID, newBalance)
                    logBox.insert(tk.END, f"User ID {userID} withdrew {amount}. New balance: {newBalance}\n")
                else:
                    logBox.insert(tk.END, f"User ID {userID} has insufficient funds for withdrawal.\n")
            elif task == "Check Balance":
                logBox.insert(tk.END, f"User ID {userID}'s balance: {currentBalance}\n")