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
  background-color: var(--accent-green-hover);
  border-color: var(--accent-green-hover);
  color: var(--bg-primary);
}

.btn-primary:hover:not(.btn-disabled) {
  background-color: var(--accent-green-dark);
  border-color: var(--accent-green-dark);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px var(--green-glow-strong);
}

.btn-secondary {
  background-color: var(--bg-gradient-end);
  border-color: var(--border-primary);
  color: var(--text-primary);
}

.btn-secondary:hover:not(.btn-disabled) {
  background-color: var(--bg-tertiary);
  border-color: var(--border-gradient-1);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px var(--shadow-color);
}

.btn-outline {
  background-color: transparent;
  border-color: var(--text-primary);
  color: var(--text-primary);
}

.btn-outline:hover:not(.btn-disabled) {
  background-color: transparent;
  border-color: var(--accent-green-hover);
  color: var(--text-primary);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px var(--green-glow);
  text-shadow: 0 0 8px var(--green-glow);
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
  outline: 2px solid var(--accent-green-hover);
  outline-offset: 2px;
}

/* Responsive */
@media (max-width: 768px) {
  .btn {
    width: 100%;
    min-height: 48px;
  }
  
  .btn-medium {
    padding: 0.875rem 1.5rem;
    font-size: 1rem;
  }

  .btn-large {
    padding: 1rem 1.75rem;
    font-size: 1.125rem;
  }
}

@media (max-width: 480px) {
  .btn {
    min-height: 44px;
  }

  .btn-small {
    padding: 0.625rem 1rem;
    font-size: 0.9rem;
  }

  .btn-medium {
    padding: 0.75rem 1.25rem;
    font-size: 0.95rem;
  }

  .btn-large {
    padding: 0.875rem 1.5rem;
    font-size: 1rem;
  }
}
</style>

