import random
import time
import fut
session = fut.Core('xxx@gmail.com','xxx','test',platform='ps4',debug=True)
wItems = session.watchlist()
if len(wItems) > 0:
	for a in wItems:
		if a['tradeId'] == -1:
			session.quickSell(a['id'])
count=0
i=0
size = session.watchlist_size - len(wItems)
print("so luong card can bid %s" % (size))
while True:
	items = session.searchAuctions('player',max_price=700, min_buy = 900, start=i,defId=177326)
	for x in items:
		if x['currentBid']>=700 :break
		if count>=size: break
		flag=session.bid(x['tradeId'], 700)
		print(flag)
		if flag:
			count += 1
			print("count:%d" % (count))
	print("wait for 5,10s ...")
	i += 20
	time.sleep(random.randint(10,15))
session.logout(); # Need to be fixed here
