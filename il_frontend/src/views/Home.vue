<template>
  <div class="home">
    <header-banner />
    <div class="il-container">
      <navigation />
      <home-video />
    </div>
    <footer-info />
  </div>
</template>

<script>
import Navigation from "@/components/Navigation";
import HeaderBanner from "@/components/HeaderBanner";
import FooterInfo from "@/components/FooterInfo";
import HomeVideo from "@/components/HomeVideo";

export default {
  name: "Home",
  components: { HomeVideo, FooterInfo, HeaderBanner, Navigation },
};
</script>

<style scoped>
.home {
  font-family: "Lato", sans-serif;
}
</style>
