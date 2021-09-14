import Vue from "vue";
import VueRouter from "vue-router";
import Home from "@/views/Home.vue";
import Calendar from "@/views/Calendar";
import TournamentTable from "@/views/TournamentTable";
import Teams from "@/views/Teams";
import Team from "@/views/Team";
import RaceInfo from "@/views/RaceInfo";
import Regulations from "@/views/Regulations";
import ConstructorsCup from "@/views/ConstructorsCup";
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
    path: ROUTES.constructors_cup,
    name: "ConstructorsCup",
    component: ConstructorsCup,
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
  {
    path: ROUTES.regulations,
    name: "Regulations",
    component: Regulations,
  },
];

const router = new VueRouter({
  base: "/f1_international_league/",
  routes,
  mode: "history",
});

export default router;
