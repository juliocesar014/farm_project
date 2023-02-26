<template>
  <div>
    <h1>Página Inicial - Dashboard de Fazendas</h1>
    <router-link to="/criar"><ButtonCreate /></router-link>
    <h1>Lista de Fazendas</h1>
    <table class="table">
      <thead>
        <tr>
          <th scope="col">id</th>
          <th scope="col">Nome</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="farm in farms" :key="farm.id">
          <th scope="row">{{ farm.id }}</th>
          <td>{{ farm.name }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import ButtonCreate from "@/components/ButtonCreate.vue";

export default {
  name: "HomeDash",
  data() {
    return {
      farms: null,
    };
  },
  components: {
    ButtonCreate,
  },
  methods: {
    async getFarms() {
      const response = await fetch("http://localhost:3000/farms");
      const data = await response.json();
      this.farms = data;
    },
  },
  mounted() {
    this.getFarms();
  },
};
</script>
