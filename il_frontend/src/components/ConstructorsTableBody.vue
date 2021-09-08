<template>
  <tbody class="il-table-body" v-if="teams.length">
    <router-link
      tag="tr"
      class="il-table-row il-table-team-row"
      :to="{
        name: 'Team',
        path: '/team' + team.url_name,
        params: { teamName: team.url_name },
      }"
      v-for="(team, index) in teams"
      :key="index"
    >
      <td
        class="il-table-col"
        :class="{
          gold: index + 1 === $options.POSITIONS.FIRST,
          silver: index + 1 === $options.POSITIONS.SECOND,
          bronze: index + 1 === $options.POSITIONS.THIRD,
        }"
      >
        {{ index + 1 }}
      </td>
      <td
        class="il-table-col"
        :class="{
          gold: index + 1 === $options.POSITIONS.FIRST,
          silver: index + 1 === $options.POSITIONS.SECOND,
          bronze: index + 1 === $options.POSITIONS.THIRD,
        }"
      >
        {{ team.name }}
      </td>
      <td
        class="il-table-col"
        :class="{
          gold: index + 1 === $options.POSITIONS.FIRST,
          silver: index + 1 === $options.POSITIONS.SECOND,
          bronze: index + 1 === $options.POSITIONS.THIRD,
        }"
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
        :class="{
          gold: index + 1 === $options.POSITIONS.FIRST,
          silver: index + 1 === $options.POSITIONS.SECOND,
          bronze: index + 1 === $options.POSITIONS.THIRD,
        }"
        v-else-if="league === $options.LEAGUES.SECOND"
      >
        <div v-if="team.total_score_league2 % 1 !== 0">
          {{ team.total_score_league2 }}
        </div>
        <div v-else>
          {{ parseInt(team.total_score_league2) }}
        </div>
      </td>
    </router-link>
  </tbody>
</template>

<script>
import { LEAGUES } from "@/const";
import { POSITIONS } from "@/const";

export default {
  name: "ConstructorsTableBody",
  LEAGUES,
  POSITIONS,
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
};
</script>

<style scoped>
.il-table-team-row.il-table-team-row.il-table-team-row.il-table-team-row {
  cursor: pointer;
}
</style>
