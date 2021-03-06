import requests
import json
import os

cookies = {
    'NTES_YD_SESS': 'Your cookie info',
    '_gat': 'Your cookie info',
    'STAREIG': 'Your cookie info',
}

headers = {
    'Host': 'star.8.163.com',
    'Origin': 'https://star.8.163.com',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_2 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B202star_client_1.0.0',
    'Referer': 'https://star.8.163.com/m',
    'Accept-Language': 'zh-cn',
    'X-Requested-With': 'XMLHttpRequest',
}

def collectCoins(coinId):
	headers = {
	    'Host': 'star.8.163.com',
	    'Accept': 'application/json, text/plain, */*',
	    'X-Requested-With': 'XMLHttpRequest',
	    'Accept-Language': 'zh-cn',
	    'Cache-Control': 'max-age=0',
	    'Content-Type': 'application/json;charset=UTF-8',
	    'Origin': 'https://star.8.163.com',
	    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_2 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B202star_client_1.0.0',
	    'Referer': 'https://star.8.163.com/m',
	}

	data = '{"id":%s}' %coinId
	response = requests.post('https://star.8.163.com/api/starUserCoin/collectUserCoin', headers=headers, cookies=cookies, data=data)

cookies['NTES_YD_SESS'] = os.environ["NTES_YD_SESS"]
cookies['_ga'] = os.environ["GA"]
cookies['STAREIG'] = os.environ["STAREIG"]

response = requests.post('https://star.8.163.com/api/home/index', headers=headers, cookies=cookies)
jsonData = json.loads(response.text)
collectCoinsList = jsonData['data']['collectCoins']
if len(collectCoinsList) == 0:
	print('no star...')
else:
	for collectCoinsItem in collectCoinsList:
		print(collectCoinsItem)
		collectCoins(collectCoinsItem['id'])