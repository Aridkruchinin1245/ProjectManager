
<template>
<title>Профиль - Project Manager</title>
    <div class="profile-container">
        <router-link class="back-btn" to="/list">← Назад к проектам</router-link>
        
        <div class="profile-header">
            <div class="avatar">ИФ</div>
            <div class="profile-info">
                <h1>Иван Фёдоров</h1>
                <div class="role">Project Manager</div>
                <div class="join-date">В команде с 15 января 2023</div>
            </div>
        </div>

        <div class="profile-content">
            <div class="left-column">
                <div class="section">
                    <h2>Основная информация</h2>
                    <div class="info-grid">
                        <div class="info-item">
                            <span class="info-label">Email</span>
                            <span class="info-value">ivan.fedorov@company.com</span>
                        </div>
                        <div class="info-item">
                            <span class="info-label">Телефон</span>
                            <span class="info-value">+7 (999) 123-45-67</span>
                        </div>
                        <div class="info-item">
                            <span class="info-label">Отдел</span>
                            <span class="info-value">Разработка продуктов</span>
                        </div>
                        <div class="info-item">
                            <span class="info-label">Статус</span>
                            <span class="info-value" style="color: #27ae60;">Активен</span>
                        </div>
                    </div>
                </div>

                <div class="section">
                    <h2>Статистика</h2>
                    <div class="stats-grid">
                        <div class="stat-item">
                            <div class="stat-number">8</div>
                            <div class="stat-label">Активных проектов</div>
                        </div>
                        <div class="stat-item">
                            <div class="stat-number">24</div>
                            <div class="stat-label">Завершённых</div>
                        </div>
                        <div class="stat-item">
                            <div class="stat-number">96%</div>
                            <div class="stat-label">Успешных</div>
                        </div>
                        <div class="stat-item">
                            <div class="stat-number">18</div>
                            <div class="stat-label">Участников в команде</div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="right-column">
                <div class="section">
                    <h2>Активные проекты</h2>
                    <div class="projects-list">
                        <div class="project-card">
                            <div class="project-name">Веб-сайт компании</div>
                            <div class="project-role">Менеджер проекта</div>
                            <div class="project-meta">
                                <span>12 задач</span>
                                <span>3 участника</span>
                                <span>Срок: 15.12.2024</span>
                            </div>
                        </div>
                        <div class="project-card">
                            <div class="project-name">Мобильное приложение</div>
                            <div class="project-role">Product Owner</div>
                            <div class="project-meta">
                                <span>8 задач</span>
                                <span>2 участника</span>
                                <span>Срок: 20.11.2024</span>
                            </div>
                        </div>
                        <div class="project-card">
                            <div class="project-name">Обновление CRM</div>
                            <div class="project-role">Scrum Master</div>
                            <div class="project-meta">
                                <span>20 задач</span>
                                <span>5 участников</span>
                                <span>Срок: 30.01.2025</span>
                            </div>
                        </div>
                        <div class="project-card">
                            <div class="project-name">UI/UX дизайн</div>
                            <div class="project-role">Менеджер проекта</div>
                            <div class="project-meta">
                                <span>9 задач</span>
                                <span>2 участника</span>
                                <span>Срок: 10.12.2024</span>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="section">
                    <h2>Навыки</h2>
                    <div style="display: flex; flex-wrap: wrap; gap: 8px;">
                        <span style="background: #e3f2fd; color: #1976d2; padding: 6px 12px; border-radius: 20px; font-size: 12px;">Управление проектами</span>
                        <span style="background: #e8f5e8; color: #2e7d32; padding: 6px 12px; border-radius: 20px; font-size: 12px;">Agile/Scrum</span>
                        <span style="background: #f3e5f5; color: #7b1fa2; padding: 6px 12px; border-radius: 20px; font-size: 12px;">Jira</span>
                        <span style="background: #e0f2f1; color: #00695c; padding: 6px 12px; border-radius: 20px; font-size: 12px;">Risk Management</span>
                        <span style="background: #fff3e0; color: #ef6c00; padding: 6px 12px; border-radius: 20px; font-size: 12px;">Team Leadership</span>
                    </div>
                </div>
            </div>
        </div>
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

        .profile-container {
            background: white;
            border-radius: 12px;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 900px;
            padding: 40px;
        }

        .profile-header {
            display: flex;
            align-items: center;
            gap: 25px;
            margin-bottom: 40px;
            padding-bottom: 30px;
            border-bottom: 1px solid #e1e5e9;
        }

        .avatar {
            width: 100px;
            height: 100px;
            border-radius: 50%;
            background: #3498db;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 36px;
            font-weight: bold;
            flex-shrink: 0;
        }

        .profile-info h1 {
            color: #2c3e50;
            font-size: 32px;
            font-weight: 600;
            margin-bottom: 8px;
        }

        .profile-info .role {
            color: #3498db;
            font-size: 18px;
            font-weight: 500;
            margin-bottom: 8px;
        }

        .profile-info .join-date {
            color: #7f8c8d;
            font-size: 14px;
        }

        .profile-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 40px;
        }

        .section {
            margin-bottom: 30px;
        }

        .section h2 {
            color: #2c3e50;
            font-size: 20px;
            font-weight: 600;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #3498db;
        }

        .info-grid {
            display: grid;
            gap: 15px;
        }

        .info-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 12px 0;
            border-bottom: 1px solid #f1f2f6;
        }

        .info-label {
            color: #7f8c8d;
            font-weight: 500;
        }

        .info-value {
            color: #2c3e50;
            font-weight: 500;
        }

        .projects-list {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .project-card {
            background: #f8f9fa;
            border-radius: 8px;
            padding: 16px;
            border-left: 4px solid #3498db;
            transition: transform 0.2s;
        }

        .project-card:hover {
            transform: translateX(5px);
        }

        .project-name {
            color: #2c3e50;
            font-weight: 600;
            margin-bottom: 6px;
        }

        .project-role {
            color: #7f8c8d;
            font-size: 14px;
            margin-bottom: 8px;
        }

        .project-meta {
            display: flex;
            gap: 15px;
            font-size: 12px;
            color: #95a5a6;
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 15px;
            margin-top: 10px;
        }

        .stat-item {
            background: #f8f9fa;
            border-radius: 8px;
            padding: 15px;
            text-align: center;
        }

        .stat-number {
            color: #3498db;
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 5px;
        }

        .stat-label {
            color: #7f8c8d;
            font-size: 12px;
        }

        .back-btn {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            color: #3498db;
            text-decoration: none;
            font-weight: 500;
            margin-bottom: 20px;
            transition: color 0.3s;
        }

        .back-btn:hover {
            color: #2980b9;
        }

        @media (max-width: 768px) {
            .profile-content {
                grid-template-columns: 1fr;
                gap: 20px;
            }
            
            .profile-header {
                flex-direction: column;
                text-align: center;
                gap: 15px;
            }
            
            .profile-container {
                padding: 30px 20px;
            }
            
            .stats-grid {
                grid-template-columns: 1fr;
            }
        }
</style>