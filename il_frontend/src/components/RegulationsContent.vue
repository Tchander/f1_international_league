<template>
  <div class="il-regulations">
    <div class="il-regulations-contents">
      <h2 class="il-regulations-contents__title">Содержание</h2>
      <ol class="il-regulations-contents__list">
        <li v-for="(c, index) in $options.CONTENTS" :key="index">
          <a href="#" class="il-regulations-contents__link">{{ c.title }}</a>
        </li>
      </ol>
    </div>
    <section id="basic-provisions" class="il-regulations-content">
      <ol>
        <li>
          <h4 class="il-regulations-content__title">Основные положения</h4>
          <ol>
            <li>
              «International League (PC)»– онлайн чемпионат по кольцевым
              автогонкам на формульных болидах класса «Formula 1» в игре F1 2021
              by Codemasters.
            </li>
            <li>
              Настоящим Регламентом Чемпионата (РЧ) регулируются правила
              участия, порядок организации и проведения чемпионата
              «International League (PC)» (1 и 2 лиг соответственно).
            </li>
          </ol>
        </li>
      </ol>
    </section>
  </div>
</template>

<script>
import { CONTENTS } from "@/const";

export default {
  name: "RegulationsContent",
  CONTENTS,
};
</script>

<style scoped>
.il-regulations {
  background-color: #242c41;
  margin-bottom: 40px;
}
.il-regulations-contents {
  padding-bottom: 50px;
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
.il-regulations-content {
  width: 100%;
  max-width: 1000px;
  margin: 0 auto;
  text-align: left;
}
.il-regulations-content__title {
  text-align: center;
}
.il-regulations-content li {
  position: relative;
  list-style-type: none;
}
.il-regulations-content ol {
  counter-reset: list1;
}
.il-regulations-content ol li:before {
  position: absolute;
  left: 360px;
  padding: 0 5px;
  text-align: center;
  counter-increment: list1;
  content: counter(list1) ".";
}
.il-regulations-content ol ol {
  counter-reset: list2;
}
.il-regulations-content ol ol li:before {
  position: absolute;
  left: -46px;
  counter-increment: list2;
  content: counter(list1) "." counter(list2) ". ";
}
</style>
