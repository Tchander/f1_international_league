import { CLASS_MAPPER } from "@/const";
export const getClassByPosition = (index) => {
  return CLASS_MAPPER[index + 1];
};
