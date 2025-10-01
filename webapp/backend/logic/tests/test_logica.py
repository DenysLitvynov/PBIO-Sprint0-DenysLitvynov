
"""
Autor: Denys Litvynov Lymanets
Fecha: 29-09-2025
Descripción: Tests profesionales para la clase Logica usando base de datos temporal.
Cada test es independiente y no depende de otro método de la clase.
"""

# ---------------------------------------------------------

import sqlite3
import pytest
from logic.logica import Logica

# ---------------------------------------------------------

def test_guardar_medida_inserta_en_bd(db_temporal):
    """
    Test que verifica que 'guardar_medida' inserta correctamente un valor en la BD.
    - No depende de 'obtener_ultima_medida'.
    """
    logica = Logica(ruta_bd=db_temporal)
    logica.guardar_medida(555)

    # Conexión directa a la BD para comprobar
    with sqlite3.connect(db_temporal) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT measurement FROM measurements ORDER BY timestamp DESC LIMIT 1")
        fila = cursor.fetchone()

    assert fila is not None
    assert fila[0] == 555

# ---------------------------------------------------------
# ---------------------------------------------------------

def test_obtener_ultima_medida_devuelve_valor(db_temporal):
    """
    Test que verifica que 'obtener_ultima_medida' devuelve correctamente el último valor.
    - Insertamos los datos directamente en la BD con SQL, no usamos 'guardar_medida'.
    """
    # Insertamos un valor adicional
    with sqlite3.connect(db_temporal) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO measurements (measurement, timestamp) VALUES (?, ?)",
            (777, "2025-09-29T12:00:00")
        )
        conn.commit()

    logica = Logica(ruta_bd=db_temporal)
    resultado = logica.obtener_ultima_medida()
    assert resultado == 777

# ---------------------------------------------------------
# ---------------------------------------------------------

def test_obtener_ultima_medida_vacia(tmp_path):
    """
    Test que verifica que 'obtener_ultima_medida' devuelve None si la tabla está vacía.
    - Se crea una base de datos temporal vacía usando tmp_path.
    - No se insertan datos.
    """
    db_file = tmp_path / "empty.db"
    with sqlite3.connect(db_file) as conn:
        conn.execute("CREATE TABLE measurements (measurement REAL, timestamp TEXT)")
        conn.commit()

    logica = Logica(ruta_bd=str(db_file))
    resultado = logica.obtener_ultima_medida()
    assert resultado is None

# ---------------------------------------------------------
# ---------------------------------------------------------

def test_obtener_ultima_medida_varios_registros(db_temporal):
    """
    Test que verifica que 'obtener_ultima_medida' devuelve siempre el último registro
    cuando hay varios registros en la BD.
    - Usamos la fixture con datos fake ya insertados (3 registros).
    """
    logica = Logica(ruta_bd=db_temporal)
    resultado = logica.obtener_ultima_medida()
    # Asumimos que insert_measurements.sql inserta 3 registros: 100, 200, 300
    assert resultado == 300

# ---------------------------------------------------------
# ---------------------------------------------------------

