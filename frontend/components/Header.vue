<!-- components/Header.vue -->
<template>
    <header class="header">
      <div class="logo">
        <a href="/" alt="BusPlaner">BusPlaner</a>
      </div>
      <nav class="navbar">
        <ul>
          <li><NuxtLink to="/">Rozkłady</NuxtLink></li>
          <li><NuxtLink to="/aboutUs">O nas</NuxtLink></li>
        </ul>
      </nav>
      <div class="login-button">
        <button @click="login">Logowanie</button>
      </div>
    </header>
  </template>
  
  <script setup>
  import { useRouter } from 'vue-router'
  
  const router = useRouter()
  
  // Funkcja logowania (przekierowanie na stronę login.vue)
  const login = () => {
    router.push('/login')  // Przekierowanie do strony logowania
  }
  </script>
  
  <style scoped>
  /* Stylowanie paska górnego */
  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #333;
    padding: 10px 20px;
  }
  
  .logo a {
    color: white;
    font-size: 24px;
    text-decoration: none;
  }
  
  .navbar ul {
    display: flex;
    list-style-type: none;
    margin: 0;
    padding: 0;
  }
  
  .navbar li {
    margin-left: 20px;
  }
  
  .navbar a {
    color: white;
    text-decoration: none;
    font-size: 18px;
  }
  
  .navbar a:hover {
    text-decoration: underline;
  }
  
  /* Stylowanie przycisku logowania */
  .login-button button {
    background-color: #4CAF50;
    color: white;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
    border-radius: 5px;
  }
  
  .login-button button:hover {
    background-color: #45a049;
  }
  </style>
  