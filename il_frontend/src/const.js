export const API_MEDIA_URL = "http://localhost:8000";
export const ROUTES = {
  home: "/",
  calendar: "/calendar",
  tournament_table: "/table",
  teams: "/teams",
  team: "/team/:teamName",
  race: "/race/:country",
  regulations: "/regulations",
};
export const CONTENTS = [
  {
    title: "Основные положения",
  },
  {
    title: "Регистрация и участие в соревнованиях",
  },
  {
    title: "Общие правила поведения",
  },
  {
    title: "Правила поведения во время квалификации и гонки",
  },
  {
    title: "Классификация",
  },
  {
    title: "Начисление очков",
  },
  {
    title: "СК и порядок подачи претензии",
  },
  {
    title: "Нарушения и наказания за них",
  },
];

export const BASE_URL = "http://localhost:8000/api/v1/";
export const BASE_TEAMS_URL = BASE_URL + "teams/";
export const BASE_PILOTS_URL = BASE_URL + "pilots/";
export const BASE_RACES_URL = BASE_URL + "races/";
export const LEAGUES = {
  FIRST: 1,
  SECOND: 2,
};
