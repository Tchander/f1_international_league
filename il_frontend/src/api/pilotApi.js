import axios from "axios";
import { BASE_PILOTS_URL } from "@/const";

export const getAllPilots = async () => await axios.get(BASE_PILOTS_URL);
