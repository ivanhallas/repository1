pip install pandas
import pandas
import numpy as np
import wbdata
import matplotlib.pyplot as plt
from pandas_datareader import wbdata
countries = wbdata.get_country(display=False)
#set up the countries I want
countries = ["CL","UY","HU"]
indicators = {'NY.GNP.PCAP.CD':'GNI per Capita'}
df = wbdata.get_dataframe(indicators, country=countries, convert_date=False)
dfu = df.unstack(level=0)
dfu.plot(); 
plt.legend(loc='best'); 
plt.title("GNI Per Capita ($USD, Atlas Method)"); 
plt.xlabel('Date'); plt.ylabel('GNI Per Capita ($USD, Atlas Method')
wbdata.get_source()
import pandas as pd
from pandas_datareader import wb
import wbdata as wb
from pandas_datareader.data import DataReader
from datetime import date
start = date(2015, 1, 1)
end = date (2016, 12, 31)
ticker = "GOOG"
data_source = "google"
stock_data = DataReader(indicator, data_source, start, end)