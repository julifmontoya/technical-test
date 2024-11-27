import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "productList",
      component: () => import("../views/ProductList.vue"),
    },
    {
      path: "/full",
      name: "productFull",
      component: () => import("../views/ProductFull.vue"),
    },
    {
      path: "/product-create",
      name: "productCreate",
      component: () => import("../views/ProductCreate.vue"),
    },
    {
      path: "/transactions",
      name: "Transaction",
      component: () => import("../views/Transaction.vue"),
    },
  ],
});

export default router;
