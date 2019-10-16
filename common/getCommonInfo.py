import requests
import read.readConfig as readConfig
import json
from common.configHttp import RunMain
import unittest



url = readConfig.ReadConfig().get_http("gzhbaseurl")#获取配置文件中的url地址

response = requests.get(url+'/api/login/detail?token=gzhlogin:bf230607-309c-4f3c-9f66-2f9f9739f764')

versionInfo = response.text

versionInfoPython = json.loads(versionInfo)

dataList = versionInfoPython.get('Data')

shipOwnerId = dataList.get('ShipOwnerId')

goods = requests.get(url+'/api/ware/'+shipOwnerId+'/shipowner/alllist')

goodsInfo = goods.text

goodsList = json.loads(goodsInfo).get('Data')

WareDTOs = goodsList.get('WareDTOs')

wareId = WareDTOs[0].get('Id')

xcxtoken = 'xcxlogin%3A7b51c26e-43a2-4f7b-91b4-53c9f757961e&status=&AppInfoCode=code001&MerchantId=645d5071-1c22-4161-a093-7566f5cca058'


print(shipOwnerId,wareId,xcxtoken)
def getShipOwnerId():
    return shipOwnerId

def getWareId():
    return wareId

def getXcxToken():
    return xcxtoken


