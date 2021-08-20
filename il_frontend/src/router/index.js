import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/calendar",
    name: "Calendar",
    component: () => import("../views/Calendar.vue"),
  },
  {
    path: "/tournament_table",
    name: "TournamentTable",
    component: () => import("../views/TournamentTable.vue"),
  },
  {
    path: "/teams",
    name: "Teams",
    component: () => import("../views/Teams.vue"),
  },
  {
    path: "/team/:teamName",
    name: "Team",
    component: () => import("../views/Team.vue"),
    props: true,
  },
];

const router = new VueRouter({
  routes,
  mode: "history",
});

export default router;
