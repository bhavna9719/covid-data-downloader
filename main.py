import urllib.request
from pandas import read_html
import pandas
import time


#URL = "https://www.covid19india.org/"
url = "https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/"

while True:


    req = urllib.request.Request(
        url, 
        data=None, 
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )

    f = urllib.request.urlopen(req)
    html_data = f.read().decode('utf-8')

    x = read_html(html_data)

    pandas.set_option("display.max_rows", None, "display.max_columns", None)


    from datetime import datetime

    filename = str(round(datetime.now().timestamp()))
    print(filename)

    f = open("data/"+ filename +  ".csv","w")

    for row in x:
        f.write(str(row.to_csv()))
    
    f.close()
    time.sleep(10)


