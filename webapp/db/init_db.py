""" 
Autor: Denys Litvynov Lymanets 
Fecha: 20-09-2025 
Descripción: Script para la creación e introducción de datos fake en la bd.  

"""

# ---------------------------------------------------------

from pathlib import Path
import sqlite3

# Rutas relativas a los archivos 
BASE_DIR = Path(__file__).resolve().parent
SCHEMA_FILE = BASE_DIR / "sql" / "create_measurements.sql"
INSERT_FILE = BASE_DIR / "sql" / "insert_measurements.sql"
DB_FILE = BASE_DIR / "measurements.db"

# ---------------------------------------------------------


# ---------------------------------------------------------
# ---------------------------------------------------------

def ejecutar_fichero_sql(cursor, filepath):
    """
    Método para ejecutar scripts sql.
    
    Args:
        Cursor (cursor): objeto para ejecutar sentencias SQL
    
    Returns:
        None: No devuelve ningun valor. 
    """
    with open(filepath, "r", encoding = "utf-8") as f: 
        sql_script = f.read()
    cursor.executescript(sql_script)
 

# ---------------------------------------------------------
# ---------------------------------------------------------

def inicializar_db(): 
    """
    Método para ejecutar ficheros sql llamando al método anterior. 
    
    Args:
        None (type): No recibe nada
    
    Returns:
        None: No devuelve nada
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor() # objeto que ejecuta sentencias SQL
    ejecutar_fichero_sql(cursor, SCHEMA_FILE) # crear tabla
    ejecutar_fichero_sql(cursor, INSERT_FILE) # insertar datos fake
    conn.commit()
    conn.close()
    print("Base de datos creada en", DB_FILE)
    

# --------------------------------------------------------- 
# ---------------------------------------------------------

if __name__ == "__main__":
    inicializar_db()

# ---------------------------------------------------------
# ---------------------------------------------------------
