import fut
session = fut.Core('xxx@gmail.com','xxx','test',platform='ps4',debug=True)
count=0
items = session.watchlist()
for x in items:
        if count>=8: break
        flag=session.sendToClub(x['id'])
        print(flag)
        if flag:
                session.applyConsumable(x['id'], 5003065)
                count += 1
                print("count:%d" % (count))
                print("sent card to tradepile")
                session.sendToTradepile(x['id'])
                session.sell(x['id'], 1200, 1300)
        else:
                a = session.club(defId='164985')
                if a[0]['position'] == 'LW' :
                        session.applyConsumable(a[0]['id'], 5003065)
                session.sendToTradepile(a[0]['id'])
                session.sell(a[0]['id'], 1200, 1300)                
print("wait for 5,10s ...")
session.logout()
