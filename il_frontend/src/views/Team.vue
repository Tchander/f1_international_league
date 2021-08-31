<template>
  <div>
    <header-banner />
    <div class="il-container">
      <navigation :color="'lightGrey'" />
      <team-cards :teamName="teamName" />
    </div>
    <footer-info :color="'lightGrey'" />
  </div>
</template>

<script>
import HeaderBanner from "@/components/HeaderBanner";
import Navigation from "@/components/Navigation";
import FooterInfo from "@/components/FooterInfo";
import TeamCards from "@/components/TeamCards";

export default {
  name: "Team",
  components: { TeamCards, FooterInfo, Navigation, HeaderBanner },
  props: {
    teamName: {
      type: String,
      required: true,
    },
  },
};
</script>

<style scoped></style>
