# Detalles

## 1. Diseño
#### Arquitectura Modular:
- Componentización: Se separaron componentes reutilizables como BaseInput y Modal para mejorar la reutilización y el mantenimiento.
- Servicios Centralizados: El archivo service.js utiliza Axios para centralizar la lógica de llamadas HTTP, facilitando cambios globales como la configuración de baseURL desde variables de entorno.

#### Gestión de Estados con ref y computed:
- Se usaron variables reactivas como products, isOpen y batchData para manejar datos dinámicos.
- Computadas como filteredProducts permiten implementar funcionalidades como el filtrado sin necesidad de lógica compleja adicional.

#### Capa de Presentación:
- Uso de plantillas <template> bien estructuradas para mostrar datos en tablas y formularios.
- Modales e inputs están diseñados para ser reutilizables y adaptables.

#### Interacción con el Usuario:
- Formularios modales y alertas proporcionan un flujo intuitivo de creación y visualización de lotes de productos.
- Enlaces y botones con router-link facilitan la navegación entre vistas.

#### Carga Asíncrona y Modularidad:
- Uso de onMounted para cargar los datos iniciales.
- Métodos de acciones claras (fetchData, submitBatchForm, openBatchModal) garantizan que cada acción esté separada y sea fácil de modificar.

## 2. Mejoras
### Paginación y Filtrado
Incorporar paginación y filtros avanzados desde el servidor para manejar grandes cantidades de datos de productos.

### Mejora interfaz de usuario
- Implementar carga de estado visual (spinners) mientras se buscan datos.
- Mejorar la accesibilidad de los modales
- Formularios con validación más robusta y Soporte para teclado.
