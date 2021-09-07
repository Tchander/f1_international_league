<template>
  <div class="il-constructors-tables">
    <div>
      <h1 class="il-constructors-league-title">Лига 1</h1>
      <v-simple-table class="il-table il-constructor-table" v-if="teams.length">
        <template v-slot:default>
          <constructors-table-head />
          <constructors-table-body
            :teams="filteredTeamsByLeague(teams, $options.LEAGUES.FIRST)"
            :league="$options.LEAGUES.FIRST"
          />
        </template>
      </v-simple-table>
    </div>
    <div>
      <h1 class="il-constructors-league-title">Лига 2</h1>
      <v-simple-table class="il-table il-constructor-table" v-if="teams.length">
        <template v-slot:default>
          <constructors-table-head />
          <constructors-table-body
            :teams="filteredTeamsByLeague(teams, $options.LEAGUES.SECOND)"
            :league="$options.LEAGUES.SECOND"
          />
        </template>
      </v-simple-table>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from "vuex";
import ConstructorsTableHead from "@/components/ConstructorsTableHead";
import ConstructorsTableBody from "@/components/ConstructorsTableBody";
import { LEAGUES } from "@/const";
export default {
  name: "ConstructorsTable",
  LEAGUES,
  components: {
    ConstructorsTableBody,
    ConstructorsTableHead,
  },
  computed: {
    ...mapState("teams", {
      teams: "teams",
    }),
  },
  methods: {
    ...mapActions("teams", ["getAllTeams"]),
    filteredTeamsByLeague(teams, league) {
      if (league === LEAGUES.FIRST) {
        return teams.sort(
          (prev, next) => next.total_score_league1 - prev.total_score_league1
        );
      } else if (league === LEAGUES.SECOND) {
        return teams.sort(
          (prev, next) => next.total_score_league2 - prev.total_score_league2
        );
      }
    },
  },
  async mounted() {
    await this.getAllTeams();
  },
};
</script>

<style scoped>
.il-constructors-tables {
  display: flex;
  justify-content: space-between;
}
.il-constructor-table.il-constructor-table.il-constructor-table {
  width: 580px;
}
.il-constructors-league-title {
  margin-bottom: 20px;
  padding: 10px 0;
  background-color: #242c41;
  color: #fff;
  font-size: 32px;
}
</style>
