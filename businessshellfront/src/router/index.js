import { createRouter, createWebHistory } from 'vue-router';
import Registration from '@/components/RegisterComp.vue';
import Login from '@/components/LoginComp.vue';

const routes = [
  {
    path: '/register',
    name: 'Registration',
    component: Registration,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
