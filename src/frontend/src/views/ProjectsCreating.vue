<template>
  <body>
    <div class="create-project-form">
      <router-link class="back-btn" to="/list">← Назад к проектам</router-link>
      <router-link class="back-btn" :to="`/profile/${user_id}`">{{name }}</router-link>
    </div>

    <div class="create-project-form">
      <h2>Создать новый проект</h2>

      <form
        action="/create-project"
        method="post"
        class="form"
        @submit.prevent="sendData()"
      >
        <div class="form-group">
          <label for="projectName">Название проекта</label>
          <input
            type="text"
            id="projectName"
            name="projectName"
            v-model="title"
            required
          />
        </div>

        <div class="form-group">
          <label for="projectDescription">Описание</label>
          <textarea
            id="projectDescription"
            name="projectDescription"
            rows="4"
            v-model="description"
            required
          ></textarea>
        </div>

        <div class="form-group">
          <label for="teamSelect">Выберите команду</label>
          <select
            id="teamSelect"
            v-model="selectedTeam"
            @change="chooseCommand"
          >
            <option disabled value="">-- пока не доступно --</option>
            <!-- <option>Создать новую команду...</option> -->
            <option v-for="team in teams" :key="team.id" :value="team.id">
              {{ team.name }}
            </option>
          </select>
          <button class="btn-submit">Узнать о команде</button>
        </div>

        <div class="form-group">
          <label for="start_date">Предполагаемая дата начала работы</label>
          <input
            type="date"
            id="start_date"
            name="start_date"
            v-model="start_date"
            :min="getToday()"
            required
          />
        </div>

        <div class="form-group">
          <label for="deadline">Срок завершения</label>
          <input
            type="date"
            id="deadline"
            name="deadline"
            v-model="deadline"
            :min="getToday()"
            required
          />
        </div>

        <div class="form-actions">
          <button type="submit" class="btn-submit">Создать</button>
          <button type="reset" class="btn-reset">Очистить</button>
        </div>
      </form>
    </div>
  </body>
</template>

<style scoped>
select {
  margin: 10px;
}

#teamSelect {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-family: "Segoe UI", Arial, sans-serif;
  font-size: 14px;
  transition: border-color 0.2s;
}
#teamSelect:focus {
  border-color: #3498db;
  outline: none;
}

.create-project-form {
  background: #f8f9fa; /* такой же как фон блоков проектов */
  border-radius: 8px;
  padding: 20px;
  margin-top: 40px;
  border: 1px solid #e1e5e9;
}

.create-project-form h2 {
  color: #2c3e50;
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 20px;
  padding-bottom: 10px;
  border-bottom: 2px solid #3498db;
}

.form {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.form-group {
  display: flex;
  flex-direction: column;
}

.form-group label {
  margin-bottom: 6px;
  color: #7f8c8d;
  font-weight: 500;
}

.form-group input,
.form-group textarea {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-family: "Segoe UI", Arial, sans-serif;
  font-size: 14px;
  transition: border-color 0.2s;
}

.form-group input:focus,
.form-group textarea:focus {
  border-color: #3498db;
  outline: none;
}

.form-actions {
  display: flex;
  gap: 10px;
  justify-content: flex-start;
  margin-top: 10px;
}

.btn-submit,
.btn-reset {
  padding: 10px 20px;
  border: none;
  border-radius: 20px;
  font-weight: 500;
  cursor: pointer;
  transition: background 0.3s, color 0.3s;
}

.btn-submit {
  background-color: #3498db;
  color: #fff;
}

.btn-submit:hover {
  background-color: #2980b9;
}

.btn-reset {
  background-color: #e0e0e0;
  color: #2c3e50;
}

.btn-reset:hover {
  background-color: #bdbdbd;
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
  padding: 10px;
}
</style>

<script setup>
import { useRouter } from "vue-router";
import { auth } from "@/utils/auth";
import { onBeforeMount, ref } from "vue";
import { api_service } from "@/services/api";

const router = useRouter();

const name = ref("");
const user_id = ref("");
const team_id = ref("");
const title = ref("");
const description = ref("");
const deadline = ref("");
const start_date = ref("");

const getName = async () => {
  const response = await api_service.get_name(auth.getToken());
  name.value =
    response["first_name"] + " " + response["last_name"] ?? "Не указано";
  user_id.value = response["user_id"];
};

onBeforeMount(() => {
  if (!auth.getToken()) {
    router.push("/registration");
  } else {
    getName();
  }
});

const chooseCommand = () => {
  alert(team_id.value);
};

const sendData = async () => {
  try {
    await api_service.send_project_data(
      auth.getToken(),
      title.value,
      description.value,
      1111,
      deadline.value
    );
    title.value = deadline.value = team_id.value = description.value = "";
  } catch (error) {
    if (error.status === 401) {
      router.push("/registration");
    } else if (error.status === 409) {
      alert("Проект с таким названием уже существует");
    }
  }
};

const getToday = () => {
  const today = new Date();
  return today.toISOString().split("T")[0];
};
</script>
