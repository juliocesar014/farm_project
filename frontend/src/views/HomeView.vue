<template>
  <div class="home">
    <HomeDash />
  </div>
</template>

<script>
// @ is an alias to /src
import HomeDash from "@/components/HomeDash.vue";
export default {
  name: "HomeView",
  components: {
    HomeDash,
  },
};
</script>
