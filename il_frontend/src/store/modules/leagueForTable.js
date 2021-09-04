import {LEAGUES} from "@/const";

export default {
  namespaced: true,
  actions: {
    switchLeagueNumber({ commit }, data) {
      try {
        commit("updateLeagueForTable", data);
      } catch (e) {
        console.log(e);
      }
    },
  },
  mutations: {
    updateLeagueForTable(state, payload) {
      state.leagueForTable = payload;
    },
  },
  state: {
    leagueForTable: LEAGUES.FIRST,
  },
};
