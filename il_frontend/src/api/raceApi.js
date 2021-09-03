import axios from "axios";
import { BASE_RACES_URL } from "@/const";

export const getAllRace = async () => await axios.get(BASE_RACES_URL);
export const getRaceByCountry = async (country) =>
  await axios.get(BASE_RACES_URL + country + "/");
