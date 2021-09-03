import { getAllRace, getRaceByCountry } from "@/api/raceApi";
export default {
  namespaced: true,
  actions: {
    async getAllRace({ commit }) {
      try {
        const { data } = await getAllRace();
        commit("updateRace", data);
      } catch (e) {
        console.log(e);
      }
    },
    async getRaceByCountry({ commit }, country) {
      try {
        const { data } = await getRaceByCountry(country);
        commit("updateCurrentRace", data);
      } catch (e) {
        console.log(e);
      }
    },
  },
  mutations: {
    updateRace(state, payload) {
      state.race = payload;
    },
    updateCurrentRace(state, payload) {
      state.currentRace = payload;
    },
  },
  state: {
    race: [],
    currentRace: null,
  },
};
