import { API_PATHS } from "shared/dist/constants";
import { StatsStockType, StockSuggestType } from "shared/dist/types";
import { StockMapping } from "@models/stock_mapping.model";
import _ from "lodash";
import { QueryBuilder } from "objection";
import { RawComment } from "@models/raw_comment.model";

export const Service = {
  getStatisStock: async (req: any, res: any, next: any) => {
    const dayAfterAWeek = new Date(+new Date() - 7 * 24 * 60 * 60 * 1000);
    const query = StockMapping.query().where("time", ">=", dayAfterAWeek);

    const data: any = await query
      .clone()
      .orderBy("time", "desc")
      .withGraphFetched("comment(sortByTime)")
      .modifiers({
        sortByTime: (bulder: QueryBuilder<RawComment>) => {
          bulder.orderBy("time", "desc");
        },
      });

    const statis = _.groupBy(data, "stock");
    const result: StatsStockType[] = Object.values(statis).map(
      (array: any, index: number) => {
        const total = array.length;
        const numbuy = 0;
        const numsell = 0;
        const numhold = 0;
        const suggest = "buy";

        return {
          name: array[0].stock,
          total,
          comments: _.map(array, "comment.content"),
          dateUpdated: _.get(array, "0.time"),
          hotTrend: index < 3,
          numbuy,
          numsell,
          numhold,
          suggest,
        } as StatsStockType;
      }
    );
    res.json(result);
  },
  getNewStocks: async (req: any, res: any, next: any) => {
    const dayAfterAWeek = new Date(+new Date() - 7 * 24 * 60 * 60 * 1000);
    const query = StockMapping.query().where("time", ">=", dayAfterAWeek);

    const data: any = await query
      .clone()
      .orderBy("time", "desc")
      .limit(30)
      .withGraphFetched("comment(sortByTime)")
      .modifiers({
        sortByTime: (bulder: QueryBuilder<RawComment>) => {
          bulder.orderBy("time", "desc");
        },
      });

    res.json(data);
  },
};
