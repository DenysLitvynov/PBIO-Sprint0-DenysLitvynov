
""" 
Autor: Denys Litvynov Lymanets 
Fecha: 29-09-2025 
Descripción: Tests para la clase Logica usando la base de datos temporal.
"""

# ---------------------------------------------------------

import sqlite3
import pytest
from logic.logica import Logica

# ---------------------------------------------------------

def test_obtener_ultima_medida_devuelve_valor(db_temporal):
    logica = Logica(ruta_bd=db_temporal)
    resultado = logica.obtener_ultima_medida()
    assert isinstance(resultado, (int, float))  # ✅ solo la medida
    assert resultado is not None

# ---------------------------------------------------------

def test_guardar_medida_inserta_en_bd(db_temporal):
    logica = Logica(ruta_bd=db_temporal)
    logica.guardar_medida(999)

    conn = sqlite3.connect(db_temporal)
    cursor = conn.cursor()
    cursor.execute("SELECT measurement FROM measurements ORDER BY timestamp DESC LIMIT 1")
    fila = cursor.fetchone()
    conn.close()

    assert fila is not None
    assert fila[0] == 999

# ---------------------------------------------------------

def test_obtener_ultima_medida_vacia(tmp_path):
    # BD vacía sin tabla
    db_file = tmp_path / "empty.db"
    conn = sqlite3.connect(db_file)
    conn.execute("CREATE TABLE measurements (measurement REAL, timestamp TEXT)")
    conn.commit()
    conn.close()

    logica = Logica(ruta_bd=str(db_file))
    resultado = logica.obtener_ultima_medida()
    assert resultado is None

# ---------------------------------------------------------
