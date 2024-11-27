<template>
  <div class="max-width">
    <form @submit.prevent="createProduct">
      <h1 class="mb-15">Product details</h1>
      <div class="flex-space-between-wrap">
        <BaseInput
          label="Product Code:"
          placeholder="Escribe el codigo"
          v-model="product.code"
          type="text"
          required
          :dynamicClass="'col48xs'"
        />
        <BaseInput
          label="Product Name:"
          placeholder="Escribe el nombre"
          v-model="product.name"
          type="text"
          required
          :dynamicClass="'col48xs'"
        />
      </div>

      <div v-if="error">
        <p class="error-message">{{ error }}</p>
      </div>

      <div class="text-center">
        <button type="submit" class="btn btn--blue mr-10">Create</button>
        <button type="button" class="btn btn--white" @click="goBack">
          Back
        </button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import service from "../services/service";
import BaseInput from "../components/BaseInput.vue";

const router = useRouter();
const product = ref({
  code: "",
  name: "",
});
const error = ref("");

const createProduct = async () => {
  try {
    const response = await service.post("products/create/", product.value);
    console.log("Product created:", response.data);
    router.push({ name: "productList" });
  } catch (e) {
    error.value = e.response.data.code[0];
    console.log("Error creating product:", e.response);
  }
};

const goBack = () => {
  router.back();
};
</script>
