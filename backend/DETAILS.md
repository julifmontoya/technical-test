# Detalles

## 1. Diseño
1. Identificación de Requisitos: Analicé las necesidades del proyecto, los flujos de datos y las relaciones entre entidades principales.
2. Diagramación: Utilicé draw.io para crear un esquema ER (Entidad-Relación) y definir las entidades, atributos y relaciones (1:1, 1:N, N:M).
3. Traducción a Modelos Django: Convertí las entidades en clases Django. Implementé relaciones con ForeignKey. Añadí validaciones y restricciones.
4. Generación del Esquema: Usé migraciones de Django (makemigrations y migrate) para aplicar el diseño a la base de datos.
Esto permitió un diseño escalable, limpio y fácil de integrar con DRF.

## 2. Implementacion

### Separación de Responsabilidades
El diseño separa las entidades principales (Product, ProductBatch, Transaction) para asegurar que cada clase sea responsable de un aspecto específico del dominio:

- Product: Representa la entidad del producto, rastreando detalles básicos del mismo y agregando datos de inventario.
- LoteProducto: Gestiona los lotes con fechas de vencimiento específicas y cantidades.
- Transacción: Rastrea los movimientos de inventario (entrada/salida) para un control preciso del stock.


## 3. Mejoras