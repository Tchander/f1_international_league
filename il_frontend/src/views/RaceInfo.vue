<template>
  <div>
    <header-banner />
    <div class="il-container">
      <navigation :color="'lightGrey'" />
      <v-simple-table class="il-table" v-if="currentRace">
        <template v-slot:default>
          <thead>
            <tr class="il-table-head">
              <th class="text-center">Поз.</th>
              <th class="text-center">Пилот</th>
              <th class="text-center">Команда</th>
              <th class="text-center">Позиция на старте</th>
              <th class="text-center">Лучший круг</th>
              <th class="text-center">Очки</th>
            </tr>
          </thead>
          <tbody class="il-table-body">
            <tr
              class="il-table-row"
              v-for="(result, index) in filterResultsByLeague(
                currentRace.results
              )"
              :key="index"
            >
              <td
                class="il-table-col"
                :class="
                  $options.getClassByPosition(Number(result.race_position) - 1)
                "
              >
                {{ result.race_position }}
              </td>
              <td
                class="il-table-col"
                :class="
                  $options.getClassByPosition(Number(result.race_position) - 1)
                "
              >
                {{ result.pilot }}
              </td>
              <td
                class="il-table-col"
                :class="
                  $options.getClassByPosition(Number(result.race_position) - 1)
                "
              >
                {{ result.team }}
              </td>
              <td
                class="il-table-col"
                :class="
                  $options.getClassByPosition(Number(result.race_position) - 1)
                "
              >
                {{ result.qualifying_position }}
              </td>
              <td
                class="il-table-col"
                :class="
                  $options.getClassByPosition(Number(result.race_position) - 1)
                "
              >
                {{ result.best_lap }}
              </td>
              <td
                class="il-table-col"
                :class="
                  $options.getClassByPosition(Number(result.race_position) - 1)
                "
              >
                <div v-if="result.score % 1 !== 0">
                  {{ result.score }}
                </div>
                <div v-else>
                  {{ parseInt(result.score) }}
                </div>
              </td>
            </tr>
          </tbody>
        </template>
      </v-simple-table>
    </div>
    <footer-info :color="'lightGrey'" />
  </div>
</template>

<script>
import FooterInfo from "@/components/FooterInfo";
import Navigation from "@/components/Navigation";
import HeaderBanner from "@/components/HeaderBanner";
import { mapActions, mapState } from "vuex";
import { POSITIONS } from "@/const";
import { getClassByPosition } from "@/helpers";

export default {
  name: "RaceInfo",
  POSITIONS,
  getClassByPosition,
  components: { FooterInfo, Navigation, HeaderBanner },
  props: {
    country: {
      type: String,
      required: true,
    },
  },
  computed: {
    ...mapState("race", {
      currentRace: "currentRace",
    }),
    ...mapState("leagueForTable", {
      leagueForTable: "leagueForTable",
    }),
  },
  methods: {
    ...mapActions("race", ["getRaceByCountry"]),
    ...mapActions("leagueForTable", ["switchLeagueNumber"]),
    filterResultsByLeague(results) {
      return results.filter((res) => res.league === this.leagueForTable);
    },
    changeLeagueNumber() {
      const { league } = this.$route.query;
      if (league) {
        this.switchLeagueNumber(Number(league));
      }
    },
  },
  created() {
    this.changeLeagueNumber();
  },
  async mounted() {
    await this.getRaceByCountry(this.country);
  },
};
</script>
