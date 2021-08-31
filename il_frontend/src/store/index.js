import Vue from "vue";
import Vuex from "vuex";
import teams from "@/store/modules/teams";
import pilots from "@/store/modules/pilots";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    teams,
    pilots,
  },
});
