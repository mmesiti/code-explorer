#!/usr/bin/env python3
from sys import argv
import sqlite3
import pandas as pd
import plotly.express as px

cloc_db_filename = argv[1]
output_fig_filename = argv[2]

connection = sqlite3.connect(cloc_db_filename)
df = pd.read_sql_query("SELECT * from t;",connection)
connection.close()
paths = df["File"].str.split('/',expand=True)
df_expanded = df.merge(paths, 
                       left_index=True,
                       right_index=True)

fig = px.treemap(df_expanded, 
                 path=list(range(0,len(paths.columns))),
                 color="Language",
                 values="nCode")

fig.show()
fig.write_html(output_fig_filename)
