
<template>
    <div>
        <router_view/>
        <header class="header">
            <h1 @click="router.push('/')">Project Manager</h1>
            <router-link class="text-link" to="/authorisation">Авторизация</router-link>
            <router-link class="text-link" to="/projectsCreating">Создать новый проект</router-link>
            <router-link class="text-link" to="/users">Пользователи</router-link>
            <div class="profile">
                <div class="avatar">PM</div>
                <router-link class="text-link" :to="`/profile/${user_id}`">{{ name }}</router-link>
            </div>
            
        </header>

        <div class="container">
            <aside class="sidebar">
                <div class="projects-header">
                    <h2>Проекты</h2>
                </div>
                <div class="projects-list">
                    <div class="project-item active" v-for="project in projects_ref" :key="project.id" @click="getInformation(project)">
                        <div class="project-name">{{ project.title }}</div>
                    </div>
                </div>
            </aside>

            <main class="content">
                <div class="welcome-message" v-if="!project_title">
                    <h2>Добро пожаловать в Project Manager</h2>
                    <p>Выберите проект из списка слева для начала работы</p>
                </div>

                <div class="welcome-message" v-else>
                    <div class="block-main">
                        <h2>{{ project_title }}</h2>
                        <div>Статус: {{ project_status }} </div>  
                        <div>Лидер: 
                            <router-link class="text-link" :to="`profile/${project_leader_id}`" v-if="project_leader_id">{{ project_leader_name }}</router-link>
                            <div v-else>{{ project_leader_name }}</div>
                        </div>
                        <div>
                            Создатель:
                            <router-link class="text-link" :to="`profile/${project_creator_id}`" v-if="project_creator_id">{{ project_creator_name }}</router-link>
                            <div v-else>{{ project_creator_name }}</div>
                        </div>
                    </div>

                    <div class="block-dates">
                        <li>Создан: {{project_created_at}}</li>
                        <li>Запланированное начало: {{ project_start_date }}</li>
                        <li>Дедлайн: {{ project_deadline }}</li>
                    </div>

                    <div class="block-status">
                        <div>{{ project_description }}</div>  

                    </div>
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
        router-link {
            padding: 10px;
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
            background: #a4b1bd;
        }

        .project-item.active {
            background: #2c3e50;
            border-left-color: #3498db;
        }
        .project-item.active:hover {
            background: #677888;
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
            display: flex;
            flex-direction: column; /* Элементы в колонку */
            padding: 30px;
            background: #f8f9fa;
            flex: 1;
            justify-content: flex-start; /* Вертикально сверху */
            align-items: center; /* Горизонтальное центрирование */
        }

        .welcome-message {
            text-align: center;
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

        .block-main {
            padding: 10px;
            border-bottom: 1px solid #3498db;
            text-align: start;
        }

        .block-dates {
            padding: 10px;
            border-bottom: 1px solid #3498db;
            text-align: start;
            color: #2c3e50;
        }
        .block-status {
            padding: 10px;
            border-bottom: 1px solid #3498db;
            text-align: start;
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
    const projects_ref = ref()

    const project_title = ref("")
    const project_description = ref("")
    const project_status = ref("")
    const project_leader_id = ref("")
    const project_leader_name = ref("")
    const project_created_at = ref("")
    const project_deadline = ref("")
    const project_start_date = ref("")
    const project_creator_id = ref("")
    const project_creator_name = ref("")

    const getName = async() => {
        try {
        const response = await api_service.get_name(auth.getToken())
        name.value = response['first_name'] + " " + response['last_name'] ?? "Не указано"
        user_id.value = response['user_id']
        }
        catch (error) {
            if (error.status == '401') {
                router.push('/registration')
            }
            else if (error.status == '500') {
                alert('Ошибка на сервере, попробуйте снова')
            }
        }
    }

    const getProjects = async() => {
        const projects = await api_service.get_projects(auth.getToken())
        projects_ref.value = projects
    }

    onBeforeMount(() => {
    if (auth.getToken() == 'undefined') {
        router.push('/registration')
    }
    else {
        getName()
        getProjects()
    }
    })

    const getInformation = (project) => {
        project_title.value = project.title ?? 'Не указано'
        project_status.value = project.status ?? 'Не указано'
        project_created_at.value = project.created_at ?? 'Не указано'
        project_start_date.value = project.start_date ?? 'Не указано'
        project_description.value = project.description ?? 'Не указано'
        project_deadline.value = project.deadline ?? 'Не указано'
        project_creator_id.value = project.creator_id ?? 'Не указано'
        project_leader_id.value = project.lead_id ?? 'Не указано'
        project_creator_name.value = project.creator_name ?? 'Не указано'
        project_leader_name.value = project.leader_name ?? 'Не указано'
    }
</script>