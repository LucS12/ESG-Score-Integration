#Necessary Packages:
import pandas as pd
import pdblp as bl

#Connection to Bloomberg Terminal:
con = bl.BCon(debug=False, port = 8194, timeout=5000)
con.start()

#Price field + start/end dates:
p = 'PX_LAST'
start = '20170101'
end='20220428'

#Get stock symbols:
sym_data = pd.read_csv('esg_scores.csv', index_col='ticker')
symbols = list(sym_data.index)
spx = 'SPX Index'

#Get historical data:
prices = con.bdh(symbols, p, start, end)
spx_prices = con.bdh(spx, p, start, end)

#Place price data into CSV files:
prices.to_csv('daily_prices.csv')
spx_prices.to_csv('daily_spx.csv')
