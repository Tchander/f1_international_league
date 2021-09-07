<template>
  <div>
    <header-banner />
    <div class="il-container">
      <navigation :color="'lightGrey'" />
      <constructors-table />
    </div>
    <footer-info :color="'lightGrey'" />
  </div>
</template>

<script>
import Navigation from "@/components/Navigation";
import FooterInfo from "@/components/FooterInfo";
import HeaderBanner from "@/components/HeaderBanner";
import ConstructorsTable from "@/components/ConstructorsTable";
export default {
  name: "ConstructorsCup",
  components: { ConstructorsTable, FooterInfo, Navigation, HeaderBanner },
};
</script>

<style scoped></style>
