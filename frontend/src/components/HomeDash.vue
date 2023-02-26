<template>
  <div>
    <h1>Página Inicial - Dashboard de Fazendas</h1>
    <router-link to="/criar"><ButtonCreate /></router-link>
    <h1>Lista de Fazendas</h1>
    <div class="farm-list">
      <table class="table">
        <thead>
          <tr>
            <th scope="col">id</th>
            <th scope="col">Nome</th>
          </tr>
        </thead>
        <tbody class="farm">
          <tr v-for="farm in farms" :key="farm.id" @click="selectFarm(farm)">
            <th scope="row">{{ farm.id }}</th>
            <td>{{ farm.name }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <FarmDetails :farm="selectedFarm" v-if="selectedFarm" />
  </div>
</template>

<script>
import ButtonCreate from "@/components/ButtonCreate.vue";
import FarmDetails from "@/components/FarmDetails.vue";

export default {
  name: "HomeDash",
  data() {
    return {
      farms: null,
      selectedFarm: null,
    };
  },
  components: {
    ButtonCreate,
    FarmDetails,
  },
  methods: {
    async getFarms() {
      const response = await fetch("http://localhost:3000/farms");
      const data = await response.json();
      this.farms = data;
    },
    selectFarm(farm) {
      this.selectedFarm = farm;
    },
  },
  mounted() {
    this.getFarms();
  },
};
</script>

<style scoped>
.farm-list {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.farm {
  cursor: pointer;
}
</style>
