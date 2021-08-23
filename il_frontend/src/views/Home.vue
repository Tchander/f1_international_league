<template>
  <div class="home">
    <header-banner />
    <div class="il__container">
      <navigation />
      <iframe
        class="il__video"
        width="800"
        height="450"
        src="https://www.youtube.com/embed/DDLqjtwd9Aw"
        title="YouTube video player"
        frameborder="No"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen
      ></iframe>
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
  margin-bottom: 35px;
}
</style>
