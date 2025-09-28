""" 
Autor: Denys Litvynov Lymanets 
Fecha: 20-09-2025 
Descripción: Clase para implementar la lógica de negocio. 

"""

# ---------------------------------------------------------

import sqlite3
from datetime import datetime

# ---------------------------------------------------------

class Logica:

    def __init__(self, ruta_bd):
        self.ruta_bd = ruta_bd

    # ---------------------------------------------------------
    # ---------------------------------------------------------
    
    def obtener_ultima_medida(self):
        """
        Método para obtener la última medición como tupla o None si no hay datos.
        
        Returns:
            tuple: devuelve una tupla formato (medida, fecha) o None si no hay datos
        """
        conn = None
        try:
            conn = sqlite3.connect(self.ruta_bd)
            cursor = conn.cursor()
            cursor.execute(
                "SELECT measurement, timestamp FROM measurements ORDER BY timestamp DESC LIMIT 1"
            )
            fila = cursor.fetchone()
            return fila
        except sqlite3.Error as e:
            raise RuntimeError(f"Error accediendo a la base de datos: {e}")
        finally:
            if conn:
                conn.close()
   

    # ---------------------------------------------------------
    # ---------------------------------------------------------
   
    def guardar_medida(self, medida: int):
        
        conn = None
        try:
            #timestamp actual 
            now = datetime.now().isoformat()
            conn = sqlite3.connect(self.ruta_bd)
            cursor = conn.cursor()
            cursor.execute(
                    "INSERT INTO measurements (measurement, timestamp) VALUES (?, ?)", (medida, now)
                    )
            conn.commit()
        except sqlite3.Error as e: 
            raise RuntimeError (f"Error guardando en la base de datos: {e}")
        finally: 
            if conn: 
                conn.close()


    # ---------------------------------------------------------
    # ---------------------------------------------------------

# Class

