
# ATM Simulator

A multithreaded ATM simulation system that demonstrates how multiple ATMs handle transactions concurrently.
## Features

- **Multi-ATM Simulation**: Each ATM runs as an independent thread, capable of handling user transactions simultaneously.
- **Thread Synchronization**: Prevents race conditions and ensures no overdrawing occurs by using locks to manage account access.
- **Transaction Logging**: Records every transaction (deposit, withdrawal, balance inquiry) for auditing and debugging.
- **Realistic ATM Operations**: Users can:
  - Deposit funds
  - Withdraw funds (with balance checks)
  - Check their account balance
- **SQLite Database**: Persistent storage for user accounts and balances.

## Tech Stack

**Programming Language**: Python

**Database**: SQLite for managing user data and transaction records.

**GUI Framework**: Tkinter for creating a simple and interactive user interface.

**Threading**: Python's `threading` module for simulating multiple ATMs concurrently.
## Run Locally

Clone the project

```bash
  git clone https://github.com/Ahmed-M-Aboutaleb/PP-2025-ATM-Simulator.git
```

Go to the project directory

```bash
  cd PP-2025-ATM-Simulator
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the project

```bash
  py main.py
```


## Contributing

Contributions are always welcome!
## Authors

- [@Ahmed Aboutaleb](https://www.github.com/Ahmed-M-Aboutaleb)
- [@Ahmed Ragab](https://www.github.com/A7medrajab1)
- [@Ahmed Mohamed](https://www.github.com/Eng-AhmedMohamed)
- [@Asem Hamed](https://www.github.com/Asemhamed)
- [@Abdelrhman Hany](https://www.github.com/AbdoHany0310)