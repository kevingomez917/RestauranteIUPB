# entityproducto.py
# Entidad Producto para el sistema RestauranteIUPB.

from pydantic import BaseModel, Field


class EntityProducto(BaseModel):
    nombre: str = Field(min_length=1, description="Nombre del plato o bebida")
    descripcion: str = Field(min_length=1, description="Descripción del producto")
    categoria: str = Field(min_length=1, description="Categoría del menú")
    precio: float = Field(gt=0, description="Precio mayor que cero")
    cantidad: int = Field(ge=0, description="Cantidad disponible")
    estado: bool = Field(description="Indica si el producto está disponible")
