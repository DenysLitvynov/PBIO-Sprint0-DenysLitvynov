""" 
Autor: Denys Litvynov Lymanets 
Fecha: 20-09-2025 
Descripción: Clase con métodos para inicializar bases de datos con tablas y oopcionalmente, datos fake. 
"""

# ---------------------------------------------------------

from pathlib import Path
import sqlite3

# ---------------------------------------------------------

class DBInitializer:
    """
    Clase para inicializar bases de datos SQLite, creando tablas y opcionalmente
    insertando datos fake.
    """

    def __init__(self, schema_path: Path, insert_path: Path):
        self.schema_path = schema_path
        self.insert_path = insert_path

    # ---------------------------------------------------------
    # ---------------------------------------------------------
    
    def ejecutar_fichero_sql(self, cursor, filepath):
        """Ejecuta un script SQL completo en un cursor."""
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                sql_script = f.read()
            cursor.executescript(sql_script)
        except sqlite3.Error as e:
            raise RuntimeError(f"Error ejecutando SQL en {filepath}: {e}")
        except FileNotFoundError:
            raise RuntimeError(f"Archivo SQL no encontrado: {filepath}")

    # ---------------------------------------------------------
    # ---------------------------------------------------------
    
    def inicializar(self, conn: sqlite3.Connection, with_fake_data=True):
        """
        Crea la estructura de la base de datos y opcionalmente inserta datos fake.
        
        Args:
            conn: conexión sqlite3
            with_fake_data: si True, inserta datos fake definidos en insert_path
        """
        try:
            cursor = conn.cursor()
            self.ejecutar_fichero_sql(cursor, self.schema_path)
            if with_fake_data:
                self.ejecutar_fichero_sql(cursor, self.insert_path)
            conn.commit()
        except Exception as e:
            raise RuntimeError(f"Error inicializando la base de datos: {e}")

# ---------------------------------------------------------
# ---------------------------------------------------------
# class

