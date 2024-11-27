# Details

## 1. Design
#### Modular Architecture:
- Componentization: Reusable components like BaseInput and Modal were separated to improve reusability and maintainability.
- Centralized Services: The service.js file uses Axios to centralize HTTP request logic, simplifying global changes such as configuring the baseURL from environment variables.

#### State Management with ref and computed:
- Reactive variables such as products, isOpen, and batchData were used to handle dynamic data.
- Computed properties like filteredProducts enable functionalities such as filtering without the need for additional complex logic.
