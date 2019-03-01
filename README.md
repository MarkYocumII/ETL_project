## ETL_project - Gas Prices, Gas Consumption, Traffic Volume
Mark Yocum and Hubert Cheng ETL Project

## Statement for use of database:

This database can be used to...


## Extract:

#### State abbreviations

Collected the 2-letter abbreviations for states<br />
https://abbreviations.yourdictionary.com/articles/state-abbrev.html

#### Federal Highway Administration Traffic Volume Data (.CSV files)
Traffice volume trends were collected from the FHWA.  Data was collected on a monthly report.  Data was collected at approximately 4,000 continuous traffic
counting locations nationwide.<br />
https://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm

#### AAA Gas Prices (Web Scrape)
AAA provides average gas prices for Regular, Mid-Grade, Premium, and Diesel.  Average price data can be collected by current, yesterday, week ago, month ago, and year ago dates.<br />
https://gasprices.aaa.com/

#### U.S. Energy Information Administration (API)


## Transform:

#### Tools: Jupyter Notebooks, Python, APIs, Splinter, ChromeDriver
    
The FHWA .csv files were downloaded through a loop in python.  Each file was extracted from the website and fed into a pandas dataframe where it could be 
formatted.  Information not pertaining to a state was dropped as well as any columns that were null.  Please see this [Jupyter Notebook](https://github.com/MarkYocumII/ETL_project/blob/master/State_vmt.ipynb)

The state names and abbreviations were found as a combination of state name and abbreviation.  This was seperated by "-" which was then made into lists for a pandas dataframe.

AAA information was web-scraped by state.  The abbreviations were collected by web-scraping the website stated above.  After a list of state names was collected, it was looped and appended to the url by state to see the gas prices for each state. Both the state names/abbreviations and the web-scrape data can be found in this [Jupyter Notebook](https://github.com/MarkYocumII/ETL_project/blob/master/Gas%20Price%20Scrape.ipynb).

EIA 

## Load:

#### SQL

This database is utilizing a relational database.  All the information provided can be linked by state.  An empty database was created in MySQL workbench
Using SQLAlchemy, each set of data was loaded into SQL as it's own individual table.

