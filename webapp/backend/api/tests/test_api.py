""" 
Autor: Denys Litvynov Lymanets 
Fecha: 29-09-2025 
Descripción: Tests para los endpoints REST de la API usando TestClient de FastAPI.
"""

# ---------------------------------------------------------

import pytest
from fastapi.testclient import TestClient
from api.app import app
from api.routes import get_logica  
from logic.logica import Logica

# ---------------------------------------------------------

client = TestClient(app)

# Con este método podemos crear una instancia de la logica pasandole la bd de pruebas.  
def override_get_logica(db_path):
    def _get_logica():
        return Logica(ruta_bd=db_path)
    return _get_logica

# ---------------------------------------------------------
# ---------------------------------------------------------

def test_post_guardar_medida(db_temporal):
    app.dependency_overrides.clear()
    app.dependency_overrides[get_logica] = override_get_logica(db_temporal)

    response = client.post("/api/v1/guardar-medida", json={"medida": 555})
    assert response.status_code == 200
    assert "exitosamente" in response.json()["message"]

# ---------------------------------------------------------
# ---------------------------------------------------------

def test_get_ultima_medida(db_temporal):
    app.dependency_overrides.clear()
    app.dependency_overrides[get_logica] = override_get_logica(db_temporal)

    response = client.get("/api/v1/ultima-medida")
    assert response.status_code == 200
    data = response.json()
    assert "medida" in data
    assert isinstance(data["medida"], (int, float))

# ---------------------------------------------------------
# ---------------------------------------------------------

def test_get_ultima_medida_sin_datos(tmp_path):
    db_file = tmp_path / "empty.db"
    import sqlite3
    conn = sqlite3.connect(db_file)
    conn.execute("CREATE TABLE measurements (measurement REAL, timestamp TEXT)")
    conn.commit()
    conn.close()

    app.dependency_overrides.clear()
    app.dependency_overrides[get_logica] = override_get_logica(str(db_file))

    response = client.get("/api/v1/ultima-medida")
    assert response.status_code == 404
    assert "No hay mediciones" in response.json()["detail"]

# ---------------------------------------------------------
# ---------------------------------------------------------
