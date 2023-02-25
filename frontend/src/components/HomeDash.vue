<template>
  <div>
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
export default {
  name: "HomeDash",
  data() {
    return {
      farms: null,
    };
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
