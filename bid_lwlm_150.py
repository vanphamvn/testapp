import random
import time
import fut
session = fut.Core('xxx@gmail.com','xxx','test',platform='ps4',debug=True)
count=0
i=0
size = int(input('Nhap so luong card can mua :'))
while True:
        items = session.searchAuctions('training',max_buy=200, start=i,category='position',position='LW-LM')
        if count>=size: break
	for x in items:
		if x['currentBid']>=200 :break
		if count>=size: break
		flag=session.bid(x['tradeId'], 150)
		print(flag)
		if flag:
			count += 1
			print("count:%d" % (count))
	print("wait for 5,10s ...")
	i += 20
	time.sleep(random.randint(10,15))
session.logout(); # Need to be fixed here
