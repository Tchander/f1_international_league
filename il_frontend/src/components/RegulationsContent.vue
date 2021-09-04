<template>
  <div class="il-regulations">
    <div class="il-regulations-contents">
      <h2 class="il-regulations-contents__title">Содержание</h2>
      <ol class="il-regulations-contents__list">
        <li>
          <a href="#" class="il-regulations-contents__link"
            >Основные положения</a
          >
        </li>
        <li>
          <a href="#" class="il-regulations-contents__link"
            >Регистрация и участие в соревнованиях</a
          >
        </li>
        <li>
          <a href="#" class="il-regulations-contents__link"
            >Общие правила поведения</a
          >
        </li>
        <li>
          <a href="#" class="il-regulations-contents__link"
            >Правила поведения во время квалификации и гонки</a
          >
        </li>
        <li>
          <a href="#" class="il-regulations-contents__link">Классификация</a>
        </li>
        <li>
          <a href="#" class="il-regulations-contents__link">Начисление очков</a>
        </li>
        <li>
          <a href="#" class="il-regulations-contents__link"
            >СК и порядок подачи претензии</a
          >
        </li>
        <li>
          <a href="#" class="il-regulations-contents__link"
            >Нарушения и наказания за них</a
          >
        </li>
      </ol>
    </div>
  </div>
</template>

<script>
export default {
  name: "RegulationsContent",
};
</script>

<style scoped>
.il-regulations {
  background-color: #242c41;
}
.il-regulations-contents__title {
  text-align: left;
  margin-left: 50px;
  padding: 15px 0;
}
.il-regulations-contents__list {
  margin-left: 20px;
}
.il-regulations-contents__list > li {
  text-align: left;
  margin-bottom: 15px;
  padding-left: 10px;
}
.il-regulations-contents__link {
  text-decoration: none;
  color: #fff;
  cursor: pointer;
  transition: all 0.3s linear;
}
.il-regulations-contents__link:hover {
  color: #ce5a5a;
}
</style>
