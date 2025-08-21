import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
import investpy
from bs4 import BeautifulSoup
import requests
import re


pio.renderers.default = "iframe"

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)



def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021-06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.write_html("/storage/emulated/0/gme_stock.html")  # or any path accessible on your device
    print("Graph saved! Open the HTML file in your browser.")
    fig.show()
    from IPython.display import display, HTML
    fig_html = fig.to_html()
    display(HTML(fig_html))
    
#This is the start of my code
# yfinance is not working at all, because I am using android to write python codes. 
#I used investpy

#Question 1
df = investpy.get_stock_historical_data(
stock = "TSLA",
country = "United States",
from_date = "01/01/1900",
to_date = "20/08/2025"
)
df.reset_index(inplace=True)  
#print("the first five rows of the tesla_data dataframe using the head function")
#print("\n \n")
#print(df.head())

#Question 2
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

###
teslarevenue_df= pd.DataFrame(columns=["Date","Revenue"])

tables = soup.find_all("table")
correctTable = tables[1]

for row in correctTable.find_all("tr"):
	cols = row.find_all("td")
	if len(cols) < 2: continue
	
	cols = row.find_all("td")
	date = cols[0].text.strip()
	revenue = cols[1].text.strip()
	revenue = re.sub(r"[\$,]", "", revenue)
	teslarevenue_df = pd.concat([teslarevenue_df, pd.DataFrame({"Date":[date], "Revenue":[revenue]})] , ignore_index = True)

teslarevenue_df["Revenue"] = pd.to_numeric(teslarevenue_df["Revenue"], errors="coerce")


teslarevenue_df.dropna(inplace=True)
teslarevenue_df = teslarevenue_df[teslarevenue_df['Revenue'] != ""]

#print("the last five rows of the tesla_revenue dataframe using the tail function")
#print("\n \n \n")
#print(teslarevenue_df.tail())
	
#Question 3

gme_data= investpy.get_stock_historical_data(
stock = "GME",
country = "United States",
from_date = "01/01/1900",
to_date = "20/08/2025"
)
gme_data.reset_index(inplace=True)

#print("the first five rows of the gme_data dataframe using the head function")
#print("\n")
#print(gme_data.head())

#Question 4

#steps:
	#1. get the text contents of the url.
	#2. parse it with beautifulsoup
	#3. create a list for all tables in the webpage
	#4. create an empty data frame that contains only the headers
	#5. create a for loop to get the data of each cell in the table.
	#6. for each row. select only the rows that have 2 or more columns.
	#7. for each row, store the cell value in temp variables.
	#8. for each row, concatinate the current row to your emptu data frame.
	#9. after completion, remove all the empty rows, and all special characters.
	#10 print your output dataframe.
	
url2 = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"

response2=requests.get(url2)
html_content2=BeautifulSoup(response2.text, "html.parser")

tables2 = html_content2.find_all("table")

gme_revenue = pd.DataFrame(columns=['Date', 'Revenue'])

for rows2 in tables2[1].find_all('tr'):
	if len(rows2.find_all('td')) < 2 : continue
	col2 = rows2.find_all('td')
	date=col2[0].text
	revenue=col2[1].text.strip()
	revenue = re.sub(r"[\$,]", "", revenue)  
	# Step 2: remove $ and commas
	gme_revenue = pd.concat([gme_revenue , pd.DataFrame([[date, revenue]] , columns=['Date', 'Revenue'])] , ignore_index=True)
	
	
gme_revenue["Revenue"] = pd.to_numeric(gme_revenue["Revenue"], errors="coerce")
gme_revenue.dropna(inplace=True)  
# remove rows where Revenue couldn't be converted

#print("the last five rows of the gme_revenue dataframe using the tail function")
#print("\n")
#print(gme_revenue.tail())

#Question 6,7: Plot Tesla and Gamestop Stock Graphs

#make_graph(gme_data, gme_revenue, 'GameStop')

