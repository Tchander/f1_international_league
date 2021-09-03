<template>
  <thead>
    <tr class="il-table-head">
      <th class="text-center">Поз.</th>
      <th class="text-center">Пилот</th>
      <th class="text-center">Команда</th>
      <th class="text-center">Очки</th>
      <th v-for="(r, index) in race" :key="index">
        <router-link
          :to="{
            name: 'Race',
            path: '/race' + r.country,
            params: { country: r.country },
          }"
        >
          <v-img
            class="il-table-image"
            :src="$options.API_MEDIA_URL + r.country_flag"
          ></v-img>
        </router-link>
      </th>
    </tr>
  </thead>
</template>

<script>
import { API_MEDIA_URL } from "@/const";
export default {
  name: "TableHead",
  API_MEDIA_URL,
  props: {
    race: {
      type: Array,
      required: true,
    },
  },
};
</script>

<style scoped>
.il-table-head.il-table-head.il-table-head {
  background-color: #242c41;
}
.il-table-head.il-table-head.il-table-head > th {
  color: #fff;
}
.il-table-image.il-table-image.il-table-image {
  width: 50px;
  height: 32px;
}
</style>
