<template>
  <div>
    <v-card class="il-team-card" v-for="(team, index) in teams" :key="index">
      <router-link
        class="il-team-link"
        :to="{
          name: 'Team',
          path: '/team' + team.url_name,
          params: { teamName: team.url_name },
        }"
      >
        <v-card-title class="il-team-card__title">{{ team.name }}</v-card-title>
        <v-card-text class="il-team-card__content">
          <v-img
            :src="$options.API_MEDIA_URL + team.image"
            class="il-team-card__image"
          ></v-img>
          <div class="il-team-card__text-content">
            <div v-for="(pilot, i) in filterByLeague(team.pilots)" :key="i">
              <h3
                v-if="pilot.league === 1 && i === 0"
                class="il-team-card__text-content__league"
              >
                Лига 1
              </h3>
              <h3
                v-if="pilot.league === 2 && i === 2"
                class="il-team-card__text-content__league"
              >
                Лига 2
              </h3>
              <h4 class="il-team-card__text-content__pilot">
                {{ i + 1 }}. {{ pilot.name }}
              </h4>
            </div>
          </div>
        </v-card-text>
      </router-link>
    </v-card>
  </div>
</template>

<script>
import { API_MEDIA_URL } from "@/const";
import { mapActions, mapState } from "vuex";
export default {
  name: "TeamsCards",
  API_MEDIA_URL,
  computed: {
    ...mapState("teams", {
      teams: "teams",
    }),
  },
  methods: {
    ...mapActions("teams", ["getAllTeams"]),
    ...mapActions("pilots", ["getAllPilots"]),
    filterByLeague(pilots) {
      return pilots.sort((prev, next) => prev.league - next.league);
    },
  },
  async mounted() {
    await this.getAllTeams();
    await this.getAllPilots();
  },
};
</script>

<style scoped>
.il-team-card.il-team-card.il-team-card {
  max-width: 1000px;
  margin: 0 auto 20px auto;
  border-radius: 20px;
  border: 1px solid #fff;
  background-color: #242c41;
  transition: 0.5s;
}
.il-team-card.il-team-card.il-team-card:hover {
  box-shadow: -5px 5px 10px 5px rgb(92, 25, 48),
    5px -5px 10px 5px rgb(23, 123, 222);
}
.il-team-card__title {
  color: #fff;
  font-size: 26px;
  font-weight: 700;
}

.il-team-card__content {
  display: flex;
}

.il-team-card__image {
  max-width: 750px;
}

.il-team-card__text-content {
  width: 100%;
  text-align: left;
  padding: 15px 0 0 40px;
}

.il-team-card__text-content__league {
  color: #fff;
  margin: 60px 0 20px 0;
  font-size: 20px;
}

.il-team-card__text-content__pilot {
  color: #fff;
  font-size: 18px;
  font-weight: 400;
  margin-bottom: 15px;
}
.il-team-link {
  text-decoration: none;
}
</style>
