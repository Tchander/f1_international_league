<template>
  <div class="il-league-buttons">
    <v-btn
      @click="switchTable(1)"
      :class="{ active: isActiveLeague1 }"
      class="il-league__btn"
      >Лига 1</v-btn
    >
    <v-btn
      @click="switchTable(2)"
      :class="{ active: isActiveLeague2 }"
      class="il-league__btn"
      >Лига 2</v-btn
    >
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
export default {
  name: "SwitchTableButtons",
  data() {
    return {
      isActiveLeague1: false,
      isActiveLeague2: false,
    };
  },
  computed: {
    ...mapState("leagueForTable", {
      leagueForTable: "leagueForTable",
    }),
  },
  methods: {
    ...mapActions("leagueForTable", ["switchLeagueNumber"]),
    switchTable(leagueNumber) {
      if (leagueNumber === 1) {
        this.isActiveLeague1 = true;
        this.isActiveLeague2 = false;
      } else {
        this.isActiveLeague1 = false;
        this.isActiveLeague2 = true;
      }
      this.switchLeagueNumber(leagueNumber);
    },
  },
  mounted() {
    this.isActiveLeague1 = true;
  },
};
</script>

<style scoped>
.il-league-buttons.il-league-buttons.il-league-buttons {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
  /*background-color: #1a202c;*/
  /*height: 60px;*/
}
.il-league__btn.il-league__btn.il-league__btn {
  width: 100%;
  max-width: 200px;
  height: 60px;
  padding: 0;
  font-size: 20px;
  text-transform: none;
  margin-left: 20px;
  color: #fff;
  background-color: #242c41;
}
.active.active.active {
  background-color: #304f9c;
}
.il-league__btn:hover.il-league__btn:hover.il-league__btn:hover {
  background-color: #304f9c;
}
</style>
