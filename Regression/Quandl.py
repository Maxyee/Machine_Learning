import pandas as pd
import quandl

db = quandl.get("WIKI/GOOGL")

print(db.head())
