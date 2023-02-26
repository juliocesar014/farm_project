import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import CriarForm from "../components/CriarForm.vue";
const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/criar",
    name: "criar",
    // route level code-splitting
    // this generates a separate chunk (criar.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "criar" */ "../components/CriarForm.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
