<template>
  <div>
    <h1>Criar Fazenda</h1>
    <router-link to="/"
      ><button type="button" class="btn btn-info">
        Voltar para Home
      </button></router-link
    >

    <form id="burguer-form" @submit="createFarm">
      <div class="input-container">
        <label for="nome">Name: </label>
        <input type="text" id="name" name="name" v-model="name" />
      </div>
      <div class="input-container">
        <label for="nome">Geometry: </label>
        <input type="text" id="geometry" name="geometry" v-model="geometry" />
      </div>
      <div class="input-container">
        <label for="nome">Área: </label>
        <input type="text" id="area" name="area" v-model="area" />
      </div>
      <div class="input-container">
        <label for="nome">CentroID: </label>
        <input type="text" id="centroid" name="centroid" v-model="centroid" />
      </div>
      <div class="input-container">
        <label for="nome">Owner_ID: </label>
        <input type="text" id="owner_id" name="owner_id" v-model="owner_id" />
      </div>
      <div>
        <input type="submit" class="submit-btn" value="Criar Fazenda" />
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: "CriarForm",
  data() {
    return {
      name: null,
      area: null,
      centroid: null,
      geometry: null,
      owner_id: null,
    };
  },
  methods: {
    async createFarm(e) {
      e.preventDefault();

      console.log("Criou a fazenda!");

      const farm = {
        name: this.name,
        area: this.area,
        centroid: this.centroid,
        geometry: this.geometry,
        owner_id: this.owner_id,
      };

      // Enviar a requisição para a API
      const farmJson = JSON.stringify(farm);
      const response = await fetch("http://localhost:3000/farms", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: farmJson,
      });

      (this.name = ""),
        (this.area = ""),
        (this.centroid = ""),
        (this.geometry = ""),
        (this.owner_id = "");

      const data = await response.json();
      console.log(data);
    },
  },
};
</script>
