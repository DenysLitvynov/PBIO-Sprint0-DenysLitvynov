""" 
Autor: Denys Litvynov Lymanets 
Fecha: 28-09-2025 
Descripción: Este archivo define los endpoints de la API.  

"""

# ---------------------------------------------------------

from re import I
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from webapp.logic.logica import Logica
from pathlib import Path

# ---------------------------------------------------------

router = APIRouter()

def get_logica():
    base_dir = Path(__file__).resolve().parent.parent
    ruta_bd = base_dir / "db" / "measurements.db" 
    return Logica(str(ruta_bd))

# ---------------------------------------------------------
# ---------------------------------------------------------


# Definimos un modelo Pydantic para validar el cuerpo de POST.
# Esto asegura que el JSON entrante tenga { "medida": "valor" }.
class Medida(BaseModel):
    medida: str  # Campo requerido de tipo string.


# ---------------------------------------------------------
# ---------------------------------------------------------


# Endpoint POST para /api/guardar
@router.post("/guardar")
def guardar_medicion(medida: Medida, logica: Logica = Depends(get_logica)):
    pass


# ---------------------------------------------------------
# ---------------------------------------------------------

# Endpoint GET para /api/última
@router.get("/ultima")
def obtener_ultima_medida(logica: Logica = Depends(get_logica)):        
    try: 
        resultado = logica.obtener_ultima_medida()
        if resultado is None: 
             raise HTTPException(status_code=404, detail="No hay mediciones disponibles")
        return {"medida": resultado}
    except RuntimeError as e: 
        raise HTTPException(status_code=500, detail=str(e))
                        
# ---------------------------------------------------------
# ---------------------------------------------------------


# ---------------------------------------------------------
# ---------------------------------------------------------
