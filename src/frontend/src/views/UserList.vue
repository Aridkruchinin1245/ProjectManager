<template>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Список пользователей - Project Manager</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    </head>
    <body>
        <div class="users-container">
            <div class="page-header">
                <div class="page-title">
                    <h1>Список пользователей</h1>
                    <div class="subtitle">Все участники проекта</div>
                </div>
                <router-link to="/list" class="back-btn">
                    <i class="fas fa-arrow-left"></i>
                    Назад к проектам
                </router-link>

                <router-link to="/list" class="back-btn">
                    <i class="fas"></i>
                    Создать команду
                </router-link>
            </div>

            <div class="filters">
                <div class="search-box">
                    <i class="fas fa-search search-icon"></i>
                    <input type="text" placeholder="Поиск пользователей...">
                </div>
                <select class="filter-select">
                    <option value="all">Все роли</option>
                    <option>CEO (Chief Executive Officer)</option>
                    <option>CTO (Chief Technology Officer)</option>
                    <option>CIO (Chief Information Officer)</option>
                    <option>Head of Development</option>
                    <option>Head of Product</option>
                    <option>Product Owner</option>
                    <option>Product Manager</option>
                    <option>Project Manager</option>
                    <option>Program Manager</option>
                    <option>Scrum Master</option>
                    <option>Business Analyst</option>
                    <option>Systems Analyst</option>
                    <option>Product Analyst</option>
                    <option>Data Analyst</option>
                    <option>BI Analyst</option>
                    <option>Software Architect</option>
                    <option>Solution Architect</option>
                    <option>Data Architect</option>
                    <option>Tech Lead</option>
                    <option>Team Lead</option>
                    <option>Engineering Manager</option>
                    <option>Backend Developer</option>
                    <option>Frontend Developer</option>
                    <option>Full Stack Developer</option>
                    <option>Java Developer</option>
                    <option>Python Developer</option>
                    <option>C# / .NET Developer</option>
                    <option>Go Developer</option>
                    <option>PHP Developer</option>
                        <option>Node.js Developer</option>
                        <option>iOS Developer</option>
                        <option>Android Developer</option>
                        <option>React Developer</option>
                        <option>Vue.js Developer</option>
                        <option>Data Scientist</option>
                        <option>Data Engineer</option>
                        <option>ML Engineer</option>
                        <option>QA Engineer (Manual)</option>
                        <option>QA Automation Engineer</option>
                        <option>DevOps Engineer</option>
                        <option>System Administrator</option>
                        <option>SRE (Site Reliability Engineer)</option>
                        <option>Security Engineer</option>
                        <option>Cloud Engineer</option>
                        <option>UX/UI Designer</option>
                        <option>Product Designer</option>
                        <option>UX Researcher</option>
                        <option>Technical Writer</option>
                        <option>SEO Specialist</option>
                        <option>Delivery Manager</option>
                        <option>Customer Success Manager</option>
                        <option>Tech Support Engineer</option>
                        <option>IT Specialist</option>
                </select>
                <select class="filter-select">
                    <option value="active">Активные</option>
                    <option value="all">Все</option>
                    <option value="inactive">Неактивные</option>
                </select>
            </div>

            <div class="users-grid">
                <!-- Пользователь -->
                <div class="user-card" v-for="user_card in user_data" :key="user_card.user_id" @click="router.push(`/profile/${user_card.user_id}`)">
                    <div class="user-avatar" @click="router.push('/')" style="background-color: #3498db;">ИФ</div>
                    <div class="user-info">
                        <div class="user-name">{{ user_card.first_name }} {{ user_card.last_name }}</div>
                        <div class="user-role">Project Manager</div>
                        <div class="user-meta">
                            <div class="user-meta-item">
                                <i class="fas fa-envelope"></i>
                                <span>{{ user_card.email }}</span>
                            </div>
                            <div class="user-meta-item">
                                <i class="fas fa-briefcase"></i>
                                <span>В разработке</span>
                            </div>
                        </div>
                        <div class="user-stats">
                            <div class="user-stat">
                                <div class="user-stat-number">В разработке</div>
                                <div class="user-stat-label">Проектов</div>
                            </div>
                            <div class="user-stat">
                                <div class="user-stat-number">В разработке</div>
                                <div class="user-stat-label">Задач</div>
                            </div>
                            <div class="user-stat">
                                <div class="user-stat-number">В разработке</div>
                                <div class="user-stat-label">Успешных</div>
                            </div>
                        </div>
                    </div>
                </div>
        </div>
        </div>
    </body>
    </html>
</template>


 <style scoped>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Arial, sans-serif;
        }

        body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }

        .users-container {
            background: white;
            border-radius: 12px;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 40px;
        }

        .page-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 30px;
            padding-bottom: 20px;
            border-bottom: 1px solid #e1e5e9;
        }

        .page-title h1 {
            color: #2c3e50;
            font-size: 32px;
            font-weight: 600;
            margin-bottom: 5px;
        }

        .page-title .subtitle {
            color: #7f8c8d;
            font-size: 16px;
        }

        .back-btn {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            color: #3498db;
            text-decoration: none;
            font-weight: 500;
            padding: 10px 16px;
            border-radius: 6px;
            transition: all 0.3s;
            border: 1px solid #e1e5e9;
        }

        .back-btn:hover {
            background-color: #f8f9fa;
            color: #2980b9;
        }

        .filters {
            display: flex;
            justify-content: space-between;
            margin-bottom: 30px;
            gap: 20px;
        }

        .search-box {
            flex: 1;
            position: relative;
        }

        .search-box input {
            width: 100%;
            padding: 12px 16px 12px 45px;
            border: 1px solid #e1e5e9;
            border-radius: 8px;
            font-size: 16px;
            transition: border-color 0.3s;
        }

        .search-box input:focus {
            outline: none;
            border-color: #3498db;
        }

        .search-icon {
            position: absolute;
            left: 16px;
            top: 50%;
            transform: translateY(-50%);
            color: #7f8c8d;
        }

        .filter-select {
            padding: 12px 16px;
            border: 1px solid #e1e5e9;
            border-radius: 8px;
            font-size: 16px;
            background-color: white;
            color: #2c3e50;
            cursor: pointer;
        }

        .filter-select:focus {
            outline: none;
            border-color: #3498db;
        }

        .users-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 25px;
        }

        .user-card {
            background: white;
            border-radius: 10px;
            padding: 20px;
            border: 1px solid #e1e5e9;
            transition: all 0.3s;
            display: flex;
            gap: 15px;
            align-items: center;
        }

        .user-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08);
            border-color: #3498db;
        }

        .user-avatar {
            width: 70px;
            height: 70px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 24px;
            font-weight: bold;
            flex-shrink: 0;
        }

        .user-info {
            flex: 1;
        }

        .user-name {
            color: #2c3e50;
            font-size: 18px;
            font-weight: 600;
            margin-bottom: 4px;
        }

        .user-role {
            color: #3498db;
            font-size: 14px;
            font-weight: 500;
            margin-bottom: 8px;
        }

        .user-meta {
            display: flex;
            flex-direction: column;
            gap: 4px;
        }

        .user-meta-item {
            display: flex;
            align-items: center;
            gap: 8px;
            color: #7f8c8d;
            font-size: 13px;
        }

        .user-meta-item i {
            width: 16px;
            text-align: center;
        }

        .user-stats {
            display: flex;
            gap: 15px;
            margin-top: 12px;
        }

        .user-stat {
            text-align: center;
        }

        .user-stat-number {
            color: #3498db;
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 2px;
        }

        .user-stat-label {
            color: #7f8c8d;
            font-size: 11px;
        }

        .pagination {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 40px;
            gap: 15px;
        }

        .pagination-btn {
            padding: 10px 16px;
            border: 1px solid #e1e5e9;
            border-radius: 6px;
            background: white;
            color: #2c3e50;
            cursor: pointer;
            transition: all 0.3s;
        }

        .pagination-btn:hover {
            background-color: #f8f9fa;
            border-color: #3498db;
        }

        .pagination-btn.active {
            background-color: #3498db;
            color: white;
            border-color: #3498db;
        }

        .pagination-btn.disabled {
            color: #bdc3c7;
            cursor: not-allowed;
        }

        .pagination-btn.disabled:hover {
            background-color: white;
            border-color: #e1e5e9;
        }

        @media (max-width: 992px) {
            .users-grid {
                grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            }
        }

        @media (max-width: 768px) {
            .users-container {
                padding: 25px 20px;
            }
            
            .page-header {
                flex-direction: column;
                align-items: flex-start;
                gap: 15px;
            }
            
            .filters {
                flex-direction: column;
            }
            
            .users-grid {
                grid-template-columns: 1fr;
            }
        }

        @media (max-width: 480px) {
            .user-card {
                flex-direction: column;
                text-align: center;
            }
            
            .user-stats {
                justify-content: center;
            }
        }
</style>

<script setup>
    import { useRouter } from 'vue-router';
    import { auth } from '@/utils/auth';
    import { onBeforeMount, ref } from 'vue';
    import { api_service } from '@/services/api';

    const router = useRouter()

    const user_data = ref([])

    const get_data = async() => {
        try {
            const data = await api_service.all_users(auth.getToken())
            user_data.value = data
        }
        catch (error) {
            if (error.status == '401') {
                router.push('/registration')
            }
            if (error.status == '500') {
                alert(error)
            }
        }
    }

    onBeforeMount(() => {
    if (auth.getToken() == 'undefined') {
        router.push('/registration')
    }
    else {
        get_data()
    }
    })
    
</script>