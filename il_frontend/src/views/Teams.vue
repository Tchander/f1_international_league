<template>
  <div>
    <header-banner />
    <div class="il__container">
      <navigation :color="'lightGrey'" />
      <v-card
        class="il__team__card"
        v-for="(team, index) in teams"
        :key="index"
        color="#242c41"
        style="border: 1px solid #fff"
      >
        <router-link
          class="il__team__link"
          :to="{
            name: 'Team',
            path: '/team' + team.urlName,
            params: { teamName: team.urlName },
          }"
        >
          <v-card-title class="il__team__card__title">{{
            team.name
          }}</v-card-title>
          <v-card-text class="il__team__card__content">
            <v-img :src="team.src" class="il__team__card__image"></v-img>
            <div class="il__team__card__text__content">
              <div v-for="(pilot, i) in team.pilots" :key="i">
                <h3
                  class="il__team__card__text__content__league"
                  v-if="pilot.league === 1 && i !== 1"
                >
                  Лига 1
                </h3>
                <h4
                  class="il__team__card__text__content__pilot"
                  v-if="pilot.league === 1"
                >
                  {{ i + 1 }}. {{ pilot.name }}
                </h4>
                <h3
                  class="il__team__card__text__content__league"
                  v-if="pilot.league === 2 && i !== 3"
                >
                  Лига 2
                </h3>
                <h4
                  class="il__team__card__text__content__pilot"
                  v-if="pilot.league === 2"
                >
                  {{ i - 1 }}. {{ pilot.name }}
                </h4>
              </div>
            </div>
          </v-card-text>
        </router-link>
      </v-card>
    </div>
    <footer-info :color="'lightGrey'" />
  </div>
</template>

<script>
import HeaderBanner from "../components/HeaderBanner";
import Navigation from "../components/Navigation";
import FooterInfo from "../components/FooterInfo";

export default {
  name: "Teams",
  components: { FooterInfo, Navigation, HeaderBanner },
  computed: {
    teams() {
      return this.$store.getters.allTeams;
    },
  },
};
</script>

<style scoped>
.il__team__card {
  max-width: 1000px;
  margin: 0 auto 20px auto;
  border-radius: 20px;
}

.il__team__card__title {
  color: #fff;
  font-size: 26px;
  font-weight: 700;
}

.il__team__card__content {
  display: flex;
}

.il__team__card__image {
  max-width: 750px;
}

.il__team__card__text__content {
  width: 100%;
  text-align: left;
  padding: 15px 0 0 40px;
}

.il__team__card__text__content__league {
  color: #fff;
  margin: 60px 0 20px 0;
  font-size: 20px;
}

.il__team__card__text__content__pilot {
  color: #fff;
  font-size: 18px;
  font-weight: 400;
  margin-bottom: 15px;
}
.il__team__link {
  text-decoration: none;
}
</style>
