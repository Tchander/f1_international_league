<template>
  <div class="il-pilot-cards" v-if="team">
    <v-card
      class="il-pilot-card"
      v-for="(pilot, index) in team.pilots"
      :key="index"
    >
      <v-card-title>
        <div class="il-pilot-card__title">
          {{ pilot.name }}
        </div>
      </v-card-title>
      <v-card-text class="il-pilot-card__content">
        <v-img
          class="il-pilot-card__image"
          :src="$options.API_MEDIA_URL + pilot.image"
        ></v-img>
        <div class="il-pilot-card__info">
          Лига: <span>{{ pilot.league }}</span>
        </div>
        <div v-if="pilot.total_score % 1 !== 0" class="il-pilot-card__info">
          Очков в личном зачёте: <span>{{ pilot.total_score }}</span>
        </div>
        <div v-else class="il-pilot-card__info">
          Очков в личном зачёте: <span>{{ parseInt(pilot.total_score) }}</span>
        </div>
        <div class="il-pilot-card__info">
          Лучший результат в гонке: <span>{{ pilot.best_race_finish }}</span>
        </div>
        <div class="il-pilot-card__info">
          Лучший результат в квалификации:
          <span>{{ pilot.highest_grid_position }}</span>
        </div>
        <div class="il-pilot-card__info">
          Побед в гонке над напарником:
          <span>{{ pilot.race_victories_over_teammate }}</span>
        </div>
        <div class="il-pilot-card__info">
          Побед в квалификации над напарником:
          <span>{{ pilot.qualifying_victories_over_teammate }}</span>
        </div>
        <div class="il-pilot-card__info">
          Количество сходов: <span>{{ pilot.do_not_finish }}</span>
        </div>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import { API_MEDIA_URL } from "@/const";
import { mapActions, mapState } from "vuex";

export default {
  name: "TeamCards",
  API_MEDIA_URL,
  props: {
    teamName: {
      type: String,
      required: true,
    },
  },
  computed: {
    ...mapState("teams", {
      team: "currentTeam",
    }),
  },
  methods: {
    ...mapActions("teams", ["getTeamByUrlName"]),
  },
  async mounted() {
    await this.getTeamByUrlName(this.teamName);
  },
};
</script>

<style scoped>
.il-pilot-cards {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  width: 100%;
}

.il-pilot-card.il-pilot-card.il-pilot-card {
  margin-bottom: 40px;
  border-radius: 20px;
  width: 48%;
  background-color: #242c41;
  border: 1px solid #fff;
  transition: 0.5s;
  cursor: pointer;
}
.il-pilot-card.il-pilot-card.il-pilot-card:hover {
  box-shadow: -5px 5px 10px 5px rgb(92, 25, 48),
    5px -5px 10px 5px rgb(23, 123, 222);
}
.il-pilot-card__title {
  color: #fff;
  font-size: 26px;
  font-weight: 700;
  margin: 0 auto;
  border-radius: 4px;
  padding: 2px 5px;
}
.il-pilot-card__image.il-pilot-card__image.il-pilot-card__image {
  width: 178px;
  height: 205px;
  margin: 0 auto 20px auto;
  border-radius: 10px;
  box-shadow: 0 0 8px rgb(92, 25, 48);
}
.il-pilot-card__info {
  color: #fff;
  font-size: 18px;
  margin-bottom: 10px;
}
.il-pilot-card__info > span {
  color: rgb(23, 123, 222);
  font-weight: 700;
  font-size: 20px;
}
</style>
