import { StatsStockType, StockSuggestType } from "../constants";

function randomInteger(min: number, max: number) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

function makeid(length: number) {
  var result = "";
  var characters =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
  var charactersLength = characters.length;
  for (var i = 0; i < length; i++) {
    result += characters.charAt(Math.floor(Math.random() * charactersLength));
  }
  return result;
}

export const generateStatsStock = (): StatsStockType[] => {
  let arr = [];
  const suggestList: StockSuggestType[] = ["buy", "sell", "hold"];
  for (let i = 0; i < 10; i++) {
    arr.push({
      name: makeid(4).toLocaleUpperCase(),
      dateUpdated: new Date().toISOString(),
      numbuy: randomInteger(1, 20),
      numhold: randomInteger(1, 20),
      numsell: randomInteger(1, 20),
      suggest: suggestList[randomInteger(0, 2)],
      hotTrend: i < 3,
    });
  }

  return arr;
};
