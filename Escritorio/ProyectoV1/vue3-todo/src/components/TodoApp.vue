<template>
  <v-app>
    <v-main
      class="d-flex align-center justify-center bg-background"
      style="min-height: 100vh"
    >
      <v-container
        class="d-flex align-center justify-center"
        fluid
        style="min-height: 100vh; padding: 0"
      >
        <v-card
          class="pa-8"
          max-width="900"
          min-width="700"
          elevation="12"
          rounded="xl"
        >
          <v-card-title
            class="text-h5 font-weight-bold text-primary d-flex justify-space-between align-center"
          >
            <div>
              <v-icon start color="primary">mdi-format-list-checks</v-icon>
              Mi lista de tareas
            </div>
            <v-btn
              icon
              @click="toggleTheme"
              :title="isDark ? 'Tema claro' : 'Tema oscuro'"
            >
              <v-icon>{{
                isDark ? "mdi-white-balance-sunny" : "mdi-weather-night"
              }}</v-icon>
            </v-btn>
          </v-card-title>

          <v-card-text>
            <v-row class="mb-4 justify-center" align="center">
              <v-col cols="12" md="8">
                <v-text-field
                  v-model="newTask"
                  label="Escribe una nueva tarea"
                  prepend-inner-icon="mdi-pencil"
                  outlined
                  clearable
                  hide-details
                />
              </v-col>
              <v-col cols="12" md="4">
                <v-select
                  v-model="newPriority"
                  :items="priorities"
                  label="Prioridad"
                  item-title="text"
                  item-value="value"
                  prepend-inner-icon="mdi-flag"
                  outlined
                  dense
                  hide-details
                ></v-select>
              </v-col>

              <v-col cols="12" class="d-flex justify-center">
                <v-btn
                  color="primary"
                  class="text-white font-weight-bold text-subtitle-1 pa-3"
                  height="56"
                  @click="addTask"
                  :disabled="!newTask"
                >
                  <v-icon start>mdi-plus</v-icon>
                  Agregar
                </v-btn>
              </v-col>
            </v-row>
            <v-divider class="mb-4"></v-divider>
            <v-btn-toggle
              v-model="filter"
              class="mb-4"
              dense
              rounded
              color="primary"
              group
            >
              <v-btn value="all">
                <v-icon start>mdi-format-list-bulleted</v-icon>
                Todas
              </v-btn>
              <v-btn value="pending">
                <v-icon start>mdi-progress-clock</v-icon>
                Pendientes
              </v-btn>
              <v-btn value="completed">
                <v-icon start>mdi-check-circle</v-icon>
                Completadas
              </v-btn>
            </v-btn-toggle>
            <v-alert
              type="info"
              border="start"
              colored-border
              elevation="1"
              class="mb-4"
              icon="mdi-information"
              text
            >
              Total: <strong>{{ taskSummary.total }}</strong> | Completadas:
              <strong>{{ taskSummary.completed }}</strong> | Pendientes:
              <strong>{{ taskSummary.pending }}</strong>
            </v-alert>

            <v-list>
              <transition-group name="fade" tag="div">
                <TodoItem
                  v-for="task in filteredTasks"
                  :key="task.id"
                  :task="task"
                  @task-updated="fetchTasks"
                  @task-deleted="handleTaskDeleted"
                />
              </transition-group>
            </v-list>

            <v-snackbar
              v-model="snackbar"
              timeout="3000"
              color="deep-purple accent-4"
              elevation="5"
              location="bottom"
              rounded="pill"
            >
              <v-icon start class="mr-2">mdi-check-circle</v-icon>
              {{ snackbarText }}
            </v-snackbar>
          </v-card-text>
        </v-card>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import axios from "../axios";
import TodoItem from "./TodoItem.vue";
import { useTheme } from "vuetify";
import { computed } from "vue";

export default {
  components: { TodoItem },
  data() {
    return {
      tasks: [],
      newTask: "",
      newPriority: "media",
      filter: "all",
      snackbar: false,
      snackbarText: "",
      priorities: [
        { text: "Alta", value: "alta" },
        { text: "Media", value: "media" },
        { text: "Baja", value: "baja" },
      ],
    };
  },
  setup() {
    const theme = useTheme();
    const isDark = computed(() => theme.global.name.value === "dark");

    const toggleTheme = () => {
      theme.global.name.value = isDark.value ? "light" : "dark";
    };

    return {
      isDark,
      toggleTheme,
    };
  },
  computed: {
    filteredTasks() {
      if (this.filter === "completed") {
        return this.tasks.filter((task) => task.completed);
      } else if (this.filter === "pending") {
        return this.tasks.filter((task) => !task.completed);
      }
      return this.tasks;
    },
    taskSummary() {
      return {
        total: this.tasks.length,
        completed: this.tasks.filter((t) => t.completed).length,
        pending: this.tasks.filter((t) => !t.completed).length,
      };
    },
  },
  methods: {
    async fetchTasks() {
      const response = await axios.get("/tasks");
      this.tasks = response.data;
    },
    async addTask() {
      if (!this.newTask) return;
      const response = await axios.post("/tasks", {
        title: this.newTask,
        completed: false,
        priority: this.newPriority,
      });
      this.tasks.push(response.data);
      this.newTask = "";
      this.newPriority = "media";

      this.showSnackbar("Tarea agregada correctamente ✅");
    },
    handleTaskDeleted() {
      this.fetchTasks();
      this.showSnackbar("Tarea eliminada correctamente ✅");
    },
    showSnackbar(message) {
      this.snackbarText = message;
      this.snackbar = true;
    },
  },
  mounted() {
    this.fetchTasks();
  },
};
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: all 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}
</style>
