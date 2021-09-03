<template>
  <div>
    <header-banner />
    <div class="il-container">
      <navigation />
      <calendar-slider />
    </div>
    <footer-info />
  </div>
</template>

<script>
import HeaderBanner from "@/components/HeaderBanner";
import Navigation from "@/components/Navigation";
import CalendarSlider from "@/components/CalendarSlider";
import FooterInfo from "@/components/FooterInfo";
export default {
  name: "Calendar",
  components: { FooterInfo, CalendarSlider, Navigation, HeaderBanner },
};
</script>

<style scoped></style>
