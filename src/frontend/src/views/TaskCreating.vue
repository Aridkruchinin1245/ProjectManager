<template>
  <body>
    <div class="create-project-form">
      <router-link class="back-btn" to="/list">← Назад к проектам</router-link>
      <router-link class="back-btn" :to="`/profile/${id}`">{{name }}</router-link>
    </div>

    <div class="create-project-form">
      <h2>Добавить задачу к {{ project_title }}</h2>

      <form
        action="/create-project"
        method="post"
        class="form"
        @submit.prevent="sendData()"
      >
        <div class="form-group">
          <label for="projectDescription">Описание задачи</label>
          <textarea
            id="projectDescription"
            name="projectDescription"
            rows="4"
            v-model="description"
            required
          ></textarea>
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
import { useRouter, useRoute } from "vue-router";
import { auth } from "@/utils/auth";
import { onBeforeMount, ref } from "vue";
import { api_service } from "@/services/api";

const router = useRouter();
const route = useRoute();

const project_title = ref("")
const name = ref("");
const id = ref("");
const description = ref("");

const getName = async () => {
  const response = await api_service.get_name(auth.getToken());
  name.value =
    response["first_name"] + " " + response["last_name"] ?? "Не указано";
  id.value = response["id"];
};

const getProjectTitle = async() => {
  const response = await api_service.getProjectName(route.params.id, auth.getToken())
  project_title.value = response['data']
}



onBeforeMount(() => {
  if (!auth.getToken()) {
    router.push("/registration");
  } else {
    getName();
    getProjectTitle()
  }
});

const sendData = async() => {
  await api_service.createNewTask(route.params.id, description.value, auth.getToken())
  router.push('/list')
};


</script>
