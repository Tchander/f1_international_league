import Vue from "vue";
import Vuex from "vuex";
import teams from "@/store/modules/teams";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    teams,
  },
});
