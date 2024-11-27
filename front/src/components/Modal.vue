<template>
  <transition name="fade">
    <div
      :class="['modal', dynamicAlignmentClass]"
      v-if="open"
      @click="handleClickOutside"
      ref="modalContainer"
    >
      <div class="modal__inner">
        <div :class="['modal__wrap', dynamicPaddingClass]" @click.stop>
          <div class="mb-20 flex-space-between align-center">
            <p class="modal__title">{{ title }}</p>
            <IconCloseModal @click="close" />
          </div>
          <slot />
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import IconCloseModal from "./icons/IconCloseModal.vue";
import { onMounted, onUnmounted, ref, computed } from "vue";

export default {
  props: {
    open: {
      type: Boolean,
      required: true,
    },
    alignment: String,
    title: String,
    padding: String,
  },
  components: {
    IconCloseModal,
  },
  setup(props, { emit }) {
    const modalContainer = ref(null);

    const close = () => emit("update:open", false);

    const handleClose = (event) => {
      if (event.key === "Escape" && props.open) close();
    };
    const handleClickOutside = (event) => {
      if (modalContainer.value && event.target === modalContainer.value)
        close();
    };

    onMounted(() => {
      document.addEventListener("keyup", handleClose);
      document.addEventListener("click", handleClickOutside);
    });

    onUnmounted(() => {
      document.removeEventListener("keyup", handleClose);
      document.removeEventListener("click", handleClickOutside);
    });

    const dynamicAlignmentClass = computed(() => ({
      "modal--top": props.alignment === "top",
      "modal--center": props.alignment === "center",
    }));

    const dynamicPaddingClass = computed(() => {
      return {
        "padd-full": props.padding === "full",
        "padd-sticky-bottom": props.padding === "sticky-bottom",
      };
    });

    return {
      close,
      modalContainer,
      handleClickOutside,
      dynamicAlignmentClass,
      dynamicPaddingClass,
    };
  },
};
</script>

<style scoped>
.modal {
  position: fixed;
  left: 0;
  width: 100%;
  height: 100%;
  overflow-x: hidden;
  overflow-y: auto;
  background-color: rgba(0, 0, 0, 0.4);
  z-index: 2;
}
.modal--top {
  top: 0;
}
.modal--center {
  top: 50%;
  transform: translateY(-50%);
  display: flex;
  justify-content: center;
  align-items: center;
}
.modal__title {
  font-size: 1.3em;
  font-weight: 600;
}
.modal__close {
  width: 1.6em;
  height: 1.6em;
}
.modal__close:hover {
  cursor: pointer;
}
.modal__wrap {
  background-color: #fff;
  border: 1px solid var(--color-border-input);
  box-shadow: 0 4px 8px rgba(68, 68, 68, 0.2);
  border-radius: 4px;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}
.padd-full {
  padding: 15px;
}
.padd-sticky-bottom {
  padding: 15px 15px 0 15px;
}
</style>
