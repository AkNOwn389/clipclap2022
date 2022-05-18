# -*- coding: utf-8 -*-
import os, sys, time, datetime, re, json
try:
  import requests
  session=requests.Session()
except ImportError:
    os.system('pip2 install session')

from requests.exceptions import ConnectionError
from datetime import date

#COLOR CODE
red='\033[1;31m'
green='\033[1;32m'
yellow='\033[1;33m'
blue='\033[1;34m'
purple='\033[1;35m'
cyan='\033[1;36m'

logo=(yellow+'''  _____ _ _            _             ____        _
 / ____| (_)          | |           |  _ \      | |
| |    | |_ _ __   ___| | __ _ _ __ | |_) | ___ | |_
| |    | | | '_ \ / __| |/ _` | '_ \|  _ < / _ \| __|
| |____| | | |_) | (__| | (_| | |_) | |_) | (_) | |_
 \_____|_|_| .__/ \___|_|\__,_| .__/|____/ \___/ \__|
           | |                | |
           |_|                |_|'''+green+'darius')

rewardtime=[]
rewardtype=[]



def bagal(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)

def bottie():
	try:
		h=open('Token.txt')
		token=h.read()
		h.close()
		j=open('User_id.txt')
		uid=j.read()
		j.close()
		k=open('uuid.txt')
		uuid=k.read()
		k.close()
	except:
		Data()
	url = "https://api.cc.lerjin.com:443/reading/timer"
	header = {"Host": "api.cc.lerjin.com","charset": "UTF-8","device-type": "2","api-version": "2","external-version": "3.8.8","device": "11","userId": "{}".format(str(uid)),"version": "42","timezone": "8","ostype": "android","lang": "en","token": "{}".format(token),"uuid": "{}".format(uuid),"app-id": "ClipClaps_gg","Content-Type": "application/json; charset=utf-8","accept-encoding": "gzip","User-Agent": "okhttp/4.2.1","Content-Length": "80"}
	body = {"userid":"{}".format(str(uid)),"token":"{}".format(str(token))}
	web = session.post(url,headers=header,json=body)
	page = json.loads(web.text)
	count_data=(page['data']['config']['timerReward'])
	count_len=len(page['data']['config']['timerReward'])
	for i in range(count_len):
		i = count_data[i]
		reward_type=(i['rewardType'])
		reward_time=(i['time'])
		rewardtime.append(reward_time)
		rewardtype.append(reward_type)
	os.system('clear')
	print(logo)
	print (50 * '\033[1;94m\xe2\x95\x90')
	print('\033[1;92m Getting ches')
	print (50 * '\033[1;94m\xe2\x95\x90')
	for i in range(len(rewardtime)):
	  today = str(date.today())
	  url = "https://api.cc.lerjin.com:443/reading/obtainReward"
	  header = {"charset": "UTF-8","api-version": "2","external-version": "3.8.8","app-id": "ClipClaps_gg","timezone": "8","ostype": "android","userId": uid,"version": "42","uuid": uuid,"token": token,"device-type": "2","lang": "en","device": "11","Content-Type": "application/json; charset=utf-8","Content-Length": "241","Host": "api.cc.lerjin.com","Connection": "Keep-Alive","Accept-Encoding": "gzip","User-Agent": "okhttp/4.2.1"}
	  body={"specific":"false","token":"{}".format(str(token)),"rewardTime":"{}".format(str(rewardtime[i])),"articleTime":"0","version":"11","rewardType":"{}".format(str(rewardtype[i])),"day":"{}".format(str(today)),"videoTime":"{}".format(str(rewardtime[i])),"activeDay":"1","userid":"{}".format(str(uid))}
	  web = session.post(url,headers=header,json=body)
	  page=json.loads(web.text)
	  code=page['code']
	  status = page["msg"]
	  if int(code) == 4000:
	    print('\033[1;92m[-] \033[1;93m Already Get this chess')
	  else:
	    print('\033[1;93mGet \033[1;92m-> \033[1;95m{}'.format(rewardtype[i]))
	Openches()
def Openches():
  try:
    h=open('Token.txt')
    token=h.read()
    h.close()
    j=open('User_id.txt')
    uid=j.read()
    j.close()
    k=open('uuid.txt')
    uuid=k.read()
    k.close()
  except:
    Data()
  print (50 * '\033[1;94m\xe2\x95\x90')
  print('\033[1;92m opening ches')
  print (50 * '\033[1;94m\xe2\x95\x90')
  url=('https://api.cc.lerjin.com:443/reward/list')
  header = {"charset": "UTF-8","api-version": "2","external-version": "3.8.8","app-id": "ClipClaps_gg","timezone": "8","ostype": "android","userId": uid,"version": "42","uuid": uuid,"token": token,"device-type": "2","lang": "en","device": "11","Content-Type": "application/json; charset=utf-8","Content-Length": "79","Host": "api.cc.lerjin.com","Connection": "Keep-Alive","Accept-Encoding": "gzip","User-Agent": "okhttp/4.2.1"}
  body={"userid":"{}".format(str(uid)),"token":"{}".format(str(token))}
  web=session.post(url,headers=header,json=body)
  page=json.loads(web.text)
  try:
    copper=(page['data']['treasureChest'][0])
    copper_count=copper['num']
    if int(copper_count)==0:
      print('\033[1;94m No copper chess')
    for i in range(int(copper_count)):
      url=('https://api.cc.lerjin.com:443/reward/treasureChest/open')
      header = {"charset": "UTF-8","api-version": "2","external-version": "3.8.8","app-id": "ClipClaps_gg","timezone": "8","ostype": "android","userId": uid,"version": "42","uuid": uuid,"token": token,"device-type": "2","lang": "en","device": "11","Content-Type": "application/json; charset=utf-8","Content-Length": "95","Host": "api.cc.lerjin.com","Connection": "Keep-Alive","Accept-Encoding": "gzip","User-Agent": "okhttp/4.2.1"}
      body={"type":"copper","userid":"{}".format(str(uid)),"token":"{}".format(str(token))}
      web=session.post(url,headers=header,json=body)
      page_=json.loads(web.text)
      message=page_['msg']
      if message=='Success':
        for i in range(len(page_['data']['rewards'])):
          data=page_['data']['rewards'][i]
          ty=data['type']
          bilang=data['quantity']
          print('\033[1;93mCopper ches \033[1;92m-> \033[1;95m{} \033[1;91m/\033[1;93m {}'.format(ty,bilang))
      else:
        pass
  except:
    print('\033[1;94m No Copper chess')
    pass
  try:
    silver=(page['data']['treasureChest'][1])
    silver_count=silver['num']
    if int(silver_count)==0:
      print('\033[1;94m No silver chess')
    for i in range(int(silver_count)):
      url=('https://api.cc.lerjin.com:443/reward/treasureChest/open')
      header={"Host": "api.cc.lerjin.com","charset": "UTF-8","api-version": "2","external-version": "3.8.0","app-id": "ClipClaps_gg","timezone": "8","ostype": "android","userid": "{}".format(str(uid)),"version": "42","uuid": "{}".format(str(uuid)),"token": "{}".format(str(token)),"device-type": "2","lang": "en","device": "11","content-type": "application/json; charset\u003dutf-8","content-length": "95","accept-encoding": "gzip","user-agent": "okhttp/4.2.1"}
      body={"type":"silver","userid":"{}".format(str(uid)),"token":"{}".format(str(token))}
      web=session.post(url,headers=header,json=body)
      page_=json.loads(web.text)
      message=page_['msg']
      if message=='Success':
        for i in range(len(page_['data']['rewards'])):
          data=page_['data']['rewards'][i]
          ty=data['type']
          bilang=data['quantity']
          print('\033[1;92mSilver ches \033[1;92m-> \033[1;96m{} \033[1;91m/\033[1;93m {}'.format(ty,bilang))
      else:
        pass
  except:
    print('\033[1;94m No silver chess')
    pass
  try:
    gold=(page['data']['treasureChest'][2])
    gold_count=gold['num']
    if int(gold_count)==0:
      print('\033[1;94m No gold chess')
    for i in range(int(gold_count)):
      url=('https://api.cc.lerjin.com:443/reward/treasureChest/open')
      header={"Host": "api.cc.lerjin.com","charset": "UTF-8","api-version": "2","external-version": "3.8.0","app-id": "ClipClaps_gg","timezone": "8","ostype": "android","userid": "{}".format(str(uid)),"version": "42","uuid": "{}".format(str(uuid)),"token": "{}".format(str(token)),"device-type": "2","lang": "en","device": "11","content-type": "application/json; charset\u003dutf-8","content-length": "95","accept-encoding": "gzip","user-agent": "okhttp/4.2.1"}
      body={"type":"gold","userid":"{}".format(str(uid)),"token":"{}".format(str(token))}
      web=session.post(url,headers=header,json=body)
      page_=json.loads(web.text)
      message=page_['msg']
      if message=='Success':
        for i in range(len(page_['data']['rewards'])):
          data=page_['data']['rewards'][i]
          ty=data['type']
          bilang=data['quantity']
          print('\033[1;92mGold ches \033[1;92m-> \033[1;96m{} \033[1;91m/\033[1;93m {}'.format(ty,bilang))
      else:
        pass
  except:
    print('\033[1;94m No Gold chess')
    pass
  try:
    newbie=(page['data']['treasureChest'][3])
    newbie_count=newbie['num']
    if int(newbie_count)==0:
      print('\033[1;94m No Newbie chess')
    for i in range(int(newbie_count)):
      url=('https://api.cc.lerjin.com:443/reward/treasureChest/open')
      header={"Host": "api.cc.lerjin.com","charset": "UTF-8","api-version": "2","external-version": "3.8.0","app-id": "ClipClaps_gg","timezone": "8","ostype": "android","userid": "{}".format(str(uid)),"version": "42","uuid": "{}".format(str(uuid)),"token": "{}".format(str(token)),"device-type": "2","lang": "en","device": "11","content-type": "application/json; charset\u003dutf-8","content-length": "95","accept-encoding": "gzip","user-agent": "okhttp/4.2.1"}
      body={"type":"newbie","userid":"{}".format(str(uid)),"token":"{}".format(str(token))}
      web=session.post(url,headers=header,json=body)
      page_=json.loads(web.text)
      message=page_['msg']
      if message=='Success':
        for i in range(len(page_['data']['rewards'])):
          data=page_['data']['rewards'][i]
          ty=data['type']
          bilang=data['quantity']
          print('\033[1;92mNewbie ches \033[1;92m-> \033[1;96m{} \033[1;91m/\033[1;93m {}'.format(ty,bilang))
      else:
        pass
  except:
    print('\033[1;94m No Newbie chess')
    pass
  try:
    diamond=(page['data']['treasureChest'][4])
    diamond_count=diamond['num']
    if int(diamond_count)==0:
      print('\033[1;94m No Diamond chess')
    for i in range(int(diamond_count)):
      url=('https://api.cc.lerjin.com:443/reward/treasureChest/open')
      header={"Host": "api.cc.lerjin.com","charset": "UTF-8","api-version": "2","external-version": "3.8.0","app-id": "ClipClaps_gg","timezone": "8","ostype": "android","userid": "{}".format(str(uid)),"version": "42","uuid": "{}".format(str(uuid)),"token": "{}".format(str(token)),"device-type": "2","lang": "en","device": "11","content-type": "application/json; charset\u003dutf-8","content-length": "95","accept-encoding": "gzip","user-agent": "okhttp/4.2.1"}
      body={"type":"diamond","userid":"{}".format(str(uid)),"token":"{}".format(str(token))}
      web=session.post(url,headers=header,json=body)
      page_=json.loads(web.text)
      message=page_['msg']
      if message=='Success':
        for i in range(len(page_['data']['rewards'])):
          data=page_['data']['rewards'][i]
          ty=data['type']
          bilang=data['quantity']
          print('\033[1;92mDiamond ches \033[1;92m-> \033[1;96m{} \033[1;91m/\033[1;93m {}'.format(ty,bilang))
      else:
        pass
  except:
    print('\033[1;94m No Diamond chess')
  print('\n\033[1;92m All ches opened')
  video()
def video():
  try:
    h=open('Token.txt')
    token=h.read()
    h.close()
    j=open('User_id.txt')
    uid=j.read()
    j.close()
    k=open('uuid.txt')
    uuid=k.read()
    k.close()
  except:
    Data()
  print (50 * '\033[1;94m\xe2\x95\x90')
  print('\033[1;92m Video bonus')
  print (50 * '\033[1;94m\xe2\x95\x90')
  url=('https://api.cc.lerjin.com:443/reward/receiveTaskAwards')
  header={'charset': 'UTF-8','api-version': '2','external-version': '3.8.0','app-id': 'ClipClaps_gg','timezone': '8','ostype': 'android','userId': '{}'.format(str(uid)),'version': '42','uuid': '{}'.format(str(uuid)),'token': '{}'.format(str(token)),'device-type': '2','lang': 'en','device': '11','Content-Type': 'application/json; charset=utf-8','Content-Length': '94','Host': 'api.cc.lerjin.com','Connection': 'Keep-Alive','Accept-Encoding': 'gzip','User-Agent': 'okhttp/4.2.1'}
  body={"type":"VIDEO","userid":"{}".format(str(uid)),"token":"{}".format(str(token))}
  b=session.post(url,headers=header,json=body)
  c=json.loads(b.text)
  if c['msg'] == 'Success':
    print('\033[1;92m Get-> \033[1;93mvideo Bonus 500\n')
  else:
    print('\033[1;94m Already Got')
  achivement()
def achivement():
  try:
    h=open('Token.txt')
    token=h.read()
    h.close()
    j=open('User_id.txt')
    uid=j.read()
    j.close()
    k=open('uuid.txt')
    uuid=k.read()
    k.close()
  except:
    Data()
  print (50 * '\033[1;94m\xe2\x95\x90')
  print('\033[1;92m Checking Achievement')
  print (50 * '\033[1;94m\xe2\x95\x90')
  url=('https://core.cc.lerjin.com:443/achievement/list')
  header={'charset': 'UTF-8','timezone': '8','appver': '3.8.0','apiver': '42','sysver': '11','ostype': 'android','lang': 'en','userId': uid,'uuid': uuid,'Content-Type': 'application/json','token': token,'Host': 'core.cc.lerjin.com','Connection': 'Keep-Alive','Accept-Encoding': 'gzip','User-Agent': 'okhttp/4.2.1'}
  web=session.get(url,headers=header)
  page_1=json.loads(web.text)
  for i in range(3):
    url=('https://core.cc.lerjin.com:443/achievement/upgrade')
    header={'charset': 'UTF-8','timezone': '8','appver': '3.8.0','apiver': '42','sysver': '11','ostype': 'android','lang': 'en','userId': '{}'.format(uid),'uuid': '{}'.format(uuid),'token': '{}'.format(token),'Content-Type': 'application/json; charset=utf-8','Content-Length': '12','Host': 'core.cc.lerjin.com','Connection': 'Keep-Alive','Accept-Encoding': 'gzip','User-Agent': 'okhttp/4.2.1'}
    zz=1
    body={"type":"{}".format(str(zz))}
    try:
      
      web=session.post(url,headers=header,json=body)
      page=json.loads(web.text)
    except:
      pass
    try:
      if bool(page['ifSuccess'])==True or str(page['ifSuccess'])=="true":
        print('\033[1;92m=> \033[1;96mGot bonus \033[1;93m'+page_1[i]['progressBar']['rewardNum'])
      else:
        pass
    except:
      pass
    zz+=1
  spinwhell()
num=['1']
def spinwhell():
  try:
    h=open('Token.txt')
    token=h.read()
    h.close()
    j=open('User_id.txt')
    uid=j.read()
    j.close()
    k=open('uuid.txt')
    uuid=k.read()
    k.close()
  except:
    Data()
  print (50 * '\033[1;94m\xe2\x95\x90')
  print('\033[1;92m Spin wheel')
  print (50 * '\033[1;94m\xe2\x95\x90')
  while True:
    num.append('+1')
    num.append('+1')
    num_=len(num)
    url=('https://api.cc.lerjin.com:443/activity/spin')
    header={"Host": "api.cc.lerjin.com","content-length": "91","version": "40","user-agent": "Mozilla/5.0 (Linux; Android 11; Infinix X695D Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36 ClipClaps/3.8.0","content-type": "application/json","accept": "*/*","origin": "https://h5.cc.lerjin.com","x-requested-with": "com.sanhe.clipclaps","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://h5.cc.lerjin.com/","accept-encoding": "gzip, deflate","accept-language": "en-US,en;q\u003d0.9,fil-PH;q\u003d0.8,fil;q\u003d0.7"}
    body={"spinType":"lucky","token":"{}".format(str(token)),"userid":"{}".format(str(uid)),"_reqidx":num_}
    
    try:
      web=session.post(url,headers=header,json=body)
    except:
      print('\033[1;91m Something when wrong')
    try:
      page=json.loads(web.text)
    except:
      print('\033[1;91m Data error')
      Data()
    try:
      if page['msg'] == 'Success':
        print('\033[;92m Get \033[1;96m{} \033[1;91m/ \033[1;93m {}'.format(page['data']['reward']['type'],page['data']['reward']['quantity']))
      else:
        print('\033[1;91m Spin charging')
        time.sleep(2)
        watching()
    except:
      pass
    
    
    
def watching():
  from datetime import datetime
  try:
    h=open('Token.txt')
    token=h.read()
    h.close()
    j=open('User_id.txt')
    uid=j.read()
    j.close()
    k=open('uuid.txt')
    uuid=k.read()
    k.close()
  except:
    print('\033[1;91m[\033[1;92mFile Missing\033[1;91m]')
    Data()
  print (50 * '\033[1;94m\xe2\x95\x90')
  print('\033[1;92m Watching Homefeed')
  print (50 * '\033[1;94m\xe2\x95\x90')
  url=('https://newfeeds.cc.lerjin.com:443/feeds/home-pull?form=user%20refresh')
  header={'charset': 'UTF-8','timezone': '8','appver': '3.8.0','apiver': '42','sysver': '11','ostype': 'android','lang': 'en','userId': '{}'.format(str(uid)),'uuid': '{}'.format(str(uuid)),'Content-Type': 'application/json','token': '{}'.format(str(token)),'Host': 'newfeeds.cc.lerjin.com','Connection': 'Keep-Alive','Accept-Encoding': 'gzip','User-Agent': 'okhttp/4.2.1'}
  a=session.get(url,headers=header)
  b=json.loads(a.text)
  try:
    url=('https://cpv.cc.lerjin.com:443/behavior/event')
    header={'charset': 'UTF-8','timezone': '8','appver': '3.8.8','apiver': '42','sysver': '11','ostype': 'android','lang': 'en','userId': uid,'uuid': uuid,'token': token,'Content-Type': 'application/json; charset=utf-8','Content-Length': '344','Host': 'cpv.cc.lerjin.com','Connection': 'Keep-Alive','Accept-Encoding': 'gzip','User-Agent': 'okhttp/4.2.1'}
    body={"sourceId":"{},{},{},{},{},{},{},{},{}".format(b[0]['sourceId'],b[1]['sourceId'],b[2]['sourceId'],b[3]['sourceId'],b[4]['sourceId'],b[5]['sourceId'],b[6]['sourceId'],b[7]['sourceId'],b[8]['sourceId']),"pullFrom":"","eventType":"SHOW"}
    c=session.post(url,headers=header,json=body)
    d=json.loads(c.text)
  except:
    print('\033[1;91mSomething rwong')
  for i in range(len(b)):
    earn=b[i]
    url=('https://cpv.cc.lerjin.com:443/behavior/event')
    header={'charset': 'UTF-8','timezone': '8','appver': '3.8.0','apiver': '42','sysver': '11','ostype': 'android','lang': 'en','userId': '{}'.format(str(uid)),'uuid': '{}'.format(str(uuid)),'Content-Type': 'application/json; charset=utf-8','Content-Length': '99','token': '{}'.format(str(token)),'Host': 'cpv.cc.lerjin.com','Connection': 'Keep-Alive','Accept-Encoding': 'gzip','User-Agent': 'okhttp/4.2.1'}
    body={"sourceId":(earn['sourceId']),"pullFrom":(earn['pullFrom']),"eventType":"VIEW"}
    try:
      f=session.post(url,headers=header,json=body)
      g=json.loads(f.text)
    except:
      pass
    url=('https://cpv.cc.lerjin.com/behavior/event')
    header={'charset': 'UTF-8','timezone': '8','appver': '3.8.0','apiver': '42','sysver': '11','ostype': 'android','lang': 'en','userId': '{}'.format(str(uid)),'uuid': '{}'.format(str(uuid)),'Content-Type': 'application/json; charset=utf-8','Content-Length': '104','token': '{}'.format(str(token)),'Host': 'cpv.cc.lerjin.com','Connection': 'Keep-Alive','Accept-Encoding': 'gzip','User-Agent': 'okhttp/4.2.1'}
    body={"sourceId":"{}".format(str(earn['sourceId'])),"pullFrom":(earn['pullFrom']),"eventType":"FULL_VIEW"}
    try:
      f=session.post(url,headers=header,json=body)
      g=json.loads(f.text)
    except:
      pass
    if str(g)=='True':
      try:
        print('\033[1;92m_watch: \033[1;93m{}'.format(earn['videoTitle']))
      except:
        try:
          print('\033[1;92m_watch: \033[1;93m{}'.format(earn['authorName']))
        except:
          try:
            print('_watch: {}'.format(earn['sourceId'][0:6]))
          except:
            pass
      url=('https://cpv.cc.lerjin.com/behavior/event')
      header={'charset': 'UTF-8','timezone': '8','appver': '3.8.0','apiver': '42','sysver': '11','ostype': 'android','lang': 'en','userId': '{}'.format(str(uid)),'uuid': '{}'.format(str(uuid)),'Content-Type': 'application/json; charset=utf-8','Content-Length': '99','token': '{}'.format(str(token)),'Host': 'cpv.cc.lerjin.com','Connection': 'Keep-Alive','Accept-Encoding': 'gzip','User-Agent': 'okhttp/4.2.1'}
      body={"sourceId":"{}".format(str(earn['sourceId'])),"pullFrom":(earn['pullFrom']),"eventType":"CLAP"}
      try:
        h=session.post(url,headers=header,json=body)
        j=json.loads(h.text)
        if str(j)=='True':
          sys.stdout.write('-> \033[1;92mClap!')
          sys.stdout.flush('-> \033[1;92mClap!')
        else:
          print('\033[1;91m denied')
      except:
        pass
      url=('https://cpv.cc.lerjin.com/behavior/event')
      header={'charset': 'UTF-8','timezone': '8','appver': '3.8.0','apiver': '42','sysver': '11','ostype': 'android','lang': 'en','userId': '{}'.format(str(uid)),'uuid': '{}'.format(str(uuid)),'Content-Type': 'application/json; charset=utf-8','Content-Length': '99','token': '{}'.format(str(token)),'Host': 'cpv.cc.lerjin.com','Connection': 'Keep-Alive','Accept-Encoding': 'gzip','User-Agent': 'okhttp/4.2.1'}
      body={"sourceId":"{}".format(str(earn['sourceId'])),"pullFrom":(earn['pullFrom']),"eventType":"SHARE"}
      try:
        h=session.post(url,headers=header,json=body)
        j=json.loads(h.text)
        if str(j)=='True':
          print('-> \033[1;92mShare!\n')
        else:
          print('\033[1;91m denied')
      except:
        pass
    else:
      print('\033[1;91m denied')
  watching()
    
          

    

  
def Home_page():
  os.system('reset')
  print(logo)
  try:
    h=open('Token.txt')
    token=h.read()
    h.close()
    j=open('User_id.txt')
    uid=j.read()
    j.close()
    k=open('uuid.txt')
    uuid=k.read()
    k.close()
  except:
    print('\033[1;91m[\033[1;92mFile Missing\033[1;91m]')
    Data()
  try:
    url = "https://api.cc.clipclaps.tv:443/reward/redeem"
    header = {"User-Agent":"okhttp/4.2.1","uuid":"{}".format(str(uuid)),"device-type":"2","api-version":"2","external-version":"3.8.8","device":"11","version":"42","timezone":"8","app-id":"ClipClaps_gg"}
    body = {"token": "{}".format(str(token)),"userid": "{}".format(str(uid)),"redeemCode": "7094385125"}
    web = session.post(url,headers=header,json=body)
    page = json.loads(web.text)
  except:
    pass
  url = "https://api.cc.lerjin.com:443/user/self/info"
  header = {"charset": "UTF-8","api-version": "2","external-version": "3.8.8","app-id": "ClipClaps_gg","timezone": "8","ostype": "android","userId": uid,"version": "42","uuid": uuid,"token": token,"device-type": "2","lang": "en","device": "11","Content-Type": "application/json; charset=utf-8","Content-Length": "79","Host": "api.cc.lerjin.com","Connection": "Keep-Alive","Accept-Encoding": "gzip","User-Agent": "okhttp/4.2.1"}
  body = {"userid":"{}".format(uid),"token":"{}".format(token)}
  body = {"token": str(token),"userid": str(uid)}
  web = session.post(url,headers=header,json=body)
  page = json.loads(web.text)
  page=page['data']
  nickname=page['nickname']
  balance=page['coinBalance']
  cash=page['cash']
  print (50 * '\033[1;94m\xe2\x95\x90')
  print ('\033[1;94m\xe2\x95\x91--\033[1;91m>\033[1;92m {}'.format(nickname))
  print ('\033[1;94m\xe2\x95\x91--\033[1;91m> \033[1;92mBalance \033[1;96m {}'.format(balance))
  print ('\033[1;94m\xe2\x95\x91--\033[1;91m> \033[1;92mCash: \033[1;96m{}'.format(cash))
  print (50 * '\033[1;94m\xe2\x95\x90')
  print ('\033[1;94m\xe2\x95\x91--\033[1;91m> \033[1;94m1.\033[1;92m Start Bot')
  print ('\033[1;94m\xe2\x95\x91--\033[1;91m> \033[1;91m0.\033[1;92m Exit')
  print ('\033[1;94m\xe2\x95\x91')
  choose()
def choose():
  pick = raw_input('\033[1;94m\xe2\x95\x9a\xe2\x95\x90\033[1;91m>>> \033[1;92m')
  if pick == '':
      print ('\033[1;94m\xe2\x95\x91\033[1;91m[Type invalid]\033[1;92m')
      choose()
  elif pick == '1':
    bottie()
  elif pick == '2':
    Openches()
  elif pick == '3':
    spinwhell()
  elif pick == '0':
    sys.exit(1)
  
  else:
    print ('\033[1;92m\xe2\x95\x91\033[1;91m[Type invalid]  \033[1;92m')
    choose()
    
    
    
def Data():
  os.system('clear')
  try:
    open('Token.txt', 'r')
    open('User_id.txt', 'r')
    open('uuid.txt', 'r')
    Home_page()
  except:
    os.system('reset')
    print ('\033[1;94m' + 50 * '\xe2\x95\x90')
    print ('\033[1;92m [\xc2\xa4] \033[1;92mCoded\033[1;91m  : \033[1;96mDARIUS\033[1;92m  \n\033[1;92m [\xc2\xa4] \033[1;92mGithub \033[1;91m: \033[1;96mhttps://github.com/dariusgab\033[1;92m\n')
    print ('\033[1;94m\xe2\x95\x94\xe2\x95\x90' + 50 * '\xe2\x95\x90')
    print ('\033[1;94m\xe2\x95\x91-> \033[1;92mToken\033[1;91m:')
    code_1 = raw_input('\033[1;94m\xe2\x95\x9a\xe2\x95\x90\033[1;92m>>> \033[1;92m')
    save=open('Token.txt', 'w')
    save.write(code_1)
    save.close()
    print ('\033[1;94m\xe2\x95\x91-> \033[1;92muuid\033[1;91m:')
    code_2 = raw_input('\033[1;94m\xe2\x95\x9a\xe2\x95\x90\033[1;92m>>> \033[1;92m')
    save=open('uuid.txt', 'w')
    save.write(code_1)
    save.close()
    print ('\033[1;94m\xe2\x95\x91->\033[1;92mUser Id\033[1;91m:')
    code_3 = raw_input('\033[1;94m\xe2\x95\x9a\xe2\x95\x90\033[1;92m>>> \033[1;92m')
    save=open('User_id.txt', 'w')
    save.write(code_3)
    save.close()
    Home_page()
Data()