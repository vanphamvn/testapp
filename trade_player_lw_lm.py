import fut
session = fut.Core('xxx@gmail.com','xxx','test',platform='ps4',debug=True)
count=0
a=0
session.relist()
soldItems = session.tradepile()
for x in soldItems:
        if x['tradeState'] == 'closed':
                session.tradepileClear()
                break;
a = session.tradepile_size - len(session.tradepile())
print("so luong card can send to tranfer %s" % a)
items = session.watchlist()
for y in items:
        if y['tradeId'] == -1:
                session.quickSell(y['id'])
                print("special case : xoa expired card %s" % (y['id']))
                break
        if y['bidState'] == 'outbid':
                session.watchlistDelete(y['tradeId'])
                print("xoa card outbid")
        if len(y) <= 2: break #Se xu li sau
        if count>=a: break
        if all([y['bidState'] == 'highest', y['tradeState'] == 'closed']):
                flag=session.sendToClub(y['id'])
                print(flag)
                if flag:
                        session.applyConsumable(y['id'], 5003065)
                        print("sent card to tradepile")
                        session.sendToTradepile(y['id'])
                        session.sell(y['id'], 1300, 1400)
                        count += 1
                        print("da send card thanh cong to Transfer, so luong %s" % count) 
                else:
                        b = session.club(defId=y['assetId']) # Nho tim defIf player put vo day
                        if b[0]['position'] == 'LW' :
                                session.applyConsumable(b[0]['id'], 5003065)
                        session.sendToTradepile(b[0]['id'])
                        session.sell(b[0]['id'], 1300, 1400)
                        count += 1
                        print("da send card thanh cong to Transfer, so luong %s" % count)
print("done ...")
session.logout()
