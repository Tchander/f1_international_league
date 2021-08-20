<template>
  <div>
    <header-banner />
    <div class="il__container">
      <navigation />
    </div>
  </div>
</template>

<script>
import Navigation from "../components/Navigation";
import HeaderBanner from "../components/HeaderBanner";

export default {
  name: "TournamentTable",
  components: { Navigation, HeaderBanner },
};
</script>

<style scoped></style>
