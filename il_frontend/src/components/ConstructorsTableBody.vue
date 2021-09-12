<template>
  <tbody class="il-table-body" v-if="teams.length">
    <tr
      class="il-table-row il-table-team-row"
      v-for="(team, index) in teams"
      :key="index"
      @click="toSelectedTeam(team.url_name)"
    >
      <td class="il-table-col" :class="$options.getClassByPosition(index)">
        {{ index + 1 }}
      </td>
      <td class="il-table-col" :class="$options.getClassByPosition(index)">
        {{ team.name }}
      </td>
      <td
        class="il-table-col"
        :class="$options.getClassByPosition(index)"
        v-if="league === $options.LEAGUES.FIRST"
      >
        <div v-if="team.total_score_league1 % 1 !== 0">
          {{ team.total_score_league1 }}
        </div>
        <div v-else>
          {{ parseInt(team.total_score_league1) }}
        </div>
      </td>
      <td
        class="il-table-col"
        :class="$options.getClassByPosition(index)"
        v-else-if="league === $options.LEAGUES.SECOND"
      >
        <div v-if="team.total_score_league2 % 1 !== 0">
          {{ team.total_score_league2 }}
        </div>
        <div v-else>
          {{ parseInt(team.total_score_league2) }}
        </div>
      </td>
    </tr>
  </tbody>
</template>

<script>
import { LEAGUES } from "@/const";
import { POSITIONS } from "@/const";
import { getClassByPosition } from "@/helpers";

export default {
  name: "ConstructorsTableBody",
  LEAGUES,
  POSITIONS,
  getClassByPosition,
  props: {
    teams: {
      type: Array,
      required: true,
    },
    league: {
      type: Number,
      required: true,
    },
  },
  methods: {
    toSelectedTeam(urlName) {
      this.$router.push({
        name: "Team",
        path: "/team" + urlName,
        params: { teamName: urlName },
      });
    },
  },
};
</script>

<style scoped>
.il-table-team-row.il-table-team-row.il-table-team-row.il-table-team-row {
  cursor: pointer;
}
</style>
