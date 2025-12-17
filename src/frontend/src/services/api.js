import axios from "axios";
import router from "@/router";

const API = axios.create({
  baseURL: process.env.VUE_APP_API_URL || "http://172.18.0.3:8000", // <=== insert there
  timeout: 10000,
  headers: {
    "Content-Type": "application/json",
  },
});
// запросы
API.interceptors.request.use(
  (config) => {
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);
// ответы
API.interceptors.response.use(
  (response) => {
    return response.data;
  },
  (error) => {
    if (error.response && error.response.status === 401) {
      // Перенаправление на страницу регистрации
      router.push("/registration");
    }
    return Promise.reject(error);
  }
);

export const api_service = {
  async send_registration_data(first_name, last_name, email, password) {
    const response = await API.post("/registration", {
      first_name: first_name,
      last_name: last_name,
      email: email,
      password: password,
    });
    return response;
  },

  async send_authorisation_data(email, password) {
    const response = await API.post("/authorisation", {
      email: email,
      password: password,
    });

    return response;
  },

  async get_name(token) {
    const response = await API.get(`/get_name`, {
      headers: {
        Authorization: `Bearer ${token}`,
        "Content-Type": "application/json",
      },
    });
    return response;
  },

  async get_name_id(id) {
    const response = await API.get(`/get_name/${id}`);
    return response;
  },

  async send_project_data(token, title, description, command_id, deadline) {
    const response = await API.post(
      "/projectsCreating",
      {
        title: title,
        description: description,
        command_id: command_id,
        deadline: deadline,
      },
      {
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json",
        },
      }
    );
    return response;
  },
  
  async get_projects(token) {
    const response = await API.get("/getProjects", {
      headers: {
        Authorization: `Bearer ${token}`,
        "Content-Type": "application/json",
      },
    });
    return response;
  },

  async delete_projects(token) {
    await API.delete("/deleteProjects", {
      headers: {
        Authorization: `Bearer ${token}`,
        "Content-Type": "application/json",
      },
    });
  },

  async delete_users(token) {
    await API.delete("/deleteUsers", {
      headers: {
        Authorization: `Bearer ${token}`,
        "Content-Type": "application/json",
      },
    });
  },

  async add_role(token, role) {
    await API.put('/addRole', {'role':role}, {
      headers: {
        Authorization: `Bearer ${token}`,
        "Content-Type": "application/json",
      }
    }
  )
  },

  async all_users(token) {
    const response = await API.get('/users', {
      headers: {
        Authorization: `Bearer ${token}`,
        "Content-Type": "application/json",
      },
    })
    return response
  }
};
