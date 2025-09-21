""" 
Autor: Denys Litvynov Lymanets 
Fecha: 21-09-2025 
Descripción: Tests para la clase Logica usando la base de datos en memoria.
"""

# ---------------------------------------------------------

from webapp.bussines_logic.logica import Logica

# ---------------------------------------------------------

def test_obtener_ultima_medida(db_temporal):
    logica = Logica(ruta_bd=db_temporal)
    resultado = logica.obtener_ultima_medida()
    assert resultado == (1234.0, "2025-09-20 12:00:00")
    
# ---------------------------------------------------------

