<template>
  <v-footer
    class="il-footer"
    :class="{
      'light-grey': color === 'lightGrey',
    }"
  >
    <v-card flat tile class="il-footer-card">
      <v-card-text
        class="il-footer-card__text"
        :class="{
          'light-grey': color === 'lightGrey',
        }"
      >
        <ul class="il-footer-social">
          <li v-for="(item, i) in items" :key="i">
            <a :href="item.href" class="il-footer-link" target="_blank">
              <img class="il-footer-link__img" :src="item.src" alt="" />
            </a>
          </li>
        </ul>
      </v-card-text>
    </v-card>
  </v-footer>
</template>

<script>
export default {
  name: "FooterInfo",
  props: {
    color: {
      type: String,
    },
  },
  data() {
    return {
      items: [
        {
          src: require("@/assets/img/vk.svg"),
          href: "https://vk.com/f1ileague",
        },
        {
          src: require("@/assets/img/telegram.svg"),
          href: "https://t.me/joinchat/JmWgNEOkS9tfo58lIOBhhw",
        },
        {
          src: require("@/assets/img/youtube.svg"),
          href: "https://youtube.com/channel/UC9F7VXNzjL4y07XXao0D4PQ",
        },
        {
          src: require("@/assets/img/discord.svg"),
          href: "https://discord.gg/g6ADEgp9tH",
        },
      ],
    };
  },
};
</script>

<style scoped>
.il-footer.il-footer.il-footer {
  background-color: #0f3368;
}
.il-footer.il-footer.il-footer.light-grey {
  background-color: #242c41;
}
.il-footer-card {
  width: 100%;
  color: #fff;
  border-radius: 5px;
}
.il-footer-card__text {
  background-color: #0f3368;
  color: #fff;
}
.il-footer-social {
  display: flex;
  align-items: center;
  justify-content: center;
}
.il-footer-social > li {
  list-style-type: none;
  width: 40px;
  height: 40px;
  margin: 0 20px;
}
.il-footer-link {
  text-decoration: none;
}
.il-footer-link__img {
  width: 40px;
  height: 40px;
}
</style>
