import time
import threading
from atm import ATM
from db import DB

def simulate_sequential(transactions, num_atms):
    atms = [ATM(i, None) for i in range(1, num_atms + 1)]

    start_time = time.time()
    logs = []
    for i, (user_id, task, amount) in enumerate(transactions):
        atm = atms[i % num_atms]
        if task == "Deposit" or task == "Withdraw":
            logs.append(atm.atmTask(task, amount, None, user_id))
        elif task == "Check Balance":
            logs.append(atm.atmTask(task, 0, None, user_id))
    end_time = time.time()

    return logs, end_time - start_time

def simulate_multithreaded(transactions, num_atms):
    atms = [ATM(i, None) for i in range(1, num_atms + 1)]

    start_time = time.time()
    threads = []
    logs = []
    logs_lock = threading.Lock()

    def task_runner(atm, user_id, task, amount):
        result = atm.atmTask(task, amount, None, user_id)
        with logs_lock:
            logs.append(result)

    for i, (user_id, task, amount) in enumerate(transactions):
        atm = atms[i % num_atms]
        thread = threading.Thread(target=task_runner, args=(atm, user_id, task, amount))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    return logs, end_time - start_time

if __name__ == "__main__":
    db = DB()
    db.addUserToDatabase("Ahmed", 1000)
    db.addUserToDatabase("Abdullah", 500)
    db.addUserToDatabase("Bioumy", 300)

    # Example transactions: (user_id, task, amount)
    transactions = [
        (1, "Deposit", 100),
        (2, "Withdraw", 200),
        (3, "Check Balance", 0),
        (1, "Withdraw", 50),
        (2, "Deposit", 150),
        (3, "Check Balance", 0),
        (1, "Withdraw", 50),
        (2, "Deposit", 150),
        (3, "Check Balance", 0),
        (1, "Withdraw", 50),
        (2, "Deposit", 150),
        (3, "Check Balance", 0),
        (1, "Withdraw", 50),
        (2, "Deposit", 150),
        (3, "Check Balance", 0),
        (1, "Withdraw", 50),
        (2, "Deposit", 150),
        (3, "Check Balance", 0),
        (1, "Withdraw", 50),
        (2, "Deposit", 150),
        (3, "Check Balance", 0),
        (1, "Withdraw", 50),
        (2, "Deposit", 150),
        (3, "Check Balance", 0),
    ]

    num_atms = 30

    # Sequential simulation
    print("Simulating Sequential Execution...")
    sequential_logs, sequential_time = simulate_sequential(transactions, num_atms)
    print("\n".join(sequential_logs))

    # Multithreaded simulation
    print("Simulating Multithreaded Execution...")
    multithreaded_logs, multithreaded_time = simulate_multithreaded(transactions, num_atms)
    print("\n".join(multithreaded_logs))
    print(f"Sequential Execution Time: {sequential_time:.4f} seconds\n")
    print(f"Multithreaded Execution Time: {multithreaded_time:.4f} seconds")
    speedup = sequential_time / multithreaded_time if multithreaded_time > 0 else 1
    print(f"\nSpeedup: {speedup:.2f}x")
