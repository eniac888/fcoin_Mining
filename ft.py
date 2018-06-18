from fcoin3 import Fcoin
import random
import time
import datetime
import os

while True:
	file = open('./mytxt.txt', 'a+')

	fcoin = Fcoin()

	fcoin.auth('xxx','xxx')
	nowtime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	resultstr = fcoin.get_market_ticker("ftusdt")
	file.write(str(resultstr)+'\n')
	wantstr = resultstr["data"]["ticker"]
	a, b = wantstr[2], wantstr[4]
	result = round(random.uniform(a, b), 6)
	file.write("random price is:"+str(result)+"now time:"+nowtime + '\n')

	file.write("buy status is:"+str(fcoin.buy('ftusdt', result, 10))+" now time:"+nowtime + '\n')
	file.write("sell status is:"+str(fcoin.sell('ftusdt', result, 10))+" now time:"+nowtime  + '\n')


	file.close()
	#执行完等5秒继续循环
	time.sleep(5)
