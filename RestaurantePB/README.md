# RestaurantePB — RestauranteIUPB

Proyecto académico de sistema transaccional para la gestión de restaurantes.

## Módulo implementado para el Laboratorio 2
API REST CRUD para productos del menú, con FastAPI, Pydantic, Swagger/OpenAPI y almacenamiento temporal en memoria (sin base de datos).

### Requisitos
- Python 3.13
- FastAPI
- Uvicorn

### Instalación
Desde esta carpeta (`Desarrollo/backend_restaurantepb`), con el entorno virtual activado:

```powershell
python -m pip install fastapi uvicorn
```

### Ejecución
```powershell
python main.py
```

La API inicia en `http://127.0.0.1:7000` y Swagger está en `http://127.0.0.1:7000/docs`.

También puede ejecutarse con:
```powershell
python -m uvicorn presentation.webapirestaurantepb:app --reload --host 127.0.0.1 --port 7000
```

### Endpoints de productos
- `POST /api/productos`: registrar un producto.
- `GET /api/productos`: consultar todos.
- `GET /api/productos/{id}`: consultar por ID.
- `PUT /api/productos/{id}`: modificar por ID.
- `DELETE /api/productos/{id}`: eliminar por ID.

Ejemplo de JSON:
```json
{
  "nombre": "Hamburguesa",
  "descripcion": "Hamburguesa clásica",
  "categoria": "Plato principal",
  "precio": 18000,
  "cantidad": 20,
  "estado": true
}
```

**Nota:** los registros solo viven en memoria y se pierden al detener el servidor, conforme al alcance del laboratorio.
