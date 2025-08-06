<template>
  <v-app>
    <TodoApp />
  </v-app>
</template>

<script>
import TodoApp from "./components/TodoApp.vue";

export default {
  components: {
    TodoApp,
  },
};
</script>

<style>
html,
body,
#app {
  height: 100%;
  margin: 0;
  padding: 0;
}

.v-application {
  min-height: 100vh;
  background-color: var(--v-theme-background) !important;
}
</style>
