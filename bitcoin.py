import requests
import json
import time
import os
import csv
from datetime import datetime, date, timedelta


start_date = date(2016, 1, 1)
end_date = date(2017, 8, 30)
current_date = start_date
for single_date in range(0, ((end_date - start_date).days/5)) :
	print current_date.strftime("%Y-%m-%d %H:%M:%S")
	str_time = current_date.strftime("%Y-%m-%d %H:%M:%S")
	curr_time = str(int(time.mktime(datetime.strptime(str_time, "%Y-%m-%d %H:%M:%S").timetuple())))
	r = requests.get('http://api.bitcoincharts.com/v1/trades.csv', params = {"symbol" : "bitstampUSD", "start" : curr_time})
	csvfile = open('bitcoinFiles/' + current_date.strftime("%Y-%m-%d") + '.csv',"wb+")
	os.chmod(csvfile.name, 0777)
	csvfile.write(r.text)
	current_date = current_date + timedelta(days = 5)