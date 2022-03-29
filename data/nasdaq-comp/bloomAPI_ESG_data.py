#Pandas + Bloomberg API Packages:
import pandas as pd
import pdblp as bl

#Activating connection to Bloomberg:
con = bl.BCon(debug = False, port=8194, timeout = 5000)
con.start()

#Read in stock names:
names = pd.read_csv('symbols.csv')
names = names.Symbol.values

#Read in Environment Fields:
env = pd.read_csv('environmental_fields.csv')
env = env.field.values

#Gather data with fields:
env_data = con.ref(list(names[:500]), list(env[:]))
