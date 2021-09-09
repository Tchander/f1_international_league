<template>
  <div>
    <header-banner />
    <div class="il-container">
      <navigation :color="'lightGrey'" />
      <regulations-content />
    </div>
    <footer-info :color="'lightGrey'" />
  </div>
</template>

<script>
import HeaderBanner from "@/components/HeaderBanner";
import Navigation from "@/components/Navigation";
import FooterInfo from "@/components/FooterInfo";
import RegulationsContent from "@/components/RegulationsContent";
export default {
  name: "Regulations",
  components: { RegulationsContent, HeaderBanner, Navigation, FooterInfo },
};
</script>
