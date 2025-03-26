<template>
    <div>
      <!-- Pasek górny -->
      <Header />
  
      <div class="login-container">
        <h2 class="text-center">Logowanie</h2>
        
        <form @submit.prevent="submitForm" class="login-form">
          <div class="form-group">
            <label for="login">Login</label>
            <input
              v-model="login"
              type="text"
              id="login"
              class="form-control"
              placeholder="Wprowadź login"
              required
            />
          </div>
          
          <div class="form-group">
            <label for="password">Hasło</label>
            <input
              v-model="password"
              type="password"
              id="password"
              class="form-control"
              placeholder="Wprowadź hasło"
              required
            />
          </div>
  
          <div class="form-group">
            <button type="submit" class="btn btn-primary w-full">
              Zaloguj się
            </button>
          </div>
        </form>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import Header from '@/components/Header.vue'
  import { useRouter } from 'vue-router'
  
  const login = ref('')
  const password = ref('')
  const router = useRouter()
  
  const submitForm = () => {
    // Przykładowa logika logowania
    if (login.value === 'user' && password.value === 'password123') {
      router.push('/')
    } else {
      alert('Niepoprawne dane logowania')
    }
  }
  </script>
  
  <style scoped>
  /* Stylowanie paska górnego */
  .login-container {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    background-color: white; /* Przywrócenie białego tła dla kontenera logowania */
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    
  }
  
.login-form{
  align-items: center;
}

  .login-form .form-group {
    margin-bottom: 1rem;
  }
  
  .login-form .btn {
    width: 100%;
  }
  
  .text-center {
    text-align: center;
  }
  
  /* Tło całej strony (dla każdej strony aplikacji) */
  html, body {
    margin: 0;
    padding: 0;
    height: 100%;
    background-color: #f0f0f0; /* Przywrócenie jasnego tła strony */
  }
  
  body {
    font-family: Arial, sans-serif;
  }
  </style>
  