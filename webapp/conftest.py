""" 
Autor: Denys Litvynov Lymanets 
Fecha: 20-09-2025 
Descripción: Fixture global para crear una base de datos SQLite temporal con datos fake para los tests.
"""

# ---------------------------------------------------------

import sys
import pytest
import sqlite3
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))
from db.db_utils import DBInitializer
import tempfile
import os

# ---------------------------------------------------------

@pytest.fixture
def db_temporal(with_fake_data=True):
    """
    Fixture que crea una base de datos SQLite temporal.
    
    Args:
        with_fake_data (bool): Si True inserta 3 registros fake, si False crea tabla vacía.
    
    Returns:
        str: Ruta del archivo de la BD temporal.
    """
    tmp_file = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
    ruta = tmp_file.name
    tmp_file.close()

    base_dir = Path(__file__).resolve().parent / "db" / "sql"
    schema_path = base_dir / "create_measurements.sql"
    insert_path = base_dir / "insert_measurements.sql"

    conn = sqlite3.connect(ruta)
    initializer = DBInitializer(schema_path, insert_path)
    initializer.inicializar(conn, with_fake_data=with_fake_data)
    conn.close()

    yield ruta

    os.remove(ruta)

# ---------------------------------------------------------
# ---------------------------------------------------------
