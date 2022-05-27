# ESG-Score-Integration

Project integrating ethically responsible criteria in investment portfolios through the use of proprietary ESG scores. The repo includes the following:
- GUI application built to take in user preferences regarding ESG criteria to generate an equity investment portfolio.
- Code and written reports of the data gathering and ESG score building processes.


## How It Works:
- The video below exhibits the platform that the code displays and how it can be used to generate an equity investment portfolio:

     https://user-images.githubusercontent.com/93154131/170358026-742f5b67-7024-4a7d-bede-82d220d406ae.mp4





## Files & Data Folders:
- **esg_investing_application.py:** Python code used to build the GUI application and the asset allocation algorithm/methodology. Necessary data input:
  - *daily_prices.csv:* CSV file containing daily price data of stocks used.
  - *daily_spx.csv:*  CSV file containing daily price data of SPX Index for beta calculations.
  - *env.csv:* CSV file containing sector/grouping information for each stock.
  - *esg_scores.csv:* CSV file containing ESG scores created for each stock.
  - *fama_french_data.csv:* CSV file containing data needed for the Fama-French 3-Factor model utilized.
  - *mktcap.csv:* CSV file containing the market capitalization of each stock.


- **data/esg_scores:** CSV files, Jupyter Notebook report, and Python code used to generate ESG scores for Nasdaq Composite Index members. 
- **data/nasdaq-comp:** CSV and Python files used to gather ESG data from the Bloomberg Terminal.
- **data/price-data:** CSV and Python files used to gather stock and index price data from the Bloomberg Terminal.
