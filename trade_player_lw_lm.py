import fut
session = fut.Core('xxx@gmail.com','xxx','test',platform='ps4',debug=True)
count=0
a=0
a = session.tradepile_size - len(session.tradepile())
print("so luong card can send to tranfer %s" % a)
items = session.watchlist()
for x in items:
        if x['tradeId'] == -1:
                session.quickSell(x['id'])
                print("special case : xoa expired card %s" % (x['id']))
                break
        if x['bidState'] == 'outbid':
                session.watchlistDelete(x['tradeId'])
                print("xoa card outbid")
        if count>=a: break
        if all([x['bidState'] == 'highest', x['tradeState'] == 'closed']):
                flag=session.sendToClub(x['id'])
                print(flag)
                if flag:
                        session.applyConsumable(x['id'], 5003065)
                        print("sent card to tradepile")
                        session.sendToTradepile(x['id'])
                        session.sell(x['id'], 1300, 1400)
                        count += 1
                        print("da send card thanh cong to Transfer, so luong %s" % count) 
                else:
                        b = session.club(defId=x['assetId']) # Nho tim defIf player put vo day
                        if b[0]['position'] == 'LW' :
                                session.applyConsumable(b[0]['id'], 5003065)
                        session.sendToTradepile(b[0]['id'])
                        session.sell(b[0]['id'], 1300, 1400)
                        count += 1
                        print("da send card thanh cong to Transfer, so luong %s" % count)
print("done ...")
session.relist()
#session.tradepileClear() # can xu li them, neu co the sold thi run it
session.logout()
