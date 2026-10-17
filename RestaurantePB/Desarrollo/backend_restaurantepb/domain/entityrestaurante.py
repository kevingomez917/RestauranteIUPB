# entityrestaurante.py

from pydantic import BaseModel

class EntityRestaurante(BaseModel):
    IdRestaurante: str
    NombreRestaurante: str