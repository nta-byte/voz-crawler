import type { NextPage } from "next";
import LayoutDefault from "../components/Layout/LayoutDetault";
import SearchBox from "../components/SeachBox";
import StockItem from "../components/StockItem";
import { StatsStockType } from "shared/dist/types";
import React from "react";
import { getStatisStock, getStocksLatest } from "../libs/client";

const Home: NextPage = () => {
  const [statsStocksDefault, setStatsStocksDefault] = React.useState<
    StatsStockType[]
  >([]);
  const [statsStocks, setStatsStocks] = React.useState<StatsStockType[]>([]);
  const [stocksLatest, setStocksLatest] = React.useState<any[]>([]);

  React.useEffect(() => {
    getStatisStock().then(async (rs: any) => {
      const dataRs = await rs.json();
      setStatsStocksDefault(dataRs);
      setStatsStocks(dataRs);
    });

    getStocksLatest().then(async (rs: any) => {
      const dataRs = await rs.json();
      setStocksLatest(dataRs);
    });
  }, []);

  const handleFilterStocks = (e: any) => {
    const filterText = String(e.target.value.trim()).toLocaleUpperCase();
    console.info("filterText", filterText);
    if (filterText) {
      setStatsStocks((current: StatsStockType[]) => {
        return statsStocksDefault.filter((item) => item.name.match(filterText));
      });
    } else {
      setStatsStocks(statsStocksDefault);
    }
  };

  return (
    <LayoutDefault>
      <div className="py-[20px]">
        <h1 className="text-3xl font-bold">
          Hackathon 2022 - BIF (Bug Is Feature)
        </h1>
      </div>

      <div>
        <h2 className="font-bold text-2xl mb-2">Top stocks in the week</h2>
        <div className="flex">
          <div className="w-3/4">
            <div className="py-[20px]">
              <SearchBox onFilter={handleFilterStocks} />
            </div>
            <div className="flex flex-col">
              {statsStocks.map((item, idx) => (
                <StockItem key={"stock-" + item.name} data={item} />
              ))}
            </div>
          </div>

          <div className="w-1/4 px-6 flex flex-col items-center ">
            <div className="text-base font-bold mb-6">TOP</div>
            <div className="">
              {stocksLatest &&
                stocksLatest.map((item: any, idx: number) => (
                  <div
                    key={item.id + "post"}
                    className={`p-2 mb-1 rounded-md flex flex-col items-center w-full animate-fade-in-down ${
                      idx % 2 === 0
                        ? "animate-bounce bg-slate-400"
                        : "bg-slate-50"
                    }`}
                  >
                    <div className="text-sm font-bold">
                      {item.comment.author}
                    </div>
                    <div className="text-xs text-center">
                      {item.comment.content.slice(0, 50)} ...
                    </div>
                  </div>
                ))}
            </div>
          </div>
        </div>
      </div>
    </LayoutDefault>
  );
};

export default Home;
