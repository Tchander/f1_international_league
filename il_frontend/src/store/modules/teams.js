import { getAllTeams, getTeamByUrlName } from "@/api/teamApi";

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
      state.teams = payload.slice(0);
      state.teamsFilteredByLeague1 = payload
        .slice(0)
        .sort(
          (prev, next) => next.total_score_league1 - prev.total_score_league1
        );
      state.teamsFilteredByLeague2 = payload
        .slice(0)
        .sort(
          (prev, next) => next.total_score_league2 - prev.total_score_league2
        );
    },
    updateCurrentTeam(state, payload) {
      state.currentTeam = payload;
    },
  },
  state: {
    teams: [],
    teamsFilteredByLeague1: [],
    teamsFilteredByLeague2: [],
    currentTeam: null,
  },
};
