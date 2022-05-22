#Necessary packages:
import tkinter as tk               
from tkinter import ttk             
import pandas as pd
import numpy as np

#Root window of GUI
root = tk.Tk()
root.geometry('700x900')
root.resizable(False, False)
root.title('ESG Investing')
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=4)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)

#%% SLIDER 1 - Enviromental ESG Score Input:
#slider current value:
current_value1 = tk.DoubleVar()


def get_current_value1():
    return '{: .2f}'.format(current_value1.get())


def slider1_changed(event):
    value1_label.configure(text=get_current_value1())
    
ttk.Label(root, text="\n ESG Asset Allocation Application", font="italic").grid(row=0,columnspan=2)
ttk.Label(root, text="Luc C. Smith & Samuel M. Reisgys").grid(row=1, columnspan= 2)
ttk.Label(root, text="_____________________________________________________________________________________________________________________________________________\n").grid(row=2,columnspan=2, ipady=5, ipadx=5)
# label for the slider1
slider1_label = ttk.Label(
    root,
    text=' (1) - How much do you care about Environmental (E) issues? \n         Ex: gas emissions, anti-pollution actions, regulatory tests, etc. \n         (100 being the most care)'
)

slider1_label.grid(
    column=0,
    row=3,
    sticky='w'
)

#  slider1
slider1 = ttk.Scale(
    root,
    from_=0,
    to=100,
    orient='horizontal',  # vertical
    command=slider1_changed,
    variable=current_value1
)

slider1.grid(
    column=1,
    row=3,
    sticky='we',
    ipady = 5
)

# current value1 label
current_value1_label = ttk.Label(
    root,
    text='Chosen Score:'
)

current_value1_label.grid(
    row=4,
    columnspan=2,
    sticky='n',
    ipadx=0,
    ipady=5
)

# value1 label
value1_label = ttk.Label(
    root,
    text=get_current_value1()
)
value1_label.grid(
    row=5,
    columnspan=2,
    sticky='n'
)

ttk.Label(root, text="_____________________________________________________________________________________________________________________________________________\n").grid(row=7,columnspan=2)

#%% SLIDER 2 - Social

# slider2 current value2
current_value2 = tk.DoubleVar()


def get_current_value2():
    return '{: .2f}'.format(current_value2.get())


def slider2_changed(event):
    value2_label.configure(text=get_current_value2())


# label for the slider2
slider2_label = ttk.Label(
    root,
    text=' (2) - How much do you care about Social (S) issues? \n         Ex: child labor, ethical policies, employee unionization, etc. \n         (100 being the most care)'
)

slider2_label.grid(
    column=0,
    row=15,
    sticky='w'
)

#  slider2
slider2 = ttk.Scale(
    root,
    from_=0,
    to=100,
    orient='horizontal',  # vertical
    command=slider2_changed,
    variable=current_value2
)

slider2.grid(
    column=1,
    row=15,
    sticky='we',
    ipady = 5
)

# current value2 label
current_value2_label = ttk.Label(
    root,
    text='Chosen Score:'
)

current_value2_label.grid(
    row=17,
    columnspan=2,
    sticky='n',
    ipadx=0,
    ipady=5
)

# value2 label
value2_label = ttk.Label(
    root,
    text=get_current_value2()
)
value2_label.grid(
    row=19,
    columnspan=2,
    sticky='n'
)
ttk.Label(root, text="_____________________________________________________________________________________________________________________________________________\n").grid(row=20,columnspan=2)

#%% SLIDER 3 - Governance

# slider3 current value3
current_value3 = tk.DoubleVar()


def get_current_value3():
    return '{: .2f}'.format(current_value3.get())


def slider3_changed(event):
    value3_label.configure(text=get_current_value3())


# label for the slider3
slider3_label = ttk.Label(
    root,
    text=' (3) - How much do you care about how a firm Governs (G) itself? \n         Ex: fairness, corruption, compensation of employees, bias, etc.\n         (100 being the most care)'
)

slider3_label.grid(
    column=0,
    row=30,
    sticky='w'
)

#  slider3
slider3 = ttk.Scale(
    root,
    from_=0,
    to=100,
    orient='horizontal',  # vertical
    command=slider3_changed,
    variable=current_value3
)

slider3.grid(
    column=1,
    row=30,
    sticky='we',
    ipady = 5
)

# current value3 label
current_value3_label = ttk.Label(
    root,
    text='Chosen Score:'
)

current_value3_label.grid(
    row=32,
    columnspan=2,
    sticky='n',
    ipadx=0,
    ipady=5
)

# value3 label
value3_label = ttk.Label(
    root,
    text=get_current_value3()
)
value3_label.grid(
    row=34,
    columnspan=2,
    sticky='n'
)

ttk.Label(root, text="_____________________________________________________________________________________________________________________________________________\n").grid(row=35,columnspan=2)

#%% Risk Aversion
current_value4 = tk.DoubleVar()


def get_current_value4():
    return '{: .2f}'.format(current_value4.get())


def slider4_changed(event):
    value4_label.configure(text=get_current_value4())


# label for the slider4
slider4_label = ttk.Label(
    root,
    text=' (4) - How much do you try to avoid risk (A)? \n         (5 avoiding most risk)  \n         (0 taking most risk)'
)

slider4_label.grid(
    column=0,
    row=36,
    sticky='w'
)

#  slider4
slider4 = ttk.Scale(
    root,
    from_=0,
    to=5,
    orient='horizontal',  # vertical
    command=slider4_changed,
    variable=current_value4
)

slider4.grid(
    column=1,
    row=36,
    sticky='we',
    ipady = 5
)

# current value4 label
current_value4_label = ttk.Label(
    root,
    text='Chosen Score:'
)

current_value4_label.grid(
    row=37,
    columnspan=2,
    sticky='n',
    ipadx=0,
    ipady=5
)

# value4 label
value4_label = ttk.Label(
    root,
    text=get_current_value4()
)
value4_label.grid(
    row=38,
    columnspan=2,
    sticky='n'
)

ttk.Label(root, text="_____________________________________________________________________________________________________________________________________________\n").grid(row=39,columnspan=2)

#%% Stock Picking
e = tk.StringVar(root)
def get_current_value5():
    global e
    value1 = e.get()
    return value1

def call_sectors():
    window = tk.Tk()
    window.geometry('250x150')
    window.title('Sector names')
    ttk.Label(window, text='   Communication Services \n   Consumer \n   Financials \n   Health Care \n   Information Technology \n   Utilities',
              ).grid(row=1, column=1)
    window.mainloop()
    
    
tk.Button(root, text="See sector names",command=call_sectors).grid(row=44,columnspan=2,ipadx=18, pady=4)


ttk.Label(root,text="Type in any sector you'd like to neglect (Separate it by commas and exact name as shown):").grid(row=40, columnspan=2)
e_entry = tk.Entry(root, width=50, textvariable = e).grid(row=41,columnspan=2, pady=2)


e2 = tk.StringVar(root)

def get_current_value6():
    global e2
    value2 = e2.get()
    return value2

ttk.Label(root, text="Stocks that should be excluded from the portfolio (Enter ticker and separate by comma, ex: TSLA, AAPL):").grid(row=45, columnspan=2)
e2_entry = tk.Entry(root, width=50, textvariable = e2).grid(row=46, columnspan=2, pady=2)





#%% Buttons

def Confirm():
    
    #Globalize variables needed:
    global esg_list
    global stock_list
    global sec_list
    global get_current_value1
    global get_current_value2
    global get_current_value3
    global get_current_value4
    global get_current_value5
    global get_current_value6
    
    #Empty lists to store inputs:
    esg_list = []
    sec_list = []
    stock_list = []
    
    #Add inputs when confirmed by user:
    esg_list.append(get_current_value1())
    esg_list.append(get_current_value2())
    esg_list.append(get_current_value3())
    esg_list.append(get_current_value4())
    sec_list.append(get_current_value5())
    stock_list.append(get_current_value6())
    
    #Exhibit confirmed values to be used:
    texter = "Selected Values:\n E:"+str(esg_list[0])+" S:"+str(esg_list[1])+" G:"+str(esg_list[2])+" R:"+str(esg_list[3])+"  "
    myLabel = tk.Label(root, text=texter)
    myLabel.grid(row=51,columnspan = 3, sticky="e")
    text1 = "Excluded sectors: "+str(sec_list)+ "  \nExcluded stocks: "+str(stock_list)+ "  "
    otherLabel = tk.Label(root, text=text1)
    otherLabel.grid(row=52, sticky="ne", rowspan= 10, columnspan=3)
    
    return esg_list, stock_list, sec_list

    

Confirm = tk.Button(root, text="Confirm Values (1)", command= Confirm)
Confirm.grid(
    row = 51, columnspan=2, sticky ="w", pady=4, ipadx=26, padx=127
)

tk.Button(root, text="Quit", command=root.destroy, bg="#ed2f2f", fg="white").grid(row=53, column = 0, pady=4)

#Create command for "Loading..." window before chart is shown:
def shut_down():
    global window
    window = tk.Toplevel(root)
    window.title("Creating Portfolio... \nIt may take up to a minute")
    Label1 = tk.Label(window, text="Portfolio created successfully.")
    Label1.pack()
    window.geometry("450x60")
    window.grab_set()
    window.lift()

#Function that generates the chart of the investment portfolio:
def get_portfolio():
    
    #Globalize variables of the lists of inputs:
    global esg_list 
    global stock_list
    global sec_list
    
    #Run loading window
    shut_down()
    
    #Fama-French 3-Factor Model function used to predict stock returns:
    def getFamaFrench3_returns(stocks):
        
        '''
        stocks: DataFrame of stock/stocks price data.
        returns: Series of Fama-French 3-Factor Model yearly return predictions for each stock.
        '''
        #Package to perform least squares regression:
        import statsmodels.api as sm
        
        #Read in Fama-French data and select same time period as price data (2017-01-01 to 2022-04-28):
        ff_data = pd.read_csv('fama_french_data.csv', index_col='date', parse_dates=True)
        ff_data = ff_data.loc[ff_data.index > '2017']
        ff_data = ff_data.resample('M').last()
        
        #Adjust price data to same period as fama-french data availability (2022-03-31):
        stocks = stocks.loc[stocks.index < '2022-04'].resample('M').last()
        
        #Take excess returns of stocks (subtract risk-free rates):
        excess = stocks.pct_change()
        excess.fillna(method='ffill', inplace=True)                  
        excess.fillna(0, inplace=True)
        excess = excess.subtract(ff_data.RF, axis=0)
        
        #Set regression variables for the three factors + add constant:
        factors = ff_data[['Mkt-RF', 'SMB', 'HML']]
        factors = sm.add_constant(factors)
        
        #Perform regression to find Fama-French 3-factor coefficients:
        ff_betas = sm.OLS(excess, factors).fit().params
        ff_betas.set_axis(excess.columns, axis=1, inplace=True)
        ff_betas = ff_betas.transpose()
        
        #Set variables for Fama-French model equation:
        r_f = ff_data.RF.mean()                         #Risk-free rate
        mkt_prem = ff_data['Mkt-RF'].mean()             #Market premium
        SMB = ff_data.SMB.mean()                        #Size premium
        HML = ff_data.HML.mean()                        #Value premium 
        ff_betas.set_axis(['const', 'b1', 'b2', 'b3'], axis=1, inplace=True)
        
        #Estimate returns with model equation + annualize it (12 months in a year):
        e_r = (r_f + ff_betas.b1*mkt_prem + ff_betas.b2*SMB + ff_betas.b3*HML)*12
        
        return e_r

    # Black-Litterman Model: Adjust Covariance + Returns to Fama-French predictions:
    def BlackLit_opt(prices, risk_a):
        '''
        prices: DataFrame of stock price data.
        risk_a: risk-aversion given by the user input.
        Black-Litterman Meucci Model using Fama-French 3-Factor model return predictions as views.
        returns: posterior returns + covariance matrix as NumPy arrays and list of stock names.
        '''
        #Packages to adjust covariances:
        from statsmodels.stats.correlation_tools import cov_nearest 
        from sklearn.covariance import LedoitWolf    

        #Views vector (Q) as Fama-French 3-Factor model predictions:
        Q = getFamaFrench3_returns(prices)
        Q = Q[Q>-1] 
        
        prices = prices.loc[:, Q.index]   #Filter price data to prediction data
        
        #Get market cap data for initial portfolio weights:
        mcap_data = pd.read_csv('mktcap.csv', index_col='ticker')
        mcap_data.index = [stock.split()[0] for stock in mcap_data.index]
        mcap_data = mcap_data.loc[prices.columns]
        mcap_data.fillna(mcap_data.mean(), inplace=True)
        
        mcap_wgts = (mcap_data / mcap_data.sum()).CUR_MKT_CAP.values  #Np array form for calculations.
        
        #Risk-aversion (A) + covariance matrix of stock returns (S):
        A = risk_a
        cov = prices.pct_change().cov()
        
        #Use LedoitWolf to shrink covariance matrix:
        cov_shrunk = LedoitWolf().fit(cov)
        S = cov_shrunk.covariance_  
        
        #Implied equilibrium excess returns vector (pi = 2A*S*w -> Meucci):
        pi = 2.0*A*(S@mcap_wgts)
        
        #Link matrix (P) with 1s showing the position of the stock for that view (return prediction):
        P = np.zeros((len(Q), len(Q)))   #Make a matrix with length of stocks and views
        np.fill_diagonal(P, 1)           #Fill matrix's diagonal with 1 for each stock
        
        #Scalar (tau) and uncertainty of views matrix (omega):
            #tau 0 between 1 --> 1 / length of time series by Meucci
            #c default is 1 by Meucci -> constant rep overall confidence in the views return estimator
            #omega = 1/c * P * S * P^T -> Meucci
        tau = 1.0/float(len(prices))
        c = 1.0
        omega = np.dot(np.dot(P, S), P.T) / c

        #BL Excess Return: (Meucci formula)
            # = pi + tau*S*P^T * (tau*P*S*P^T + omega)^-1 * (Q - P*pi)
        r2 = np.linalg.inv(tau*P@S@P.T + omega)
        post_pi = pi + np.dot((tau*S@P.T) @ r2, (Q - P@pi))
        
        #BL Covariance Matrix: (Meucci formula)
            # = (1+tau)*S - tau^2*S*P.T * (tau*P*S*P.T + omega)^-1 * P*S
        c2 = np.linalg.inv(tau*P@S@P.T + omega) 
        post_S = (1.0+tau)*S - np.dot(np.dot(tau**2.0*np.dot(S, P.T), 
                 c2), np.dot(P, S))
        
        symS = (post_S + post_S.T) / 2  #Make it symmetric
        semidefS = cov_nearest(symS)    #Ensure strict positive semi-definite 

        return post_pi, semidefS, Q.index

    #Mean-Variance Optimization integrating user preferences and Black-Lit. adjustments: 
    def allocate(E, S, G, r_a, no_sec=None, no_stock=None):
        '''
        E: Environmental score/care input (float).
        S: Social score/care input (float).
        G: Governance score/care input (float).
        ESG: Total ESG score/care input (float).
        r_a: Risk-aversion input (float).
        no_sec: list of unwanted sectors.
        no_stock: list of unwanted stocks.
        
        Uses inputs of ESG and risk-aversion preferences along with return and
                covariance adjustments of the Black-Litterman model to conduct 
                mean-variance optimization for weights of allocation.
                
        returns: DataFrame of allocation weights and beta for each stock & 
                list of portfolio metrics.
        '''
        #Necessary packages for optimization:
        import cvxpy as cp    
        from cvxpy.atoms.affine.wraps import psd_wrap
        
        #Read in price data of stocks and ESG scores:
        esg = pd.read_csv('esg_scores.csv', index_col='ticker')                       #ESG scores
        prices = pd.read_csv('daily_prices.csv', index_col='date', parse_dates=True)  #Stock prices
        
        #Make sure same stocks and add sector/group info:
        esg = esg.loc[prices.columns]
        sec = pd.read_csv('env.csv', usecols=['GICS_SECTOR_NAME', 'ticker'],index_col=0).loc[prices.columns]
        esg = pd.merge(esg, sec, left_index=True, right_index=True)
        esg = esg.sort_index()
        
        prices = prices.sort_index(axis=1)  #Make stocks in same order as esg DF
        
        #Make stock names just the symbol:
        esg.index = [stock.split()[0] for stock in esg.index]
        esg = esg.sort_index()
        prices.columns = [stock.split()[0] for stock in prices.columns]
        prices = prices.sort_index(axis=1)
        
        #Filter out unwanted stocks and sectors:
        if no_sec != None:
            esg = esg.loc[esg.GICS_SECTOR_NAME.isin(no_sec) == False].sort_index()
            prices = prices.loc[:, esg.index]
        if no_stock != None:
            esg = esg.loc[esg.index.isin(no_stock) == False].sort_index()
            prices = prices.loc[:, esg.index]
        
        #Gather returns and covariance matrix to produce risk and return variables:
        ret, cov, stocks = BlackLit_opt(prices, r_a)
        
        cov = psd_wrap(cov)     #Ensure positive semi-definite matrix 
        esg = esg.loc[stocks]   #Filter for stocks used by Black-Lit.
        
        #Variables: weights, esg scores, volatility:
        wgts = cp.Variable(len(ret))         #Variable to be optimized (weights of allocation)
        E_scr = esg.E_score.values @ wgts    #Portfolio E score
        S_scr = esg.S_score.values @ wgts    #Portfolio S score 
        G_scr = esg.G_score.values @ wgts    #Portfolio G score
        risk = cp.quad_form(wgts, cov)       #Portfolio Volatility
        
        A = r_a   #Risk-aversion parameter
        
        #Constraints and objective function:
        cons = [cp.sum(wgts)==1, wgts<=0.10, wgts>=0, E_scr>=E, S_scr>=S, G_scr>=G]
        obj = cp.Minimize(risk - A*ret@wgts)
        
        #Optimize:
        prob = cp.Problem(obj, cons)             #Optimization of objective with constraints
        prob.solve()                             #Solves the problem created (optimal variance given)
        weights = np.array(wgts.value.round(3))  #Rounding weights to 3 decimals
        
        #Place weights and returns in DF with appropriate stock:
        wgts_df = pd.DataFrame(weights, columns=['Weight'], index=stocks)
        wgts_df['Return'] = ret
        
        #Add ESG scores to a list:
        scores = [E_scr.value, S_scr.value, G_scr.value]
        
        #Get SPX Index (benchmark) price data for betas calculation:
        spx = pd.read_csv('daily_spx.csv', index_col=0, parse_dates=True)  #Benchmark prices

        #Calculate percentage returns of stocks and SPX:
        ret_1Y = prices.iloc[-252:].pct_change()    #252 trading days in a year
        ret_1Y['SPX'] = spx[-252:].pct_change()     #benchmark
        
        #Covariance of stocks and SPX:
        cov = ret_1Y.cov().iloc[:, -1]  
        
        #Beta calculation = covariace(stock, benchmark) / variance(benchmark)
        beta_1Y = cov / ret_1Y.SPX.var()
        wgts_df['Beta'] = beta_1Y[:-1]
        
        return wgts_df, scores
    
    #Get allocation weights and portfolio metrics:
    port, s = allocate(float(esg_list[0]),float(esg_list[1]),float(esg_list[2]), 
                       float(esg_list[3]),sec_list,stock_list)
    
    #Construct Pie Chart of Portfolio:
    import seaborn as sea
    import matplotlib.pyplot as plt
   
    #Portfolio beta calculation:
    po = port.Weight
    po = po[po>0]
    p_b = port.Beta.loc[po.index]
    beta = np.round(np.dot(po, p_b), 2)  #weighted average 
    
    #Weights and return of portfolio (weighted average):
    p = port.Weight*100                                       
    p.index = [stock.split()[0] for stock in p.index]         
    r = np.round(np.dot(port.Return, port.Weight)*252*100, 2)
    
    #Graph construction (pie chart):
    sea.set_theme()
    plt.figure(figsize=(10,8))
    plt.pie(p[p>0], labels=p[p>0].index, 
            autopct='%.1f%%', explode=np.full(len(p[p>0].index), 0.05))
    
    #Making it a donut-type pie chart:
    center = plt.Circle((0,0), 0.45, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(center)
    
    #Adding title and legend of stock names onto chart:
    plt.title('Investment Portfolio:', 
              bbox={'facecolor': 'none','edgecolor': 'black','boxstyle': 'round'}, 
              fontdict={'family':'serif','color':'black','weight': 'bold','size': 20})
    plt.legend(loc='upper left', title='Stocks:', bbox_to_anchor=(1.02, 1), borderaxespad=0)
    
    #Making annotation string to exhibit portfolio metrics (Risk, Return, ESG):
    esg_string = '''ESG Ratings: \n\nE:         {} \nS:         {} \nG:         {} \nTotal:   {}'''.format(np.round(s[0],1),np.round(s[1],1),np.round(s[-1],1),np.round((s[0]+s[1]+s[-1])/3,1))
    risk_ret_string = 'Annual Return: {}% \n1-Year Beta:        {}'.format(r, beta)

    #Annotating chart with strings made above:
    plt.annotate(risk_ret_string, xy=(-1.2,0.85), xytext=(-2,0.85), fontsize=14, weight='bold',
                 bbox=dict(boxstyle="round", facecolor='lightblue',edgecolor='steelblue', alpha=0.4))
    plt.annotate(esg_string, xy=(-1.2,0.45), xytext=(-2,0.21), fontsize=14, weight='bold',
                 bbox=dict(boxstyle="round", facecolor='lightblue',edgecolor='steelblue',alpha=0.3))
    
    plt.show()   #Exhibit chart

#Create button to generate the investment portfolio pie chart:
tk.Button(root, text="Create Portfolio (2)", command=get_portfolio,bg='#40e342', fg='black', font='bold').grid(row=52,columnspan=2, sticky ="w", pady=4, ipadx=7, padx=127)

root.mainloop()
