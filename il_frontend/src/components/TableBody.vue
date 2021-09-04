<template>
  <tbody class="il-table-body">
    <tr
      class="il-table-row"
      v-for="(pilot, index) in filterPilotsByLeague(pilots, leagueForTable)"
      :key="index"
    >
      <td
        class="il-table-col"
        :class="{
          gold: index + 1 === 1,
          silver: index + 1 === 2,
          bronze: index + 1 === 3,
        }"
      >
        {{ index + 1 }}
      </td>
      <td class="il-table-col">{{ pilot.name }}</td>
      <td class="il-table-col">{{ pilot.team }}</td>
      <td class="il-table-col">
        <div v-if="pilot.total_score % 1 !== 0">
          {{ pilot.total_score }}
        </div>
        <div v-else class="il-table-col">
          {{ parseInt(pilot.total_score) }}
        </div>
      </td>
      <td
        class="il-table-col"
        :class="{
          gold: result.race_position === '1',
          silver: result.race_position === '2',
          bronze: result.race_position === '3',
        }"
        v-for="(result, index) in filterPilotResultsByLeague(pilot)"
        :key="index + 'A'"
      >
        <div v-if="pilot.total_score % 1 !== 0">
          {{ result.score }} <sub>/{{ result.race_position }}</sub>
        </div>
        <div v-else>
          {{ parseInt(result.score) }}
          <sub>/{{ result.race_position }}</sub>
        </div>
      </td>
      <td
        class="il-table-col"
        v-for="index in numberOfTd(pilot.results)"
        :key="index + 'B'"
      ></td>
    </tr>
  </tbody>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "TableBody",
  props: {
    raceLength: {
      type: Number,
      required: true,
    },
    pilots: {
      type: Array,
      required: true,
    },
  },
  computed: {
    ...mapState("leagueForTable", {
      leagueForTable: "leagueForTable",
    }),
  },
  methods: {
    filterPilotsByLeague(pilots, league) {
      return pilots.filter((p) => p.league === league);
    },
    filterPilotResultsByLeague(pilot) {
      return pilot.results.filter((r) => r.league === pilot.league);
    },
    numberOfTd(number_of_finished_race) {
      return this.raceLength - number_of_finished_race.length;
    },
  },
};
</script>

<style scoped>
.il-table-body.il-table-body.il-table-body {
  background-color: #242c41;
}
.il-table-col.il-table-col.il-table-col {
  color: #fff;
  font-size: 15px;
}
.il-table-row:hover.il-table-row:hover.il-table-row:hover {
  background-color: #0f3368;
}
.gold.gold.gold {
  color: #ffd200;
}
.silver.silver.silver {
  color: #b0b0b0;
}
.bronze.bronze.bronze {
  color: #cb5d28;
}
</style>
