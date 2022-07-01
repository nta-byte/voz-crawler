export type StockSuggestType = "buy" | "sell" | "hold";

export type StatsStockType = {
  name: string;
  dateUpdated: string;
  numbuy: number;
  numsell: number;
  numhold: number;
  suggest: StockSuggestType;
  hotTrend?: boolean;
};
