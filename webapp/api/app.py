""" 
Autor: Denys Litvynov Lymanets 
Fecha: 28-09-2025 
Descripción: Archivo principal de la aplicación fastAPI. Aquí configuramos la app, middleware, rutas estáticas y routers.

"""

# ---------------------------------------------------------

from fastapi import FastAPI, HTTPException, responses
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from pydantic import BaseModel
from .routes import router as api_router

# ---------------------------------------------------------

# Creo instancia de FastAPI
app = FastAPI(title = "API REST para Proyecto Biometría y Medio Ambiente", version = "1.0.0")

# Registrar el router de routes.py con prefijo /api
app.include_router(api_router, prefix="/api")

# ---------------------------------------------------------

# Esto evita errores de CORS cuando el frontend (e.g., en browser) llama a la API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especifica dominios permitidos (e.g., ["http://localhost:3000"]).
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP (GET, POST, etc.).
    allow_headers=["*"],  # Permite todos los headers.
)

# ---------------------------------------------------------

# Montar archivos estáticos para servir el frontend (HTML, CSS, JS) 
# BASE_DIR = Path(__file__).resolve().parent.parent  # apunta al project-root
# app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

@app.get("/")
async def root():
    #return FileResponse(Path("/templates/index.html"))
    return {"message": "API REST corriendo. Usa /api/guardar (POST) o /api/ultima (GET)."}

# ---------------------------------------------------------

# Bloque para ejecutar el servidor directamente con python app.py
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)  # reload=True para hot-reload

# ---------------------------------------------------------
# ---------------------------------------------------------

