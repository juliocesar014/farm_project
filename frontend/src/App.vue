<template>
  <div id="app">
    <h1>Página Inicial - Dashboard de Fazendas</h1>
    <router-link to="/criar"><ButtonCreate /></router-link>
    <h1>Lista de Fazendas</h1>
    <HomeDash />
  </div>
  <router-view />
</template>

<script>
import ButtonCreate from "./components/ButtonCreate.vue";
import HomeDash from "./components/HomeDash.vue";

export default {
  name: "app",
  data() {
    return {};
  },
  components: {
    ButtonCreate,
    HomeDash,
  },
};
</script>

<style scoped>
* {
  margin-top: 2%;
  margin-left: 2%;
}
</style>
