
import axios from 'axios'
import router from '@/router'

const API = axios.create({
  baseURL: process.env.VUE_APP_API_URL || 'http://192.168.1.3:8000', // <=== insert there
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
}
})
// запросы
API.interceptors.request.use(
  (config) => {
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)
// ответы
API.interceptors.response.use(
  (response) => {
    return response.data
  },
  (error) => {
    if (error.response && error.response.status === 401) {
      // Перенаправление на страницу регистрации
      router.push('/registration')
    }
    else if (error.response && error.response.status === 500) {
      alert('Ошибка на сервере, уже работаем над ее исправлением')
    }
    return Promise.reject(error)
  }
)

export const api_service = {
    async send_registration_data(first_name, last_name, email, password) {
        const response = await API.post('/registration', 
            {'first_name':first_name, 'last_name':last_name, 'email':email, 'password':password}
        )
        return response
    },

    async send_authorisation_data(email, password) {
      const response = await API.post('/authorisation',
        {'email':email,
          'password':password
        })

        return response
    },

    async get_name(token) {
      const response = await API.get('/get_name', {
      headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    }})
      return response
    },
 
    // async send_project_data(token, title, description, selected_team, deadline) {
    //   const response = await API.post('/projectCreating', {title}, {
    //   headers: {
    //   'Authorization': `Bearer ${token}`,
    //   'Content-Type': 'application/json'
    //   }})
    //     return response
    //   },
    }