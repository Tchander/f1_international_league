<template>
  <div>
    <header-banner />
    <div class="il-container">
      <navigation :color="'lightGrey'" />
      <teams-cards />
    </div>
    <footer-info :color="'lightGrey'" />
  </div>
</template>

<script>
import HeaderBanner from "@/components/HeaderBanner";
import Navigation from "@/components/Navigation";
import FooterInfo from "@/components/FooterInfo";
import TeamsCards from "@/components/TeamsCards";

export default {
  name: "Teams",
  components: { TeamsCards, FooterInfo, Navigation, HeaderBanner },
};
</script>
