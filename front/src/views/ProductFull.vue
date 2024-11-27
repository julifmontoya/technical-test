<template>
  <div class="max-width">
    <h1>Product Batches</h1>

    <!-- Search input to filter by product name -->
    <BaseInput
      label="Filter by Name:"
      placeholder="Escribe el nombre"
      v-model="nameFilter"
      type="text"
      required
    />

    <!-- Table to display filtered products -->
    <table class="product-table">
      <thead>
        <tr>
          <th>Code</th>
          <th>Name</th>
          <th>Expiration Date</th>
          <th>Quantity</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody>
        <!-- Loop through the filtered products and display each one in a table row -->
        <tr v-for="product in filteredProducts" :key="product.id">
          <td>{{ product.code }}</td>
          <td>{{ product.name }}</td>
          <td>{{ product.expiration_date }}</td>
          <td>{{ product.quantity }}</td>
          <td>{{ product.status }}</td>
        </tr>
      </tbody>
    </table>
  </div>
  <!-- Back Button -->
  <div class="text-center">
    <button type="button" class="btn btn--white" @click="goBack">Back</button>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import { useRouter } from "vue-router";
import service from "../services/service";
import BaseInput from "../components/BaseInput.vue";

// Reactive variables
const router = useRouter();
const products = ref([]);
const nameFilter = ref("");

// Go back to previous page
const goBack = () => {
  router.back();
};

// Fetch products from the API
const fetchData = async () => {
  try {
    const response = await service.get("products/batches/");
    console.log("Fetched products:", response.data); // Debug: Check if the data is fetched correctly
    products.value = response.data; // Assign the response data to the products array
  } catch (e) {
    console.log("Error fetching data:", e.message);
  }
};

// Computed property to filter products by name
const filteredProducts = computed(() => {
  console.log("Filtering products", nameFilter.value); // Debug: Check filter logic
  if (!nameFilter.value) {
    return products.value; // If no filter, return all products
  }
  return products.value.filter((product) =>
    product.name.toLowerCase().includes(nameFilter.value.toLowerCase())
  );
});

// Fetch products when the component is mounted
onMounted(() => {
  fetchData();
});
</script>

<style scoped>
@import url("../assets/table.css");
</style>
