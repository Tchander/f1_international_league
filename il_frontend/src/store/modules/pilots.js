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
    // async getAllPilots(ctx) {
    //   const { data } = await axios.get("http://localhost:8000/api/v1/pilots/");
    //   ctx.commit("updatePilots", data);
    // },
  },
  mutations: {
    updatePilots(state, pilots) {
      state.pilots = pilots;
    },
  },
  state: {
    pilots: [],
  },
  getters: {
    allPilots(state) {
      return state.pilots;
    },
  },
};
