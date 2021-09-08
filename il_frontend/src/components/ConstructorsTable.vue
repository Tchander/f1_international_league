<template>
  <div class="il-constructors-tables">
    <div>
      <h1 class="il-constructors-league-title">Лига 1</h1>
      <v-simple-table
        class="il-table il-constructor-table"
        v-if="teamsFilteredByLeague1.length"
      >
        <template v-slot:default>
          <constructors-table-head />
          <constructors-table-body
            :teams="teamsFilteredByLeague1"
            :league="$options.LEAGUES.FIRST"
          />
        </template>
      </v-simple-table>
    </div>
    <div>
      <h1 class="il-constructors-league-title">Лига 2</h1>
      <v-simple-table
        class="il-table il-constructor-table"
        v-if="teamsFilteredByLeague2.length"
      >
        <template v-slot:default>
          <constructors-table-head />
          <constructors-table-body
            :teams="teamsFilteredByLeague2"
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
      teamsFilteredByLeague1: "teamsFilteredByLeague1",
      teamsFilteredByLeague2: "teamsFilteredByLeague2",
    }),
  },
  methods: {
    ...mapActions("teams", ["getAllTeams"]),
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
  border-radius: 4px;
}
</style>
