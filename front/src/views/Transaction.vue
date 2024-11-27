<template>
  <div class="max-width">
    <!-- Product Selection -->
    <div class="mb-15">
      <label for="product" class="form-label">Lotes</label>
      <select v-model="selectedProduct" id="product">
        <option v-for="batch in batches" :key="batch.id" :value="batch.id">
          {{ batch.name }} ({{ batch.expiration_date }})
        </option>
      </select>
    </div>
    <div class="mb-15">
      <label for="transaction_type" class="form-label">Transaccion</label>
      <select v-model="transaction_type" id="transaction_type">
        <option value="entry">Entrada</option>
        <option value="exit">Salida</option>
      </select>
    </div>
    <div class="mb-15">
      <label for="quantity" class="form-label">Cantidad</label>
      <input type="number" v-model="quantity" id="quantity" />
    </div>
    <div class="mb-15">
      <button type="button" class="btn btn--blue" @click="submitForm">
        Enviar
      </button>
    </div>

    <!-- Transactions Table -->
    <h1 class="mb-15">Entradas y salidas</h1>
    <table class="transaction-table">
      <thead>
        <tr>
          <th>Codigo</th>
          <th>Nombre</th>
          <th>Transaccion</th>
          <th>Cantidad</th>
          <th>Cantidad total</th>
          <th>Fecha</th>
        </tr>
      </thead>
      <tbody>
        <!-- Loop through the transactions and display each row -->
        <tr v-for="transaction in transactions" :key="transaction.id">
          <td>{{ transaction.code }}</td>
          <td>{{ transaction.name }}</td>
           <td>{{ transaction.transaction_type }}</td>
          <td>{{ transaction.quantity }}</td>
          <td>{{ transaction.total_quantity }}</td>
          <td>{{ formatTimestamp(transaction.timestamp) }}</td>
        </tr>
      </tbody>
    </table>

    <!-- Back Button -->
    <div class="text-center">
      <button type="button" class="btn btn--white" @click="goBack">Atras</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import service from "../services/service";

// Reactive variables
const router = useRouter();
const transactions = ref([]);
const batches = ref([]);
const selectedProduct = ref(null);
const quantity = ref(null);
const transaction_type = ref(null);

// Format timestamp function
const formatTimestamp = (timestamp) => {
  const date = new Date(timestamp);
  return date.toLocaleString(); // Formats to local date and time
};

// Fetch transactions data
const fetchData = async () => {
  try {
    const response = await service.get("products/transactions/");
    transactions.value = response.data;
  } catch (e) {
    console.log("Error fetching data:", e.message);
  }
};

// Fetch batches data
const fetchBatches = async () => {
  try {
    const response = await service.get("products/batches/");
    batches.value = response.data;
  } catch (e) {
    console.log("Error fetching batches:", e.message);
  }
};

// Fetch both transactions and batches on component mount
onMounted(() => {
  fetchData();
  fetchBatches(); // Call this method to fetch batches
});

// Submit the form data
const submitForm = async () => {
  if (!selectedProduct.value || !transaction_type.value || !quantity.value) {
    alert("Please fill out all fields.");
    return;
  }

  try {
    const response = await service.post("products/transactions/create/", {
      batch: selectedProduct.value,
      transaction_type: transaction_type.value,
      quantity: quantity.value,
    });
    console.log("Transaction submitted successfully:", response.data);
    fetchData();
  } catch (e) {
    console.log("Error submitting transaction:", e.message);
  }
};

// Go back to previous page
const goBack = () => {
  router.back();
};
</script>

<style scoped>
@import url("../assets/table.css");
</style>
