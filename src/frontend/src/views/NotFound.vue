<template>
    <body>
        <router-link to="/" class="link">На главную</router-link>
        <router-link to="/registration" class="link">Регистрация</router-link>
        <router-link to="/authorisation" class="link">Авторизация</router-link>
        <router-link to="/list" class="link">Проекты</router-link>
        <h1 class="link">Такой страницы пока нет</h1>
    </body>
</template>

<style scoped>
    .link {
        text-decoration: none;
        padding: 10px;
        color: aliceblue;
    }
    body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
</style>