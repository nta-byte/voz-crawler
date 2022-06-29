import React from "react";
import Image from "next/image";
type SearchBoxProps = {
  onFilter: (e: any) => void;
};

const SearchBox: React.FC<SearchBoxProps> = ({ onFilter }) => {
  return (
    <>
      <div>
        <div className="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-gray-300">
          Search
        </div>
        <div className="relative">
          <div className="flex absolute inset-y-0 left-0 items-center pl-3 pointer-events-none">
            <Image src="/search.svg" height={15} width={15} />
          </div>
          <input
            onChange={onFilter}
            type="search"
            id="default-search"
            className="block p-4 pl-10 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            placeholder="Search stock ..."
            required
          />
        </div>
      </div>
    </>
  );
};

export default SearchBox;
