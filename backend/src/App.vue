<script setup>
  import { ref, provide, watch, onMounted } from 'vue';
  import NavBar from '/src/components/NavBar.vue';
  import Intro from '/src/components/Intro.vue';
  import Button from '/src/components/Button.vue';
  import About from '/src/components/About.vue';
  import Tech from '/src/components/Tech.vue';
  import Projects from '/src/components/Projects.vue';
  import Contact from '/src/components/Contact.vue';
  import Footer from '/src/components/Footer.vue';

  const theme = ref('dark');

  const toggleTheme = () => {
    theme.value = theme.value === 'dark' ? 'light' : 'dark';
    localStorage.setItem('theme', theme.value);
  };

  onMounted(() => {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
      theme.value = savedTheme;
    }
  });

  watch(theme, (newTheme) => {
    document.body.className = newTheme;
  }, { immediate: true });

  provide('theme', theme);
  provide('toggleTheme', toggleTheme);
</script>

<template>
  <NavBar />
  <Intro />
  <About />
  <Tech />
  <Projects />
  <Contact />
  <Footer />
</template>

<style>
  /* Global styles can be added here */
</style>