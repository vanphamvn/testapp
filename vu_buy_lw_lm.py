import random
import time
import fut
session = fut.Core('xxx@gmail.com','xxx','test',platform='ps4',debug=True)
count=0
while True:
        items = session.searchAuctions('training',max_buy=250, start=20,category='position',position='LW-LM')
        for x in items:
                if count>10: break
                flag=session.bid(x['tradeId'], 250)
                print(flag)
                if flag:
                        a=session.sendToClub(x['id'])
                        if a:
                                count += 1
                                print("count:%d" % (count))
        print("wait for 5,10s ...")
        time.sleep(random.randint(10,15)
session.logout()

