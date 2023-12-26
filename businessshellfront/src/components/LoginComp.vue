<!-- src/components/Login.vue -->
<template>
  <div>
    <h2>Вход</h2>
    <form @submit.prevent="login">
      <label for="username">Имя пользователя:</label>
      <input type="text" v-model="username" required>
      <br>
      <label for="password">Пароль:</label>
      <input type="password" v-model="password" required>
      <br>
      <button type="submit">Войти</button>
    </form>
  </div>
</template>

<script>
import api from '@/api';

export default {
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    login() {
      const data = {
        username: this.username,
        password: this.password,
      };

      api.post('dj-rest-auth/registration/', data)
      .then(response => {
        console.log(response.data);
      })
      .catch(error => {
        console.error(error.response.data);
      });
    },
  },
};
</script>
