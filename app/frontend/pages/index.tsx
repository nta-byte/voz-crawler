import type { NextPage } from "next";
import LayoutDefault from "../components/Layout/LayoutDetault";
import SearchBox from "../components/SeachBox";
import StockItem from "../components/StockItem";
import { StatsStockType } from "../constants";
import { generateStatsStock } from "../libs/faker";
import React from "react";

const Home: NextPage = () => {
  const [statsStocks, setStatsStocks] = React.useState<StatsStockType[]>([]);
  const defaultDataStock = generateStatsStock();
  React.useEffect(() => {
    setStatsStocks(defaultDataStock);
  }, []);

  const handleFilterStocks = (e: any) => {
    const filterText = String(e.target.value.trim()).toLocaleUpperCase();
    console.info("filterText", filterText);
    if (filterText) {
      setStatsStocks((current: StatsStockType[]) => {
        return current.filter((item) => item.name.match(filterText));
      });
    } else {
      setStatsStocks(defaultDataStock);
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
        <div className="py-[20px]">
          <SearchBox onFilter={handleFilterStocks} />
        </div>
        <div>
          {statsStocks.map((item, idx) => (
            <StockItem key={"stock-" + item.name} data={item} />
          ))}
        </div>
      </div>
    </LayoutDefault>
  );
};

export default Home;
