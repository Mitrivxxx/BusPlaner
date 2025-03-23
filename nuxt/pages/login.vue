<template>
  <div>
    <form @submit.prevent="login">
      <input type="email" v-model="email" placeholder="Email" required />
      <input type="password" v-model="password" placeholder="Hasło" required />
      <button type="submit">Zaloguj</button>
    </form>
    <p v-if="error">{{ error }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const email = ref('')
const password = ref('')
const error = ref<string | null>(null)
const router = useRouter()

const login = async () => {
  error.value = null  // Resetuj błąd przed próbą logowania

  // Wywołanie API do logowania za pomocą useFetch
  const { data, error: fetchError } = await useFetch('http://localhost:8000/api/token/', {
    method: 'POST',
    body: {
      email: email.value,
      password: password.value
    },
  })

  // Obsługa błędów
  if (fetchError.value) {
    error.value = 'Nieprawidłowe dane logowania'
    return
  }

  // Zapisz token w localStorage
  if (data.value?.access) {
    localStorage.setItem('access_token', data.value.access)
    // Po zalogowaniu przekieruj do dashboardu
    router.push('/dashboard')
  } else {
    error.value = 'Błąd logowania'
  }
}
</script>
