#Pandas + Bloomberg API Packages:
import pandas as pd
import pdblp as bl

#Activating connection to Bloomberg:
con = bl.BCon(debug = False, port=8194, timeout = 5000)
con.start()

#Read in stock names from Nasdaq Composite Index:
names = pd.read_csv('symbols.csv')
names = names.value.values

#Read in Environmental Fields:
e = pd.read_csv('environmental_fields.csv')
e = e.env.values

#Read in Social Fields:
s = pd.read_csv('social_fields.csv')
s = s.soc.values

#Read in Governance Fields:
g = pd.read_csv('governance_fields.csv')
g = g.gov.values

#Gather data with fields:
env_data = con.ref(names, e)
soc_data = con.ref(names, s)
gov_data = con.ref(names, g)

#Place gathered data into new csv files:
env_data.to_csv('env_data.csv')
soc_data.to_csv('soc_data.csv')
gov_data.to_csv('gov_data.csv')
