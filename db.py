import sqlite3

class DB:
    def __init__(self):
        conn = sqlite3.connect("atm_simulator.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                balance REAL NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    def addUserToDatabase(self, username, balance):
        conn = sqlite3.connect("atm_simulator.db")
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, balance) VALUES (?, ?)", (username, balance))
            conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError(f"The username '{username}' is already taken. Please choose a different username.")
        finally:
            conn.close()

    def updateBalanceInDatabase(self, userID, newBalance):
        conn = sqlite3.connect("atm_simulator.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET balance = ? WHERE id = ?", (newBalance, userID))
        conn.commit()
        conn.close()

    def getUserBalance(self, userID):
        conn = sqlite3.connect("atm_simulator.db")
        cursor = conn.cursor()
        cursor.execute("SELECT balance FROM users WHERE id = ?", (userID,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None

    def userExistsById(self, userID):
        conn = sqlite3.connect("atm_simulator.db")
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM users WHERE id = ?", (userID,))
        result = cursor.fetchone()
        conn.close()
        return result is not None
