<template>
  <div class="slider_block">
    <v-carousel height="auto" cycle hide-delimiters :show-arrows="false">
      <v-carousel-item
        v-for="(item, i) in items"
        :key="i"
        :src="item.src"
      ></v-carousel-item>
    </v-carousel>
  </div>
</template>

<script>
export default {
  name: "HomeSlider",
  data() {
    return {
      items: [
        {
          src: require("@/assets/img/slider/il_driverstandings.jpg"),
        },
        {
          src: require("@/assets/img/slider/il_teamstandings.jpg"),
        },
        {
          src: require("@/assets/img/slider/il2_driverstandings.jpg"),
        },
        {
          src: require("@/assets/img/slider/il2_teamstandings.jpg"),
        },
        {
          src: require("@/assets/img/slider/calendarIL1.jpg"),
        },
        {
          src: require("@/assets/img/slider/calendarIL2.jpg"),
        },
      ],
    };
  },
};
</script>

<style scoped>
.slider_block {
  margin-bottom: 30px;
  min-height: 642px;
}
</style>
