import React from "react";

type Props = {
  children: React.ReactElement[];
};

const LayoutDefault: React.FC<Props> = ({ children }) => {
  return (
    <div className="bg-slate-400 min-h-screen py-[20px]">
      <div className="flex justify-center">
        <div className="w-[1024px] bg-white py-[20px] px-[20px] rounded-sm">
          {children}
        </div>
      </div>
    </div>
  );
};

export default LayoutDefault;
