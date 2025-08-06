# 📋 Vue 3 Task Manager

Aplicación web full stack moderna y visualmente atractiva para la gestión de tareas, desarrollada con **Vue 3 + Vuetify** en el frontend y **FastAPI + PostgreSQL** en el backend.

---

## 🚀 Funcionalidades principales

- ✅ Crear, editar y eliminar tareas
- 🔄 Animación visual al agregar y eliminar tareas
- 🧠 Asignación de prioridades (Alta, Media, Baja)
- 🌗 Cambio dinámico de tema claro/oscuro
- 🔍 Filtros de tareas: todas, completadas o pendientes
- 🕒 Visualización de fecha y hora de creación
- 🔔 Notificaciones visuales con `v-snackbar`
- 📱 Diseño moderno, limpio y responsive

---

## 🛠️ Tecnologías utilizadas

### 🔹 Frontend

- **Vue 3** – Framework progresivo de JavaScript
- **Vuetify 2** – UI Framework con Material Design
- **Axios** – Cliente HTTP para consumo de API
- **Vue Router** – Enrutador oficial para Vue.js
- **Vuex** – Manejo de estado centralizado
- **Vuelidate** – Validación de formularios reactiva

### 🔸 Backend

- **FastAPI** – Framework rápido para construir APIs con Python
- **SQLAlchemy** – ORM para gestión de base de datos
- **PostgreSQL** – Base de datos relacional robusta

---

## ⚙️ Instalación y ejecución local

### 🧩 Requisitos previos

- Python 3.10 o superior
- PostgreSQL instalado y corriendo
- Node.js + npm instalados
- Git instalado

---

### 🧪 Configuración del backend

```bash
# 1. Clona el repositorio
git clone https://github.com/SAndrade22/vue3-task-manager.git
cd vue3-task-manager/backend

# 2. Crea y activa un entorno virtual
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate

# 3. Instala dependencias
pip install fastapi uvicorn sqlmodel psycopg2-binary

# 4. Asegúrate de que tu base de datos PostgreSQL esté activa y configura la URL de conexión en database.py

# 5. Ejecuta el backend
uvicorn main:app --reload
```

---

### 🌐 Configuración del frontend

```bash
cd ../frontend

# 1. Instala dependencias
npm install

# 2. Ejecuta el servidor de desarrollo
npm run serve
```

El frontend estará disponible en: `http://localhost:8080`

---

## 📁 Estructura del proyecto

```
vue3-task-manager/
├── backend/
│   ├── main.py
│   ├── crud.py
│   ├── models.py
│   ├── schemas.py
│   └── database.py
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── TodoApp.vue
│   │   │   └── TodoItem.vue
│   │   ├── App.vue
│   │   └── main.js
│   ├── public/
│   └── package.json
├── .gitignore
└── README.md
```

---

## 👨‍💻 Autor

**Sebastián Andrade**  
Desarrollador full-stack, apasionado por la inteligencia artificial, la astronomía y la creación de interfaces limpias y funcionales.

- GitHub: [@SAndrade22](https://github.com/SAndrade22)

---

## 🏷️ Etiquetas

`vue` `vuetify` `fastapi` `postgresql` `fullstack` `todo-app` `vue3` `task-manager` `axios` `frontend-backend`

---
