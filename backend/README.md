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

## 2. Listado de productos
#### Para obtener el listado de productos, realiza una solicitud GET a:

```bash
http://127.0.0.1:8000/v1/products/
```

## 3. Crear producto
#### Para crear un nuevo producto, realiza una solicitud POST a:

```bash
http://127.0.0.1:8000/v1/products/create/
```

JSON:
```bash
{
    "code": "A!",
    "name": "asas"
}
```

## 4. Listado de lotes
#### Para obtener el listado de lotes, realiza una solicitud GET a:

```bash
http://127.0.0.1:8000/v1/products/batches/
```

## 5. Crear lote
#### Para crear un nuevo lote, realiza una solicitud POST a:

```bash
http://127.0.0.1:8000/v1/products/batches/create/
```

JSON:
```bash
{
    "product": 1,
    "expiration_date": "2024-12-01",
    "quantity": 1
}
```

## 6. Listado de transacciones
#### Para obtener el listado de transacciones, realiza una solicitud GET a:

```bash
http://127.0.0.1:8000/v1/products/transactions/
```

## 7. Crear transacción
#### Puedes elegir entre entry o exit para el tipo de transacción.

```bash
http://127.0.0.1:8000/v1/products/transactions/create/
```

JSON:
```bash
{
"batch": 6,
"transaction_type": "entry",
"quantity": 1
}
```