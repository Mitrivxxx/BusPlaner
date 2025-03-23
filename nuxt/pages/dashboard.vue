<template>
    <div>
      <h1>Dashboard</h1>
      <p>Witaj na stronie Dashboard!</p>
    </div>
  </template>
  
  <script setup>
  import { useRouter } from 'vue-router'
  import { onMounted } from 'vue'
  
  const router = useRouter()
  
  onMounted(() => {
    const token = localStorage.getItem('access_token')
    
    if (!token) {
      router.push('/login')  // Jeśli brak tokenu, przekieruj do strony logowania
    }
  })
  </script>
  