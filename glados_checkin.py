import requests
import json
import re

cookie = [None]*15
cookie[0] = '_ga=GA1.2.1579639152.1605463057; koa:sess=eyJ1c2VySWQiOjU5ODkwLCJfZXhwaXJlIjoxNjMxMzgzMTM2ODA2LCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=; koa:sess.sig=0I1bougSWfi1p_JZRHKUyjfp4CA; _gid=GA1.2.11539863.1610726686; _gat_gtag_UA_104464600_2=1'
cookie[1] = '_ga=GA1.2.1140848216.1605582834; koa:sess=eyJ1c2VySWQiOjI2NDQ1LCJfZXhwaXJlIjoxNjMxNTAyOTMwMDk2LCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=; koa:sess.sig=ZXKhcar-7EvgyNw2jCGwVdkRXP4; _gid=GA1.2.154204569.1610706667; _gat_gtag_UA_104464600_2=1'
cookie[2] = '_ga=GA1.2.53822065.1605503135; koa:sess=eyJ1c2VySWQiOjI2NDMwLCJfZXhwaXJlIjoxNjMxNDIzMjIyMjkwLCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=; koa:sess.sig=YaIUh1Y8SAlNkWPlQihy3LC8kDU; _gid=GA1.2.479072867.1610707157; _gat_gtag_UA_104464600_2=1'
cookie[3] = '_ga=GA1.2.90697324.1605503303; koa:sess=eyJ1c2VySWQiOjI2NDM2LCJfZXhwaXJlIjoxNjMxNDIzNDAzNDcyLCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=; koa:sess.sig=tCE66cOC6KoMBXhu5DOOFzozUxI; _gid=GA1.2.1842638549.1610726926; _gat_gtag_UA_104464600_2=1'
cookie[4] = '_ga=GA1.2.703625395.1605582628; koa:sess=eyJ1c2VySWQiOjI2NDM4LCJfZXhwaXJlIjoxNjMxNTAyODEyNDA4LCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=; koa:sess.sig=pg2yO8AEUo7rpk4yspqt6vbeolU; _gid=GA1.2.1897327276.1610726986; _gat_gtag_UA_104464600_2=1'
cookie[5] = '_ga=GA1.2.284549808.1605583057; koa:sess=eyJ1c2VySWQiOjM5MjUxLCJfZXhwaXJlIjoxNjMxNTAzMTI2Mzc0LCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=; koa:sess.sig=NTzTliKEmcQ-rTuhqPZnBXsY5IY; _gid=GA1.2.1645238876.1610709197; _gat_gtag_UA_104464600_2=1'
cookie[6] = '_ga=GA1.2.228425513.1605582950; koa:sess=eyJ1c2VySWQiOjM4OTA4LCJfZXhwaXJlIjoxNjMxNTAzMDE4MzQxLCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=; koa:sess.sig=7nSrExoQB-n9nc8B950NnxrT738; _gid=GA1.2.1645564151.1610727071; _gat_gtag_UA_104464600_2=1'
cookie[7] = '_ga=GA1.2.891740161.1605583215; koa:sess=eyJ1c2VySWQiOjQwOTc5LCJfZXhwaXJlIjoxNjMxNTAzMjc2NDQ4LCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=; koa:sess.sig=3RBsrlLK7DlA0gDMLA2Db1vEqRs; _gid=GA1.2.1520114299.1610727104; _gat_gtag_UA_104464600_2=1'
cookie[8] = '_ga=GA1.2.1357629097.1609430928; koa:sess=eyJ1c2VySWQiOjQwOTgwLCJfZXhwaXJlIjoxNjM1MzUxMzM3ODM1LCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=; koa:sess.sig=VzsVnNqcnv_FnLfHMa7sMA97Wqw; _gid=GA1.2.1075109263.1610727137; _gat_gtag_UA_104464600_2=1'
cookie[9] = '_ga=GA1.2.1631060423.1609431401; koa:sess=eyJ1c2VySWQiOjQwOTgxLCJfZXhwaXJlIjoxNjM1MzUxNDk2NjU4LCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=; koa:sess.sig=GmpMoajJJVnn1FXWVChUQpaa2Ho; _gid=GA1.2.2096445797.1610727185; _gat_gtag_UA_104464600_2=1'
cookie[10] = '_ga=GA1.2.1045087335.1609431532; koa:sess=eyJ1c2VySWQiOjQwOTgyLCJfZXhwaXJlIjoxNjM1MzUxNjA1MzI4LCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=; koa:sess.sig=BJExruoSqAhVHcL1Czv5nOsNheU; _gid=GA1.2.1900103615.1610727220; _gat_gtag_UA_104464600_2=1'
cookie[11] = '_ga=GA1.2.453406385.1609431737; koa:sess=eyJ1c2VySWQiOjQxNDczLCJfZXhwaXJlIjoxNjM1MzUxOTcwMDgyLCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=; koa:sess.sig=yaSgR7AY-WGxAJhUhHKRdmR-Nd8; _gid=GA1.2.899490447.1610727250; _gat_gtag_UA_104464600_2=1'
cookie[12] = '_ga=GA1.2.1699226567.1605502813; koa:sess=eyJ1c2VySWQiOjI2MDM2LCJfZXhwaXJlIjoxNjMxNDIzMDUwODU0LCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=; koa:sess.sig=aFWuuYxDct645DoP6IH4O3LqtSs; _gid=GA1.2.2035493277.1610727306; _gat_gtag_UA_104464600_2=1'
cookie[13] = '_ga=GA1.2.439794487.1609432102; koa:sess=eyJ1c2VySWQiOjQzODI4LCJfZXhwaXJlIjoxNjM1MzUyMTUwMzk3LCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=; koa:sess.sig=cSYcmd-iraGBohzoz-LcuGnuZQ4; _gid=GA1.2.311895518.1610727345; _gat_gtag_UA_104464600_2=1'
cookie[14] = '_ga=GA1.2.848820783.1605462955; koa:sess=eyJ1c2VySWQiOjI2MDM3LCJfZXhwaXJlIjoxNjMxMzgzMDEwMjI0LCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=; koa:sess.sig=gsel582xQeTPnaQYUwI43FyvOmA; _gid=GA1.2.30824702.1610706565; _gat_gtag_UA_104464600_2=1'
def checkin():
    headers = {
        'origin' : 'https://glados.rocks',
        'referer': 'https://glados.rocks/console/checkin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
        'content-type' : 'application/json;charset=UTF-8'
        #'cookie': ''
    }
    #payload类型---使用json.dumps()将python对象转化为json字符串
    data = {
        'token' : 'glados_network'
    }
    url = 'https://glados.rocks/api/user/checkin'
    #session = requests.session()
    #response = session.post(url, headers=headers,data=json.dumps(data))
    for i in range(15):
      headers['cookie'] = cookie[i]
      response = requests.post(url, headers=headers,data=json.dumps(data))
      print(response.text[8])
      print('/n')
checkin()