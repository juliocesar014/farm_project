<template>
  <div class="farm-details">
    <p><strong>Nome: </strong> {{ farm.name }}</p>
    <p><strong>ID:</strong> {{ farm.id }}</p>
    <p><strong>Geometry: </strong>{{ farm.geometry }}</p>
    <p><strong>Área:</strong> {{ farm.area }}</p>
    <p><strong>Centro_ID:</strong> {{ farm.centroid }}</p>
    <p><strong>Owner_ID:</strong> {{ farm.owner_id }}</p>
    <div class="list-btn">
      <button type="button" class="btn btn-info">Editar Fazenda</button>
      <button class="btn btn-danger" @click="deleteFarms(farm.id)">
        Deletar Fazenda
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "FarmDetails",
  data() {
    return {};
  },
  props: {
    farm: {
      type: Object,
      required: true,
    },
  },
  methods: {
    async getFarms() {
      const response = await fetch("http://localhost:3000/farms");
      const data = await response.json();
      this.farms = data;
    },

    async deleteFarms(id) {
      const response = await fetch(`http://localhost:3000/farms/${id}`, {
        method: "DELETE",
      });
      const data = await response.json();
      console.log("Data:", data);

      window.location.reload();
    },

    mounted() {
      this.getFarms();
    },
  },
};
</script>

<style scoped>
.farm-details {
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.list-btn button {
  margin-right: 10px;
}
</style>
