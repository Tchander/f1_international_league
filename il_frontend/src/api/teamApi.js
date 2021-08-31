import axios from "axios";
import { BASE_TEAMS_URL } from "@/const";

export const getTeamByUrlName = async (urlName) =>
  await axios.get(BASE_TEAMS_URL + urlName + "/");

export const getAllTeams = async () => await axios.get(BASE_TEAMS_URL);
