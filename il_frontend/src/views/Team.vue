<template>
  <div>
    <header-banner />
    <div class="il__container">
      <navigation :color="'lightGrey'" />
      <div class="il__pilot__cards">
        <v-card
          class="il__pilot__card"
          v-for="(pilot, index) in team.pilots"
          :key="index"
        >
          <v-card-title>
            <div class="il__pilot__card__title">
              {{ pilot.name }}
            </div>
          </v-card-title>
          <v-card-text class="il__pilot__card__content">
            <v-img class="il__pilot__card__image" :src="pilot.src"></v-img>
          </v-card-text>
        </v-card>
      </div>
    </div>
    <footer-info :color="'lightGrey'" />
  </div>
</template>

<script>
import HeaderBanner from "../components/HeaderBanner";
import Navigation from "../components/Navigation";
import FooterInfo from "../components/FooterInfo";

export default {
  name: "Team",
  components: { FooterInfo, Navigation, HeaderBanner },
  props: {
    teamName: {
      type: String,
      required: true,
    },
  },
  computed: {
    team() {
      return this.$store.getters.getTeamByName(this.teamName);
    },
  },
};
</script>

<style scoped>
.il__pilot__cards {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  width: 100%;
}

.il__pilot__card.il__pilot__card.il__pilot__card {
  margin-bottom: 40px;
  border-radius: 20px;
  width: 48%;
  background-color: #242c41;
  border: 1px solid #fff;
  transition: 0.5s;
}
.il__pilot__card.il__pilot__card.il__pilot__card:hover {
  /*box-shadow: 0 0 10px 5px rgb(139, 50, 81);*/
  box-shadow: -5px 5px 10px 5px rgb(92, 25, 48),
    5px -5px 10px 5px rgb(23, 123, 222);
}
.il__pilot__card__title {
  color: #fff;
  font-size: 26px;
  font-weight: 700;
  margin: 0 auto;
  border-radius: 4px;
  /*box-shadow: 0 0 8px rgb(255 255 255);*/
  padding: 2px 5px;
}

.il__pilot__card__image.il__pilot__card__image.il__pilot__card__image {
  width: 207px;
  height: 213px;
  margin: 0 auto;
  border-radius: 10px;
  box-shadow: 0 0 8px rgb(255 255 255);
}
</style>
