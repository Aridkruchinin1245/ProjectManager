<template>
    <router-link to="/">На главную</router-link>
    <button @click="delete_projects()">Удалить все проекты</button>
    <button @click="delete_users()">Удалить всех юзеров</button>
</template>

<script setup>
import { api_service } from '@/services/api';
import { auth } from '@/utils/auth';

    const delete_projects = async() => {
        await api_service.delete_projects(auth.getToken())
    }
    const delete_users = async() => {
        await api_service.delete_users(auth.getToken())
    }
</script>