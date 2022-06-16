import pandas as pd
comments = pd.read_json("data/comments-latest.json", encoding='utf-8')
comments.to_csv(r"data/comments.csv", index=None, encoding='utf-8')
comments.to_excel(r"data/comments.xlsx", index=None,
                  encoding='utf-8', sheet_name='VOZ')
