<template>
    <div>
      <!-- Pasek górny -->
      <Header />
  
      <!-- Reszta strony -->
      <main class="main-content">
        <h1>Witaj na stronie rozkładów!</h1>
        <!-- Treść strony -->
      </main>
    </div>
  </template>
  
  <script setup>
  import Header from '@/components/Header.vue'
  </script>
  
  <style scoped>
  /* Stylowanie reszty strony */
  .main-content {
    padding: 20px;
    margin-top: 20px;
    color: red;
  }
  </style>
  