<template>
  <div>
    <switch-table-buttons />
    <v-simple-table class="il-table">
      <template v-slot:default>
        <table-head :race="race" />
        <table-body :race-length="race.length" :pilots="pilots" />
      </template>
    </v-simple-table>
  </div>
</template>

<script>
import { API_MEDIA_URL } from "@/const";
import { mapActions, mapState } from "vuex";
import TableHead from "@/components/TableHead";
import TableBody from "@/components/TableBody";
import SwitchTableButtons from "@/components/SwitchTableButtons";
export default {
  name: "TableOfResults",
  components: { SwitchTableButtons, TableBody, TableHead },
  API_MEDIA_URL,
  computed: {
    ...mapState("race", {
      race: "race",
    }),
    ...mapState("pilots", {
      pilots: "pilots",
    }),
  },
  methods: {
    ...mapActions("race", ["getAllRace"]),
    ...mapActions("pilots", ["getAllPilots"]),
  },
  async mounted() {
    await this.getAllRace();
    await this.getAllPilots();
  },
};
</script>
