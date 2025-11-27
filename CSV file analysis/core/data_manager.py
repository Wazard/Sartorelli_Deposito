import csv
import numpy as np
import sqlite3
from core.custom_errors import CsvIOError,DbRelatedError

class DataManager:
    def __init__(self, db_path: str | None = None):
        """
        Initialize the DataManager with optional SQLite database path.
        """
        self.db_path = db_path
        self.conn = None
        if db_path:
            self.connect_db(db_path)

    # ---------------- CSV METHODS ----------------
    def load_csv(self, path: str) -> tuple[np.ndarray, str]:
        """
        Load a CSV file and return its contents as a NumPy array.
        Returns (array, type) where type is 'array' or 'matrix'.
        """
        try:
            with open(path, newline='') as f:
                reader = csv.reader(f)
                data = [list(map(float, row)) for row in reader if row]
        except Exception as e:
            raise CsvIOError(f"Could not read file: {e}")

        arr = np.array(data)
        if arr.size == 0:
            raise CsvIOError("CSV file is empty")

        if arr.shape[0] == 1:
            return arr.flatten(), "array"
        return arr, "matrix"

    def save_csv(self, path: str, data: np.ndarray) -> bool:
        """
        Save a NumPy array or matrix to a CSV file.
        """
        try:
            with open(path, "w", newline="") as f:
                writer = csv.writer(f)
                if data.ndim == 1:
                    writer.writerow(data.tolist())
                else:
                    writer.writerows(data.tolist())
            return True
        except Exception as e:
            raise CsvIOError(f"Could not write to file: {e}")

    # ---------------- SQLITE METHODS ----------------
    def connect_db(self, db_path: str):
        """
        Connect to SQLite database.
        """
        try:
            self.conn = sqlite3.connect(db_path)
            self.db_path = db_path
        except Exception as e:
            raise DbRelatedError(f"Could not connect to database: {e}")

    def create_table(self, table_name: str):
        """
        Create a table for storing numeric data.
        """
        if not self.conn:
            raise DbRelatedError("No database connection")
        try:
            cur = self.conn.cursor()
            cur.execute(f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    row_index INTEGER,
                    col_index INTEGER,
                    value REAL
                )
            """)
            self.conn.commit()
        except Exception as e:
            raise DbRelatedError(f"Could not create table: {e}")

    def insert_array(self, table_name: str, data: np.ndarray):
        """
        Insert array or matrix into SQLite table.
        """
        if not self.conn:
            raise DbRelatedError("No database connection")
        try:
            cur = self.conn.cursor()
            if data.ndim == 1:
                for i, val in enumerate(data):
                    cur.execute(f"INSERT INTO {table_name} (row_index, col_index, value) VALUES (?, ?, ?)",
                                (0, i, float(val)))
            else:
                for r in range(data.shape[0]):
                    for c in range(data.shape[1]):
                        cur.execute(f"INSERT INTO {table_name} (row_index, col_index, value) VALUES (?, ?, ?)",
                                    (r, c, float(data[r, c])))
            self.conn.commit()
        except Exception as e:
            raise DbRelatedError(f"Could not insert data: {e}")

    def fetch_all(self, table_name: str) -> np.ndarray | None:
        """
        Fetch all data from SQLite table and return as NumPy array.
        """
        if not self.conn:
            raise DbRelatedError("No database connection")
        try:
            cur = self.conn.cursor()
            cur.execute(f"SELECT row_index, col_index, value FROM {table_name}")
            rows = cur.fetchall()
            if not rows:
                return None
            # reconstruct matrix
            max_row = max(r[0] for r in rows)
            max_col = max(r[1] for r in rows)
            arr = np.zeros((max_row+1, max_col+1))
            for r, c, v in rows:
                arr[r, c] = v
            return arr
        except Exception as e:
            raise DbRelatedError(f"Could not fetch data: {e}")

    def close_db(self):
        """
        Close SQLite connection.
        """
        if self.conn:
            self.conn.close()
            self.conn = None