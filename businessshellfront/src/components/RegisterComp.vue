<!-- src/components/Registration.vue -->
<template>
  <div>
    <h2>Регистрация</h2>
    <form @submit.prevent="register">
      <label for="username">Имя пользователя:</label>
      <input type="text" v-model="username" required>
      <br>
      <label for="email">Email:</label>
      <input type="email" v-model="email" required>
      <br>
      <label for="password1">Пароль:</label>
      <input type="password" v-model="password1" required>
      <br>
      <button type="submit">Зарегистрироваться</button>
    </form>
  </div>
</template>

<script>
import api from '@/api';


function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}

function getCSRFToken() {
  return getCookie('csrftoken');
}

export default {
  data() {
    return {
      username: '',
      email: '',
      password1: '',
    };
  },
  methods: {
  register() {
    const data = {
      username: this.username,
      email: this.email,
      password1: this.password1,
    };

    console.log(data);

    const headers = {
      'Content-Type': 'application/json',
      'Authorization': `Token ${localStorage.getItem('token')}`,
      'X-CSRFToken': getCSRFToken(),
    };

    api.post('signup/', data, { headers })
      .then(response => {
        console.log(response.data);
      })
      .catch(error => {
        console.error('Error status:', error.response.status);
        console.error('Error data:', error.response.data);
      });
  },
},
};
</script>
