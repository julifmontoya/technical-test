# Detalles

## 1. Diseño
1. Identificación de Requisitos: Analicé las necesidades del proyecto, los flujos de datos y las relaciones entre entidades principales.
2. Diagramación: Utilicé draw.io para crear un esquema ER (Entidad-Relación) y definir las entidades, atributos y relaciones (1:1, 1:N, N:M).
3. Use sqlite3 como motor de la base de datos.
4. Traducción a Modelos Django: Convertí las entidades en clases Django. Implementé relaciones con ForeignKey. Añadí validaciones y restricciones.
5. Generación del Esquema: Usé migraciones de Django (makemigrations y migrate) para aplicar el diseño a la base de datos.
Esto permitió un diseño escalable, limpio y fácil de integrar con DRF.

## 2. Implementacion
### Separación de Responsabilidades
El diseño separa las entidades principales (Product, ProductBatch, Transaction) para asegurar que cada clase sea responsable de un aspecto específico del dominio:

- Product: Representa la entidad del producto, rastreando detalles básicos del mismo y agregando datos de inventario.
- LoteProducto: Gestiona los lotes con fechas de vencimiento específicas y cantidades.
- Transacción: Rastrea los movimientos de inventario (entrada/salida) para un control preciso del stock.

### Lógica Basada en Propiedades
- Product.total_quantity: Agrega la cantidad de todos los lotes asociados para ofrecer una visión en tiempo real del inventario.
- ProductBatch.status: Calcula dinámicamente el estado de un lote (por ejemplo, "Vencido", "Próximo a vencer", "Actual") en función de la fecha de vencimiento.

### Validaciones
TransactionCreate valida que las transacciones de salida no excedan el stock disponible. Esto garantiza la integridad de los datos y previene la sobreventa.

### Consultas Eficientes
- ProductBatchList utiliza select_related para minimizar el número de accesos a la base de datos, pre-cargando datos relacionados de productos.
- ProductBatchDetail filtra lotes en función del product_code, lo que permite una recuperación eficiente de lotes específicos por producto.

### Diseño de API RESTful
Las operaciones CRUD se implementan utilizando vistas genéricas de Django REST Framework (DRF), como ListAPIView y CreateAPIView. Esto fomenta:
- Escalabilidad a través de endpoints estandarizados.
- Separación de responsabilidades entre la recuperación y la mutación de datos.

## 3. Mejoras
### Paginación y Filtrado
Implementar paginación para ProductList y TransactionList para manejar de manera eficiente grandes volúmenes de datos. Agregar filtros a ProductBatchList y TransactionList que permitan realizar consultas por rango de fechas o estado.

### Notificaciones Avanzadas
Extiende el monitoreo del estado de ProductBatch con alertas automáticas para lotes próximos a expirar o con bajo inventario, ayudando a los responsables de inventario a tomar acciones oportunas. Celery seria una opciona  considerar.

