import sqlite3

class DatabaseManager:
    def __init__(self, db_name="datos.db"):
        self.db_name = db_name
        self.initialize_db()

    def initialize_db(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS registros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            peso REAL NOT NULL,
            descripcion TEXT
        )
        ''')
        conn.commit()
        conn.close()

    def insert_record(self, nombre, peso, descripcion):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO registros (nombre, peso, descripcion)
        VALUES (?, ?, ?)
        ''', (nombre, peso, descripcion))
        conn.commit()
        conn.close()

    def get_records(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM registros')
        records = cursor.fetchall()
        conn.close()
        return records