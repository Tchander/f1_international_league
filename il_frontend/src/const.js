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
    href: "basic-provisions",
    title: "Основные положения",
  },
  {
    href: "registration",
    title: "Регистрация и участие в соревнованиях",
  },
  {
    href: "general-rules",
    title: "Общие правила поведения",
  },
  {
    href: "rules-in-race",
    title: "Правила поведения во время квалификации и гонки",
  },
  {
    href: "classification",
    title: "Классификация",
  },
  {
    href: "score",
    title: "Начисление очков",
  },
  {
    href: "sc-and-claim",
    title: "СК и порядок подачи претензии",
  },
  {
    href: "punishments",
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
