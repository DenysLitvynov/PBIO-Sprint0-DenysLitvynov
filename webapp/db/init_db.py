""" 
Autor: Denys Litvynov Lymanets 
Fecha: 20-09-2025 
Descripción: 
"""

# ---------------------------------------------------------

import sqlite3
from pathlib import Path
from webapp.db.db_utils import DBInitializer

# ---------------------------------------------------------

def main():
    base_dir = Path(__file__).resolve().parent
    schema_path = base_dir / "sql" / "create_measurements.sql"
    insert_path = base_dir / "sql" / "insert_measurements.sql"
    db_file = base_dir / "measurements.db"

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        initializer = DBInitializer(schema_path, insert_path)
        initializer.inicializar(conn, with_fake_data=True)
        print("Base de datos de desarrollo creada en", db_file)
    except Exception as e:
        print("Error creando la base de datos:", e)
    finally:
        if conn:
            conn.close()

# ---------------------------------------------------------
# ---------------------------------------------------------

if __name__ == "__main__":
    main()

# ---------------------------------------------------------
# ---------------------------------------------------------

