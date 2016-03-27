#!/usr/bin/python
import re
import requests
from bs4 import BeautifulSoup
import sys

def getList(market='TSE'):
	if market == 'TSE':
		strMode = '2'
	elif market == 'OTC':
		strMode = '4'
	else:
		print "market must be 'TSE' or 'OTC'"
		sys.exit(0)

	url = "http://isin.twse.com.tw/isin/C_public.jsp?strMode=" + strMode
	res = requests.get(url, verify=False)
	soup = BeautifulSoup(res.text, 'html.parser')

	for row in soup.select('tr'):
		cols = row.find_all('td')
		col1 = cols[0].text.encode('utf-8')
		data = re.search(r'(.*)      (.*)', col1)
		if data is not None:
			if data.group(1) is not None:
				if data.group(2) is not None:
					if (len(cols[4].text.encode('utf-8')) != 0):
						symbolid = filter(str.isalnum, data.group(1))
						symbol = data.group(2)
						#start = cols[2].text.encode('utf-8')
						#type = cols[4].text.encode('utf-8')
						print symbolid, symbol
						
					

getList('TSE')
getList('OTC')

