import axios from 'axios';

function getCSRFToken() {
  return getCookie('csrftoken');
}

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}

const api = axios.create({
  baseURL: 'http://localhost:8000/accounts/',
  withCredentials: true,
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Token ${localStorage.getItem('token')}`,
    'X-CSRFToken': getCSRFToken(),
  },
});

export default api;