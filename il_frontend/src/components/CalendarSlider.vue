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
  name: "CalendarSlider",
  data() {
    return {
      items: [
        {
          src: require("@/assets/img/calendar/calendarIL1.jpg"),
        },
        {
          src: require("@/assets/img/calendar/calendarIL2.jpg"),
        },
      ],
    };
  },
};
</script>

<style scoped>
.slider_block {
  margin-bottom: 30px;
  min-height: 899px;
}
</style>
