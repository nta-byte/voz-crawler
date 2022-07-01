import React from "react";
import { StatsStockType, StockSuggestType } from "shared/dist/types";

const StockItem: React.FC<{
  data: StatsStockType;
}> = ({ data }) => {
  const suggestWraperGenerete = (type: StockSuggestType) => {
    let classes = [];
    if (type === "sell") {
      classes.push("bg-red-600 text-red-200");
    }

    if (type === "buy") {
      classes.push("bg-blue-800 text-blue-200");
    }

    if (type === "hold") {
      classes.push("bg-yellow-800 text-yellow-200");
    }
    return classes.join(" ");
  };

  return (
    <div className="flex border justify-between w-full hover:bg-slate-200 hover:font-bold">
      <div className="border-r-2  p-5 basis-2/6">
        <div className="text-xs text-gray-500">
          Date updated: {data.dateUpdated}
        </div>
        <div className="font-bold text-lg">{data.name}</div>
      </div>
      <div className="border-r-2 p-5 basis-1/6">
        <div className="text-xs text-blue-800">Buy</div>
        <span className="bg-blue-100 text-blue-800 text-xs font-semibold mr-2 px-2.5 py-0.5 rounded dark:bg-blue-200 dark:text-blue-800">
          {data.numbuy}
        </span>
      </div>
      <div className="border-r-2 p-5 basis-1/6">
        <div className="text-xs text-yellow-800">Hold</div>
        <span className="bg-yellow-100 text-yellow-800 text-xs font-semibold mr-2 px-2.5 py-0.5 rounded dark:bg-yellow-200 dark:text-yellow-900">
          {data.numhold}
        </span>
      </div>
      <div className="border-r-2 p-5 basis-1/6">
        <div className="text-xs text-red-800">Sell</div>
        <span className="bg-red-100 text-red-800 text-xs font-semibold mr-2 px-2.5 py-0.5 rounded dark:bg-red-200 dark:text-red-900">
          {data.numsell}
        </span>
      </div>
      <div className="border-r-2 p-5 basis-1/6">
        <div className="text-xs text-gray-500">Suggest</div>
        <div className="font-bold text-lg flex">
          <div className="relative w-5">
            {data.hotTrend && (
              <span className="animate-ping absolute w-2 h-2 left-10 rounded-full bg-red-400 opacity-75"></span>
            )}
            <span
              className={`text-xs font-semibold px-2.5 py-0.5 rounded ${suggestWraperGenerete(
                data.suggest
              )}`}
            >
              {data.suggest.toLocaleUpperCase()}
            </span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default StockItem;
