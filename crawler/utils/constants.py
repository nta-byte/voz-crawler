import os

StockCodes = ["MSN",
              "HAI",
              "NVL",
              "VIC",
              "VJC",
              "BCM",
              "VKC",
              "HNG",
              "ROS",
              "GEE",
              "FPT",
              "ACB",
              "MHC",
              "SD2",
              "API",
              "VCG",
              "GEX",
              "SD6",
              "MBB",
              "SAB",
              "SJF",
              "Bll",
              "SD5",
              "VGC",
              "IDJ",
              "MML",
              "AAA",
              "APS",
              "SBT",
              "SD3",
              "VCB",
              "DAT",
              "DNP",
              "VHM",
              "ITA",
              "AMD",
              "HDB",
              "VGI",
              "VRE",
              "BVH",
              "EIB",
              "GAS",
              "MSB",
              "GVR",
              "TPB",
              "PNJ",
              "HCD",
              "ART",
              "POW",
              "APG",
              "REE",
              "NHH",
              "CSC",
              "VC9",
              "STB",
              "AGM",
              "VEA",
              "IDC",
              "TCH",
              "SHB",
              "MCH",
              "THD",
              "SD7",
              "KBC",
              "KLF",
              "BSR",
              "SSI",
              "HPG",
              "JVC",
              "TCD",
              "HVN",
              "SDA",
              "BID",
              "IDI",
              "HAG",
              "ASM",
              "VIB",
              "VIX",
              "BHN",
              "KDH",
              "CTG",
              "BCG",
              "VPB",
              "VNM",
              "DXS",
              "ACV",
              "APH",
              "PDR",
              "FLC",
              "TGG",
              "CTR",
              "FOX",
              "HUT",
              "DXG",
              "HHS",
              "PLX",
              "DPG",
              "SMT",
              "TCB",
              "SD9",
              "MWG",
              "MSR",
              "PGV",
              "SD4"]

TableVOZStockComment = 'voz_stock_mapping'
TableVOZRawComment = 'voz_rawcomment'
TableVOZLink = 'voz_link'
PG_USER = os.environ['PG_USER']
PG_PASSWORD = os.environ['PG_PASSWORD']
PG_PORT = os.environ['PG_PORT']
PG_HOST = os.environ['PG_HOST']
DB_CONNECTION = f'postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/postgress'

MAX_STOCKMAPPING_INSERT = 1000
