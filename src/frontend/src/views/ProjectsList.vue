
<template>
    <div>
        <router_view/>
        <header class="header">
            <h1>Project Manager</h1>
            <router-link class="text-link" to="/authorisation">Авторизация</router-link>
            <router-link class="text-link" to="/projectsCreating">Создать новый проект</router-link>
            <div class="profile">
                <div class="avatar">PM</div>
                <router-link class="text-link" :to="`/profile/${user_id}`">{{ name }}</router-link>
            </div>
            
        </header>

        <div class="container">
            <aside class="sidebar">
                <div class="projects-header">
                    <h2>Мои проекты</h2>
                </div>
                <div class="projects-list">
                    <div class="project-item active">
                        <div class="project-name">Веб-сайт компании</div>
                        <div class="project-meta">12 задач • 3 участника</div>
                    </div>
                </div>
            </aside>

            <main class="content">
                <div class="welcome-message">
                    <h2>Добро пожаловать в Project Manager</h2>
                    <p>Выберите проект из списка слева для начала работы</p>
                </div>
            </main>
        </div>
    </div>
</template>


 <style scoped>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Arial, sans-serif;
        }

        body {
            display: flex;
            flex-direction: column;
            height: 100vh;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }

        .header {
            background: #ffffff;
            padding: 15px 30px;
            border-bottom: 1px solid #e1e5e9;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }

        .header h1 {
            color: #2c3e50;
            font-size: 24px;
            font-weight: 600;
        }

        .profile {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .avatar {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: #3498db;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: bold;
        }

        .container {
            display: flex;
            flex: 1;
            overflow: hidden;
        }

        .sidebar {
            width: 280px;
            background: #2c3e50;
            color: white;
            display: flex;
            flex-direction: column;
            height: 100vh;
        }

        .projects-header {
            padding: 20px;
            border-bottom: 1px solid #34495e;
        }

        .projects-header h2 {
            font-size: 18px;
            font-weight: 500;
        }

        .projects-list {
            flex: 1;
            overflow-y: auto;
            padding: 10px 0;
        }

        .project-item {
            padding: 12px 20px;
            cursor: pointer;
            transition: background 0.2s;
            border-left: 3px solid transparent;
        }

        .project-item:hover {
            background: #34495e;
        }

        .project-item.active {
            background: #34495e;
            border-left-color: #3498db;
        }

        .project-name {
            font-weight: 500;
            margin-bottom: 4px;
        }

        .project-meta {
            font-size: 12px;
            color: #bdc3c7;
        }

        .content {
            flex: 1;
            padding: 30px;
            background: #f8f9fa;
            overflow-y: auto;
        }

        .welcome-message {
            text-align: center;
            margin-top: 100px;
            color: #7f8c8d;
        }

        .welcome-message h2 {
            font-size: 28px;
            margin-bottom: 10px;
            color: #2c3e50;
        }

        .text-link {
            color: black;
            text-decoration: none;
        }
    </style>


<script setup>
    import { useRouter } from 'vue-router';
    import { auth } from '@/utils/auth';
    import { onBeforeMount, ref } from 'vue';
    import { api_service } from '@/services/api';

    const router = useRouter()
    
    const name = ref("")
    const user_id = ref("")

    const getName = async() => {
        const response = await api_service.get_name(auth.getToken())
        name.value = response['first_name'] + " " + response['last_name'] ?? "Не указано"
        user_id.value = response['user_id']
    }

    onBeforeMount(() => {
    if (auth.getToken() == 'undefined') {
        router.push('/registration')
    }
    else {
        getName()
    }
    })
</script>