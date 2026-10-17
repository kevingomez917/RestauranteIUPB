# webapirestaurantepb.py
# API REST de RestauranteIUPB. Almacenamiento temporal en memoria.

from fastapi import FastAPI, HTTPException, status
from domain.entityrestaurante import EntityRestaurante
from domain.entityproducto import EntityProducto

app = FastAPI(
    title="RestauranteIUPB",
    description=(
        "API REST del sistema transaccional de restaurantes. "
        "Este módulo administra productos del menú."
    ),
    version="1.0.0"
)

# Almacenamiento temporal: los datos se pierden al detener el servidor.
restaurantes = []
productos = []
siguiente_producto_id = 1


# Endpoints existentes para Restaurante (se mantienen como base).
@app.get(
    "/consultarrestaurantetodo",
    summary="Consultar restaurantes",
    tags=["Restaurante"]
)
async def consultar_restaurante_todo():
    return {"success": True, "message": "Consulta realizada", "data": restaurantes}


@app.get(
    "/consultarrestaurante/{IdRestaurante}",
    summary="Consultar restaurante por ID",
    tags=["Restaurante"]
)
async def consultar_restaurante_uno(IdRestaurante: str):
    for restaurante in restaurantes:
        if restaurante["IdRestaurante"] == IdRestaurante:
            return {"success": True, "message": "Restaurante encontrado", "data": restaurante}
    raise HTTPException(status_code=404, detail="Restaurante no encontrado")


# POST: registrar un producto.
@app.post("/api/productos", status_code=status.HTTP_201_CREATED, tags=["Productos"],
          summary="Registrar producto")
def crear_producto(producto: EntityProducto):
    global siguiente_producto_id
    nuevo = {"id": siguiente_producto_id, **producto.model_dump()}
    productos.append(nuevo)
    siguiente_producto_id += 1
    return {"success": True, "message": "Producto creado correctamente", "data": nuevo}


# GET: consultar todos los productos.
@app.get("/api/productos", tags=["Productos"], summary="Consultar todos los productos")
def listar_productos():
    return {"success": True, "message": "Consulta realizada correctamente", "data": productos}


# GET por ID: consultar un producto específico.
@app.get("/api/productos/{id}", tags=["Productos"], summary="Consultar producto por ID")
def consultar_producto(id: int):
    for producto in productos:
        if producto["id"] == id:
            return {"success": True, "message": "Producto encontrado", "data": producto}
    raise HTTPException(
        status_code=404,
        detail={"success": False, "message": "El producto no existe", "data": None}
    )


# PUT: reemplazar los datos de un producto existente.
@app.put("/api/productos/{id}", tags=["Productos"], summary="Modificar producto")
def modificar_producto(id: int, producto: EntityProducto):
    for indice, existente in enumerate(productos):
        if existente["id"] == id:
            actualizado = {"id": id, **producto.model_dump()}
            productos[indice] = actualizado
            return {
                "success": True,
                "message": "Producto actualizado correctamente",
                "data": actualizado
            }
    raise HTTPException(
        status_code=404,
        detail={"success": False, "message": "El producto no existe", "data": None}
    )


# DELETE: retirar un producto.
@app.delete("/api/productos/{id}", tags=["Productos"], summary="Eliminar producto")
def eliminar_producto(id: int):
    for indice, producto in enumerate(productos):
        if producto["id"] == id:
            eliminado = productos.pop(indice)
            return {
                "success": True,
                "message": "Producto eliminado correctamente",
                "data": eliminado
            }
    raise HTTPException(
        status_code=404,
        detail={"success": False, "message": "El producto no existe", "data": None}
    )
