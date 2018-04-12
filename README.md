# zerodha-task1
Task1 for  Zerodha Careers


## Download latest csv in zip format from  http://www.bseindia.com/markets/equity/EQReports/BhavCopyDebt.aspx?expandable=3 and extarct it

```python
import urllib.request
import urllib
import datetime
import zipfile


def download_csv_zip_extract():
	# get today's date and use this to generate URL for downloading latest CSV in ZIP format
	today = str(datetime.date.today())
	year, month, day = today.split("-")
	date = "{}-{}-{}".format(day, month, year)
	print("Today's Date: ", date)

	base_url = "https://www.bseindia.com/download/BhavCopy/Equity/EQ{}{}{}_CSV.ZIP".format(int(day)-1, month, year[2:])
	print(base_url)
	filename = base_url.split("/")[-1]
	print(filename)
	file = urllib.request.urlretrieve(base_url, filename)
	zip_ref = zipfile.ZipFile(filename, 'r')
	zip_ref.extractall()
	zip_ref.close()




if __name__ == '__main__':
	download_csv_zip_extract()

```

## Selcting Column Fields: code, name, open, high, low, close from the CSV File 

```python
import pandas as pd
data =(pd.read_csv(filename, usecols=["SC_CODE", "SC_NAME", "OPEN", "HIGH", "LOW", "CLOSE"]))

```

## Top 10 Stock Comapnies by Closing Price

```python
import pandas as pd
data =(pd.read_csv(filename, usecols=["SC_CODE", "SC_NAME", "OPEN", "HIGH", "LOW", "CLOSE"]))
print("Top 10 Stock Comapnies by Closing Price")
data.sort_values(by="CLOSE" ,ascending=False ) [:10]

```

Steps to run the notebook files:
1. Install the requirements by using  this command:

```code
pip install -r requirements.txt
```

2. Run jupyter-notebook by using this command:

```code
jupyter-notebok
```
![Screenshot](https://github.com/gauravssnl/zerodha-task1/blob/master/ScreenShots/Screenshot%20from%202018-04-12%2016-57-54.png)

