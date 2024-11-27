# Details

## 1. Design
#### Modular Architecture:
- Componentization: Reusable components like BaseInput and Modal were separated to improve reusability and maintainability.
- Centralized Services: The service.js file uses Axios to centralize HTTP request logic, simplifying global changes such as configuring the baseURL from environment variables.

#### State Management with ref and computed:
- Reactive variables such as products, isOpen, and batchData were used to handle dynamic data.
- Computed properties like filteredProducts enable functionalities such as filtering without the need for additional complex logic.

#### Presentation Layer:
- Well-structured <template> blocks are used to display data in tables and forms.
- Modals and inputs are designed to be reusable and adaptable.

#### User Interaction:
- Modal forms and alerts provide an intuitive flow for creating and viewing product batches
- Links and buttons using router-link facilitate navigation between views.

#### Asynchronous Loading and Modularity:
- onMounted is used to load initial data.
- Clear action methods (fetchData, submitBatchForm, openBatchModal) ensure that each action is separate and easy to modify

## 2. Improvements
### Pagination and Filtering
Incorporate pagination and advanced filtering from the server to handle large amounts of product data.

### Mejora interfaz de usuario
- Implement visual loading states (spinners) while fetching data.
- Improve modal accessibility.
- Enhance form validation for robustness and add keyboard support.
