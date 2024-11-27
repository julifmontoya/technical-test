# Inventarios Backend
## 1. Instalación
#### Instala las dependencias necesarias:
```bash
pip install -r requirements.txt
```

#### Crea las migraciones y aplica los cambios a la base de datos:
```bash
python manage.py makemigrations
python manage.py migrate
```

#### Inicia el servidor de desarrollo:
```bash
python manage.py runserver
```

## 2. Endpoints
#### Listado de productos
```bash
  GET /v1/products/
```

#### Crear producto
#### Para crear un nuevo producto, realiza una solicitud POST a:
```bash
  POST /v1/products/create/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `code`      | `string` | **Required** |
| `name`      | `string` | **Required** |


#### Listado de lotes
```bash
  GET /v1/products/batches/
```

#### Crear lote
#### Para crear un nuevo lote, realiza una solicitud POST a:

```bash
POST /v1/products/batches/create/
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `product`      | `id` | **Required** |
| `expiration_date`      | `date` | **Required** |
| `quantity`      | `int` | **Required** |


#### Listado de transacciones
```bash
GET /v1/products/transactions/
```

#### Crear transacción
#### Puedes elegir entre entry o exit para el tipo de transacción.

```bash
POST /v1/products/transactions/create/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `batch"`      | `id` | **Required** |
| `transaction_type`      | `str` | **entry or exit** |
| `quantity`      | `int` | **Required** |
