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

#Get historical data:
prices = con.bdh(symbols, p, start, end,
                 elms=[('periodicitySelection', 'MONTHLY')])
