import random
import time
import fut
session = fut.Core('xxx@gmail.com','xxx','test',platform='ps4',debug=True)
count=0
i = int(input('Nhap so luong card can mua :'))
while True:
        items = session.searchAuctions('training',max_buy=200, start=i,category='position',position='LW-LM')
        for x in items:
                if count>i: break
                flag=session.bid(x['tradeId'], 200)
                print(flag)
                if flag:
                        a=session.sendToClub(x['id'])
                        if a:
                                count += 1
                                print("count:%d" % (count))
        print("wait for 5,10s ...")
        i += 20
        time.sleep(random.randint(10,15))
session.logout()
