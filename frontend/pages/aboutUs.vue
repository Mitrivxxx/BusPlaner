<template>
    <div>
      <!-- Pasek górny -->
      <Header />
  
      <!-- Sekcja z informacjami o autorach -->
      <main class="about-content">
        <h1>O nas</h1>
        <p>Strona stworzona na potrzeby zajęć.</p>
        <h3>Autorzy:</h3>
        <ul>
          <li>Mateusz Smaga</li>
          <li>Hubert Ziemba</li>
        </ul>
      </main>
    </div>
  </template>
  
  <script setup>
  import Header from '@/components/Header.vue'
  </script>
  
  <style scoped>
  /* Stylowanie sekcji 'O nas' */
  .about-content {
    padding: 20px;
    margin-top: 20px;
  }
  
  .about-content h1 {
    font-size: 2em;
  }
  
  .about-content h3 {
    margin-top: 20px;
    font-size: 1.5em;
  }
  
  .about-content ul {
    list-style-type: none;
    padding: 0;
  }
  
  .about-content li {
    font-size: 1.2em;
    margin-bottom: 10px;
  }
  </style>
  