<template>
    <title>Вход - Project Manager</title>
    <div class="login-container">
        <div class="logo">
            <h1>Project Manager</h1>
            <p>Войдите в свою учетную запись</p>
        </div>

        <form>
            <div class="form-group">
                <label for="email">Email</label>
                <input 
                    type="email" 
                    id="email" 
                    class="form-control" 
                    placeholder="your@email.com"
                    required
                >
            </div>

            <div class="form-group">
                <label for="password">Пароль</label>
                <input 
                    type="password" 
                    id="password" 
                    class="form-control" 
                    placeholder="Введите пароль"
                    required
                >
            </div>

            <div class="checkbox-group">
                <input type="checkbox" id="remember">
                <label for="remember">Запомнить меня</label>
            </div>

            <button type="submit" class="btn">Войти</button>

            <div class="links">
                <a href="#">Забыли пароль?</a>
                <span> • </span>
                <router-link to="/registration">Регистрация</router-link>
            </div>
        </form>
    </div>
</template>

<style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Arial, sans-serif;
        }

        body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }

        .login-container {
            background: white;
            border-radius: 12px;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 400px;
            padding: 40px;
        }

        .logo {
            text-align: center;
            margin-bottom: 30px;
        }

        .logo h1 {
            color: #2c3e50;
            font-size: 28px;
            font-weight: 600;
            margin-bottom: 8px;
        }

        .logo p {
            color: #7f8c8d;
            font-size: 14px;
        }

        .form-group {
            margin-bottom: 20px;
        }

        .form-group label {
            display: block;
            margin-bottom: 8px;
            color: #2c3e50;
            font-weight: 500;
            font-size: 14px;
        }

        .form-control {
            width: 100%;
            padding: 12px 16px;
            border: 2px solid #e1e5e9;
            border-radius: 8px;
            font-size: 14px;
            transition: border-color 0.3s;
            background: #f8f9fa;
        }

        .form-control:focus {
            outline: none;
            border-color: #3498db;
            background: white;
        }

        .btn {
            width: 100%;
            padding: 12px;
            background: #3498db;
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: background 0.3s;
        }

        .btn:hover {
            background: #2980b9;
        }

        .links {
            text-align: center;
            margin-top: 25px;
            padding-top: 20px;
            border-top: 1px solid #e1e5e9;
        }

        .links a {
            color: #3498db;
            text-decoration: none;
            font-size: 14px;
            transition: color 0.3s;
        }

        .links a:hover {
            color: #2980b9;
            text-decoration: underline;
        }

        .footer {
            text-align: center;
            margin-top: 30px;
            color: rgba(255, 255, 255, 0.8);
            font-size: 12px;
        }

        .checkbox-group {
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 20px;
        }

        .checkbox-group input[type="checkbox"] {
            width: 16px;
            height: 16px;
        }

        .checkbox-group label {
            margin: 0;
            color: #7f8c8d;
            font-size: 14px;
        }
</style>