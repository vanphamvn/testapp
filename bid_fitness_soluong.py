import random
import time
import fut
session = fut.Core('vanphamvn@gmail.com', 'Wasd123!@#', 'test', platform='pc', debug=True)
print(session.credits)
wItems = session.watchlist()
if len(wItems) > 0:
	for a in wItems:
		if a['tradeId'] == -1:
			session.quickSell(a['id'])
count=0
i=0
# size = session.watchlist_size - len(wItems)
size = 20
# print("so luong card can bid %s" % (size))
# pid = int(input('Nhap id player can bid :'))
# mprice = int(input('Nhap max bid mong muon: '))
# mbuy = int(input('Nhap min buy now mong muon: '))
pid = 5002006
mprice = 1300
# mbuy = int(input('Nhap min buy now mong muon: '))
while True:
	if session.credits < 50000: break
	items = session.searchAuctions('development', max_price=mprice, min_buy = 1900, start=i, defId=pid) #177326, 164985
	if count>=size: break
	for x in items:
		if x['currentBid']>=mprice :break
		if count>=size: break
		flag=session.bid(x['tradeId'], mprice)
		print(flag)
		if flag:
			count += 1
			print("count:%d" % (count))
	print("wait for 5,10s ...")
	i += 20
	time.sleep(random.randint(10,15))
session.logout(); # Need to be fixed here
