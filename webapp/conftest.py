""" 
Autor: Denys Litvynov Lymanets 
Fecha: 20-09-2025 
Descripción: Fixture global para crear una base de datos SQLite en memoria con datos fake para los tests.
"""

# ---------------------------------------------------------

# conftest.py
import pytest
import sqlite3
from pathlib import Path
from webapp.db.db_utils import DBInitializer
import tempfile
import os

@pytest.fixture
def db_temporal():
    """Crea un archivo SQLite temporal con datos fake y devuelve su ruta."""
    # Archivo temporal
    tmp_file = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
    ruta = tmp_file.name
    tmp_file.close()

    # Inicializar BD
    base_dir = Path(__file__).resolve().parent / "db" / "sql"
    schema_path = base_dir / "create_measurements.sql"
    insert_path = base_dir / "insert_measurements.sql"

    conn = sqlite3.connect(ruta)
    initializer = DBInitializer(schema_path, insert_path)
    initializer.inicializar(conn, with_fake_data=True)
    conn.close()

    yield ruta  # Aquí entregamos la ruta de la BD para los tests

    # Eliminar archivo al final
    os.remove(ruta)
