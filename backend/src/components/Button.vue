<script setup>
defineProps({
  variant: {
    type: String,
    default: 'primary', // primary, secondary, outline
    validator: (value) => ['primary', 'secondary', 'outline'].includes(value)
  },
  size: {
    type: String,
    default: 'medium', // small, medium, large
    validator: (value) => ['small', 'medium', 'large'].includes(value)
  },
  disabled: {
    type: Boolean,
    default: false
  },
  href: {
    type: String,
    default: null
  }
})

defineEmits(['click'])
</script>

<template>
  <component 
    :is="href ? 'a' : 'button'"
    :href="href"
    :target="href ? '_blank' : undefined"
    :rel="href ? 'noopener noreferrer' : undefined"
    :disabled="disabled"
    :class="['btn', `btn-${variant}`, `btn-${size}`, { 'btn-disabled': disabled }]"
    @click="$emit('click', $event)"
  >
    <slot />
  </component>
</template>

<style scoped>
.btn {
  font-family: 'Courier New', Courier, Monaco, monospace;
  font-weight: 600;
  border: 2px solid;
  cursor: pointer;
  transition: all 0.3s ease;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  letter-spacing: 0.5px;
}

/* Sizes */
.btn-small {
  padding: 0.5rem 1rem;
  font-size: 0.875rem;
}

.btn-medium {
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
}

.btn-large {
  padding: 1rem 2rem;
  font-size: 1.125rem;
}

/* Variants */
.btn-primary {
  background-color: #00ff00;
  border-color: #00ff00;
  color: #000000;
}

.btn-primary:hover:not(.btn-disabled) {
  background-color: #00cc00;
  border-color: #00cc00;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 255, 0, 0.4);
}

.btn-secondary {
  background-color: #1a1a1a;
  border-color: #333333;
  color: #ffffff;
}

.btn-secondary:hover:not(.btn-disabled) {
  background-color: #2a2a2a;
  border-color: #444444;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(255, 255, 255, 0.1);
}

.btn-outline {
  background-color: transparent;
  border-color: #00ff00;
  color: #00ff00;
}

.btn-outline:hover:not(.btn-disabled) {
  background-color: #00ff00;
  color: #000000;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 255, 0, 0.4);
}

/* Disabled state */
.btn-disabled {
  opacity: 0.5;
  cursor: not-allowed;
  transform: none !important;
  box-shadow: none !important;
}

/* Active state */
.btn:active:not(.btn-disabled) {
  transform: translateY(0);
}

/* Focus state for accessibility */
.btn:focus-visible {
  outline: 2px solid #00ff00;
  outline-offset: 2px;
}

/* Responsive */
@media (max-width: 480px) {
  .btn-large {
    padding: 0.875rem 1.75rem;
    font-size: 1rem;
  }
}
</style>

