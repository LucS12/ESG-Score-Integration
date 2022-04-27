"""
Create ESG scores: No Sector Relativity
    - Scores relative to all stocks
"""
#Pakcages needed:
import pandas as pd
import numpy as np

### Environmental (E) Score ###
#Read in files:
env = pd.read_csv('env.csv', index_col='ticker')

#Revenue Based Fields (Emissions per Sales & Eligible Revenue):
rev_f = ['GICS_SECTOR_NAME',
         "TOTAL_GHG_CO2_ESTIMATE_PER_SALES",
         "TOTAL_GHG_ESTIMATE",
         "GHG_SCOPE_1_ESTIMATE",
         "GHG_SCOPE_2_ESTIMATE"]

#Policy fields:
pol_f = ['GICS_SECTOR_NAME',
         "BIODIVERSITY_POLICY",
         "GREEN_BUILDING",
         "EMISSION_REDUCTION",
         "ENERGY_EFFIC_POLICY",
         "INDEPENDENT_ASSESSMENT_CONDUCTED",
         "RENEWABLE_ELECTRICITY_TARGET_POL",
         "SUS_SUP_GDL_ENC_ESG_AREA_PUB_DIS",
         "CLIMATE_CHG_POLICY",
         "ENVIRON_QUAL_MGT",
         "ENVIRON_SUPPLY_MGT",
         "WATER_POLICY"]

#Regulation fields (Paris Climate Convention Targets/Testing):    
reg_f = ['GICS_SECTOR_NAME',
         "EU_TAX_EST_DNSH_ADP_LVL_1",
         "EU_TAX_EST_DNSH_BIODIV_LVL_1",
         "EU_TAX_EST_DNSH_MIT_LVL_1",
         "EU_TAX_EST_DNSH_POLLUTION_LVL_1",
         "EU_TAX_EST_ELIGIBLE_REV_PCT",
         "EU_TAX_EST_DNSH_WASTE_LVL_1"]
    
#Revenue data:
rev = pd.read_csv('revenue_adj.csv', index_col='ticker')

#Adjust fields needed the fill of NaNs:
env = env_o.loc[:, (rev_f + reg_f[1:])]

#Fill in NaNs with sector mean:
#List of sectors:
sectors = list(env.groupby('GICS_SECTOR_NAME').GICS_SECTOR_NAME.count().index)

#Loop to fill NaNs with sector mean + empty list to store each df:
dfs = []
for sec in sectors:
    
    #Mean of sector
    mean = env[env.GICS_SECTOR_NAME == sec].iloc[:,1:].mean()
    
    #Filtered df for current sector:
    filt = env[env.GICS_SECTOR_NAME == sec].iloc[:, 1:]   
    
    #Fill in with mean + append to list of dfs:
    filled_df = filt.fillna(mean)
    dfs.append(filled_df)

#Put all filled dfs into one again + add back the sector columns:    
e_1 = pd.concat(dfs)
e_1 = e_1.sort_index()
e_1 = e_1.merge(env.GICS_SECTOR_NAME, right_on='ticker', left_on='ticker')

#Make each field per sales (divide by sales):
e_1.iloc[:, 1:4] = e_1.iloc[:, 1:4].div(rev.values, axis=0)

## E Score Part 1: GHG ##
e_ghg = e_1.iloc[:, :4]
e_ghg = np.abs(e_ghg)

#Invert Scores as More is Worse:
ghg_inv = e_ghg.max() - e_ghg

#Calculate percentage of max:
ghg_max = ghg_inv / ghg_inv.max()

#Take average of all fields:
num_fields = len(ghg_max.columns)
ghg_max['ghg_score'] = ghg_max.sum(axis=1) / num_fields

## E Score Part 2: Policies ##
e_pol = env_o.loc[:, pol_f]

#Fill NaNs and Ns with 0 and Ys with 1:
e_pol.replace(['N', None], 0, inplace=True)  #NaNs and Ns to 0
e_pol.replace('Y', 1, inplace=True)          #Ys to 1

#Average of each firm:
num_fields = len(e_pol.columns[1:])
e_pol['avg_score'] = e_pol.iloc[:, 1:].sum(axis=1) / num_fields 

## E Score Part 3: Paris Testing/Regulation ###
e_test = env.loc[:, reg_f[1:]]

#Already in percentage, take average of all fields:
num_fields = len(e_test.columns)
e_test['reg_score'] = e_test.sum(axis=1) / num_fields 

#Calculate total E score with weights:
    #emissions weight: 0.35
    #Policy weight: 0.15
    #regulations weight: 0.5
ghg_weight = 0.35
pol_weight = 0.15
reg_weight = 0.5
E_raw = (ghg_max.ghg_score*ghg_weight)+(e_pol.avg_score*pol_weight)+(e_test.reg_score*reg_weight)

E_score = E_raw.rank(pct=True)  #Final E Score

### SOCIAL (S) SCORE ###
#Read in Social data:
soc = pd.read_csv('soc.csv', index_col='ticker')

#Social fields:
s_fields = ["GICS_SECTOR_NAME",
            "ANTI-BRIBERY_ETHICS_POLICY",
            "EMPLOYEE_CSR_TRAINING",
            "EMP_PROT_WHISTLE_BLOWER_POLICY",
            "ETHICS_POLICY",
            "HEALTH_SAFETY_POLICY",
            "HUMAN_RIGHTS_POLICY",
            "MODERN_SLAVERY_STATEMENT",
            "POLICY_AGAINST_CHILD_LABOR",
            "PCT_EMPLOYEES_UNIONIZED"]

#Fill NaNs and Ns with 0 and Ys with 1:
s.iloc[:, 1:9] = s.iloc[:, 1:9].replace('Y', 1)
s.iloc[:, 1:9] = s.iloc[:, 1:9].replace(['N', None], 0)

#Fill in percentage field with sector means:
dfs = []
for sec in sectors:
    
    #Mean of sector
    mean = s[s.GICS_SECTOR_NAME == sec].iloc[:, -1].mean()
    
    #Filtered df for current sector:
    filt = s[s.GICS_SECTOR_NAME == sec].iloc[:, -1]   
    
    #Fill in with mean + append to list of dfs:
    filled_df = filt.fillna(mean)
    dfs.append(filled_df)

#Concatenate dfs into one again and add back sector column:
s_f = pd.concat(dfs)
s_f = s_f.sort_index()
s_f = pd.DataFrame(s_f)
s_f = s_f.merge(s.iloc[:,:-1], right_on='ticker', left_on='ticker')
s_f = s_f[s_fields]

#Policy score component (average of sum):
num_fields = len(s_f.columns[1:9])
s_f['pol_score'] = s_f.iloc[:,1:9].sum(axis=1) / num_fields

#Standardize PCT Employees to be decimal form:
s_f['PCT_EMPLOYEES_UNIONIZED'] = s_f['PCT_EMPLOYEES_UNIONIZED'] / 100

#S Raw Score:
    #Policies: 80%
    #PCT Employees: 20%
pol_wgt = 0.8
pct_wgt = 0.2
S_raw = (s_f.PCT_EMPLOYEES_UNIONIZED*pct_wgt) + (pol_wgt*s_f.pol_score)

#Rank raw scores:
S_score = S_raw.rank(pct=True)

### Governance (G) SCORE ###
#Read in Governance data:
gov = pd.read_csv('gov.csv', index_col='ticker')

#Meeting commitments fields:
g_meet = ["GICS_SECTOR_NAME",
          "AUDIT_COMMITTEE_MEETINGS",
          "BOARD_MEETINGS_PER_YR",
          "NOMINATION_CMTE_MTG_ATTEND_%",
          "NUM_OF_MEMBERS_OF_CMPNSTN_CMTE",
          "SIZE_OF_AUDIT_COMMITTEE"]

#Diversity fields:
g_diverse = ["GICS_SECTOR_NAME",
             "BOARD_OF_DIRECTORS_AGE_RANGE",
             "PERCENTAGE_OF_FEMALE_EXECUTIVES",
             "PCT_WOMEN_ON_BOARD",
             "NUM_EXECUTIVE_CHANGES",
             "YEARS_AUDITOR_EMPLOYED"]

#Interest/bias/fairness/integrity fields:
g_bias = ["GICS_SECTOR_NAME",
          "PCT_EXECUTIVES_HOLDING_SHARES",
          "NUM_OF_NON_EXECUTIVE_DIR_ON_BRD",
          "PCT_INDEPENDENT_DIRECTORS",
          "PCT_NON_EXEC_DIR_ON_AUD_CMTE",
          "PCT_NON_EXEC_DIR_ON_CMPNSTN_CMTE",
          "PCT_NON_EXEC_DIR_ON_NOM_CMTE",
          "PCT_OF_NON_EXEC_DIR_ON_BRD"]

#Filter data for all fields above:
g_f = gov.loc[:, (g_meet+g_diverse[1:]+g_bias[1:])]

#Fill NaNs with sector means:
dfs = []
for sec in sectors:
    
    #Mean of sector
    mean = g_f[g_f.GICS_SECTOR_NAME == sec].iloc[:,1:].mean()
    
    #Filtered df for current sector:
    filt = g_f[g_f.GICS_SECTOR_NAME == sec].iloc[:, 1:]   
    
    #Fill in with mean + append to list of dfs:
    filled_df = filt.fillna(mean)
    dfs.append(filled_df)

#Concatenate dfs into one again and add back sector column:
g_all = pd.concat(dfs)
g_all = g_all.sort_index()

##1. G Meetings Component ##
#Filter to meeting commitment fields:
g_m = g_all.loc[:, g_meet[1:]]

#Make pct field as pct:
g_m['NOMINATION_CMTE_MTG_ATTEND_%'] = g_m['NOMINATION_CMTE_MTG_ATTEND_%']/ 100

#Divide data by max:
g_m.iloc[:, [0,1,3,4]] = g_m.iloc[:, [0,1,3,4]] / g_m.iloc[:, [0,1,3,4]].max()

#Take average of fields:
num = len(g_m.columns)
g_m['meet_score'] = g_m.sum(axis=1) / num  

##2. G Diversity ##
g_div = g_all.loc[:, g_diverse[1:]]

#Invert Exec Changes field:
g_div["NUM_EXECUTIVE_CHANGES"] = g_div["NUM_EXECUTIVE_CHANGES"].max() - g_div["NUM_EXECUTIVE_CHANGES"]

#Divide it by max:
g_div = g_div / g_div.max()

#Take average of all fields:
num_fields = len(g_div.columns)
g_div['div_score'] = g_div.sum(axis=1) / num_fields 

##3. G Bias/Integrity/Interest ##
g_b = g_all.loc[:, g_bias[1:]]

#Make num of non execs on board as pct:
g_b['NUM_OF_NON_EXECUTIVE_DIR_ON_BRD'] = g_b['NUM_OF_NON_EXECUTIVE_DIR_ON_BRD'] / g_b['NUM_OF_NON_EXECUTIVE_DIR_ON_BRD'].max()

#Make pct fields as pct:
g_b.iloc[:, [0, 2,3,4,5,6]] = g_b.iloc[:, [0, 2,3,4,5,6]] / 100

#Take average of all fields:
num_fields = len(g_b.columns)
g_b['bias_score'] = g_b.sum(axis=1) / num_fields

# G raw score:
    #meetings: 30%
    #diversity: 20%
    #bias/integrity/interest: 50%
m_wgt = 0.3
d_wgt = 0.2
b_wgt = 0.5

G_raw = (g_m.meet_score*m_wgt) + (g_div.div_score*d_wgt) + (g_b.bias_score*b_wgt)

#G Final Score:
G_score = G_raw.rank(pct=True)

### TOTAL ESG SCORE ###
esg = (E_score + S_score + G_score) / 3

#Put all scores in CSV file:
esg_df = pd.DataFrame()        #Empty DF

esg_df['E_score'] = E_score    #Environmental
esg_df['S_score'] = S_score    #Social 
esg_df['G_score'] = G_score    #Governance
esg_df['ESG_score'] = esg      #ESG Total
 
esg_df = esg_df*100            #Format style to %
esg_df = esg_df.round(2)       #making it 2 decimals