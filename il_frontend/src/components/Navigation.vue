<template>
  <nav
    class="navigation"
    :class="{
      'light-grey': color === 'lightGrey',
    }"
  >
    <router-link class="logo__link" to="/">
      <img class="logo__img" src="../assets/img/il_logo.jpg" alt="logo" />
      <div class="logo__home">Главная</div>
    </router-link>
    <div class="navigation__links">
      <router-link class="navigation__link" to="/calendar"
        >Календарь</router-link
      >
      <router-link class="navigation__link" to="/table"
        >Турнирная таблица</router-link
      >
      <router-link class="navigation__link" to="/teams">Команды</router-link>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Navigation",
  props: {
    color: {
      type: String,
    },
  },
};
</script>

<style scoped>
.navigation {
  width: 100%;
  max-width: 1440px;
  margin: 0 auto 40px auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 5px 15px;
  background-color: #0f3368;
  /*background-color: #2a76e6;*/
  /*background-color: #2aaae6;*/
  /*background-color: rgb(66, 6, 1);*/
  /*background-color: rgb(166, 33, 22);*/
  border-radius: 5px;
}
.navigation.light-grey {
  background-color: #242c41;
}
.logo__link {
  display: flex;
  justify-content: space-between;
  align-items: center;
  text-decoration: none;
}
.logo__img {
  width: 60px;
  height: 60px;
  border-radius: 50%;
}
.logo__home {
  margin-left: 20px;
  text-decoration: none;
  list-style-type: none;
  color: #fff;
  font-weight: 700;
}
.logo__home:hover {
  /*color: rgb(95, 2, 2);*/
  /*color: #1a202c;*/
  color: #fff;
}
.navigation__link {
  text-decoration: none;
  list-style-type: none;
  margin-left: 35px;
  color: #fff;
  font-weight: 700;
}
.navigation__link:hover {
  /*color: rgb(95, 2, 2);*/
  /*color: #1a202c;*/
  color: #fff;
}
</style>
