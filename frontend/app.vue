<template>
  <NuxtPage />
</template>

<script setup>
import { useRouter } from 'vue-router'
import { onMounted } from 'vue'

// Gdy komponent 'app.vue' zostanie zamontowany, wykonaj przekierowanie
onMounted(() => {
  const router = useRouter()
  router.push('/')  // Przekierowanie do strony 'index.vue'
})
</script>
