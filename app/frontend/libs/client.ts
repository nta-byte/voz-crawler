import { API } from "./constants";
import { API_PATHS } from "shared/dist/constants";

export const getStatisStock = () => {
  return fetch(API + API_PATHS.statisStock);
};
