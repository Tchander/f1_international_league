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
  getters: {
    allTeams(state) {
      return state.teams;
    },
    getTeamByName: (state) => (urlName) => {
      return state.teams.find((team) => team.url_name === urlName);
    },
  },
  // state: {
  //   teams: [
  //     {
  //       name: "Alfa Romeo",
  //       id: 1,
  //       urlName: "alfaromeo",
  //       src: require("@/assets/img/teams/alfa_romeo.jpg"),
  //       pilots: [
  //         {
  //           id: 1,
  //           name: "A. Osadchiy",
  //           src: require("@/assets/img/pilots/league1/osadchiy.jpg"),
  //           league: 1,
  //           status: "active",
  //         },
  //         {
  //           id: 2,
  //           name: "A. Zakharov",
  //           src: require("@/assets/img/pilots/league1/zakharov.jpg"),
  //           league: 1,
  //           status: "active",
  //         },
  //         {
  //           id: 3,
  //           name: "D. Tsvetkov",
  //           src: require("@/assets/img/pilots/league1/osadchiy.jpg"),
  //           league: 2,
  //           status: "active",
  //         },
  //         {
  //           id: 4,
  //           name: "E. Bragin",
  //           src: require("@/assets/img/pilots/league1/osadchiy.jpg"),
  //           league: 2,
  //           status: "active",
  //         },
  //       ],
  //     },
  //     {
  //       name: "Alpha Tauri",
  //       id: 2,
  //       urlName: "alphatauri",
  //       src: require("@/assets/img/teams/alpha_tauri.jpg"),
  //       pilots: [
  //         {
  //           id: 1,
  //           name: "S. Shibanov",
  //           src: require("@/assets/img/pilots/league1/shibanov.jpg"),
  //           league: 1,
  //           status: "active",
  //         },
  //         {
  //           id: 2,
  //           name: "A. Derbasov",
  //           src: require("@/assets/img/pilots/league1/derbasov.jpg"),
  //           league: 1,
  //           status: "active",
  //         },
  //         {
  //           id: 3,
  //           name: "V. Dronzikov",
  //           src: require("@/assets/img/pilots/league1/derbasov.jpg"),
  //           league: 2,
  //           status: "active",
  //         },
  //         {
  //           id: 4,
  //           name: "E. Khichin",
  //           src: require("@/assets/img/pilots/league1/derbasov.jpg"),
  //           league: 2,
  //           status: "active",
  //         },
  //       ],
  //     },
  //     {
  //       name: "Alpine",
  //       id: 3,
  //       urlName: "alpine",
  //       src: require("@/assets/img/teams/alpine.jpg"),
  //       pilots: [
  //         {
  //           id: 1,
  //           name: "A. Shilov",
  //           src: require("@/assets/img/pilots/league1/shilov.jpg"),
  //           league: 1,
  //           status: "active",
  //         },
  //         {
  //           id: 2,
  //           name: "O. Antonenko",
  //           src: require("@/assets/img/pilots/league1/antonenko.jpg"),
  //           league: 1,
  //           status: "active",
  //         },
  //         {
  //           id: 3,
  //           name: "A. Alexeev",
  //           src: require("@/assets/img/pilots/league1/antonenko.jpg"),
  //           league: 2,
  //           status: "active",
  //         },
  //         {
  //           id: 4,
  //           name: "D. Poltorak",
  //           src: require("@/assets/img/pilots/league1/antonenko.jpg"),
  //           league: 2,
  //           status: "active",
  //         },
  //       ],
  //     },
  //     {
  //       name: "Aston Martin",
  //       id: 4,
  //       urlName: "astonmartin",
  //       src: require("@/assets/img/teams/aston_martin.jpg"),
  //       pilots: [
  //         {
  //           id: 1,
  //           name: "N. Savosin",
  //           src: require("@/assets/img/pilots/league1/tomazov.jpg"),
  //           league: 1,
  //           status: "active",
  //         },
  //         {
  //           id: 2,
  //           name: "A. Tomazov",
  //           src: require("@/assets/img/pilots/league1/tomazov.jpg"),
  //           league: 1,
  //           status: "active",
  //         },
  //         {
  //           id: 3,
  //           name: "W. Borg",
  //           src: require("@/assets/img/pilots/league1/tomazov.jpg"),
  //           league: 2,
  //           status: "active",
  //         },
  //         {
  //           id: 4,
  //           name: "A. Strelkov",
  //           src: require("@/assets/img/pilots/league1/tomazov.jpg"),
  //           league: 2,
  //           status: "active",
  //         },
  //       ],
  //     },
  //     {
  //       name: "Ferrari",
  //       id: 5,
  //       urlName: "ferrari",
  //       src: require("@/assets/img/teams/ferrari.jpg"),
  //       pilots: [
  //         {
  //           id: 1,
  //           name: "V. Pavlyukevich",
  //           src: require("@/assets/img/pilots/league1/pavlyukevich.jpg"),
  //           league: 1,
  //           status: "active",
  //         },
  //         {
  //           id: 2,
  //           name: "A. Vlasov",
  //           src: require("@/assets/img/pilots/league1/vlasov.jpg"),
  //           league: 1,
  //           status: "active",
  //         },
  //         {
  //           id: 3,
  //           name: "A. Korzhikov",
  //           src: require("@/assets/img/pilots/league1/pavlyukevich.jpg"),
  //           league: 2,
  //           status: "active",
  //         },
  //         {
  //           id: 4,
  //           name: "V. Bublyk",
  //           src: require("@/assets/img/pilots/league1/pavlyukevich.jpg"),
  //           league: 2,
  //           status: "active",
  //         },
  //       ],
  //     },
  //     {
  //       name: "Haas",
  //       id: 6,
  //       urlName: "haas",
  //       src: require("@/assets/img/teams/haas.jpg"),
  //       pilots: [
  //         {
  //           id: 1,
  //           name: "R. Lavrov",
  //           src: require("@/assets/img/pilots/league1/lavrov.jpg"),
  //           league: 1,
  //           status: "active",
  //         },
  //         {
  //           id: 2,
  //           name: "S. Nevazgniy",
  //           src: require("@/assets/img/pilots/league1/nevazgny.jpg"),
  //           league: 1,
  //           status: "active",
  //         },
  //         {
  //           id: 3,
  //           name: "D. Tymoshenko",
  //           src: require("@/assets/img/pilots/league1/lavrov.jpg"),
  //           league: 2,
  //           status: "active",
  //         },
  //         {
  //           id: 4,
  //           name: "M. Zhurkovich",
  //           src: require("@/assets/img/pilots/league1/lavrov.jpg"),
  //           league: 2,
  //           status: "active",
  //         },
  //       ],
  //     },
  //     {
  //       name: "McLaren",
  //       id: 7,
  //       urlName: "mclaren",
  //       src: require("@/assets/img/teams/mclaren.jpg"),
  //       pilots: [
  //         {
  //           id: 1,
  //           name: "V. Solomko",
  //           src: require("@/assets/img/pilots/league1/solomko.jpg"),
  //           league: 1,
  //           status: "active",
  //         },
  //         {
  //           id: 2,
  //           name: "N. Sklyarenko",
  //           src: require("@/assets/img/pilots/league1/sklyarenko.jpg"),
  //           league: 1,
  //           status: "active",
  //         },
  //         {
  //           id: 3,
  //           name: "A. Perminow",
  //           src: require("@/assets/img/pilots/league1/solomko.jpg"),
  //           league: 2,
  //           status: "active",
  //         },
  //         {
  //           id: 4,
  //           name: "M. Boyko",
  //           src: require("@/assets/img/pilots/league1/solomko.jpg"),
  //           league: 2,
  //           status: "active",
  //         },
  //       ],
  //     },
  //     {
  //       name: "Mercedes",
  //       id: 8,
  //       urlName: "mercedes",
  //       src: require("@/assets/img/teams/mercedes.jpg"),
  //       pilots: [
  //         {
  //           id: 1,
  //           name: "S. Makin",
  //           src: require("@/assets/img/pilots/league1/makin.jpg"),
  //           league: 1,
  //           status: "active",
  //         },
  //         {
  //           id: 2,
  //           name: "A. Akhmetov",
  //           src: require("@/assets/img/pilots/league1/akhmetov.jpg"),
  //           league: 1,
  //           status: "active",
  //         },
  //         {
  //           id: 3,
  //           name: "S. Belov",
  //           src: require("@/assets/img/pilots/league1/makin.jpg"),
  //           league: 2,
  //           status: "active",
  //         },
  //         {
  //           id: 4,
  //           name: "J. Stakanova",
  //           src: require("@/assets/img/pilots/league1/makin.jpg"),
  //           league: 2,
  //           status: "active",
  //         },
  //       ],
  //     },
  //     {
  //       name: "RedBull",
  //       id: 9,
  //       urlName: "redbull",
  //       src: require("@/assets/img/teams/red_bull.jpg"),
  //       pilots: [
  //         {
  //           id: 1,
  //           name: "N. Lipchenko",
  //           src: require("@/assets/img/pilots/league1/lipchenko.jpg"),
  //           league: 1,
  //           status: "active",
  //         },
  //         {
  //           id: 2,
  //           name: "S. Kryukov",
  //           src: require("@/assets/img/pilots/league1/kryukov.jpg"),
  //           league: 1,
  //           status: "active",
  //         },
  //         {
  //           id: 3,
  //           name: "S. Bortsova",
  //           src: require("@/assets/img/pilots/league1/lipchenko.jpg"),
  //           league: 2,
  //           status: "active",
  //         },
  //         {
  //           id: 4,
  //           name: "A. Dzis",
  //           src: require("@/assets/img/pilots/league1/lipchenko.jpg"),
  //           league: 2,
  //           status: "active",
  //         },
  //       ],
  //     },
  //     {
  //       name: "Williams",
  //       id: 10,
  //       urlName: "williams",
  //       src: require("@/assets/img/teams/williams.jpg"),
  //       pilots: [
  //         {
  //           id: 1,
  //           name: "I. Shurakov",
  //           src: require("@/assets/img/pilots/league1/shurakov.jpg"),
  //           league: 1,
  //           status: "active",
  //         },
  //         {
  //           id: 2,
  //           name: "A. Pogodin",
  //           src: require("@/assets/img/pilots/league1/pogodin.jpg"),
  //           league: 1,
  //           status: "active",
  //         },
  //         {
  //           id: 3,
  //           name: "E. Chander",
  //           src: require("@/assets/img/pilots/league1/pogodin.jpg"),
  //           league: 2,
  //           status: "active",
  //         },
  //         {
  //           id: 4,
  //           name: "D. Bondarev",
  //           src: require("@/assets/img/pilots/league1/pogodin.jpg"),
  //           league: 2,
  //           status: "active",
  //         },
  //       ],
  //     },
  //   ],
  // },
  // getters: {
  //   allTeams(state) {
  //     return state.teams;
  //   },
  //   getTeamByName: (state) => (urlName) => {
  //     return state.teams.find((team) => team.urlName === urlName);
  //   },
  // },
};
