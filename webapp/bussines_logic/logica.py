""" 
Autor: Denys Litvynov Lymanets 
Fecha: 20-09-2025 
Descripción: Clase para implementar la lógica de negocio. 

"""

# ---------------------------------------------------------

import sqlite3

# ---------------------------------------------------------

class Logica:

    def __init__(self, ruta_bd):
        self.ruta_bd = ruta_bd

    # ---------------------------------------------------------
    # ---------------------------------------------------------
    
    def obtener_ultima_medida(self):
        """
        Método para obtener la última medición como tupla o None si no hay datos. 
        
        Args:
            self (type): recibe la ruta a la bd desde el constructor
        
        Returns:
            tuple: devuelve una tupla formato (medida, fecha)
        """    
        conn = sqlite3.connect(self.ruta_bd)
        cursor = conn.cursor()
        cursor.execute(
                "SELECT measurement, timestamp FROM measurements ORDER BY timestamp DESC LIMIT 1"
                )
        fila = cursor.fetchone()
        conn.close()
        return fila


    # ---------------------------------------------------------
    # ---------------------------------------------------------
   
    def guardar_medida(self, medida):
        pass


    # ---------------------------------------------------------
    # ---------------------------------------------------------

# Class

