import { getTeamByUrlName, getAllTeams } from "@/api/teamApi";
export default {
  namespaced: true,
  actions: {
    async getAllTeams({ commit }) {
      try {
        const { data } = await getAllTeams();
        commit("updateTeams", data);
      } catch (e) {
        console.log(e);
      }
    },
    async getTeamByUrlName({ commit }, urlName) {
      try {
        const { data } = await getTeamByUrlName(urlName);
        commit("updateCurrentTeam", data);
      } catch (e) {
        console.log(e);
      }
    },
  },
  mutations: {
    updateTeams(state, payload) {
      state.teams = payload;
    },
    updateCurrentTeam(state, payload) {
      state.currentTeam = payload;
    },
  },
  state: {
    teams: [],
    currentTeam: null,
  },
};
