# coding=UTF-8
import requests
host = 'https://idcert.market.alicloudapi.com'
path = '/idcard'
method = 'GET'

'''
Replace APP_CODE with your own Aliyun appcode
'''
appcode = 'APP_CODE'

def checkID(_id,_name):
    querys = f'idCard={_id}&name={_name}'
    bodys = {}
    url = host + path + '?' + querys
    header = {"Authorization":'APPCODE ' + appcode}
    try:
        res = requests.get(url,headers=header)
    except :
        return "err"
    httpStatusCode = res.status_code

    if(httpStatusCode == 200):
        return(res.json())
    else:
        return "err"
