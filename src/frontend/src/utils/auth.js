export const auth = {
  // Сохранить токен
  setToken(token) {
    localStorage.setItem('access_token', token)
  },
  
  // Получить токен
  getToken() {
    return localStorage.getItem('access_token')
  },
  
  // Удалить токен
  removeToken() {
    localStorage.removeItem('access_token')
  },
  
  // Проверить наличие токена
  isAuthenticated() {
    return !!this.getToken()
  }
}