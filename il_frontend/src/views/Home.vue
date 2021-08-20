<template>
  <div class="home">
    <header-banner />
    <div class="il__container">
      <navigation />
      <video
        class="il__video"
        src="../assets/video/il_introduction.webm"
        autoplay
        loop
        controls
        muted
        width="1200px"
      ></video>
    </div>
    <footer-info />
  </div>
</template>

<script>
import Navigation from "../components/Navigation";
import HeaderBanner from "../components/HeaderBanner";
import FooterInfo from "../components/FooterInfo";

export default {
  name: "Home",
  components: { FooterInfo, HeaderBanner, Navigation },
};
</script>

<style scoped>
.home {
  font-family: "Lato", sans-serif;
}
.il__video {
  margin-bottom: 30px;
}
</style>
