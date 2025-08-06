<template>
  <v-list-item class="mb-1" elevation="1" rounded="lg">
    <v-list-item-content>
      <div v-if="!editMode">
        <v-list-item-title
          :class="
            task.completed ? 'text-decoration-line-through text-grey' : ''
          "
        >
          <v-icon color="success" v-if="task.completed" class="mr-1">
            mdi-check-circle
          </v-icon>
          {{ task.title }}

          <v-chip
            class="ml-2"
            :color="getPriorityColor(task.priority)"
            text-color="white"
            small
            label
          >
            <v-icon start small>mdi-flag</v-icon>
            {{ task.priority }}
          </v-chip>
        </v-list-item-title>
      </div>

      <div v-else>
        <v-text-field
          v-model="editedTitle"
          dense
          hide-details
          variant="outlined"
        ></v-text-field>
      </div>
    </v-list-item-content>

    <v-list-item-action>
      <v-btn
        icon
        @click="toggleComplete"
        :title="'Marcar como ' + (task.completed ? 'pendiente' : 'completada')"
      >
        <v-icon>{{
          task.completed ? "mdi-checkbox-marked" : "mdi-checkbox-blank-outline"
        }}</v-icon>
      </v-btn>

      <v-btn icon @click="toggleEdit" :title="editMode ? 'Guardar' : 'Editar'">
        <v-icon>{{ editMode ? "mdi-content-save" : "mdi-pencil" }}</v-icon>
      </v-btn>

      <v-btn icon @click="deleteTask" color="red" title="Eliminar">
        <v-icon>mdi-delete</v-icon>
      </v-btn>
    </v-list-item-action>
  </v-list-item>
</template>

<script>
import axios from "../axios";

export default {
  props: {
    task: Object,
  },
  data() {
    return {
      editMode: false,
      editedTitle: this.task.title,
    };
  },
  methods: {
    async toggleComplete() {
      await axios.put(`/tasks/${this.task.id}`, {
        title: this.task.title,
        completed: !this.task.completed,
        priority: this.task.priority,
      });
      this.$emit("task-updated");
    },
    toggleEdit() {
      if (this.editMode) {
        this.updateTask();
      }
      this.editMode = !this.editMode;
    },
    async updateTask() {
      await axios.put(`/tasks/${this.task.id}`, {
        title: this.editedTitle,
        completed: this.task.completed,
        priority: this.task.priority,
      });
      this.$emit("task-updated");
    },
    async deleteTask() {
      await axios.delete(`/tasks/${this.task.id}`);
      this.$emit("task-deleted");
    },
    getPriorityColor(priority) {
      switch (priority) {
        case "alta":
          return "red darken-1";
        case "media":
          return "orange darken-2";
        case "baja":
          return "green darken-2";
        default:
          return "grey";
      }
    },
  },
};
</script>

<style scoped>
.text-decoration-line-through {
  text-decoration: line-through;
}
.text-grey {
  color: #999;
}
</style>
