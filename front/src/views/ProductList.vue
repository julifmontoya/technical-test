<template>
  <div class="max-width">
    <p class="mb-15">Listo para gestionar tu inventario?.</p>
    <router-link to="/transactions">- Entradas y salidas</router-link>
    <p>
      - Ver tu Lista por:
      <router-link to="/">
        <a>Producto</a>
      </router-link>
      |
      <router-link to="/full">
        <a>Full</a>
      </router-link>
    </p>
    <p class="mb-15">- Crea un Nuevo Producto</p>
    <router-link to="/product-create">
      <a class="btn btn--white">Crear</a>
    </router-link>

    <!-- Search Input -->
    <div class="mt-15">
      <BaseInput
        label="Filtrar:"
        placeholder="Escribe el nombre"
        v-model="searchQuery"
        type="text"
        required
      />
    </div>

    <table>
      <thead>
        <tr>
          <th>Codigo</th>
          <th>Nombre</th>
          <th>Cantidad Total</th>
          <th>Lote</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="product in filteredProducts" :key="product.id">
          <td>{{ product.code }}</td>
          <td>{{ product.name }}</td>
          <td>{{ product.total_quantity }}</td>
          <td>
            <a class="sbox-modal" @click="openAddBatchModal(product.id)"
              >Agregar</a
            >
            -
            <a class="sbox-modal" @click="openBatchModal(product.code)">Ver</a>
          </td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- ModalAdd -->
  <Modal
    v-model:open="isOpen"
    :alignment="'center'"
    :padding="'full'"
    :title="'Lotes'"
  >
    <div class="modal__content">
      <form @submit.prevent="submitBatchForm">
        <BaseInput
          label="Fecha vencimiento:"
          v-model="expirationDate"
          type="date"
          required
        />
        <BaseInput
          label="Cantidad:"
          v-model="quantity"
          type="number"
          required
        />
        <div class="text-center">
          <button type="submit" class="btn btn--blue">Enviar</button>
        </div>
      </form>
    </div>
  </Modal>

  <!-- ModalBatch -->
  <Modal
    v-model:open="isOpenSecond"
    :alignment="'center'"
    :padding="'full'"
    :title="'Lotes'"
  >
    <div class="modal__content">
      <table v-if="batchData.length > 0">
        <thead>
          <tr>
            <th>Vencimiento</th>
            <th>Cantidad</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="batch in batchData" :key="batch.id">
            <td>{{ batch.expiration_date }}</td>
            <td>{{ batch.quantity }}</td>
            <td>{{ batch.status }}</td>
          </tr>
        </tbody>
      </table>
      <p v-else>No hay lotes disponibles para este producto.</p>
    </div>
  </Modal>
</template>

<script setup>
import { ref, onMounted, computed } from "vue";
import service from "../services/service";
import Modal from "../components/Modal.vue";
import BaseInput from "../components/BaseInput.vue";

// Reactive variables
const products = ref([]);
const isOpen = ref(false);
const isOpenSecond = ref(false);
const productId = ref(null);
const expirationDate = ref(null);
const quantity = ref(null);
const productCode = ref(null);
const batchData = ref([]);
const searchQuery = ref(""); // User input for search

// Fetch products
const fetchData = async () => {
  try {
    const response = await service.get("products/");
    products.value = response.data;
  } catch (e) {
    console.log("Error fetching data:", e.message);
  }
};

onMounted(() => {
  fetchData();
});

// Filter products based on searchQuery
const filteredProducts = computed(() => {
  return products.value.filter((product) => {
    return product.name.toLowerCase().includes(searchQuery.value.toLowerCase());
  });
});

// Modal
const openAddBatchModal = (product) => {
  productId.value = product;
  isOpen.value = true;
  expirationDate.value = "";
  quantity.value = "";
};

const openBatchModal = async (productCode) => {
  try {
    const response = await service.get(`products/batches/${productCode}/`);
    batchData.value = response.data; // Set the batch data
    isOpenSecond.value = true;
  } catch (e) {
    console.log("Error fetching batch data:", e.message);
  }
};

const submitBatchForm = async () => {
  try {
    const response = await service.post("products/batches/create/", {
      product: productId.value,
      expiration_date: expirationDate.value,
      quantity: quantity.value,
    });
    alert("Batch created successfully!");
    isOpen.value = false;
    fetchData(); // Re-fetch the products if needed
  } catch (e) {
    console.log("Error creating batch:", e.message);
    alert("Failed to create batch.");
  }
};
</script>

<style scoped>
@import url("../assets/table.css");
</style>
