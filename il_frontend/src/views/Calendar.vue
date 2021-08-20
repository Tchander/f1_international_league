<template>
  <div>
    <header-banner />
    <div class="il__container">
      <navigation />
    </div>
  </div>
</template>

<script>
import HeaderBanner from "../components/HeaderBanner";
import Navigation from "../components/Navigation";
export default {
  name: "Calendar",
  components: { Navigation, HeaderBanner },
};
</script>

<style scoped></style>
