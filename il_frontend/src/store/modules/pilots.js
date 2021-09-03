import { getAllPilots } from "@/api/pilotApi";
export default {
  namespaced: true,
  actions: {
    async getAllPilots({ commit }) {
      try {
        const { data } = await getAllPilots();
        commit("updatePilots", data);
      } catch (e) {
        console.log(e);
      }
    },
  },
  mutations: {
    updatePilots(state, payload) {
      state.pilots = payload;
    },
  },
  state: {
    pilots: [],
  },
};
