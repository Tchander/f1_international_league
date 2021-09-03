import Vue from "vue";
import VueRouter from "vue-router";
import Home from "@/views/Home.vue";
import Calendar from "@/views/Calendar";
import TournamentTable from "@/views/TournamentTable";
import Teams from "@/views/Teams";
import Team from "@/views/Team";
import RaceInfo from "@/views/RaceInfo";
import { ROUTES } from "@/const";

Vue.use(VueRouter);

const routes = [
  {
    path: ROUTES.home,
    name: "Home",
    component: Home,
  },
  {
    path: ROUTES.calendar,
    name: "Calendar",
    component: Calendar,
  },
  {
    path: ROUTES.tournament_table,
    name: "TournamentTable",
    component: TournamentTable,
  },
  {
    path: ROUTES.teams,
    name: "Teams",
    component: Teams,
  },
  {
    path: ROUTES.team,
    name: "Team",
    component: Team,
    props: true,
  },
  {
    path: ROUTES.race,
    name: "Race",
    component: RaceInfo,
    props: true,
  },
];

const router = new VueRouter({
  routes,
  mode: "history",
});

export default router;
