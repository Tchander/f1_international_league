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
              <th class="text-center">Очки</th>
            </tr>
          </thead>
          <tbody class="il-table-body">
            <tr
              class="il-table-row"
              v-for="(result, index) in filterResults(currentRace.results)"
              :key="index"
            >
              <td class="il-table-col">{{ index + 1 }}</td>
              <td class="il-table-col">{{ result.pilot }}</td>
              <td class="il-table-col">{{ result.team }}</td>
              <td class="il-table-col">
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

export default {
  name: "RaceInfo",
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
    filterResults(results) {
      return results
        .filter(
          (res) =>
            res.league === this.leagueForTable && res.race_position !== "DNS"
        )
        .sort((prev, next) => next.score - prev.score);
    },
  },
  async mounted() {
    await this.getRaceByCountry(this.country);
  },
};
</script>

<style scoped></style>
