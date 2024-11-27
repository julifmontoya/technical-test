# Details

## 1. Design:
1. Requirement Identification: I analyzed the project's needs, data flows, and relationships between main entities.
2. Diagramming: I used draw.io to create an ER (Entity-Relationship) diagram, defining entities, attributes, and relationships (1:1, 1:N, N:M).
3. Database Engine: Used sqlite3 as the database engine.
4. Translation to Django Models: Converted entities into Django classes. Implemented relationships using ForeignKey. Added validations and constraints.
5. Schema Generation: Used Django migrations (makemigrations and migrate) to apply the design to the database.
This approach enabled a scalable, clean design that was easy to integrate with DRF

## 2. Key Design Decisions
### Separation of Concerns
The design separates core entities (Product, ProductBatch, Transaction) to ensure each class is responsible for a specific domain aspect:

Product: Represents the product entity, which tracks basic product details and aggregates stock data.
ProductBatch: Manages batches with specific expiration dates and quantities.
Transaction: Tracks inventory movements (entry/exit) for precise stock control.

### Property-Based Logic
- Product.total_quantity aggregates the quantity across all associated batches for real-time stock insights.
- ProductBatch.status dynamically calculates the status of a batch (e.g., "Expired", "Expiring", "Current") based on expiration date.

### Validation on Critical Operations
TransactionCreate validates that exit transactions do not exceed available stock. This ensures data integrity and prevents overselling.

### Efficient Querying
- ProductBatchList leverages select_related to minimize database hits by prefetching related product data.
- ProductBatchDetail filters batches based on the product_code for efficient retrieval of product-specific batches.

### RESTful API Design
CRUD operations are implemented using Django REST Framework (DRF) generic views (ListAPIView, CreateAPIView). This promotes:
- Scalability via standardized endpoints.
- Separation of concerns between data retrieval and mutation.

## 3. Suggestions for Scaling and Improvement
### Pagination and Filtering
Implement pagination for ProductList and TransactionList to handle large datasets efficiently. Add filters for ProductBatchList and TransactionList to allow querying by date range or status.

### Advanced Notifications
Extend ProductBatch status monitoring with automated alerts for expiring or low-stock batches, helping inventory managers take timely actions.

