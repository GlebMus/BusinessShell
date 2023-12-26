<!-- src/App.vue -->
<template>
  <div id="app">
    <router-view />
    <router-link to="/register">Регистрация</router-link>
    <router-link to="/login">Вход</router-link>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>
