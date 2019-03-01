## ETL Project Team Members
Mark Yocum<br />
Hubert Cheng

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

The EIA provides monthly and annual state-level petroleum consumption data through their API.  In this case we analyzed gasoline specifically. <br />
https://www.eia.gov/opendata/qb.php?category=404254



## Transform:

#### Tools: Jupyter Notebooks, Python, APIs, Splinter, ChromeDriver
    
The FHWA .csv files were downloaded through a loop in python.  Each file was extracted from the website and fed into a pandas dataframe where it could be 
formatted.  Information not pertaining to a state was dropped as well as any columns that were null.  Please see this [Jupyter Notebook](https://github.com/MarkYocumII/ETL_project/blob/master/State_vmt.ipynb).

The state names and abbreviations were found as a combination of state name and abbreviation.  This was seperated by "-" which was then made into lists for a pandas dataframe.

AAA information was web-scraped by state.  The abbreviations were collected by web-scraping the website stated above.  After a list of state names was collected, it was looped and appended to the url by state to see the gas prices for each state. Both the state names/abbreviations and the web-scrape data can be found in this [Jupyter Notebook](https://github.com/MarkYocumII/ETL_project/blob/master/Gas%20Price%20Scrape.ipynb).

EIA:  There are two separate API calls; the first one calls the series id's for each state for gasoline consumption, the second API call uses the series ID to pull the actual monthly and annual consumption data at the state level.  We reduced the data set for all months in 2016 and later, and removed annual data to retain monthly data only.  
[Jupyter Notebook](https://github.com/MarkYocumII/ETL_project/blob/master/EIA_Test_Data.ipynb)


## Load:

#### SQL

This database is utilizing a relational database.  All the information provided can be linked by state.  An empty database was created in MySQL workbench
Using SQLAlchemy, each set of data was loaded into SQL as it's own individual table.

#### Schema for the database: <br />
*gasprices (retail gasoline prices)<br />
*cons (consumption)<br />
*vmt (vehicle miles travelled)


## Hypothetical use of database:

This database can be used to identify trends and relationships at the state level between gasoline consumption, gasoline prices, and how many miles were driven.  These are the principle components of gasoline demand forecasting, and ideally the database could be expanded by adding more demographic and socioeconomic data.
