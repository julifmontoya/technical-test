<template>
    <div :class="['mb-15', dynamicClass]">
      <label class="form-label">{{ label }}</label>
      <input
        v-bind="$attrs"
        :placeholder="placeholder"
        :value="modelValue"
        @input="$emit('update:modelValue', $event.target.value)"
        class="form-control"
      />
     </div>
  </template>
  
  <script>
  export default {
    props: {
      modelValue: {
        type: [String, Number],
        default: "",
      },
      placeholder: String,
      label: String,
      dynamicClass: String
    },
  };
  </script>
  